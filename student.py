from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector

# custom tkinter setting
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class Student:
    def __init__(self, root):
        self.root=root

        # code for full screen height and width ----------------------------
        Width= root.winfo_screenwidth()               
        Height= root.winfo_screenheight()               
        # root.geometry("%dx%d" % (Width, Height))

        # for maximize the window -------------------------
        # root.state('zoomed') 


        Grid.rowconfigure(root, index=0, weight=1)
        Grid.columnconfigure(root, index=0, weight=1)

         # for complete full screen view --------------------
        root.attributes('-fullscreen', True)
        self.root.title("Face Recogniton System")



        # Variables -------------------------------------------------

        self.dep = StringVar()
        self.batch = StringVar()
        self.sem = StringVar()
        self.id = StringVar()
        self.name = StringVar()
        self.gender = StringVar()
        self.phone = StringVar()
        self.dob = StringVar()
        self.add = StringVar()
        self.search = StringVar()
        self.search_entry = StringVar()

        
        # bg image
        img3=Image.open(r"images\bgimg.jpg")

        img3=img3.resize((Width, Height), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(width=Width,height=Height)

        title_lbl=ctk.CTkLabel(root, text="STUDENT MANAGEMENT SYSTEM")
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
        main_frame.place(relx=0.5, rely=0.55, anchor=CENTER)


        
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
        dep_label=ctk.CTkLabel(current_course_frame, text="Department*")
        dep_label.configure(font=("Lato",15))
        dep_label.place(relx=0.2, rely=0.2, anchor=NE)

        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.dep, font=("times new roman",12,"bold"), state="readonly")
        dep_combo["values"]=("Select Department", "CSE", "IT", "ECE", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.place(relx=0.4, rely=0.2, anchor=N)

        # # Year
        year_label=ctk.CTkLabel(current_course_frame, text="Batch*")
        year_label.configure(font=("Lato",15))
        year_label.place(relx=0.7, rely=0.7, anchor=E)

        year_combo=ttk.Combobox(current_course_frame, textvariable=self.batch, font=("times new roman",12,"bold"), state="readonly")
        year_combo["values"]=("Select Batch", "2018","2019", "2020","2021")
        year_combo.current(0)
        year_combo.place(relx=0.8, rely=0.6, anchor=N)

        # #Semester
        semester_label=ctk.CTkLabel(current_course_frame, text="Semester*")
        semester_label.configure(font=("Lato",15))
        semester_label.place(relx=0.2, rely=0.7, anchor=E)

        semester_combo=ttk.Combobox(current_course_frame, textvariable=self.sem, font=("times new roman",12,"bold"), state="readonly")
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
        studentId_label=ctk.CTkLabel(class_Student_frame, text="StudentID*: ")
        studentId_label.configure(font=("Lato",14))
        studentId_label.place(relx=0.2, rely=0.2, anchor=E)

        studentID_entry = ctk.CTkEntry(class_Student_frame,
                               textvariable=self.id,
                               placeholder_text="Enter StudentID here",
                               width=220,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        studentID_entry.place(relx=0.4, rely=0.2, anchor=CENTER)

        # # student name
        studenName_label=ctk.CTkLabel(class_Student_frame, text="Student Name*: ")
        studenName_label.configure(font=("Lato",14))
        studenName_label.place(relx=0.25, rely=0.35, anchor=E)

        studentName_entry = ctk.CTkEntry(class_Student_frame,
                               textvariable=self.name,
                               placeholder_text="Enter Name here",
                               width=220,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        studentName_entry.place(relx=0.4, rely=0.35, anchor=CENTER)

        # # Address
        add_label=ctk.CTkLabel(class_Student_frame, text="Address*: ")
        add_label.configure(font=("Lato",14))
        add_label.place(relx=0.20, rely=0.5, anchor=E)

        add_entry = ctk.CTkEntry(class_Student_frame,
                               textvariable=self.add,
                               placeholder_text="Enter Address here",
                               width=450,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        add_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        # # Gender
        gender_label=ctk.CTkLabel(class_Student_frame, text="Gender: ")
        gender_label.configure(font=("Lato",14))
        gender_label.place(relx=0.8, rely=0.35, anchor=E)

        gender_combo=ttk.Combobox(class_Student_frame, textvariable=self.gender, font=("times new roman",12,"bold"), state="readonly", width=10)
        gender_combo["values"]=("Select", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.place(relx=0.8, rely=0.35, anchor=W)

        # # DOB
        dob_label=ctk.CTkLabel(class_Student_frame, text="DOB: ")
        dob_label.configure(font=("Lato",14))
        dob_label.place(relx=0.20, rely=0.65, anchor=E)

        dob_entry = ctk.CTkEntry(class_Student_frame,
                               textvariable=self.dob,
                               placeholder_text="DD/MM/YYYY",
                               width=140,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        dob_entry.place(relx=0.3, rely=0.65, anchor=CENTER)
        

        # # Phone no
        phone_label=ctk.CTkLabel(class_Student_frame, text="Phone No: ")
        phone_label.configure(font=("Lato",14))
        phone_label.place(relx=0.65, rely=0.65, anchor=E)

        phone_entry = ctk.CTkEntry(class_Student_frame,
                               textvariable=self.phone,
                               placeholder_text="Enter Phone No here",
                               width=180,
                               height=40,
                               border_width=1,
                               corner_radius=10)
        phone_entry.place(relx=0.8, rely=0.65, anchor=CENTER)

        # #buttons
        
        save_btn=ctk.CTkButton(class_Student_frame,command=self.add_data, text="Save", cursor="hand2")
        save_btn.place(relx=0.15, rely=0.85,width=160,height=60,  anchor=S)

        update_btn=ctk.CTkButton(class_Student_frame, text="Update", cursor="hand2")
        update_btn.place(relx=0.35, rely=0.85,width=160,height=60,  anchor=S)

        delete_btn=ctk.CTkButton(class_Student_frame, text="Delete", cursor="hand2", fg_color="red", text_font=("bold"))
        delete_btn.place(relx=0.65, rely=0.85,width=160,height=60,  anchor=S)

        reset_btn=ctk.CTkButton(class_Student_frame, command=self.reset_data, text="Reset", cursor="hand2")
        reset_btn.place(relx=0.85, rely=0.85,width=160,height=60,  anchor=S)

        take_photo_btn=ctk.CTkButton(class_Student_frame, text="Take Photo", cursor="hand2")
        take_photo_btn.place(relx=0.3, rely=0.98,width=300,height=60,  anchor=S)

        update_photo_btn=ctk.CTkButton(class_Student_frame, text="Update Photo", cursor="hand2")
        update_photo_btn.place(relx=0.7, rely=0.98,width=300,height=60,  anchor=S)

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

        search_combo=ttk.Combobox(Right_frame, textvariable=self.search, font=("times new roman",12,"bold"), state="readonly", width=10)
        search_combo["values"]=("Select", "Roll_No","Student ID")
        search_combo.current(0)
        search_combo.place(relx=0.27, rely=0.1, anchor=W)

        search_entry = ctk.CTkEntry(Right_frame,
                               textvariable=self.search_entry,
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
        table_frame.place(relx=0.5, rely=0.9,width=wt/2,height=ht-100,  anchor=S)
        

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, columns=("dep","batch","sem","id","name","gender","phone","dob","add"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("batch", text="Batch")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Id")
        self.student_table.heading ("name", text="Name")
        self.student_table.heading ("gender", text="Gender")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading ("add", text="Address")
        # self.student_table.heading("photo", text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=95)
        self.student_table.column("batch", width=90)
        self.student_table.column("sem", width=80)
        self.student_table.column("id", width=35)
        self.student_table.column("name", width=150)
        self.student_table.column("gender", width=65)
        self.student_table.column("phone", width=90)
        self.student_table.column("dob", width=90)
        self.student_table.column("add", width=150)
        # self.student_table.column("photo", width=60)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        # # Exit button        
        b6_1=ctk.CTkButton(Right_frame,text="Exit", cursor="hand2", command = root.destroy, fg_color="red", text_font=("Verdana",13,"bold"))
        b6_1.place(relx=0.8, rely=0.95,width=200,height=60,  anchor=CENTER)


    # -----------------function works-----------------------------------------------------------------------
    def add_data(self):
        if self.dep.get()=="Select Department" or self.batch.get()=="Select Batch" or self.sem.get()=="Select Semester" or self.id.get()=="" or self.add.get()=="":
            messagebox.showerror("Error", "All (*) fields are required!", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Subhadip@321#", database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.dep.get(),
                                                                                            self.batch.get(),
                                                                                            self.sem.get(),
                                                                                            self.id.get(),
                                                                                            self.name.get(),
                                                                                            self.gender.get(),
                                                                                            self.phone.get(),
                                                                                            self.dob.get(),
                                                                                            self.add.get()

                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","The Student Data has saved", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}", parent=self.root)

    # ===============fetch Data====================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Subhadip@321#", database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    # ===============get cursor==================

    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.dep.set(data[0]),
        self.batch.set(data[1]),
        self.sem.set(data[2]),
        self.id.set(data[3]),
        self.name.set(data[4]),
        self.gender.set(data[5]),
        self.phone.set(data[6]),
        self.dob.set(data[7]),
        self.add.set (data[8])

    def reset_data(self):
        self.dep.set("Select Department")
        self.year.set("Select Year")
        self.sem.set("Select Semester")
        self.id.set("")
        self.name.set("")
        self.roll.set("")
        self.dob.set("")
        self.gender.set("Select")
        self.phone.set("")
        
        messagebox.showinfo("Reset", "Reset successful")

if __name__ == "__main__":
    root=ctk.CTk()
    obj=Student(root)
    root.mainloop()
