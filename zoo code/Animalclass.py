from tkinter import *
from tkinter import ttk

import pymysql


class Animal:
     def __init__(self, root):
        self.root = root #main window for GUI
        self.root.title("ZOO Management System")
        self.root.geometry("1600x1024+0+0")

        title = Label(self.root,text = "Zoo Management System",bd=10,relief = GROOVE,font = ("times new roman",40,"bold"),bg="yellow",fg="red" )
        title.pack(side=TOP,fill = X)
        #-------------------------------VARIABLES -------------------------
        self.animal_ID_var = StringVar()
        self.animal_type_var = StringVar()
        self.animal_breed_var = StringVar()
        self.ani_dob_var = StringVar()
        self.animal_dateofarrival_var = StringVar()
        self.gender_var = StringVar()
        self.diet_var =StringVar()
        self.weight_var =StringVar()
        self.disposedate_var =StringVar()
        self.cageID = StringVar()
        self.Emp_ID = StringVar()

        #======================================MANAGE FRAMES =========================================================
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#f0e8c9")
        Manage_Frame.place(x=10,y=90,width=1900,height=60)

        AddUpdateBtn = Button(Manage_Frame,text="Add/Update",command=self.addanimal,font = ("times new roman",20,"bold"), width=20).grid(row=0,column=0,padx=5,pady=5)
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
        AddBtn = Button(Btn_Frame2, text="Add",command =self.addanimal, font=("times new roman", 20, "bold"), width=20).grid(
            row=0, column=0, padx=10, pady=10)
        UpdateBtn = Button(Btn_Frame2, text="Update",command =self.updateanimal, font=("times new roman", 20, "bold"),
                                 width=20).grid(row=1, column=0, padx=10, pady=10)
        DeleteBtn = Button(Btn_Frame2, text="Delete",command = self.delete_animal, font=("times new roman", 20, "bold"),
                                  width=20).grid(row=2, column=0, padx=10, pady=10)
        ClearBtn = Button(Btn_Frame2, text="clear All Fields",command=self.clear, font=("times new roman", 20, "bold"),
                           width=20).grid(row=3, column=0, padx=10, pady=10)


        # ======================================FORM FRAMES =========================================================
        Form_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#202842")
        Form_Frame.place(x=400-30, y=170, width=380*2, height=820)

        mtitle = Label(Form_Frame,text="The Form Of Adding/Modify Data",bg="crimson",fg="white",font=("times new roman", 35, "bold") )
        mtitle.grid(row=0, columnspan=4, pady=10, padx=20,sticky="w")

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Animal ID >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_AniID = Label(Form_Frame, text="Animal ID : ", bg="#202842", fg="white",font=("times new roman", 20, "bold"))
        lbl_AniID.grid(row=1, column=0, pady=10, padx=10+5,sticky="w")

        txt_AniID = Entry(Form_Frame,textvariable=self.animal_ID_var, font=("times new roman", 20, "bold"),bd=5,relief=GROOVE)
        txt_AniID.grid(row=1, column=1, pady=10, padx=5, sticky="w")

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Animal Type >>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_AniType = Label(Form_Frame, text="Animal Type : ", bg="#202842", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_AniType.grid(row=2, column=0, pady=10, padx=10 + 5, sticky="w")

        txt_AniType = Entry(Form_Frame,textvariable = self.animal_type_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_AniType.grid(row=2, column=1, pady=10, padx=5, sticky="w")

        #>>>>>>>>>>>>>>>>>>>>>>>>>Breed>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
        lbl_Animal_breed = Label(Form_Frame, text="Animal Breed : ", bg="#202842", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_Animal_breed.grid(row=3, column=0, pady=10, padx=10 + 5, sticky="w")

        txt_Animal_breed = Entry(Form_Frame, textvariable=self.animal_breed_var, font=("times new roman", 20, "bold"), bd=5,
                            relief=GROOVE)
        txt_Animal_breed.grid(row=3, column=1, pady=10, padx=5, sticky="w")

        # >>>>>>>>>>>>>>>>>>>>>>>COMBOBOX FOR GENDER >>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_Anigender = Label(Form_Frame, text="Gender : ", bg="#202842", fg="white",
                              font=("times new roman", 20, "bold"))
        lbl_Anigender.grid(row=4, column=0, pady=10, padx=10 + 5, sticky="w")

        Anigender = ttk.Combobox(Form_Frame,textvariable=self.gender_var, font=("times new roman", 15), state ='readonly')
        Anigender['values'] = ('M', 'F')
        Anigender.current(0)
        Anigender.grid(row=4, column=1, pady=10, padx= 5, sticky="w")

        #>>>>>>>>>>>>>>>>>>>>>>>>>DATE OF BIRTH >>>>>>>>>>>>>>>>>>>>>>>>
        lbl_Anidob = Label(Form_Frame, text="Date of Birth : ", bg="#202842", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Anidob.grid(row=5, column=0, pady=10, padx=15, sticky="w")

        txt_Anidob = Entry(Form_Frame,textvariable = self.ani_dob_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_Anidob.grid(row=5, column=1, pady=10, padx=5, sticky="w")


        #>>>>>>>>>>>>>>>>>r>>>>>>>>>>>>>>>Weight >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_Weight = Label(Form_Frame,text="Weight: ", bg="#202842", fg="white",font=("times new roman", 20, "bold"))
        lbl_Weight.grid(row=7, column=0, pady=10, padx=10 + 5, sticky="w")

        txt_Weight = Entry(Form_Frame,textvariable=self.weight_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_Weight.grid(row=7, column=1, pady=10, padx=5, sticky="w")

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>JOINING DATE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_Join = Label(Form_Frame, text="Date Of Arrival: ", bg="#202842", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Join.grid(row=8, column=0, pady=10, padx=10 + 5, sticky="w")

        txt_Join = Entry(Form_Frame,textvariable=self.animal_dateofarrival_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_Join.grid(row=8, column=1, pady=10, padx=5, sticky="w")



        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Diet>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_Diet = Label(Form_Frame, text="Diet  : ", bg="#202842", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Diet.grid(row=9, column=0, pady=10, padx=10 + 5, sticky="w")

        txt_Diet = Entry(Form_Frame,textvariable=self.diet_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_Diet.grid(row=9, column=1, pady=10, padx=5, sticky="w")
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Dispose Date >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_Dispose_Date = Label(Form_Frame, text="Dispose Date   : ", bg="#202842", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Dispose_Date.grid(row=12, column=0, pady=10, padx=10 + 5, sticky="w")

        txt_Dispose_Date = Entry(Form_Frame, textvariable=self.disposedate_var, font=("times new roman", 20, "bold"), bd=5,
                           relief=GROOVE)
        txt_Dispose_Date.grid(row=12, column=1, pady=10, padx=5, sticky="w")


        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Cage ID >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_CageID = Label(Form_Frame, text="Cage ID: ", bg="#202842", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_CageID.grid(row=10, column=0, pady=10, padx=10 + 5, sticky="w")

        txt_CageID = Entry(Form_Frame,textvariable = self.cageID, width=10, font=("times new roman", 20, "bold"), bd=5,
                                 relief=GROOVE)
        txt_CageID.grid(row=10, column=1, pady=10, padx=5, sticky="w")
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Emp ID >>>>>>>>>>>>>>>>>>>>>>>>
        lbl_EmpID = Label(Form_Frame, text="Emp ID: ", bg="#202842", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_EmpID.grid(row=11, column=0, pady=10, padx=10 + 5, sticky="w")

        txt_EmpID = Entry(Form_Frame,textvariable=self.Emp_ID, width=10, font=("times new roman", 20, "bold"), bd=5,
                                relief=GROOVE)
        txt_EmpID.grid(row=11, column=1, pady=10, padx=5, sticky="w")


        # ======================================RESULT FRAMES =========================================================
        Result_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#c9e7f0")
        Result_Frame.place(x=400+380*2+10-30, y=170, width=360+380+30, height=820-80)

        Rtitle = Label(Result_Frame, text="Result Window ", bg="crimson", fg="white", font=("times new roman", 35, "bold"))
        Rtitle.grid(row=0, columnspan=4, pady=10, padx=20, sticky="w")



#Functions
     #-----------------------------Function to Add in Animal --------------------------------
     def addanimal(self):
        con = pymysql.connect(user='root', password='Password@21',
                              host='localhost', database='ZOOMANAGEMENT')
        cur = con.cursor()
        query= "insert into animal(animal_ID,animal_type,breed,date_of_arrival,gender,diet,weight,birth_date,disposed,Emp_ID,cage_ID) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(self.animal_ID_var.get(),self.animal_type_var.get(),self.animal_breed_var.get(),self.animal_dateofarrival_var.get(),self.gender_var.get(),self.diet_var.get(),self.weight_var.get(),self.ani_dob_var.get(),self.disposedate_var.get(),self.Emp_ID.get(),self.cageID.get())
                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                  
        print("Query Executed")

        cur.execute(query)
        con.commit()
        con.close()
     #--------------------Function to Update in animal ---------------------------------------

     def updateanimal(self):
         con = pymysql.connect(user='root', password='Password@21',
                              host='localhost', database='ZOOMANAGEMENT')
         cur = con.cursor()
         query = "update animal set animal_ID = '{}', animal_type = '{}', breed = '{}', date_of_arrival = '{}',gender = '{}',diet = '{}', weight = '{}', birth_date = '{}', disposed = '{}', Emp_ID = '{}', cage_ID = '{}' where animal_ID = '{}'".format(
            self.animal_ID.get(),self.animal_type_var.get(),                                                                           self.animal_breed_var.get(),                                                                                                                                                             self.ani_dob_var.get(),    self.gender_var.get(),                                                                                                                                                               self.animal_dateofarrival_var.get(),                                                                                                                                                                                                                                                         self.diet_var.get(),                                                                                                                                      self.weight_var.get(),self.disposedate_var.get(),self.cageID.get(),self.Emp_ID.get())
            
         print("Query Executed")

         cur.execute(query)
         con.commit()
         con.close()
         
         
    #Delete animal
    
     def delete_animal(self):
         con = pymysql.connect(user='root', password='Password@21', host='localhost', database='ZOOMANAGEMENT')
         cur = con.cursor()
         query = "delete from animal where animal_ID = '{}'".format(self.animal_breed_var.get())
         con.commit()
         con.close()
         
    #-----------------------Function To Clear All Field ---------------------------------
     def clear(self):
         self.animal_ID_var.set("")
         self.animal_type_var.set("")
         self.animal_breed_var.set("")
         self.ani_dob_var.set("")
         self.animal_dateofarrival_var.set("")
         self.gender_var.set("")
         self.diet_var.set("")
         self.weight_var.set("")
         self.disposedate_var.set("")
         self.cageID.set("")
         self.Emp_ID.set("")

    # --------------------------Function To Exit The Program -----------------------------
     def exit(self):
         exit()
         
