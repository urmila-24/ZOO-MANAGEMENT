from tkinter import *
from tkinter import ttk
from ZooStaff import Staff
import pymysql

'''Author : SAGAR VED BAIRWA
    Machine: Ubuntu 20.04'''

class view:
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


        SearchTypelbl = Label(Btn_Frame2,text="Search By",bg="#d996c1",font=("times new roman", 15) )
        SearchTypelbl.grid(row=0,column=0, pady=10, padx=5, sticky="w")

        SearchType = ttk.Combobox(Btn_Frame2, font=("times new roman", 14),state='readonly')
        SearchType['values'] = ('Emp ID', 'Name ', 'Mobile No.')
        SearchType.current(0)
        SearchType.grid(row=0,column=1, pady=10, padx=5, sticky="w")

        SearchTypetxt = Label(Btn_Frame2, text="Input ",bg="#d996c1", font=("times new roman", 15))
        SearchTypetxt.grid(row=1, column=0, pady=10, padx=5, sticky="w")

        txt_search = Entry(Btn_Frame2,textvariable=self.Emp_ID_var, font=("times new roman", 14, "bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=1, column=1, pady=10, padx=5)
        Search_Btn = Button(Btn_Frame2, text="Search",font=("times new roman", 15, "bold"),
                        width=20).grid(
            row=2, columnspan=2, padx=10, pady=10)
        ViewAll_Btn = Button(Btn_Frame2, text="View All", font=("times new roman", 15, "bold"),
                           width=20).grid(row=3, columnspan=2, padx=5, pady=5)
        #DeleteBtn = Button(Btn_Frame2, text="Delete", font=("times new roman", 20, "bold"),
                           #width=20).grid(row=2, column=0, padx=10, pady=10)
        ClearBtn = Button(Btn_Frame2, text="clear All Fields",font=("times new roman", 15, "bold"),
                          width=20).grid(row=4, columnspan=2, padx=5, pady=5)

        # ======================================VIEW FRAMES =========================================================
        View_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#c9e7f0")
        View_Frame.place(x=370, y=170, width=1530, height=820)

        scroll_x = Scrollbar(View_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(View_Frame, orient=VERTICAL)

        self.Staff_table = ttk.Treeview(View_Frame, columns=(
        "Emp_ID", "emp_name", "dob", "gender", "work_as", "Joining_date", "Mobile", "Address"),
                                   xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Staff_table.xview)
        scroll_y.config(command=self.Staff_table.yview)

        self.Staff_table.heading("Emp_ID", text="Employee ID")
        self.Staff_table.heading("emp_name", text="Employee Name")
        self.Staff_table.heading("dob", text="Date Of Birth")
        self.Staff_table.heading("gender", text="Gender")
        self.Staff_table.heading("work_as", text="work_as")
        self.Staff_table.heading("Joining_date", text="Joining_date")
        self.Staff_table.heading("Mobile", text="Mobile")
        self.Staff_table.heading("Address", text="Address")
        self.Staff_table['show'] = 'headings'

        self.Staff_table.column("Emp_ID", width=180)
        self.Staff_table.column("emp_name", width=240)
        self.Staff_table.column("dob", width=180)
        self.Staff_table.column("gender", width=120)
        self.Staff_table.column("work_as", width=160)
        self.Staff_table.column("Joining_date", width=130)
        self.Staff_table.column("Mobile", width=140)
        self.Staff_table.column("Address", width=360)
        self.Staff_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.Staff_table.pack(fill=BOTH, expand=1)
        self.fetchdata()



    # Functions
    def fetchdata(self):
        con = pymysql.connect(user='root', password='Password@21',
                              host='localhost', database='ZOOMANAGEMENT')
        cur = con.cursor()
        query = "select * from staff"
        cur.execute(query)
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Staff_table.delete(*self.Staff_table.get_children())
            for row in rows:
                self.Staff_table.insert('', END, values=row)
            con.commit()
        con.close()

    def get_cursor(self, ev):
        cursor_row = self.Staff_table.focus()
        contents = self.Staff_table.item(cursor_row)
        row = contents['values']
        print(row)

    def exit(self):
        exit()