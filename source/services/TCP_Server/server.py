import sys
import os
# Add the root directory to sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(root_dir)

import socket
import threading
import mysql.connector  # Import MySQL connector
from utils.getIp import get_ipv4_address
# from .config import config
from services.TCP_Server.config import config
from dotenv import load_dotenv

load_dotenv() 

# MySQL Database Configuration
connection = mysql.connector.connect(
    host=config.get("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=config.get("DB_NAME"),
    port=config.get("DB_PORT"),
    autocommit=config.get("DB_AUTOCOMMIT"),
)

cursor = connection.cursor(buffered=True)

HOST = get_ipv4_address() 

PORT = 3333

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

# Function to broadcast messages to all clients
def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            remove_client(client)


# Function to insert a message into the database
def insert_message(nickname, message):
    try:
        sql = "INSERT INTO messages (nickname, message) VALUES (%s, %s)"
        values = (nickname, message)
        db_cursor.execute(sql, values)
        db_connection.commit()
    except Exception as e:
        print(f"Error inserting message into database: {e}")


# Function to remove a client from the list
def remove_client(client):
    if client in clients:
        index = clients.index(client)
        nickname = nicknames[index]
        print(f"{nickname} disconnected.")
        clients.remove(client)
        nicknames.remove(nickname)
        client.close()
        broadcast(f"{nickname} left the chat.".encode("utf-8"))


# Function to handle communication with a single client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                # Insert message into database
                decoded_message = message.decode("utf-8")
                nickname = decoded_message.split(":")[0]
                insert_message(nickname, decoded_message)

                # Broadcast the message to other clients
                broadcast(message)
            else:
                remove_client(client)
                break
        except:
            remove_client(client)
            break


# Function to accept and manage new connections
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname: {nickname} joined the chat.")
        broadcast(f"{nickname} joined the chat!".encode("utf-8"))
        client.send("You are connected to the server!".encode("utf-8"))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


print("Server is running and waiting for connections...")
receive()
