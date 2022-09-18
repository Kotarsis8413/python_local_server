from tkinter import *
from tkinter import messagebox
import time
from start import *

root = Tk()
root.title('SERVER START PANEL')
root.geometry('650x550')
def redbutton():
    messagebox.showwarning('RED BUTTON PRESED', message="Bomb dropped")
    root.destroy()
    serverWU()
Button(root, font="Roman 20 bold", text="RED BUTTON", bg="red", highlightcolor="red", command=redbutton).pack()
root.mainloop()

