from tkinter import *
from tkinter import ttk

import pymysql


class Staff:
     def __init__(self, root):
        self.root = root #main window for GUI
        self.root.title("ZOO Management System")
        self.root.geometry("1600x1024+0+0")

        title = Label(self.root,text = "Zoo Management System",bd=10,relief = GROOVE,font = ("times new roman",40,"bold"),bg="yellow",fg="red" )
        title.pack(side=TOP,fill = X)
        #-------------------------------VARIABLES -------------------------
        self.Emp_ID_var = StringVar()
        self.emp_name_var = StringVar()
        self.dob_var = StringVar()
        self.gender_var = StringVar()
        self.work_as_var =StringVar()
        self.joining_date_var =StringVar()
        self.mobile_var =StringVar()

        #======================================MANAGE FRAMES =========================================================
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#f0e8c9")
        Manage_Frame.place(x=10,y=90,width=1900,height=60)
        
        AddUpdateBtn = Button(Manage_Frame,text="Add/Update",font = ("times new roman",20,"bold"), width=20).grid(row=0,column=0,padx=5,pady=5)
        VieweBtn = Button(Manage_Frame, text="View ", font=("times new roman", 20, "bold"),width=20).grid(row=0, column=1, padx=5, pady=5)
        TicketBtn = Button(Manage_Frame, text="Ticket ", font=("times new roman", 20, "bold"), width=20).grid(row=0, column=2, padx=5, pady=5)
        ExitBtn = Button(Manage_Frame, text="Exit ",command=exit, font=("times new roman", 20, "bold"), width=20).grid(row=0, column=3, padx=700, pady=5)


        # ======================================MENU FRAMES =========================================================
        Menu_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#c9e7f0")
        Menu_Frame.place(x=10, y=170, width=380-30, height=820)

        #+++++++++++++++++++++++++++++++++++Frame 1 ++++++++++++++++++++++++++++
        Btn_Frame = Frame(Menu_Frame, bd=4, relief=RIDGE, bg="#d996c1")
        Btn_Frame.place(x=10, y=10, width=320, height=400)
        ModifyStaffBtn = Button(Btn_Frame, text="Modify In Staff", font=("times new roman", 20, "bold"), width=20).grid(row=0, column=0, padx=10, pady=10)
        ModifyAnimalBtn = Button(Btn_Frame, text="Modify In Animal", font=("times new roman", 20, "bold"), width=20).grid(row=1, column=0,padx=10, pady=10)
        ModifyVisitorBtn = Button(Btn_Frame, text="Modify In Visitor", font=("times new roman", 20, "bold"), width=20).grid(row=2, column=0, padx=10, pady=10)
        #++++++++++++++++++++++++++++++++Frame 2 +++++++++++++++++++++++++++++++
        Btn_Frame2 = Frame(Menu_Frame, bd=4, relief=RIDGE, bg="#d996c1")
        Btn_Frame2.place(x=10, y=430, width=320, height=370)
        AddBtn = Button(Btn_Frame2, text="Add",command =self.addStaff, font=("times new roman", 20, "bold"), width=20).grid(
            row=0, column=0, padx=10, pady=10)
        UpdateBtn = Button(Btn_Frame2, text="Update",command =self.updatestaff, font=("times new roman", 20, "bold"),
                                 width=20).grid(row=1, column=0, padx=10, pady=10)
        DeleteBtn = Button(Btn_Frame2, text="Delete",command = self.delete_staff, font=("times new roman", 20, "bold"),
                                  width=20).grid(row=2, column=0, padx=10, pady=10)
        ClearBtn = Button(Btn_Frame2, text="clear All Fields",command=self.clear, font=("times new roman", 20, "bold"),
                           width=20).grid(row=3, column=0, padx=10, pady=10)


        # ======================================FORM FRAMES =========================================================
        Form_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#202842")
        Form_Frame.place(x=400-30, y=170, width=380*2, height=820)

        mtitle = Label(Form_Frame,text="The Form Of Adding/Modify Data ",bg="crimson",fg="white",font=("times new roman", 35, "bold") )
        mtitle.grid(row=0, columnspan=4, pady=10, padx=20,sticky="w")

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Employee ID >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_EmpID = Label(Form_Frame, text="Employee ID : ", bg="#202842", fg="white",font=("times new roman", 20, "bold"))
        lbl_EmpID.grid(row=1, column=0, pady=10, padx=10+5,sticky="w")

        txt_EmpID = Entry(Form_Frame,textvariable=self.Emp_ID_var, font=("times new roman", 20, "bold"),bd=5,relief=GROOVE)
        txt_EmpID.grid(row=1, column=1, pady=10, padx=5, sticky="w")
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Emp Name >>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_EmpName = Label(Form_Frame, text="Employee Name : ", bg="#202842", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_EmpName.grid(row=2, column=0, pady=10, padx=10 + 5, sticky="w")

        txt_EmpName = Entry(Form_Frame,textvariable = self.emp_name_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_EmpName.grid(row=2, column=1, pady=10, padx=5, sticky="w")
        # >>>>>>>>>>>>>>>>>>>>>>>COMBOBOX FOR GENDER >>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_Empgender = Label(Form_Frame, text="Gender : ", bg="#202842", fg="white",
                              font=("times new roman", 20, "bold"))
        lbl_Empgender.grid(row=3, column=0, pady=10, padx=10 + 5, sticky="w")

        Empgender = ttk.Combobox(Form_Frame,textvariable=self.gender_var, font=("times new roman", 15), state ='readonly')
        Empgender['values'] = ('M', 'F', 'O')
        Empgender.current(0)
        Empgender.grid(row=3, column=1, pady=10, padx= 5, sticky="w")

        #>>>>>>>>>>>>>>>>>>>>>>>>>DATE OF BIRTH >>>>>>>>>>>>>>>>>>>>>>>>
        lbl_Empdob = Label(Form_Frame, text="Date of Birth : ", bg="#202842", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Empdob.grid(row=4, column=0, pady=10, padx=15, sticky="w")

        txt_Empdob = Entry(Form_Frame,textvariable = self.dob_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_Empdob.grid(row=4, column=1, pady=10, padx=5, sticky="w")


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WORK AS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_WorkAs = Label(Form_Frame,text="Work As : ", bg="#202842", fg="white",font=("times new roman", 20, "bold"))
        lbl_WorkAs.grid(row=7, column=0, pady=10, padx=10 + 5, sticky="w")

        txt_WorkAs = Entry(Form_Frame,textvariable=self.work_as_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_WorkAs.grid(row=7, column=1, pady=10, padx=5, sticky="w")

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>JOINING DATE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_Join = Label(Form_Frame, text="Joining Date: ", bg="#202842", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Join.grid(row=8, column=0, pady=10, padx=10 + 5, sticky="w")

        txt_Join = Entry(Form_Frame,textvariable=self.joining_date_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_Join.grid(row=8, column=1, pady=10, padx=5, sticky="w")



        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>MOBILE FIELD >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_Mobile = Label(Form_Frame, text="Mobile : ", bg="#202842", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Mobile.grid(row=9, column=0, pady=10, padx=10 + 5, sticky="w")

        txt_Mobile = Entry(Form_Frame,textvariable=self.mobile_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_Mobile.grid(row=9, column=1, pady=10, padx=5, sticky="w")

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ADDRESS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_Address = Label(Form_Frame, text="Address : ", bg="#202842", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=10, column=0, pady=10, padx=10 + 5, sticky="w")

        self.txt_Address=Text(Form_Frame, width =30,height = 4, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        self.txt_Address.grid(row=10, column=1, pady=10, padx=5, sticky="w")

        # ======================================RESULT FRAMES =========================================================
        Result_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#c9e7f0")
        Result_Frame.place(x=400+380*2+10-30, y=170, width=360+380+30, height=820-80)

        Rtitle = Label(Result_Frame, text="Result Window ", bg="crimson", fg="white", font=("times new roman", 35, "bold"))
        Rtitle.grid(row=0, columnspan=4, pady=10, padx=20, sticky="w")



#Functions
     #-----------------------------Function to Add in Staff --------------------------------
     def addStaff(self):
        con = pymysql.connect(user='root', password='Password@21',
                              host='localhost', database='ZOOMANAGEMENT')
        cur = con.cursor()
        query= "insert into staff(Emp_ID, emp_name,dob, gender, work_as, joining_date,mobile,Address) values('{}', '{}', '{}','{}','{}', '{}', '{}','{}')".format(self.Emp_ID_var.get(),
                                                                                                                                                                  self.emp_name_var.get(),
                                                                                                                                                                  self.dob_var.get(),
                                                                                                                                                                  self.gender_var.get(),
                                                                                                                                                                  self.work_as_var.get(),
                                                                                                                                                                  self.joining_date_var.get(),
                                                                                                                                                                  self.mobile_var.get(),
                                                                                                                                                                  self.txt_Address.get('1.0',END))
        print("Query Executed")

        cur.execute(query)
        con.commit()
        con.close()
     #--------------------Function to Update in staff ---------------------------------------

     def updatestaff(self):
         con = pymysql.connect(user='root', password='Password@21',
                              host='localhost', database='ZOOMANAGEMENT')
         cur = con.cursor()
         query = "update staff set emp_name = '{}', dob = '{}', gender = '{}', work_as = '{}',joining_date = '{}', mobile = '{}' where Emp_ID = '{}'".format(
            self.emp_name_var.get(), self.dob_var.get(), self.gender_var.get(),
            self.work_as_var.get(), self.joining_date_var.get(), self.mobile_var.get(),self.Emp_ID_var.get())
         print("Query Executed")

         cur.execute(query)
         con.commit()
         con.close()
    #Delete Staff
     def delete_staff(self):
         con = pymysql.connect(user='root', password='Password@21', host='localhost', database='ZOOMANAGEMENT')
         cur = con.cursor()
         query = "delete from staff where Emp_ID = '{}'".format(self.Emp_ID_var.get())
         con.commit()
         con.close()
    #-----------------------Function To Clear All Field ---------------------------------
     def clear(self):
        self.Emp_ID_var.set(" ")
        self.emp_name_var.set(" ")
        self.dob_var.set(" ")
        self.gender_var.set(" ")
        self.work_as_var.set(" ")
        self.joining_date_var.set(" ")
        self.mobile_var.set(" ")

    # --------------------------Function To Exit The Program -----------------------------
     def exit(self):
         exit()
