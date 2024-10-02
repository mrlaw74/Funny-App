import tkinter as tk
from gui.login.gui import loginWindow
from gui.mainwindow.main import mainWindow
from gui.register.gui import registerWindow


root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window


if __name__ == "__main__":

    # loginWindow()
    mainWindow()
    # registerWindow()

#  root.mainloop()
