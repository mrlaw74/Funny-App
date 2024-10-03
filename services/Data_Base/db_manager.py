import mysql.connector
import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox

# Load environment variables from the .env file
load_dotenv()

# SQL Connection
connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),  # Ensure the database is selected here
    port="3306",
    autocommit=os.getenv("DB_AUTOCOMMIT") == 'true',
)

# Ensure the database is set correctly
cursor = connection.cursor(buffered=True)
cursor.execute("USE mydb")  # Set the database context explicitly

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
    if check_user(username):
        messagebox.showerror("Error", "Username already exists.")
        return False
    
    try:
        cmd = "INSERT INTO login (username, password, sec_que, sec_ans) VALUES (%s, %s, %s, %s)"
        cursor.execute(cmd, (username, password, sec_que, sec_ans))
        connection.commit()
        messagebox.showinfo("Success", "User registered successfully.")
        return True
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return False

# Function to delete a user
def delete_user(username):
    """
    TODO
    """
    if username:
        try:
            cmd = "DELETE FROM login WHERE username = %s"  # Prepared statement for safety
            cursor.execute(cmd, (username,))
            connection.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "User deleted successfully!")
            else:
                messagebox.showwarning("Warning", "User not found.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to delete user: {err}")

# UI Application
class UserManagementApp:
    """
    TODO
    """
    def __init__(self, master):
        self.master = master
        master.title("User Management")
        master.geometry("300x200")

        # Username input
        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        # Password input
        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show='*')
        self.password_entry.pack()

        # Add user button
        self.add_button = tk.Button(master, text="Add User", command=self.add_user)
        self.add_button.pack()

        # Delete user button
        self.delete_button = tk.Button(master, text="Delete User", command=self.delete_user)
        self.delete_button.pack()

    def add_user(self):
        """
        TODO
        """
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            register_user(username, password)  # Using the existing function
        else:
            messagebox.showwarning("Input Error", "Please enter both username and password.")

    def delete_user(self):
        """
        TODO
        """
        username = self.username_entry.get()
        if username:
            delete_user(username)  # Using the existing function
        else:
            messagebox.showwarning("Input Error", "Please enter a username.")

# Close connection when the app is closed
def on_closing():
    """
    TODO
    """
    cursor.close()
    connection.close()
    root.destroy()

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagementApp(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)  # Ensure connection closes on exit
    root.mainloop()
