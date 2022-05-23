import collections
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogniton System")

        # bg image
        img3=Image.open(r"images\bgimg.jpg")
        img3=img3.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(bg_img, text="STUDET MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0,width=1530,height=45)

        # Main Frame
        main_frame=Frame (bg_img, bd=2,bg="white")
        main_frame.place(x=20, y=55, width=1480,height=600)
        
        # left label frame
        Left_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10,width=730,height=580)

        # current course information
        current_course_frame=LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5, y=10, width=720,height=125)

        # Department
        dep_label=Label(current_course_frame, text="Department", font=("times new roman",13,"bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo=ttk.Combobox(current_course_frame, font=("times new roman",13,"bold"), state="readonly", width=20)
        dep_combo["values"]=("Select Department", "CSE", "IT", "ECE", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label=Label(current_course_frame, text="Course", font=("times new roman",13,"bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo=ttk.Combobox(current_course_frame, font=("times new roman",13,"bold"), state="readonly", width=20)
        course_combo["values"]=("Select Course", "FE", "SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label=Label(current_course_frame, text="Year", font=("times new roman",13,"bold"), bg="white")
        year_label.grid (row=1,column=0, padx=10, sticky=W)

        year_combo=ttk.Combobox(current_course_frame, font=("times new roman", 13, "bold"), state="readonly",width=20)
        year_combo["values"]=("Select Year", "2018-19","2019-20", "2020-21","2021-22")
        year_combo.current(0)
        year_combo.grid(row=1,column=1, padx=2, pady=10, sticky=W)

        #Semester
        semester_label=Label(current_course_frame, text="Semester", font=("times new roman",13,"bold"), bg="white")
        semester_label.grid (row=1,column=2, padx=10, sticky=W)

        semester_combo=ttk.Combobox(current_course_frame, font=("times new roman",13,"bold"), state="readonly",width=20)
        semester_combo["values"]=("Select Semester", "Sem-1", "Sem-2", "Sem-3", "Sem-4", "Sem-5", "Sem-6", "Sem-7", "Sem-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3, padx=2, pady=10, sticky=W)


        # Class Student information
        class_Student_frame=LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information")
        class_Student_frame.place(x=5,y=180,width=720,height=300)

        # student id
        studentId_label=Label(class_Student_frame, text="StudentID: ", font=("times new roman", 13, "bold"),bg="white")
        studentId_label.grid(row=0,column=0, padx=10, pady=5, sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame, width=20, font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0,column=1, padx=10, pady=5, sticky=W)

        # student name
        studenName_label=Label(class_Student_frame, text="Student Name: ", font=("times new roman", 13, "bold"), bg="white")
        studenName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class didvision
        class_div_label=Label(class_Student_frame, text="Class Division:", font=("times new roman",13, "bold"), bg="white")
        class_div_label.grid(row=1,column=0, padx=10, pady=5, sticky=W)

        class_div_entry=ttk.Entry(class_Student_frame, width=20, font=("times new roman", 13, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label=Label(class_Student_frame, text="Roll No: ", font=("times new roman",13,"bold"), bg="white")
        roll_no_label.grid(row=1,column=2, padx=10, pady=5, sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame, width=20, font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3, padx=10, pady=5,sticky=W)

        # Gender
        gender_label=Label(class_Student_frame, text="Gender:", font=("times new roman",13,"bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_entry=ttk.Entry(class_Student_frame, width=20, font=("times new roman",13,"bold"))
        gender_entry.grid(row=2,column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label=Label(class_Student_frame, text="DOB: ", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry=ttk.Entry(class_Student_frame, width=20, font=("times new roman",13,"bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label=Label(class_Student_frame, text="Email: ", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry=ttk.Entry(class_Student_frame,width=20, font=("times new roman",13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        #phone no
        phone_label=Label (class_Student_frame, text="Phone No: ", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3,column=2, padx=10, pady=5, sticky=W)

        phone_entry=ttk.Entry(class_Student_frame, width=20, font=("times new roman",13, "bold"))
        phone_entry.grid(row=3, column=3,padx=10, pady=5, sticky=W)

        # Address
        address_label=Label(class_Student_frame, text="Address:", font=("times new roman",13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry=ttk.Entry(class_Student_frame, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # radio button
        radiobtn1=ttk.Radiobutton(class_Student_frame, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2=ttk.Radiobutton(class_Student_frame, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        #buttons frame
        btn_frame1=Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=200, width=715, height=35)

        save_btn=Button(btn_frame1, text="Save", width=17 , font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame1, text="Update", width=17, font=("times new roman",13,"bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn=Button(btn_frame1, text="Delete", width=17, font=("times new roman",13,"bold"), bg="blue", fg="white")
        delete_btn.grid (row=0, column=2)

        reset_btn=Button(btn_frame1, text="Reset",width=17, font=("times new roman",13,"bold"),bg="blue", fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame2=Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame2.place(x=0, y=235, width=715, height=35)

        take_photo_btn=Button(btn_frame2, text="Take Photo Sample", width=35, font=("times new roman",13,"bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame2, text="Update Photo Sample", width=35, font=("times new roman",13,"bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)



        # Right label frame
        Right_frame=LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE,text="Student Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        # ===========================Search System=======================================================
        Search_frame=LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman",12,"bold"))
        Search_frame.place(x=5, y=10, width=710,height=70)

        search_label=Label(Search_frame, text="Search By: ", font=("times new roman",15,"bold"),bg="red", fg="white")
        search_label.grid (row=0,column=0, padx=10, pady=5, sticky=W)

        search_combo=ttk.Combobox(Search_frame, font=("times new roman",13,"bold"), state="readonly", width=15)
        search_combo["values"]=("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid (row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry=ttk.Entry(Search_frame, width=15, font=("times new roman",13,"bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn=Button(Search_frame, text="Search", width=12, font=("times new roman",12,"bold"), bg="blue", fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button (Search_frame, text="Show All", width=12, font=("times new roman",12,"bold"),bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # # ===========================Table Frame=======================================================
        table_frame=Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, columns=("dep","course","year","sem","id","name","roll","gender","div","dob","email","phone","address","photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading ("name", text="Name")
        self.student_table.heading ("roll", text="Roll")
        self.student_table.heading ("gender", text="Gender")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading ("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH,expand=1)

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
