import tkinter as tk
from Admin import admin_dashboard
from tkinter import messagebox as mess


class Login(object):

    def validate_login(self):
        # Get form data
        username = self.username.get()
        password = self.password.get()

        if username == "" or password == "":
            mess.showerror('Error', 'Please enter the fields')

        else:
            if username == "Admin" and password == "admin1":
                self.close_window()
                root = tk.Tk()
                root.geometry("960x600")
                root.config(bg='#fed1ef')
                root.title("Student Attendance System")
                admin_dashboard.adminWindow(root)

            else:
                mess.showerror('Error', 'Invalid Login details')

    def close_window(self):
        self.top.destroy()

    def __init__(self, master):
        top = self.top = tk.Toplevel(master)
        self.master = master
        top.title('Admin Login')

        # name
        self.username_label = tk.Label(top, font='arial 12', text='Username:').grid()
        self.username = tk.Entry(top, font='arial 12')
        self.username.grid(row=0, column=1, padx=10)

        # Email
        self.password_label = tk.Label(top, font='arial 12', text='Password:').grid(row=3)
        self.password = tk.Entry(top, font='arial 12')
        self.password.grid(row=3, column=1)

        # cancel
        self.cancel_button = tk.Button(top, font='arial 12', bg='red', text='Cancel', command=self.close_window)
        self.cancel_button.grid(row=12, column=0, pady=10)

        # Add
        self.add_button = tk.Button(top, font='arial 12', text='Submit', command=lambda: self.validate_login())
        self.add_button.grid(row=12, column=3, pady=10, padx=10, sticky=tk.E)
