import socket
import threading
from pathlib import Path
import tkinter as tk
from tkinter import Frame, Entry, Label, Button, scrolledtext, Canvas, PhotoImage
import queue

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def get_ipv4_address():
    """
    TODO
    """
    hostname = socket.gethostname()  # Get the hostname of the machine
    ipv4_address = socket.gethostbyname(hostname)  # Get the IPv4 address using the hostname
    return ipv4_address


def relative_to_assets(path: str) -> Path:
    """
    TODO
    """
    return ASSETS_PATH / Path(path)


class ChattingRoom(Frame):
    """
    TODO
    """
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(bg="#6ecaf5")

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Create a queue for messages
        self.message_queue = queue.Queue()
        self.stop_thread = threading.Event()  # Event to signal thread to stop


        # Nickname input canvas
        self.nickname_canvas = Canvas(
            self,
            bg="#5eff8c",
            height=400,  # Adjust the height as needed
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.nickname_canvas.place(x=20, y=10)

        self.nickname_canvas.create_text(
            20,
            10,
            anchor="nw",
            text="Enter your nickname:",
            fill="#5E95FF",
            font=("Montserrat Bold", 12),  # Adjust font size as needed
        )

        self.nickname_entry = Entry(self.nickname_canvas, bd=0, bg="#EFEFEF", \
        highlightthickness=0, font=("Montserrat Bold", 20 * -1))
        self.nickname_entry.place(x=73, y=50, width=336.0, height=30)  # Adjust x and y positions as needed
        self.nickname_entry.bind("<Return>", self.start_client)

        self.after(100, self.update_chat_box)

    def update_chat_box(self):
        """
        TODO
        """
        while not self.message_queue.empty():
            message, align = self.message_queue.get()
            self.chat_box.config(state='normal')
            self.chat_box.insert('end', message + "\n", align)
            self.chat_box.config(state='disabled')
            self.chat_box.yview('end')
        self.after(100, self.update_chat_box)  # Schedule next update

    def receive(self):
        """
        TODO
        """
        while not self.stop_thread.is_set():
            try:
                message = self.client.recv(1024).decode("utf-8")
                if not message:
                    break  # Exit loop if no message is received
                if message == "NICK":
                    self.client.send(self.nickname.encode("utf-8"))
                else:
                    if message.startswith(f"{self.nickname}:"):
                        self.message_queue.put((message, "right"))
                    else:
                        self.message_queue.put((message, "left"))
            except (ConnectionAbortedError, ConnectionResetError):
                self.message_queue.put(("Disconnected from server.", "center"))
                break
            except Exception as e:
                self.message_queue.put(("An unexpected error occurred.", "center"))
                break
        self.client.close()

    def send_message(self, event=None):
        """
        TODO
        """
        message = f"{self.nickname}: {self.msg_entry.get()}"
        try:
            self.client.send(message.encode("utf-8"))
            self.msg_entry.delete(0, 'end')
        except Exception:
            self.message_queue.put(("Message could not be sent.\
            Server may be down.", "center"))

    def exit_chat(self):
        """
        TODO
        """
        self.stop_thread.set()  # Signal the thread to stop
        self.client.close()  # Close the client socket
        self.after(0, self.quit)  # Ensure Tkinter quits on the main thread

    def start_client(self, event=None):
        """
        TODO
        """
        self.nickname = self.nickname_entry.get()

        if self.nickname:
                    # Chat display frame (initially hidden)
            self.chat_frame = Frame(self)
            self.chat_frame.place(x=10, y=10)

            # Chat display area (read-only)
            self.chat_box = scrolledtext.ScrolledText(self.chat_frame, \
                state='disabled', wrap='word', width=80, height=15)
            self.chat_box.pack(padx=20, pady=5, fill='both', expand=True)

            # Message input frame (hidden initially)
            self.input_frame = Frame(self)
            self.input_frame.place(x=20, y=350)

            self.msg_entry = Entry(self.input_frame, width=70)
            self.msg_entry.pack(side='left', padx=10, pady=5, fill='x', expand=True)
            self.msg_entry.bind("<Return>", self.send_message)

            self.send_button = Button(self.input_frame, text="Send",\
                command=self.send_message)
            self.send_button.pack(side='right', padx=10, pady=5)

            # Exit chat button (hidden initially)
            self.exit_button = Button(self, text="Exit Chat", command=self.exit_chat)
            self.exit_button.place(x=150, y=400)
            self.exit_button.place_forget()  # Initially hide the exit button
            # Hide nickname input and enable chat area
            # self.nickname_frame.place_forget()
            self.nickname_canvas.place_forget()
            self.chat_frame.place(x=20, y=50)
            self.input_frame.place(x=20, y=350)
            self.exit_button.place(x=150, y=400)  # Show exit button

            # Clear message entry and connect to server
            self.msg_entry.delete(0, 'end')  # Clear the entry field
            self.input_frame.place(x=20, y=350)

            # Connect to the server (replace with actual server IP if needed)
            HOST = get_ipv4_address() 
            self.client.connect((HOST, 3333))

            # Start threads for receiving messages
            receive_thread = threading.Thread(target=self.receive)
            receive_thread.start()


def chat():
    """
    TODO
    """
    window = tk.Tk()
    window.geometry("400x550")
    ChattingRoom(window)
    window.mainloop()
