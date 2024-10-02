"""
Login window module for the GUI application.

This module defines the login functionality and integrates it with the database.
"""

from pathlib import Path
from tkinter import Toplevel, Canvas, Entry, Button, PhotoImage, messagebox
from services.Data_Base.db_service import *
from ..mainwindow.main import mainWindow

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

user = None  # Define global variable

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def login_window():
    """
    Opens the login window for user authentication.
    """
    Login()


class Login(Toplevel):
    """
    Represents the login window in the GUI application.
    """
    def __init__(self, *args, **kwargs):

        Toplevel.__init__(self, *args, **kwargs)

        self.title("Login Window")

        self.geometry("1012x506")
        self.configure(bg="#5eff8c")

        self.canvas = Canvas(
            self,
            bg="#5eff8c",
            height=506,
            width=1012,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(469.0, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline="")

        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(736.0, 331.0, image=entry_image_1)
        entry_1 = Entry(self.canvas, bd=0, bg="#EFEFEF", highlightthickness=0)
        entry_1.place(x=568.0, y=294.0, width=336.0, height=0)

        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(736.0, 229.0, image=entry_image_2)
        entry_2 = Entry(self.canvas, bd=0, bg="#EFEFEF", highlightthickness=0)
        entry_2.place(x=568.0, y=192.0, width=336.0, height=0)

        self.canvas.create_text(
            573.0,
            306.0,
            anchor="nw",
            text="Password",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.canvas.create_text(
            573.0,
            204.0,
            anchor="nw",
            text="Username",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )
        self.canvas.create_text(
            553.0,
            66.0,
            anchor="nw",
            text="Enter your login details",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        button_image_1 = PhotoImage(file=relative_to_assets("login.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.login_func,
            relief="flat",
        )
        button_1.place(x=740.0, y=412.0, width=190.0, height=48.0)

        button_image_2 = PhotoImage(file=relative_to_assets("register.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.register_func,
            relief="flat",
        )
        button_2.place(x=540.0, y=412.0, width=190.0, height=48.0)


        entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(736.0, 241.0, image=entry_image_3)
        self.username = Entry(
            self.canvas,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 16 * -1),
            foreground="#777777",
        )
        self.username.place(x=573.0, y=229.0, width=326.0, height=22.0)

        entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(736.0, 342.0, image=entry_image_4)
        self.password = Entry(
            self.canvas,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 16 * -1),
            foreground="#777777",
            show="•",
        )
        self.password.place(x=573.0, y=330.0, width=326.0, height=22.0)

        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(428.0, 306.0, image=image_image_1)

        self.canvas.create_text(
            20.0,
            10.0,
            anchor="nw",
            text="Funny app is an app that allows users to chat",
            fill="#1d3040",
            font=("MV Boli", 18 * -1),
        )

        self.canvas.create_text(
            20.0,
            39.0,
            anchor="nw",
            text="together!",
            fill="#1d3040",
            font=("MV Boli", 18 * -1),
        )

        self.canvas.create_text(
            20.0,
            68.0,
            anchor="nw",
            text="Join conversations, make friends, and have fun!",
            fill="#1d3040",
            font=("MV Boli", 18 * -1),
        )

        self.canvas.create_text(
            20.0,
            97.0,
            anchor="nw",
            text="Let's get started!",
            fill="#1d3040",
            font=("MV Boli", 18 * -1),
        )

        self.resizable(False, False)
        self.mainloop()

    def login_func(self):
        """
        Authenticates the user and opens the main window if successful.
        """
        global user
        if check_user(self.username.get().lower(), self.password.get()):
            user = self.username.get().lower()
            self.destroy()
            mainWindow()
            return
        messagebox.showerror(
            title="Invalid Credentials",
            message="The username and password don't match",
        )

    def register_func(self):
        """
        Opens the register window for new user registration.
        """
        from ..register.gui import registerWindow
        self.destroy()
        registerWindow()