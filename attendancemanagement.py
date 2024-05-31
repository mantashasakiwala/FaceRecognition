from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attendance Management System")
        
        #variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        
        # First image
        image_path1 = r"C:\face_recognition_system\image\OIP88.jpg"
        self.image1 = Image.open(image_path1)
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.label1 = Label(root, image=self.photo1)
        self.label1.place(x=0, y=0, width=800, height=200)
        
        
        # second image
        image_path2 = r"C:\face_recognition_system\image\OIP56.jpg"
        self.image2 = Image.open(image_path2)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.label2 = Label(root, image=self.photo2)
        self.label2.place(x=800, y=0, width=400, height=200)
        
        
        # Third image
        image_path3 = r"C:\face_recognition_system\image\OIP71.jpg"
        self.image3 = Image.open(image_path3)
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.label3 = Label(root, image=self.photo3)
        self.label3.place(x=1200, y=0, width=400, height=200)
        
        # background image
        image_path5 = r"C:\face_recognition_system\image\OIP23.jpg"
        self.image5 = Image.open(image_path5)
        self.photo5 = ImageTk.PhotoImage(self.image5)
        self.label5 = Label(root, image=self.photo5)
        self.label5.place(x=0, y=200, width=1550, height=710)
        
        title_lbl=Label(self.label5,text="ATTENDANCE  MANAGEMENT  SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0, y=0, width=1550,height=40)
        
        main_frame=Frame(self.label5,bd=2,bg="white")
        main_frame.place(x=10, y=50, width=1510, height=600)
        
        #leftlabelframe
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10, y=10, width=760,height=580)
        
        image_path5 = r"C:\face_recognition_system\image\OIP65.jpg"
        self.image5 = Image.open(image_path5)
        self.photo5 = ImageTk.PhotoImage(self.image5)
        self.label5 = Label(left_frame, image=self.photo5)
        self.label5.place(x=3, y=0, width=750, height=140)
        
        
        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0, y=145, width=730, height=370)
        
        
        #label and entry
        
        
        #attendanceID
        attendance_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
        attendance_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendance_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendance_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        
        #rollno
        rollno1_label=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        rollno1_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        rollno1_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        rollno1_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        
        
        #name
        name1_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name1_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        name1_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        name1_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        
        #department
        department1_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        department1_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        department1_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        department1_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
        
        #time
        time1_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time1_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time1_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        time1_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        
        
        #date
        date1_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date1_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date1_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        date1_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        #attendance
        attendance1_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attendance1_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        attendance1_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly",width=18)
        attendance1_combo["values"]=("Status","Present","Absent")
        attendance1_combo.current(0)
        attendance1_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        
        #buttonsframe
        btn_frame=Frame(left_inside_frame,bd=3,relief=RIDGE,bg="white")
        btn_frame.place(x=100, y=300, width=530,height=30)


        #importcsvbutton
        import_btn=Button(btn_frame,text="Import  CSV",command=self.importCsv,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)


        #exportcsvbutton
        export_btn=Button(btn_frame,text="Export  CSV",command=self.exportCsv,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)


       

        #resetbutton
        reset1_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset1_btn.grid(row=0,column=3)
        
        
        
        
        #rightlabelframe
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=780, y=10, width=720,height=580)
        
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5, y=5, width=700,height=455)
        
        
        #scrollbar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
    #fetch data    
    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    #import csv       
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
            
            
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"successfully",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
                
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    
    
        
        
        
    
        
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
        

                        
        
        
        
        





        




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()        