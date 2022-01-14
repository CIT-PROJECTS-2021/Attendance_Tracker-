import sys
import tkinter as tk
import datetime
import random

import main
from Admin import admin_dashboard
from Admin import add_student_confirmation as asc

sys.path.insert(0, '..')


class AddStudent(object):
    def close_window(self):
        self.top.destroy()

    def field_return(self):
        # List to hold form data
        field_list = [' ', ' ', ' ', ' ', ' ', ' ']

        # Get form data
        student_name = self.name.get()
        email = self.email.get()
        mobile = self.mobile.get()
        course = self.course.get()
        cohort = self.cohort.get()

        # generate student registration number
        random_num = str(random.randint(1, 10001))
        year = str(datetime.datetime.now().date().strftime("%Y"))
        reg_no = year + "/CIT/" + random_num

        field_vars = [student_name, email, mobile, course, cohort, reg_no]

        # Add form data to field_list
        for i in range(6):
            field_list[i] = field_vars[i]

        if field_list[0] != '':
            main.add_student(field_list)
        else:
            self.confirm = asc.confirmationWindow(self.master)

        admin_dashboard.adminWindow(self.master)
        self.close_window()

    def __init__(self, master):
        top = self.top = tk.Toplevel(master)
        self.master = master
        top.title('Add Student')

        # name
        self.name_label = tk.Label(top, font='arial 12', text='Name:').grid()
        self.name = tk.Entry(top, font='arial 12')
        self.name.grid(row=0, column=1, padx=10)

        # Email
        self.email_label = tk.Label(top, font='arial 12', text='Email:').grid(row=3)
        self.email = tk.Entry(top, font='arial 12')
        self.email.grid(row=3, column=1)

        # Mobile
        self.mobile_label = tk.Label(top, font='arial 12', text='Mobile:').grid(row=5)
        self.mobile = tk.Entry(top, font='arial 12')
        self.mobile.grid(row=5, column=1)

        # course
        self.course_label = tk.Label(top, font='arial 12', text='Course:').grid(row=8)
        self.course = tk.Entry(top, font='arial 12')
        self.course.grid(row=8, column=1)

        # cohort
        self.cohort_label = tk.Label(top, font='arial 12', text='Cohort:').grid(row=9)
        self.cohort = tk.Entry(top, font='arial 12')
        self.cohort.grid(row=9, column=1)

        # cancel
        self.cancel_button = tk.Button(top, font='arial 12', bg='red', text='Cancel', command=self.close_window)
        self.cancel_button.grid(row=12, column=1, pady=10)

        # Add
        self.add_button = tk.Button(top, font='arial 12', text='Add', command=self.field_return)
        self.add_button.grid(row=12, column=1, pady=10, padx=10, sticky=tk.E)
