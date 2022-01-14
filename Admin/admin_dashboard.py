import csv
import datetime
import sys
import time
import tkinter as tk
from tkinter import ttk

import main
from DataBase import db_functions
from Admin import add_student as asw


class adminWindow(object):
    def popup_add(self):
        self.w = asw.AddStudent(self.master)
        self.master.wait_window(self.w.top)

    def view_attendance(self):
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        with open("Attendance_" + date + ".csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            i = 0
            for lines in reader1:
                print(lines)
                if i > 0:
                    if i % 2 == 0:
                        self.tv.insert('', 0, values=(
                            str(lines[0]), str(lines[2]), str(lines[4]), str(lines[6]), str(lines[8]), str(lines[10]),
                            str(lines[12]), str(lines[14])))
                i = i + 1
        csvFile1.close()

    def save(self):
        db_functions.db_commit()

    def quit(self):
        sys.exit()

    def __init__(self, master):
        self.master = master
        master.title('Admin Dashboard')

        # Menu bar
        menu_bar = tk.Menu(self.master)
        options = tk.Menu(menu_bar, tearoff=0)

        # File Menu
        options.add_command(label="Save", font='arial 10', command=self.save)
        options.add_command(label="Quit", font='arial 10', command=self.quit)
        options.add_separator()
        menu_bar.add_cascade(label="File", menu=options)

        self.master.config(menu=menu_bar)

        # Scroll bar and box list of students
        self.scrollbar = tk.Scrollbar(master)

        # Add student button
        self.add_button = tk.Button(master, font='arial 12', text='Add student',
                                    command=self.popup_add)
        self.add_button.grid(row=0, column=0, sticky=tk.W, padx=12)

        self.frame1 = tk.Frame(master, bg='#fff8f3')
        self.frame1.grid(row=3, column=0, sticky=tk.W, padx=12)

        self.lbl = tk.Label(self.frame1,
                            text="Attendance For {}".format(str(datetime.datetime.now().date().strftime("%d-%m-%Y"))),
                            width=20, fg="black", bg='#fff8f3', height=1,
                            font=('times', 17, ' bold '))
        self.lbl.grid(row=0, column=5, sticky=tk.W, padx=12)

        self.tv = ttk.Treeview(self.frame1, height=13,
                               columns=('name', 'email', 'mobile', 'course', 'cohort', 'regno', 'date', 'time'))
        self.tv.column('#0', width=10)
        self.tv.column('name', width=130)
        self.tv.column('email', width=130)
        self.tv.column('mobile', width=130)
        self.tv.column('course', width=130)
        self.tv.column('cohort', width=130)
        self.tv.column('regno', width=130)
        self.tv.column('date', width=133)
        self.tv.column('time', width=133)
        self.tv.grid(row=1, column=0, padx=(0, 0), pady=(10, 0), columnspan=9)
        self.tv.heading('name', text='NAME')
        self.tv.heading('email', text='EMAIL')
        self.tv.heading('mobile', text='PHONE NO.')
        self.tv.heading('course', text='COURSE')
        self.tv.heading('cohort', text='COHORT')
        self.tv.heading('regno', text='REG NO.')
        self.tv.heading('date', text='DATE')
        self.tv.heading('time', text='TIME')

        # SCROLLBAR

        scroll = ttk.Scrollbar(self.frame1, orient='vertical', command=self.tv.yview)
        scroll.grid(row=2, column=9, padx=(0, 100), pady=(150, 0), sticky='ns')
        self.tv.configure(yscrollcommand=scroll.set)

        self.view_attendance()
