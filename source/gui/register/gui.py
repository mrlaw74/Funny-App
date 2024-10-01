from pathlib import Path

from tkinter import Toplevel, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

from services.Data_Base.db_service import *
from ..mainwindow.main import mainWindow
from utils.checkvalid import *

OUTPUT_PATH = Path(__file__).parent
print(OUTPUT_PATH)
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def registerWindow():
    Register()


class Register(Toplevel):
    # Login check function
    def back2Login(self):
        if check_username(self.username.get()) and check_pw(self.password.get()):
            if (register_user(self.username.get(),self.password.get())):
                from ..login.gui import loginWindow
                self.destroy()
                loginWindow()
                return
            else:
                messagebox.showerror(
                    title="Invalid Username",
                    message="Username has already registered, please register with another name",
                )
        else:
            messagebox.showerror(
                title="Invalid Credentials",
                message="Invalid username or password, input again",
            )

    def __init__(self, *args, **kwargs):

        Toplevel.__init__(self, *args, **kwargs)

        self.title("Register")

        self.geometry("1012x506")
        self.configure(bg="#5f95ff")

        self.canvas = Canvas(
            self,
            bg="#5f95ff",
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
            text="Enter your information details",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        button_image_2 = PhotoImage(file=relative_to_assets("register.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.back2Login,
            relief="flat",
        )
        button_2.place(x=650.0, y=412.0, width=190.0, height=48.0)

        image_image_1 = PhotoImage(file=relative_to_assets("reg.png"))
        image_1 = self.canvas.create_image(225.0, 286.0, image=image_image_1)

        self.canvas.create_text(
            10.0,
            10.0,
            anchor="nw",
            text="Welcome to Funny app",
            fill="#1d3040",
            font=("Segoe Script", 36 * -1),
        )

        self.resizable(False, False)
        self.mainloop()
