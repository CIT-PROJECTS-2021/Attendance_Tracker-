__author__ = 'sethsilver'

from tkinter import *
#import BUTTON_ACTIONS
root = Tk()
root.geometry("500x500")
root.title("ATTENDANCE TRACKER")

def root_submit():
    '''
    Checks if the code entered is associated with any name
    -> If yes, confirms registration of user attendance: (TABLE IS UPDATED WITH A NEW DATE COLUMN SHOWING ABSENT OR PRESENT )
    -> If Not, an exception is raised to request user to SIGN-UP
    :return:
    '''
    root_top = Toplevel()
    root_top.geometry("400x300")
    root_top.title("Submission")
    my_text = '''
    Confirms if code is existent in DB, else raises exception for new entrant 
    Adds name to current column of attendants
    '''
    root_sub_label = Label(root_top, text=my_text)
    root_sub_label.grid(row=1, column=1)

def sign_up():
    global new_window
    new_window = Toplevel() #creating instance of a new window
    new_window.title("SIGN-UP")

    #Name Field
    name = Label(new_window, text="Enter Name")
    name.grid(row=0, column=0)
    name_entry = Entry(new_window, width=30)
    name_entry.grid(row=0, column=1, padx=20)

    #Contact Field
    contact = Label(new_window, text="Phone Number")
    contact.grid(row=1, column=0)
    contact_entry = Entry(new_window, width=30)
    contact_entry.grid(row=1, column=1, padx=20)

    #Buttons:
    submission = Button(new_window, text="SUBMIT DETAIL", command=new_submit)
    submission.grid(row=2, column=0)

    cancellation = Button(new_window, text="CANCEL", command=new_window.quit)
    cancellation.grid(row=2, column=2)


#Actions:


def new_submit():
    '''
    Defines Actions to be performed when one is joining meeting/event for the very first time
     '''

    '''
    1. Enter Detail into Database
    2. print -> Detail confirmed
    3. Generate random number code
    4. Store code in data-base in association with name of user
    '''
    import random
    myrange = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', '0', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    my_code = random.sample(myrange, k=4)
    #print("Detail confirmed,: ")
    #print("Your Secret Attendance Code is: ")
    code_to_return = ""
    for value in my_code:
        code_to_return += str(value)
        confirm_code = Label(new_window, text="Detail confirmed\n"+"Your Secret Attendance Code is:\n " + code_to_return)
        confirm_code.grid(row=3, column=1)
        #print(value, end="")


code_label = Label(root, text="Enter Attendance Code")
code_label.grid(row=0, column=1)

code_entry = Entry(root, width=30)
code_entry.insert(0, "Enter your secret code here")
code_entry.grid(row=1, column=1, padx=20)

#Code Buttons
submit_button = Button(root, text="SUBMIT CODE", command=root_submit)
submit_button.grid(row=2, column=0)

cancel_button = Button(root, text="CANCEL", command=root.quit)
cancel_button.grid(row=2, column=2)

#New Entrants Alternative:
alternative = Label(root, text="--OR--")
alternative.grid(row=4, column=1)

alternative_prompt = Label(root, text="FIRST TIME ENTRANT?")
alternative_prompt.grid(row=5, column=1)

SIGNUP_button = Button(root, text="SIGN-UP", command=sign_up)
SIGNUP_button.grid(row=6, column=1)


def admin():
    admin_window = Toplevel()
    admin_window.title("ADMINISTRATIVE")
    admin_window.geometry("400x400")
    retrieval_button = Button(admin_window, text="VIEW ATTENDEES")
    retrieval_button.grid(row=0, column=1, pady=10)

    #DropDown_Menu
    def exporter():
        drop_window = Toplevel()
        drop_window.title("Export as a File")
        drop_window.geometry("300x300")

        drop_label = Label(drop_window, text="Choose File Type")
        drop_label.grid(row=0, column=0)

        drop_button = Button(drop_window, text="Download")
        drop_button.grid(row=3, column=0)

        choice = StringVar()
        file_types = OptionMenu(drop_window, choice, ".pdf", ".xlsx", ".csv")
        file_types.grid(row=9, column=0)


    export_button = Button(admin_window, text="Export Table", command=exporter)
    export_button.grid(row=8, column=1, pady=10)


#Administrative:
admin_button = Button(root, text="ADMINISTRATIVE", command=admin)
admin_button.grid(row=7, column=1, columnspan=1)


root.mainloop()
