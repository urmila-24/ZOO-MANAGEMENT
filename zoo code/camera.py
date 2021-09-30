from tkinter import *
from tkinter import ttk

import pymysql


class cameraClass:
     def __init__(self, root):
        self.root = root #main window for GUI
        self.root.title("ZOO Management System")
        self.root.geometry("1600x1024+0+0")

        title = Label(self.root,text = "Zoo Management System",bd=10,relief = GROOVE,font = ("times new roman",40,"bold"),bg="yellow",fg="red" )
        title.pack(side=TOP,fill = X)
        #-------------------------------VARIABLES -------------------------
        self.camera_ID_var = StringVar()
        self.cage_ID_var = StringVar()
        self.Installation_date_var = StringVar()
        self.warranty_var = StringVar()
        

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
        ModifycameraBtn = Button(Btn_Frame, text="Modify In camera", font=("times new roman", 20, "bold"), width=20).grid(row=0, column=0, padx=10, pady=10)
        ModifyAnimalBtn = Button(Btn_Frame, text="Modify In Animal", font=("times new roman", 20, "bold"), width=20).grid(row=1, column=0,padx=10, pady=10)
        ModifyVisitorBtn = Button(Btn_Frame, text="Modify In Visitor", font=("times new roman", 20, "bold"), width=20).grid(row=2, column=0, padx=10, pady=10)
        #++++++++++++++++++++++++++++++++Frame 2 +++++++++++++++++++++++++++++++
        Btn_Frame2 = Frame(Menu_Frame, bd=4, relief=RIDGE, bg="#d996c1")
        Btn_Frame2.place(x=10, y=430, width=320, height=370)
        AddBtn = Button(Btn_Frame2, text="Add",command =self.addcamera, font=("times new roman", 20, "bold"), width=20).grid(
            row=0, column=0, padx=10, pady=10)
        UpdateBtn = Button(Btn_Frame2, text="Update",command =self.updatecamera, font=("times new roman", 20, "bold"),
                                 width=20).grid(row=1, column=0, padx=10, pady=10)
        DeleteBtn = Button(Btn_Frame2, text="Delete",command = self.delete_camera, font=("times new roman", 20, "bold"),
                                  width=20).grid(row=2, column=0, padx=10, pady=10)
        ClearBtn = Button(Btn_Frame2, text="clear All Fields",command=self.clear, font=("times new roman", 20, "bold"),
                           width=20).grid(row=3, column=0, padx=10, pady=10)


        # ======================================FORM FRAMES =========================================================
        Form_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#202842")
        Form_Frame.place(x=400-30, y=170, width=380*2, height=820)

        mtitle = Label(Form_Frame,text="The Form Of Adding/Modify Data ",bg="crimson",fg="white",font=("times new roman", 35, "bold") )
        mtitle.grid(row=0, columnspan=4, pady=10, padx=20,sticky="w")

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>camera ID >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_camera = Label(Form_Frame, text="Camera ID : ", bg="#202842", fg="white",font=("times new roman", 20, "bold"))
        lbl_camera.grid(row=1, column=0, pady=10, padx=10+5,sticky="w")

        txt_camera = Entry(Form_Frame,textvariable=self.camera_ID_var, font=("times new roman", 20, "bold"),bd=5,relief=GROOVE)
        txt_camera.grid(row=1, column=1, pady=10, padx=5, sticky="w")
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>cage ID >>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_cageID = Label(Form_Frame, text="Cage ID : ", bg="#202842", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_cageID.grid(row=2, column=0, pady=10, padx=10 + 5, sticky="w")

        txt_cageID = Entry(Form_Frame,textvariable = self.cage_ID_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_cageID.grid(row=2, column=1, pady=10, padx=5, sticky="w")
        # >>>>>>>>>>>>>>>>>>>>>>>COMBOBOX FOR warranty >>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_Installation_date = Label(Form_Frame, text="Installation Date : ", bg="#202842", fg="white",
                                         font=("times new roman", 20, "bold"))
        lbl_Installation_date.grid(row=3, column=0, pady=10, padx=15, sticky="w")

        txt_Installation_date = Entry(Form_Frame, textvariable=self.Installation_date_var,
                                         font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_Installation_date.grid(row=3, column=1, pady=10, padx=5, sticky="w")

        #>>>>>>>>>>>>>>>>>>>>>>>>>DATE OF BIRTH >>>>>>>>>>>>>>>>>>>>>>>>
        lbl_Warrenty_date = Label(Form_Frame, text="Warrenty : ", bg="#202842", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Warrenty_date.grid(row=4, column=0, pady=10, padx=15, sticky="w")

        txt_Warrenty_date = Entry(Form_Frame,textvariable = self.Installation_date_var, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_Warrenty_date.grid(row=4, column=1, pady=10, padx=5, sticky="w")


      

        # ======================================RESULT FRAMES =========================================================
        Result_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#c9e7f0")
        Result_Frame.place(x=400+380*2+10-30, y=170, width=360+380+30, height=820-80)

        Rtitle = Label(Result_Frame, text="Result Window ", bg="crimson", fg="white", font=("times new roman", 35, "bold"))
        Rtitle.grid(row=0, columnspan=4, pady=10, padx=20, sticky="w")



#Functions
     #-----------------------------Function to Add in camera --------------------------------
     def addcamera(self):
        con = pymysql.connect(user='root', password='Password@21',
                              host='localhost', database='ZOOMANAGEMENT')
        cur = con.cursor()
        query= "insert into camera(camera_ID, cage_ID,Installation_date, warranty) values('{}', '{}', '{}')".format(self.camera_ID_var.get(),
                                                                                                                                                                  self.cage_ID_var.get(),
                                                                                                                                                                  self.Installation_date_var.get(),
                                                                                                                                                                  self.warranty_var.get(),
                                                                                                                                                                  )
        print("Query Executed")

        cur.execute(query)
        con.commit()
        con.close()
     #--------------------Function to Update in camera ---------------------------------------

     def updatecamera(self):
         con = pymysql.connect(user='root', password='Password@21',
                              host='localhost', database='ZOOMANAGEMENT')
         cur = con.cursor()
         query = "update camera set cage_ID = '{}', Installation_date = '{}', warranty = '{}' where camera_ID = '{}'".format(
            self.cage_ID_var.get(), self.Installation_date_var.get(), self.warranty_var.get(),
            self.camera_ID_var.get())
         print("Query Executed")

         cur.execute(query)
         con.commit()
         con.close()
    #Delete camera
     def delete_camera(self):
         con = pymysql.connect(user='root', password='Password@21', host='localhost', database='ZOOMANAGEMENT')
         cur = con.cursor()
         query = "delete from camera where camera_ID = '{}'".format(self.camera_ID_var.get())
         con.commit()
         con.close()
    #-----------------------Function To Clear All Field ---------------------------------
     def clear(self):
        self.camera_ID_var.set(" ")
        self.cage_ID_var.set(" ")
        self.Installation_date_var.set(" ")
        self.warranty_var.set(" ")
        

    # --------------------------Function To Exit The Program -----------------------------
     def exit(self):
         exit()
