# Attendance_Tracker 
CIT Cohort 2021, GROUP 12 PROJECT: Virtual Attendance Tracker

# Description:
The project is designed to track Virtual event attendance using registration numbers

The Admin is able to login, add students and view attendance.

Only the admin is able to add student details. Upon adding a student, their registration number is generated automatically.

All registered students are verified using their email addresses. The verification allows them to know their registration numbers which they will be using for recording their attendance.

Verified students record their attendance using the registration numbers. If existent, student details, date and time of attendance registration are added to the excel(CSV file).

If non-existent, exception is raised, and user is requested to verify their existence inorder to know their registration numbers.

On the admin dashboard, the day's attendance is displayed in a table.

# Requirements:
- Python3
- Tkinter

# How to run:
1. Clone this repo.
2. Open the folder using your IDE or editor (PyCharm or VS Code)
3. Run _main.py_ or Type `python main.py` in the terminal

# Future Work:
1. Using face recognition instead of registration numbers.
2. Allow admin to view attendance of any day and also filtering by course
3. Allow admin to view and edit student details
