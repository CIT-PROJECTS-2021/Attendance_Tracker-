import tkinter as tk
import home

from DataBase import db_functions


def select_student(student):
    for row in db_functions.get_entry(db_functions.get_id(student)):
        return row


def add_student(student):
    db_functions.insert_student(student)


def search(search_string):
    return db_functions.search_student(search_string)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("960x600")
    root.config(bg='#fed1ef')
    root.title("Student Attendance System")
    db_functions.db_init()
    home.homeDashboard(root)
    root.mainloop()
