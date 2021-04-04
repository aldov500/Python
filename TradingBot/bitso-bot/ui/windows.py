import PIL.Image
from PIL import ImageTk
#from tkinter import *
import tkinter as tk

class MainWindow:

    def __init__(self, tkinter_obj):
        tkinter_obj.geometry("640x480")
        tkinter_obj.title = "Title of window"
        image = image.resize(200,200)
        image = PIL.Image.open("images/bitso_logo.png")
        app_logo = ImageTk.PhotoImage(image)
        image_logo = tk.Label(tkinter_obj, image=app_logo, bd=0)
        image_logo.pack(anchor="n", side="left")

        self.tkinter_obj = tkinter_obj
        self.frame = tk.Frame(self.tkinter_obj)
        self.btn_new_window = tk.Button(self.frame, text='New Window', width=25, command=self.new_window)
        self.btn_new_window.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()
