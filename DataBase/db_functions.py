import sqlite3 as sql
import os.path as path
import sys
sys.path.insert(0, '..')

from DataBase import config


def db_init():
    # Create/Open and initialize a database
    if db_exists('student_details'):
        config.DB = sql.connect('student_details.db')
        config.C = config.DB.cursor()
        print('Database already exists')

    else:
        config.DB = sql.connect('student_details.db')
        config.C = config.DB.cursor()
        config.C.execute('CREATE TABLE Students(Name TEXT, Email TEXT, Mobile TEXT, Course TEXT, Cohort TEXT, '
                         'Reg_No TEXT)')
        config.DB.commit()
        print('Table created')


def db_exists(db_name):
    if path.isfile(db_name + '.db'):
        return True
    else:
        return False


def get_id(email):
    entry_id = "SELECT rowid, * FROM Contacts WHERE Email = ?"
    config.C.execute(entry_id, [email])
    for row in config.C:
        return row[0]


def insert_student(student):
    config.C.execute('INSERT INTO Students VALUES (?,?,?,?,?,?)',
                  student)
    config.DB.commit()



def get_entry(entry_id):
    config.C.execute("SELECT * FROM Students WHERE rowid = ?", [entry_id])
    return config.C


def db_commit():
    config.DB.commit()


def edit_student(entry_id, entry):
    entry_update = '''UPDATE Students SET Name= ?, Email =?, Mobile = ?, Course = ?, Cohort =? WHERE rowid = ? '''

    config.C.execute(entry_update, [entry[0], entry[1], entry[2], entry[3],
                                 entry[4], '{}'.format(entry_id)])


def search_student(search_str):
    search_name = '''SELECT * FROM Students WHERE (Name|| Email || Mobile || Course || Cohort || Reg_No) LIKE '%' || ? || '%' 
    ORDER BY Email ASC '''
    config.C.execute(search_name, [search_str])

    return config.C
