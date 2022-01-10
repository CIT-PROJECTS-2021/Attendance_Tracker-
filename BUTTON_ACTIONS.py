__author__ = 'sethsilver'

from tkinter import *
root = Tk()
#root.title("ATTENDANCE TRACKER")


def sign_up():
    new_window = Toplevel() #creating instance of a new window
    new_window.title("SIGN-UP")
    name = Label(root, text="Enter Name")
    name.grid(row=0, column=0)
    name_entry = Entry(root, width=30)
    name_entry.grid(row=1, column=1, padx=20)


def cancel1():
    root.quit()


def submit1():
    return

#root.mainloop()