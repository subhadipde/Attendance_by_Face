from cmath import e
import collections
from textwrap import fill
from tkinter import*
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

# custom tkinter setting
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class Student:
    def __init__(self, root):
        self.root=root

        # code for full screen height and width
        Width= root.winfo_screenwidth()               
        Height= root.winfo_screenheight()               
        root.geometry("%dx%d" % (Width, Height))

        # for maximize the window
        root.state('zoomed') 

        # root.attributes('-fullscreen', True)                      # for complete full screen view
        self.root.title("Face Recogniton System")

        # bg image
        img3=Image.open(r"images\bgimg.jpg")
        img3=img3.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl=ctk.CTkLabel( text="STUDET MANAGEMENT SYSTEM")
        title_lbl.configure(font=("Lato",25))
        title_lbl.place(relx=0.5, rely=0.05, anchor=CENTER)

        # height and width of the main frame
        ht = 550
        wt = 1200

        # Main Frame
        main_frame = ctk.CTkFrame(root,
                               width=wt,
                               height=ht,
                               corner_radius=10)
        main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)


        
        # left label frame
        Left_frame = ctk.CTkFrame(main_frame,
                               width=wt/2+50,
                               height=ht,
                               corner_radius=10)
        Left_frame.place(relx=0.55, rely=0.5, anchor=E)

        # current course information
        current_course_frame = ctk.CTkFrame(Left_frame,
                               width=wt/2+80,
                               height=100,
                               corner_radius=10)
        current_course_frame.place(relx=0.5, rely=0, anchor=N)

        # Department
        dep_label=ctk.CTkLabel(current_course_frame, text="Department")
        dep_label.configure(font=("Lato",15))
        dep_label.place(relx=0.2, rely=0.2, anchor=NE)

        dep_combo=ttk.Combobox(current_course_frame, font=("times new roman",12,"bold"), state="readonly")
        dep_combo["values"]=("Select Department", "CSE", "IT", "ECE", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.place(relx=0.4, rely=0.2, anchor=N)

        # # Year
        year_label=ctk.CTkLabel(current_course_frame, text="Year")
        year_label.configure(font=("Lato",15))
        year_label.place(relx=0.7, rely=0.7, anchor=E)

        year_combo=ttk.Combobox(current_course_frame, font=("times new roman",12,"bold"), state="readonly")
        year_combo["values"]=("Select Year", "2019-20","2020-21", "2021-22","2022-23")
        year_combo.current(0)
        year_combo.place(relx=0.8, rely=0.6, anchor=N)

        # #Semester
        semester_label=ctk.CTkLabel(current_course_frame, text="Semester")
        semester_label.configure(font=("Lato",15))
        semester_label.place(relx=0.2, rely=0.7, anchor=E)

        semester_combo=ttk.Combobox(current_course_frame, font=("times new roman",12,"bold"), state="readonly")
        semester_combo["values"]=("Select Semester", "Sem-1", "Sem-2", "Sem-3", "Sem-4", "Sem-5", "Sem-6", "Sem-7", "Sem-8")
        semester_combo.current(0)
        semester_combo.place(relx=0.35, rely=0.6, anchor=N)


        # # Class Student information
        class_Student_frame = ctk.CTkFrame(Left_frame,
                               width=wt/2+80,
                               height=450,
                               corner_radius=10)
        class_Student_frame.place(relx=0.5, rely=1, anchor=S)

        # # student id
        studentId_label=ctk.CTkLabel(class_Student_frame, text="StudentID: ")
        studentId_label.configure(font=("Lato",14))
        studentId_label.place(relx=0.2, rely=0.2, anchor=E)

        studentID_entry = ctk.CTkEntry(class_Student_frame,
                               placeholder_text="Enter StudentID here",
                               width=220,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        studentID_entry.place(relx=0.4, rely=0.2, anchor=CENTER)

        # # student name
        studenName_label=ctk.CTkLabel(class_Student_frame, text="Student Name: ")
        studenName_label.configure(font=("Lato",14))
        studenName_label.place(relx=0.25, rely=0.35, anchor=E)

        studentName_entry = ctk.CTkEntry(class_Student_frame,
                               placeholder_text="Enter Name here",
                               width=220,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        studentName_entry.place(relx=0.4, rely=0.35, anchor=CENTER)

        # # Roll No
        roll_no_label=ctk.CTkLabel(class_Student_frame, text="Roll No: ")
        roll_no_label.configure(font=("Lato",14))
        roll_no_label.place(relx=0.20, rely=0.5, anchor=E)

        roll_no_entry = ctk.CTkEntry(class_Student_frame,
                               placeholder_text="Enter Roll here",
                               width=220,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        roll_no_entry.place(relx=0.4, rely=0.5, anchor=CENTER)

        # # Gender
        gender_label=ctk.CTkLabel(class_Student_frame, text="Gender: ")
        gender_label.configure(font=("Lato",14))
        gender_label.place(relx=0.8, rely=0.35, anchor=E)

        gender_combo=ttk.Combobox(class_Student_frame, font=("times new roman",12,"bold"), state="readonly", width=10)
        gender_combo["values"]=("Select", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.place(relx=0.8, rely=0.35, anchor=W)

        # # DOB
        dob_label=ctk.CTkLabel(class_Student_frame, text="DOB: ")
        dob_label.configure(font=("Lato",14))
        dob_label.place(relx=0.20, rely=0.65, anchor=E)

        dob_entry = ctk.CTkEntry(class_Student_frame,
                               placeholder_text="DD/MM/YYYY",
                               width=140,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        dob_entry.place(relx=0.3, rely=0.65, anchor=CENTER)

        phone_label=ctk.CTkLabel(class_Student_frame, text="Phone No: ")
        phone_label.configure(font=("Lato",14))
        phone_label.place(relx=0.65, rely=0.65, anchor=E)

        phone_entry = ctk.CTkEntry(class_Student_frame,
                               placeholder_text="Enter Phone No here",
                               width=180,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        phone_entry.place(relx=0.8, rely=0.65, anchor=CENTER)

        # #buttons

        save_btn=ctk.CTkButton(class_Student_frame, text="Save", cursor="hand2")
        save_btn.place(relx=0.20, rely=0.85,width=160,height=60,  anchor=S)

        update_btn=ctk.CTkButton(class_Student_frame, text="Update", cursor="hand2")
        update_btn.place(relx=0.40, rely=0.85,width=160,height=60,  anchor=S)

        delete_btn=ctk.CTkButton(class_Student_frame, text="Delete", cursor="hand2", fg_color="red")
        delete_btn.place(relx=0.60, rely=0.85,width=160,height=60,  anchor=S)

        reset_btn=ctk.CTkButton(class_Student_frame, text="Reset", cursor="hand2")
        reset_btn.place(relx=0.80, rely=0.85,width=160,height=60,  anchor=S)

        take_photo_btn=ctk.CTkButton(class_Student_frame, text="Take Photo", cursor="hand2")
        take_photo_btn.place(relx=0.3, rely=0.95,width=400,height=60,  anchor=S)

        update_photo_btn=ctk.CTkButton(class_Student_frame, text="Update Photo", cursor="hand2")
        update_photo_btn.place(relx=0.7, rely=0.95,width=400,height=60,  anchor=S)

        # # Right label frame
        Right_frame = ctk.CTkFrame(main_frame,
                               width=wt/2-75,
                               height=ht,
                               corner_radius=10)
        Right_frame.place(relx=0.56, rely=0.5, anchor=W)

        # # ===========================Search System=======================================================
        search_label=ctk.CTkLabel(Right_frame, text="Search By: ")
        search_label.configure(font=("Lato",14))
        search_label.place(relx=0.05, rely=0.1, anchor=W)

        search_combo=ttk.Combobox(Right_frame, font=("times new roman",12,"bold"), state="readonly", width=10)
        search_combo["values"]=("Select", "Roll_No","Student ID")
        search_combo.current(0)
        search_combo.place(relx=0.27, rely=0.1, anchor=W)

        search_entry = ctk.CTkEntry(Right_frame,
                               placeholder_text="Enter here",
                               width=200,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        search_entry.place(relx=0.5, rely=0.1, anchor=W)

        search_btn=ctk.CTkButton(Right_frame, text="Search", cursor="hand2")
        search_btn.place(relx=0.6, rely=0.2,width=180,height=60,  anchor=W)


        # # # ===========================Table Frame=======================================================
        table_frame=Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(relx=0.5, rely=0.9,width=wt/2+100,height=ht-100,  anchor=S)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, columns=("dep","year","sem","id","name","roll","gender","dob","phone","photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading ("name", text="Name")
        self.student_table.heading ("roll", text="Roll")
        self.student_table.heading ("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH,expand=1)

if __name__ == "__main__":
    root=ctk.CTk()
    obj=Student(root)
    root.mainloop()
