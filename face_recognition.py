from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import cv2
import os
import mysql.connector
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attendance Management System")
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="black",fg="yellow")
        title_lbl.place(x=0, y=0, width=1550,height=40)

        # First image
        image_path1 = r"C:\face_recognition_system\image\OIP85.jpg"
        self.image1 = Image.open(image_path1)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.label1 = Label(root, image=self.photo1)
        self.label1.place(x=0, y=40, width=700, height=775)
        
        # Second image
        image_path2 = r"C:\face_recognition_system\image\OIP84.jpg"
        self.image2 = Image.open(image_path2)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.label2 = Label(root, image=self.photo2)
        self.label2.place(x=700, y=50, width=900, height=700)

        
        #button
        b1_1=Button(self.root,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="red",fg="white")
        b1_1.place(x=1005, y=705, width=300,height=40)
    
    
    #face recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn=mysql.connector.connect(host="localhost",username="root",password="Mantasha@123",database=" face_recognition_system")            
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                if n is not None:
                    n = "+".join(n)
                else:
                    n = ""
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                if r is not None:
                    r = "+".join(r)
                else:
                    r = ""
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                if d is not None:
                    d = "+".join(d)
                else:
                    d = ""

                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
            return coord
        
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        
        video_cap.release()
        cv2.destroyAllWindows()
                    
    
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()






