from tkinter import *
from tkinter import ttk
from ZooStaff import Staff
import pymysql

'''Author : SAGAR VED BAIRWA
    Machine: Ubuntu 20.04'''

class Ticket:
    def __init__(self, root):
        self.root = root  # main window for GUI
        self.root.title("ZOO Management System")
        self.root.geometry("1600x1024+0+0")

        title = Label(self.root, text="Zoo Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)
        # -------------------------------VARIABLES -------------------------
        self.Emp_ID_var = StringVar()
        self.emp_name_var = StringVar()
        self.dob_var = StringVar()
        self.gender_var = StringVar()
        self.work_as_var = StringVar()
        self.joining_date_var = StringVar()
        self.mobile_var = StringVar()

        # ======================================MANAGE FRAMES =========================================================
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#f0e8c9")
        Manage_Frame.place(x=10, y=90, width=1900, height=60)

        AddUpdateBtn = Button(Manage_Frame, text="Add/Update", font=("times new roman", 20, "bold"), width=20).grid(
            row=0, column=0, padx=5, pady=5)
        VieweBtn = Button(Manage_Frame, text="View ", font=("times new roman", 20, "bold"), width=20).grid(row=0,
                                                                                                           column=1,
                                                                                                           padx=5,
                                                                                                           pady=5)
        TicketBtn = Button(Manage_Frame, text="Ticket ", font=("times new roman", 20, "bold"), width=20).grid(row=0,
                                                                                                              column=2,
                                                                                                              padx=5,
                                                                                                              pady=5)
        ExitBtn = Button(Manage_Frame, text="Exit ",command=exit, font=("times new roman", 20, "bold"), width=20).grid(row=0,
                                                                                                          column=3,
                                                                                                          padx=700,
                                                                                                          pady=5)

        # ======================================MENU FRAMES =========================================================
        Menu_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#c9e7f0")
        Menu_Frame.place(x=10, y=170, width=380 - 30, height=820)
        Btn_Frame = Frame(Menu_Frame, bd=4, relief=RIDGE, bg="#d996c1")
        Btn_Frame.place(x=10, y=10, width=320, height=400)
        View_StaffBtn = Button(Btn_Frame, text="View For Staff", font=("times new roman", 20, "bold"), width=20).grid(
            row=0, column=0, padx=10, pady=10)
        View_AnimalBtn = Button(Btn_Frame, text="View For Animal", font=("times new roman", 20, "bold"),
                                 width=20).grid(row=1, column=0, padx=10, pady=10)
        View_VisitorBtn = Button(Btn_Frame, text="View For Visitor", font=("times new roman", 20, "bold"),
                                  width=20).grid(row=2, column=0, padx=10, pady=10)

        Btn_Frame2 = Frame(Menu_Frame, bd=4, relief=RIDGE, bg="#d996c1")
        Btn_Frame2.place(x=10, y=430, width=320, height=370)


        txt_search = Entry(Btn_Frame2,textvariable=self.Emp_ID_var, font=("times new roman", 20, "bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0, column=0, pady=10, padx=5)
        Search_Btn = Button(Btn_Frame2, text="Search",font=("times new roman", 20, "bold"),
                        width=20).grid(
            row=1, column=0, padx=10, pady=10)
        ViewAll_Btn = Button(Btn_Frame2, text="View All", font=("times new roman", 20, "bold"),
                           width=20).grid(row=2, column=0, padx=10, pady=10)
        #DeleteBtn = Button(Btn_Frame2, text="Delete", font=("times new roman", 20, "bold"),
                           #width=20).grid(row=2, column=0, padx=10, pady=10)
        ClearBtn = Button(Btn_Frame2, text="clear All Fields",font=("times new roman", 20, "bold"),
                          width=20).grid(row=3, column=0, padx=10, pady=10)

        # ======================================TICKET  FRAMES =========================================================


    def exit(self):
        exit()