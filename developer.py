from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attendance Management System")
        
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="yellow",fg="blue")
        title_lbl.place(x=0, y=0, width=1550,height=40)
        
        # First image
        image_path1 = r"C:\face_recognition_system\image\OIP97.png"
        self.image1 = Image.open(image_path1)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.label1 = Label(root, image=self.photo1)
        self.label1.place(x=0, y=45, width=1568, height=750)
        
        
        
        main_frame=Frame(self.label1,bd=2,bg="black")
        main_frame.place(x=1000, y=0, width=500, height=600)
        
        
        image_path2 = r"C:\face_recognition_system\image\OIP98.png"
        self.image2 = Image.open(image_path2)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.label2 = Label(main_frame, image=self.photo2)
        self.label2.place(x=300, y=0, width=190, height=200)
        
        #developer info
        developer_label=Label(main_frame,text="Developed By:",font=("times new roman",20,"bold"),bg="white")
        developer_label.place(x=0,y=5)
        
        developer_label=Label(main_frame,text="Mantasha Sakiwala And Miral Khunt",font=("times new roman",13,"bold"),bg="pink")
        developer_label.place(x=0,y=60)
        
        
        
        image_path3 = r"C:\face_recognition_system\image\img2.jpg"
        self.image3 = Image.open(image_path3)
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.label3 = Label(main_frame, image=self.photo3)
        self.label3.place(x=0, y=210, width=500, height=400)
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()        