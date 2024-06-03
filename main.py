from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from Student import Student

class Face_recognation_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognation System")

    # First Image
        img=Image.open(r"D:\Final Year Project\Face Recognation System\Images\banner.jpg")
        img =img.resize((505,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=505,height=130)

    # Second Image
        img1=Image.open(r"D:\Final Year Project\Face Recognation System\Images\face-off-banner.jpg")
        img1 =img1.resize((550,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)

    # Third Image
        img2=Image.open(r"D:\Final Year Project\Face Recognation System\Images\banner1.jpg")
        img2 =img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1050,y=0,width=500,height=130)

    # BG Image
        img3=Image.open(r"D:\Final Year Project\Face Recognation System\Images\bg3.jpg")
        img3 =img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM  SOFTWARE", font=("Hobo Std",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

    # Student Button
        img4=Image.open(r"D:\Final Year Project\Face Recognation System\Images\std1.jpg")
        img4 =img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4, command=self.student_pannels, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details", command=self.student_pannels,cursor="hand2",font=("OCR A Extended",15, "bold"), bg="white",fg="blue")
        b1_1.place(x=200,y=300,width=220,height=40)


    # Detect face Button
        img5=Image.open(r"D:\Final Year Project\Face Recognation System\Images\det1.jpg")
        img5 =img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("OCR A Extended",15, "bold"), bg="white",fg="blue")
        b1_1.place(x=500,y=300,width=220,height=40)


    # Attendance Button
        img6=Image.open(r"D:\Final Year Project\Face Recognation System\Images\att.jpg")
        img6 =img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("OCR A Extended",15, "bold"), bg="white",fg="blue")
        b1_1.place(x=800,y=300,width=220,height=40)


    # Help Desk Button
        img7=Image.open(r"D:\Final Year Project\Face Recognation System\Images\hlp.jpg")
        img7 =img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("OCR A Extended",15, "bold"), bg="white",fg="blue")
        b1_1.place(x=1100,y=300,width=220,height=40)

    # Train Face Button
        img8=Image.open(r"D:\Final Year Project\Face Recognation System\Images\tra1.jpg")
        img8 =img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",font=("OCR A Extended",15, "bold"), bg="white",fg="blue")
        b1_1.place(x=200,y=580,width=220,height=40)


    # Photos Face Button
        img9=Image.open(r"D:\Final Year Project\Face Recognation System\Images\f_det1.gif")
        img9 =img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("OCR A Extended",15, "bold"), bg="white",fg="blue")
        b1_1.place(x=500,y=580,width=220,height=40)

    # Developer Button
        img10=Image.open(r"D:\Final Year Project\Face Recognation System\Images\dev.jpg")
        img10 =img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("OCR A Extended",15, "bold"), bg="white",fg="blue")
        b1_1.place(x=800,y=580,width=220,height=40)


    # Exit Button
        img11=Image.open(r"D:\Final Year Project\Face Recognation System\Images\exi.jpg")
        img11 =img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("OCR A Extended",15, "bold"), bg="white",fg="blue")
        b1_1.place(x=1100,y=580,width=220,height=40)

# ==================Functions Buttons=====================
        
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        

    
if __name__ =="__main__":
    root=Tk()
    obj=Face_recognation_system(root)
    root.mainloop()
