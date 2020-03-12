from tkinter import *
from tkinter import ttk
import pymysql
class Student:
	def __init__(self,root):
		self.root=root
		self.root.title("Student Management System")
		self.root.geometry("1600x850+0+0")

		title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
		title.pack(side=TOP,fill=X)

		#All variables
		self.rollno_var=StringVar()
		self.name_var=StringVar()
		self.email_var=StringVar()
		self.gender_var=StringVar()
		self.contact_var=StringVar()
		self.dob_var=StringVar()

        #Manage Frame
		Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
		Manage_Frame.place(x=20,y=100,width=500,height=700)

		m_title=Label(Manage_Frame,text="Manage Student",bg="green",fg="white",font=("times new roman",30,"bold"))
		m_title.grid(row=0,columnspan=2,pady=20)

		lbl_roll=Label(Manage_Frame,text="Roll No:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
		lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

		text_roll=Entry(Manage_Frame,textvariable=self.rollno_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
		text_roll.grid(row=1,column=1,pady=10,padx=20)

		lbl_name=Label(Manage_Frame,text="Name:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
		lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

		text_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
		text_name.grid(row=2,column=1,pady=10,padx=20)

		lbl_email=Label(Manage_Frame,text="Email:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
		lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

		text_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
		text_email.grid(row=3,column=1,pady=10,padx=20)

		lbl_gender=Label(Manage_Frame,text="Gender:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
		lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

		combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",20,"bold"),state="readonly")
		combo_gender["values"]=("MALE","FEMALE","OTHERS")
		combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        
        

		lbl_contact=Label(Manage_Frame,text="Contact:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
		lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

		text_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
		text_contact.grid(row=5,column=1,pady=10,padx=20)

		lbl_dob=Label(Manage_Frame,text="D.O.B:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
		lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

		text_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
		text_dob.grid(row=6,column=1,pady=10,padx=20)

		lbl_add=Label(Manage_Frame,text="Address:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
		lbl_add.grid(row=7,column=0,pady=10,padx=20,sticky="w")

		self.txt_add=Text(Manage_Frame,width=35,height=6)
		self.txt_add.grid(row=7,column=1,pady=10,padx=20,sticky="w")

		Btn_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
		Btn_Frame.place(x=40,y=720,width=445)

		add_btn=Button(Btn_Frame,text="ADD",width=7).grid(row=0,column=0,padx=10,pady=10)
		update_btn=Button(Btn_Frame,text="UPDATE",width=7).grid(row=0,column=1,padx=10,pady=10)
		delete_btn=Button(Btn_Frame,text="DELETE",width=7).grid(row=0,column=2,padx=10,pady=10)
		clear_btn=Button(Btn_Frame,text="CLEAR",width=7).grid(row=0,column=3,padx=10,pady=10)

        #Manage Frame
		Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
		Detail_Frame.place(x=550,y=100,width=1000,height=700)

		lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
		lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

		combo_search=ttk.Combobox(Detail_Frame,width=10,font=("times new roman",20,"bold"),state="readonly")
		combo_search["values"]=("Name","Roll","Contact")
		combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")

		text_search=Entry(Detail_Frame,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
		text_search.grid(row=0,column=2,pady=10,padx=20)

		search_btn=Button(Detail_Frame,text="SEARCH",width=7).grid(row=0,column=3,padx=10,pady=10)
		showall_btn=Button(Detail_Frame,text="SHOW ALL",width=7).grid(row=0,column=4,padx=10,pady=10)

		#table frame

		Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
		Table_Frame.place(x=20,y=80,width=960,height=540)

		scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
		scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
		Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","add"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_x.config(command=Student_table.xview)
		scroll_y.config(command=Student_table.yview)
		Student_table.heading("roll",text="ROLL NO")
		Student_table.heading("name",text="NAME")
		Student_table.heading("email",text="EMAIL")
		Student_table.heading("gender",text="GENDER")
		Student_table.heading("contact",text="CONTACT")
		Student_table.heading("dob",text="DOB")
		Student_table.heading("add",text="ADDRESS")
		Student_table.column("roll",width=130)
		Student_table.column("name",width=210)
		Student_table.column("email",width=250)
		Student_table.column("gender",width=130)
		Student_table.column("contact",width=180)
		Student_table.column("dob",width=130)
		Student_table.column("add",width=400)
		Student_table['show']='headings'
		Student_table.pack(fill=BOTH,expand=1)
	def add_student(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="stm")





root=Tk()
ob=Student(root)
root.mainloop()
