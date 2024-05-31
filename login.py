from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from main import Face_Recognition_System

class main_loop:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attendance Management System")

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login")
        
        image_path5 = r"C:\face_recognition_system\image\OIP14.jpg"
        self.image5 = Image.open(image_path5)
        self.photo5 = ImageTk.PhotoImage(self.image5)
        self.label5 = Label(root, image=self.photo5)
        self.label5.place(x=0, y=0, width=1550, height=910)
        
        main_frame = Frame(self.label5, bd=2, bg="black")
        main_frame.place(x=500, y=150, width=500, height=480)
        
        image_path1 = r"C:\face_recognition_system\image\img12.jpg"
        self.image1 = Image.open(image_path1)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.label1 = Label(root, image=self.photo1, bg="white", borderwidth=0)
        self.label1.place(x=710, y=165, width=100, height=100)
        
        get_str = Label(main_frame, text="Get Started", font=("times new roman", 20, "bold"), bg="black", fg="white")
        get_str.place(x=0, y=120, width=520, height=40)
        
        lbl_username = Label(main_frame, text="Username:", font=("times new roman", 15, "bold"), bg="black", fg="white")
        lbl_username.place(x=50, y=200, width=120, height=30)
        self.txt_username = Entry(main_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_username.place(x=180, y=200, width=250, height=30)
        
        lbl_password = Label(main_frame, text="Password:", font=("times new roman", 15, "bold"), bg="black", fg="white")
        lbl_password.place(x=50, y=250, width=120, height=30)
        self.txt_password = Entry(main_frame, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_password.place(x=180, y=250, width=250, height=30)
        
        btn_login = Button(main_frame, text="Login", command=self.login_function, font=("times new roman", 20, "bold"), bg="blue", fg="white", activeforeground="white", activebackground="blue")
        btn_login.place(x=200, y=300, width=120, height=45)
        
    def login_function(self):
        if self.txt_username.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        elif self.txt_username.get() != "Admin" or self.txt_password.get() != "123456":
            messagebox.showerror("Error", "Invalid Username/Password", parent=self.root)
        else:
            messagebox.showinfo("Welcome","WELCOME TO SMART ATTENDANCE MANAGEMENT SYSTEM",parent=self.root)
            self.root.destroy()  
            main_root = Tk()  
            main_window = Face_Recognition_System(main_root)  
            main_root.mainloop()  

if __name__ == "__main__":
    root = Tk()
    obj = Login_window(root)
    root.mainloop()
