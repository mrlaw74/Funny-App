from pathlib import Path
from tkinter import (
    Toplevel,
    Frame,
    Canvas,
    Button,
    Entry,
    PhotoImage,
    messagebox,
    StringVar,
)
from gui.mainwindow.dashboard.gui import Dashboard
from gui.mainwindow.chattingroom.gui import ChattingRoom
from gui.mainwindow.admin.gui import Admin
from .. import login

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    """
    TODO
    """
    return ASSETS_PATH / Path(path)


def mainWindow():
    """
    TODO
    """
    MainWindow()


class MainWindow(Toplevel):
    """
    TODO
    """
    global user

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

        self.title("My app")

        self.geometry("1012x506")
        # self.geometry("1312x806")
        self.configure(bg="#5E95FF")

        self.current_window = None
        self.current_window_label = StringVar()

        self.canvas = Canvas(
            self,
            bg="#5E95FF",
            height=506,
            width=1012,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.heading = self.canvas.create_text(
            255.0,
            33.0,
            anchor="nw",
            text="Hello",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(215, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline="")

        # Add a frame rectangle
        self.sidebar_indicator = Frame(self, background="#FFFFFF")

        self.sidebar_indicator.place(x=0, y=133, height=47, width=7)

        image_image_1 = PhotoImage(file=relative_to_assets("icon.png"))
        image_1 = self.canvas.create_image(95.0, 75.0, image=image_image_1)

        button_image_1 = PhotoImage(file=relative_to_assets("dashboard.png"))
        self.dashboard_btn = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.dashboard_btn, "dash"),
            cursor="hand2",
            activebackground="#5E95FF",
            relief="flat",
        )
        self.dashboard_btn.place(x=7.0, y=140.0, width=208.0, height=47.0)

        button_image_2 = PhotoImage(file=relative_to_assets("chatting.png"))
        self.rooms_btn = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.rooms_btn, "roo"),
            cursor="hand2",
            activebackground="#5E95FF",
            relief="flat",
        )
        self.rooms_btn.place(x=7.0, y=190.0, width=208.0, height=47.0)

        button_image_3 = PhotoImage(file=relative_to_assets("admin.png"))
        self.admin_btn= Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.admin_btn, "adm"),
            cursor="hand2",
            activebackground="#5E95FF",
            relief="flat",
        )
        self.admin_btn.place(x=7.0, y=240.0, width=208.0, height=47.0)

        button_image_5 = PhotoImage(file=relative_to_assets("logout.png"))
        self.logout_btn = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.logout,
            relief="flat",
        )
        self.logout_btn.place(x=0.0, y=441.0, width=215.0, height=47.0)

        # Loop through windows and place them
        self.windows = {
            "dash": Dashboard(self),
            "roo": ChattingRoom(self),
            "adm": Admin(self),
            # "abt": About(self),
            # "res": Reservations(self),
        }

        self.handle_btn_press(self.dashboard_btn, "dash")
        self.sidebar_indicator.place(x=0, y=133)

        self.current_window.place(x=215, y=72, width=1013.0, height=506.0)

        self.current_window.tkraise()
        self.resizable(False, False)
        self.mainloop()

    def place_sidebar_indicator(self):
        """
        TODO
        """
        pass

    def handle_btn_press(self, caller, name):
        """
        TODO
        """
        # Place the sidebar on respective button
        self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Set ucrrent Window
        self.current_window = self.windows.get(name)

        # Show the screen of the button pressed
        self.windows[name].place(x=215, y=72, width=1013.0, height=506.0)

        # Handle label change
        current_name = self.windows.get(name)._name.split("!")[-1].capitalize()
        self.canvas.itemconfigure(self.heading, text=current_name)

    def handle_dashboard_refresh(self):
        """
        TODO
        """
        # Recreate the dash window
        self.windows["dash"] = Dashboard(self)

    def logout(self):
        """
        TODO
        """
        confirm = messagebox.askyesno("Confirm log-out", "Do you really want to log out?")
        if confirm == True:
            user = None
            self.destroy()
            login.gui.loginWindow()
