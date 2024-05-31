from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from student import Student
import tkinter
from tkinter import messagebox
import os
from train import Train
import mysql.connector
from attendancemanagement import Attendance
from face_recognition import Face_Recognition
from developer import Developer
from help import Helpdesk



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attendance Management System")
        
        
        # First image
        image_path1 = r"C:\face_recognition_system\image\OIP9.jpg"
        self.image1 = Image.open(image_path1)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.label1 = Label(root, image=self.photo1)
        self.label1.place(x=0, y=0, width=400, height=140)
        
        
        # Second image
        image_path2 = r"C:\face_recognition_system\image\OIP11.jpg"
        self.image2 = Image.open(image_path2)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.label2 = Label(root, image=self.photo2)
        self.label2.place(x=400, y=0, width=400, height=140)
        
        
        # Third image
        image_path3 = r"C:\face_recognition_system\image\OIP10.jpg"
        self.image3 = Image.open(image_path3)
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.label3 = Label(root, image=self.photo3)
        self.label3.place(x=800, y=0, width=400, height=140)

        # Fourth image
        image_path4 = r"C:\face_recognition_system\image\OIP13.jpg"
        self.image4 = Image.open(image_path4)
        self.photo4 = ImageTk.PhotoImage(self.image4)
        self.label4 = Label(root, image=self.photo4)
        self.label4.place(x=1200, y=0, width=400, height=140)
        
        # background image
        image_path5 = r"C:\face_recognition_system\image\OIP23.jpg"
        self.image5 = Image.open(image_path5)
        self.photo5 = ImageTk.PhotoImage(self.image5)
        self.label5 = Label(root, image=self.photo5)
        self.label5.place(x=0, y=140, width=1550, height=710)
        
        title_lbl=Label(self.label5,text="SMART  ATTENDANCE  MANAGEMENT  SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0, y=0, width=1550,height=40)

        
    
        
    
        
        
        #studentdetailsbutton
        image_path6 = r"C:\face_recognition_system\image\OIP27.jpg"
        self.image6 = Image.open(image_path6)
        self.photo6 = ImageTk.PhotoImage(self.image6)

        b1=Button(self.label5,image=self.photo6,command=self.student_details,cursor="hand2")
        b1.place(x=200, y=100, width=220,height=220)

        b1_1=Button(self.label5,text="Students Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=300, width=220,height=40)

        
        #facerecognitionbutton
        image_path7 = r"C:\face_recognition_system\image\OIP48.png"
        self.image7 = Image.open(image_path7)
        self.photo7 = ImageTk.PhotoImage(self.image7)

        b1=Button(self.label5,image=self.photo7,cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=220,height=220)

        b1_1=Button(self.label5,text="Face Recognition",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500, y=300, width=220,height=40)
        
        
        #Attendancebutton
        image_path8 = r"C:\face_recognition_system\image\OIP45.jpg"
        self.image8 = Image.open(image_path8)
        self.photo8 = ImageTk.PhotoImage(self.image8)

        b1=Button(self.label5,image=self.photo8,cursor="hand2",command=self.attendance_data)
        b1.place(x=800, y=100, width=220,height=220)

        b1_1=Button(self.label5,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800, y=300, width=220,height=40)
        
        
        
        #helpdeskbutton
        image_path9 = r"C:\face_recognition_system\image\OIP53.jpg"
        self.image9 = Image.open(image_path9)
        self.photo9 = ImageTk.PhotoImage(self.image9)

        b1=Button(self.label5,image=self.photo9,cursor="hand2",command=self.help_info)
        b1.place(x=1100, y=100, width=220,height=220)

        b1_1=Button(self.label5,text="Help Desk",cursor="hand2",command=self.help_info,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100, y=300, width=220,height=40)
        
        
        
        #traindatabutton
        image_path10 = r"C:\face_recognition_system\image\OIP35.jpg"
        self.image10 = Image.open(image_path10)
        self.photo10 = ImageTk.PhotoImage(self.image10)

        b1=Button(self.label5,image=self.photo10,cursor="hand2",command=self.train_data)
        b1.place(x=200, y=375, width=220,height=220)

        b1_1=Button(self.label5,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=575, width=220,height=40)
        
        
        #photosbutton
        image_path11 = r"C:\face_recognition_system\image\OIP37.jpg"
        self.image11 = Image.open(image_path11)
        self.photo11 = ImageTk.PhotoImage(self.image11)

        b1=Button(self.label5,image=self.photo11,cursor="hand2",command=self.open_img)
        b1.place(x=500, y=375, width=220,height=220)

        b1_1=Button(self.label5,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500, y=575, width=220,height=40)
        
        
        #developerbutton
        image_path12 = r"C:\face_recognition_system\image\OIP46.jpg"
        self.image12 = Image.open(image_path12)
        self.photo12 = ImageTk.PhotoImage(self.image12)

        b1=Button(self.label5,image=self.photo12,cursor="hand2",command=self.developer_info)
        b1.place(x=800, y=375, width=220,height=220)

        b1_1=Button(self.label5,text="Developer",cursor="hand2",command=self.developer_info,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800, y=575, width=220,height=40)
        
        
        #exitbutton
        image_path13 = r"C:\face_recognition_system\image\OIP47.jpg"
        self.image13 = Image.open(image_path13)
        self.photo13 = ImageTk.PhotoImage(self.image13)

        b1=Button(self.label5,image=self.photo13,cursor="hand2",command=self.iExit)
        b1.place(x=1100, y=375, width=220,height=220)

        b1_1=Button(self.label5,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100, y=575, width=220,height=40)
        
    #photofunctionbutton
    def open_img(self):
        os.startfile("data")
    
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
    
    
    
    #functionsbutton
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    
    
    def developer_info(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
        
    def help_info(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpdesk(self.new_window)
    
    
    
    
    
    
    
    
    
    
    
    
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
    