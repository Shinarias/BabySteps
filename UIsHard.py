import tkinter
from tkinter import messagebox


def ButtonPress():
    messagebox.showinfo("Hello Python", "Hello World")


mainWindow = tkinter.Tk()

printButton = tkinter.Button(mainWindow, text="Moooin", command=ButtonPress)

printButton.pack()
mainWindow.mainloop()
