import csv
import os
import datetime
import numpy as np
import sqlite3 as sql
import pandas as pd
import time
import tkinter as tk
from tkinter import messagebox as mess

import login
from DataBase import config

config.DB = sql.connect('DataBase/student_details.db')
config.C = config.DB.cursor()

global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year = date.split("-")

months = {'01': 'January',
          '02': 'February',
          '03': 'March',
          '04': 'April',
          '05': 'May',
          '06': 'June',
          '07': 'July',
          '08': 'August',
          '09': 'September',
          '10': 'October',
          '11': 'November',
          '12': 'December'
          }


class homeDashboard(object):
    def timer(self):
        time_string = time.strftime('%H:%M:%S')
        self.clock.config(text=time_string)
        self.clock.after(200, self.timer)

    def popup_login(self):
        self.w = login.Login(self.master)
        self.master.wait_window(self.w.top)

    def write_to_csv(self, data):
        header_col_names = ['Name', '', 'Email', '', 'Mobile', '', 'Course', '', 'Cohort', '', 'Date', '', 'Time']

        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

        attendance = [data[0], '', data[1], '', data[2], '', data[3], '', data[4], '', data[5], '', str(date), '',
                      str(timeStamp)]

        exists = os.path.isfile("Attendance_" + date + ".csv")
        if exists:
            with open("Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(attendance)
            csvFile1.close()
        else:
            with open("Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(header_col_names)
                writer.writerow(attendance)
            csvFile1.close()

    def attendance(self):
        regcode = self.reg_code_txt.get()

        if regcode == "":
            mess.showerror('Error', 'Please enter your registration number')
        else:
            query2 = f"select * from 'Students' where Reg_No='{regcode}'"
            data = config.C.execute(query2).fetchone()
            if data[0] != "":
                self.write_to_csv(data)
                mess.showinfo('Success', 'Your attendance has been recorded')
            else:
                mess.showerror('Error',
                               f'Student not found with \nReg- {regcode}\nVerify Yourself if it your first time')

    def search_for_student(self):
        email = self.email_txt.get()

        if email == "":
            mess.showerror('Error', 'Please enter the Email')
        else:
            try:
                query2 = f"select Reg_No from 'Students' where Email='{email}'"
                data = config.C.execute(query2).fetchone()
                mess.showinfo('Success', 'Your Reg No is: {}'.format(data[0]))
            except:
                mess.showerror('Error', f'Student not found with \nEmail:- {email}\nContact Admin to add you')

    def __init__(self, master):
        self.master = master

        self.title = tk.Label(self.master, text="STUDENT ATTENDANCE TRACKER", fg="black", bg="#A3E4DB", width=50,
                              height=1,
                              font=('comic', 30, ' bold '))
        self.title.pack(padx=0, ipady=10, fill='x')

        self.dateframe = tk.Frame(self.master, height=1, bg="#1c6dd0")
        self.dateframe.pack(padx=0, ipady=5, fill='x')

        self.datef = tk.Label(self.dateframe, text=months[month] + " " + day + ", " + year, bg="#1c6dd0", fg="#fff8f3",
                              font=('comic', 22, ' bold '))
        self.datef.pack(ipadx=10, ipady=5, expand=True, fill='both', side='left')

        self.clock = tk.Label(self.dateframe, bg="#1c6dd0", fg="#fff8f3", font=('comic', 22, ' bold '))
        self.clock.pack(ipadx=10, ipady=5, expand=True, fill='both', side='left')
        self.timer()

        self.content = tk.Frame(self.master)
        self.content.pack(padx=0, ipady=5, fill='both', expand=True)

        self.frame1 = tk.Frame(self.content, width=50, bg='#fff8f3')
        self.frame1.pack(padx=10, ipadx=10, ipady=10, expand=True, fill='both', side='left')

        self.frame2 = tk.Frame(self.content, width=50, bg='#fff8f3')
        self.frame2.pack(ipady=10, expand=True, fill='both', side='right')

        self.head1 = tk.Label(self.frame1, text="For Fully verified Students", fg="black", bg='#fff8f3',
                              font=('comic', 18, ' bold '))
        self.head1.pack(ipadx=10, ipady=10, fill='x')

        self.head2 = tk.Label(self.frame2, text="First Time Verification", fg="black", bg='#fff8f3',
                              font=('comic', 18, ' bold '))
        self.head2.pack(ipadx=10, ipady=10, fill='x')

        self.reg_frame = tk.Frame(self.frame1, bg='#fff8f3')
        self.reg_frame.pack(padx=20, ipady=5, pady=10, fill='x')

        self.lbl_reg = tk.Label(self.reg_frame, text="Enter Your Reg No.", fg="black", bg='#fff8f3',
                                font=('comic', 14, ' bold ')).pack(ipadx=10, ipady=5, pady=10, side='left')

        self.reg_code_txt = tk.Entry(self.reg_frame, fg="black", font=('comic', 16, ' bold '))
        self.reg_code_txt.pack(ipadx=10, ipady=5,
                               pady=10,
                               side='left')

        self.register_attendance = tk.Button(self.frame1, text="Register Your Attendance", borderwidth=0, fg="black",
                                             command=lambda: self.attendance(), bg='#fed1ef',
                                             font=('comic', 16, ' bold ')).pack(ipadx=10, ipady=10)

        self.email_frame = tk.Frame(self.frame2, bg='#fff8f3')
        self.email_frame.pack(padx=20, ipady=5, pady=10, fill='x')

        self.lbl_email = tk.Label(self.email_frame, text="Enter Your Email", fg="black", bg='#fff8f3',
                                  font=('comic', 14, ' bold ')).pack(ipadx=10, ipady=5, pady=10, side='left')

        self.email_txt = tk.Entry(self.email_frame, fg="black", font=('comic', 16, ' bold '))
        self.email_txt.pack(ipadx=10, ipady=5, pady=10, side='left')

        self.verify = tk.Button(self.frame2, text="Submit", fg="white", bg="#1c6dd0", borderwidth=0,
                                font=('comic', 15, ' bold '), command=lambda: self.search_for_student())
        self.verify.pack(ipadx=10, ipady=5, pady=10)

        self.admin = tk.Frame(self.master, height=1).pack(padx=0, fill='x')

        self.admin_login = tk.Button(self.admin, text="Admin Login", fg="white", bg="#1c6dd0", borderwidth=0,
                                     command=lambda: self.popup_login(), font=('comic', 15, ' bold '))
        self.admin_login.pack(pady=10, ipadx=5, ipady=1)

        self.footer = tk.Frame(self.master, height=1)
        self.footer.pack(padx=0, fill='x')

        self.quitWindow = tk.Button(self.footer, text="Quit", command=self.master.destroy, fg="black", borderwidth=0,
                                    bg="#A3E4DB",
                                    font=('comic', 15, ' bold '))
        self.quitWindow.pack(pady=10, ipadx=5, ipady=1, side='right')

        #   MENUBAR
        self.menubar = tk.Menu(self.master, relief='ridge')
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Quit', command=self.master.destroy)
        self.menubar.add_cascade(label='File', menu=self.filemenu)

        self.master.configure(menu=self.menubar)
