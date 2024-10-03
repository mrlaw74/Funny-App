from pathlib import Path
from tkinter import Frame, Canvas, Entry, PhotoImage, N
from services.Data_Base.db_service import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    """
    TODO
    """
    return ASSETS_PATH / Path(path)


def dashboard():
    """
    TODO
    """
    Dashboard()


class Dashboard(Frame):
    """
    TODO
    """
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=432,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        canvas.place(x=0, y=0)
        canvas.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(115.0, 81.0, image=canvas.entry_image_1)
        entry_1 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 150),
        )
        entry_1.place(x=55.0, y=30.0 + 2, width=120.0, height=0)

        canvas.create_text(
            56.0,
            45.0,
            anchor="nw",
            text="Users:",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )
        canvas.create_text(
            164.0,
            63.0,
            anchor="ne",
            text=get_total_users(),
            fill="#5E95FF",
            font=("Montserrat Bold", 48 * -1),
            justify="right",
        )
