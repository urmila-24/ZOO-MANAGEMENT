from ZooStaff import Staff
from tkinter import *
import mysql.connector as connector
#Function to Display Content in The Frame
#def display_result():
   # greeting_display = tk.Text(master=Result_Frame)

def addStaff():
    con = connector.connect(user='root', password='Password@21',
                                 host='localhost', auth_plugin='mysql_native_password', database='ZOO')
    cur = con.cursor()
    cur.execute("insert into Staff values(%s,%s,%s,%s,%s,%s,%s)"),()
    )