from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognation System")

#===================== Variables ======================
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



# First Image
        img=Image.open(r"D:\Final Year Project\Face Recognation System\Images\smart-attendance.jpg")
        img =img.resize((505,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=505,height=130)

# Second Image
        img1=Image.open(r"D:\Final Year Project\Face Recognation System\Images\iStock-182059956_18390_t12.jpg")
        img1 =img1.resize((550,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)

# Third Image
        img2=Image.open(r"D:\Final Year Project\Face Recognation System\Images\face-recognition.png")
        img2 =img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1050,y=0,width=500,height=130)

# BG Image
        img3=Image.open(r"D:\Final Year Project\Face Recognation System\Images\wp2551980.jpg")
        img3 =img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="Welcome To Student Pannel", font=("OCR A Extended",35,"bold"),bg="white",fg="navyblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=15,y=55,width=1500,height=600)

# Left label Frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",fg="navyblue",font=("Papyrus"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"D:\Final Year Project\Face Recognation System\Images\AdobeStock_303989091.jpeg")
        img_left =img_left.resize((710,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=710,height=130)

# ================== Current Course ====================
        
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("verdana",12,"bold"),fg="navyblue")
        current_course_frame.place(x=5,y=135,width=720,height=110)

# label Department
        dep_label=Label(current_course_frame,text="Department",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        #combo box 
        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.var_dep,width=15,font=("verdana",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","Civil","Mechanical","Electrical","ETC")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)

# label Course
        dep_label=Label(current_course_frame,text="Course",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=0,column=2,padx=10,sticky=W)

        #combo box 
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course, width=15,font=("verdana",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Course","Diploma","B-Tech","ITI","PHD","M-Tech")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=3,pady=10,sticky=W)

# label Year
        dep_label=Label(current_course_frame,text="Year",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=1,column=0,padx=10,sticky=W)

        #combo box 
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year, width=15,font=("verdana",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Year","2017-20","2018-21","2019-22","2020-23","2021-24")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=3,pady=10,sticky=W)

# label Semester
        dep_label=Label(current_course_frame,text="Semester",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=1,column=2,padx=10,sticky=W)

        #combo box 
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester, width=15,font=("verdana",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=3,pady=10,sticky=W)

# =================== Class Student Information =======================
        
        class_Student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("verdana",12,"bold"),fg="navyblue")
        class_Student_frame.place(x=5,y=250,width=720,height=300)

# Student id
        studentId_label = Label(class_Student_frame, text="Student ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id, width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)      

# Student name
        student_name_label = Label(class_Student_frame,text="Student Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name, width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

# Class Didvision
        student_div_label = Label(class_Student_frame,text="Class Division:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div, width=13,font=("verdana",12,"bold"),state="readonly")
        div_combo["values"]=("Morning","Afternoon")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W) 

# Roll No
        student_roll_label = Label(class_Student_frame,text="Roll-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll, width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)  

# Gender
        student_gender_label = Label(class_Student_frame,text="Gender:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #combo box 
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender, width=13,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Transgender")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

# Date of Birth
        student_dob_label = Label(class_Student_frame,text="DOB:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        student_dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob, width=15,font=("verdana",12,"bold"))
        student_dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

# Email
        student_email_label = Label(class_Student_frame,text="Email:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email, width=15,font=("verdana",12,"bold"))
        student_email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

# Phone Number
        student_mob_label = Label(class_Student_frame,text="Mob-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_mob_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        student_mob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_mob, width=15,font=("verdana",12,"bold"))
        student_mob_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

# Address
        student_address_label = Label(class_Student_frame,text="Address:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address, width=15,font=("verdana",12,"bold"))
        student_address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

# Teacher Name
        student_tutor_label = Label(class_Student_frame,text="Teacher Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_tutor_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        student_tutor_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher, width=15,font=("verdana",12,"bold"))
        student_tutor_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

# Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=10,pady=5,sticky=W)
                       
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="No Photo Sample",value="No")
        radiobtn1.grid(row=5,column=1,padx=10,pady=5,sticky=W)   

# =================== Button Frame ===========================================
        
        btn_frame = Frame(bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=60,y=700,width=635,height=60)

# save button
        save_btn=Button(btn_frame,text="Save", command=self.add_data, width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

# update button
        update_btn=Button(btn_frame,text="Update",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

# delete button
        del_btn=Button(btn_frame,text="Delete",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

# reset button
        reset_btn=Button(btn_frame,text="Reset",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

# take photo button
        take_photo_btn=Button(btn_frame,text="Take Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

# update photo button
        update_photo_btn=Button(btn_frame,text="Update Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_photo_btn.grid(row=0,column=5,padx=5,pady=10,sticky=W)             

#----------------------------------------------------------------------            

# ================= Right label Frame =============================
        
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",fg="navyblue",font=("Papyrus"))
        Right_frame.place(x=750,y=10,width=720,height=580)        

# Searching System in Right Label Frame 
        
        search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(x=10,y=5,width=695,height=80)

# Phone Number
        search_label = Label(search_frame,text="Search by:",font=("verdana",10,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        #combo box 
        search_combo=ttk.Combobox(search_frame,width=12,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll-No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        search_entry = ttk.Entry(search_frame,width=15,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

# -----------------------------Table Frame----------------------------------
        
# Searching System in Right Label Frame 
        
        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=695,height=440)

# Scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

# create table 
        self.student_table = ttk.Treeview(table_frame,column=("ID","Name","Dep","Course","Year","Sem","Div","Gender","DOB","Mob-No","Address","Roll-No","Email","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Mob-No",text="Mob-No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Roll-No",text="Roll-No")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSample")
        self.student_table["show"]="headings"

        # Set Width of Colums 
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Mob-No",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Roll-No",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)

# ==================Function Decleration==============================
        
    def add_data(self):
        if self.var_dep.get()=="Select Department" :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='12345',host='localhost',port=3306,database='face_recognition')
                mycursor = conn.cursor()
                mycursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_div.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_mob.get(),
                self.var_address.get(),
                self.var_roll.get(),
                self.var_email.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
                ))

                conn.commit()
                # self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added Successfully ",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)        

if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()        