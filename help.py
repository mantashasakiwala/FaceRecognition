from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

import mysql.connector
import cv2

class Helpdesk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attendance Management System")
        
        title_lbl=Label(self.root,text="HELP  DESK",font=("times new roman",35,"bold"),bg="yellow",fg="black")
        title_lbl.place(x=0, y=0, width=1550,height=40)
        
        
        image_path1 = r"C:\face_recognition_system\image\img3.jpeg"
        self.image1 = Image.open(image_path1)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.label1 = Label(root, image=self.photo1)
        self.label1.place(x=0, y=45, width=1568, height=750)
        
        
        
        
        help_label=Label(self.label1,text="E-mail:sakiwalamantasha15@gmail.com",font=("times new roman",20,"bold"),bg="white")
        help_label.place(x=550,y=10)
        
        help_label=Label(self.label1,text="E-mail:miralkhunt06@gmail.com",font=("times new roman",20,"bold"),bg="white")
        help_label.place(x=550,y=45)
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Helpdesk(root)
    root.mainloop()        