from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attendance Management System")
        
        
        
        title_lbl=Label(self.root,text="TRAIN  DATA  SET",font=("times new roman",35,"bold"),bg="black",fg="yellow")
        title_lbl.place(x=0, y=0, width=1550,height=40)
        
        # First image
        image_path1 = r"C:\face_recognition_system\image\OIP75.jpg"
        self.image1 = Image.open(image_path1)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.label1 = Label(root, image=self.photo1)
        self.label1.place(x=0, y=50, width=400, height=325)
        
        # Second image
        image_path2 = r"C:\face_recognition_system\image\OIP75.jpg"
        self.image2 = Image.open(image_path2)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.label2 = Label(root, image=self.photo2)
        self.label2.place(x=400, y=50, width=400, height=325)
        
        
        # Third image
        image_path3 = r"C:\face_recognition_system\image\OIP75.jpg"
        self.image3 = Image.open(image_path3)
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.label3 = Label(root, image=self.photo3)
        self.label3.place(x=800, y=50, width=400, height=325)

        # Fourth image
        image_path4 = r"C:\face_recognition_system\image\OIP75.jpg"
        self.image4 = Image.open(image_path4)
        self.photo4 = ImageTk.PhotoImage(self.image4)
        self.label4 = Label(root, image=self.photo4)
        self.label4.place(x=1200, y=50, width=400, height=325)
        
        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0, y=350, width=1530,height=80)
        
        
        # Fifth image
        image_path5 = r"C:\face_recognition_system\image\OIP83.jpg"
        self.image5 = Image.open(image_path5)
        self.photo5 = ImageTk.PhotoImage(self.image5)
        self.label5 = Label(root, image=self.photo5)
        self.label5.place(x=0, y=425, width=400, height=400)
        
        # sixth image
        image_path6 = r"C:\face_recognition_system\image\OIP83.jpg"
        self.image6 = Image.open(image_path6)
        self.photo6 = ImageTk.PhotoImage(self.image6)
        self.label6 = Label(root, image=self.photo6)
        self.label6.place(x=400, y=425, width=400, height=400)
        
        
        # seventh image
        image_path7 = r"C:\face_recognition_system\image\OIP83.jpg"
        self.image7 = Image.open(image_path7)
        self.photo7 = ImageTk.PhotoImage(self.image7)
        self.label7 = Label(root, image=self.photo7)
        self.label7.place(x=800, y=425, width=400, height=400)
        
        
        # eighth image
        image_path8 = r"C:\face_recognition_system\image\OIP83.jpg"
        self.image8 = Image.open(image_path8)
        self.photo8 = ImageTk.PhotoImage(self.image8)
        self.label8 = Label(root, image=self.photo8)
        self.label8.place(x=1200, y=425, width=400, height=400)
        
    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image_path in path:
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Load image as grayscale
            id = int(os.path.split(image_path)[1].split('.')[1])

            faces.append(img)
            ids.append(id)

        ids = np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")

        messagebox.showinfo("Result", "Training datasets completed successfully",parent=self.root)

                        

        
        



if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()