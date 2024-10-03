import os
import mysql.connector
from dotenv import load_dotenv
from .config import config

load_dotenv()  # Load environment variables from the .env file

# SQL Connection
connection = mysql.connector.connect(
    host=config.get("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=config.get("DB_NAME"),
    port=config.get("DB_PORT"),
    autocommit=config.get("DB_AUTOCOMMIT"),
)

cursor = connection.cursor(buffered=True)

# Function to check if the user exists
def check_user(username, password=None):
    """
    TODO
    """
    cmd = f"SELECT COUNT(username) FROM login WHERE username='{username}' AND BINARY password='{password}'"
    cursor.execute(cmd)
    result = cursor.fetchone()[0] >= 1
    return result

# Function to add/register a new user
def register_user(username, password, sec_que=None, sec_ans=None):
    """
    TODO
    """
    """
    Register a new user by adding their information to the database.
    :param username: The username to add.
    :param password: The password to add.
    :param sec_que: The security question (optional).
    :param sec_ans: The answer to the security question (optional).
    :return: True if the registration is successful, False otherwise.
    """
    # Check if the username already exists
    if check_user(username):
        print("Username already exists.")
        return False
    
    # Insert the new user into the 'login' table
    try:
        cmd = "INSERT INTO login (username, password, sec_que, sec_ans) VALUES (%s, %s, %s, %s)"
        cursor.execute(cmd, (username, password, sec_que, sec_ans))
        connection.commit()  # Commit the transaction to save changes
        print("User registered successfully.")
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

# Function to get total users count
def get_total_users():
    """
    TODO
    """
    """
    Retrieve the total number of users in the 'login' table.
    :return: The total number of users, or False if there are no users.
    """
    cmd = "SELECT COUNT(username) FROM login;"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchone()[0]

# Close the cursor and connection when done
def close_connection():
    """
    TODO
    """
    cursor.close()
    connection.close()
