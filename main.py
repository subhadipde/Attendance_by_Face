from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student

class Face_Recognition_System:
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

        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0,width=1530,height=45)

        # Student button
        img4=Image.open(r"images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button (bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300,width=220,height=40)

        # Face Recognition button
        img4=Image.open(r"images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b2=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b2.place(x=650,y=100,width=220,height=220)

        b2_1=Button (bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=650, y=300,width=220,height=40)

        # Attendance button
        img4=Image.open(r"images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b3=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b3.place(x=1100,y=100,width=220,height=220)

        b3_1=Button (bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=1100, y=300,width=220,height=40)

        # Train Data button
        img4=Image.open(r"images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b4.place(x=200,y=400,width=220,height=220)

        b4_1=Button (bg_img, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_1.place(x=200, y=600,width=220,height=40)

        # Photos button
        img4=Image.open(r"images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b5=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b5.place(x=650,y=400,width=220,height=220)

        b5_1=Button (bg_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=650, y=600,width=220,height=40)

        # Exit button
        img4=Image.open(r"images\Exit_Button.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b6=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b6.place(x=1100,y=400,width=220,height=220)

        b6_1=Button (bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=1100, y=600,width=220,height=40)

    #==========Functions buttons=======================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)









if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
