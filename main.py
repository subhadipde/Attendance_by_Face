from tkinter import*
from tkinter import ttk
from tkinter import font
import customtkinter as ctk
from PIL import Image, ImageTk
from student import Student

# custom tkinter setting
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class Face_Recognition_System:
    def __init__(self, root):
        self.root=root

        # code for full screen height and width
        width= root.winfo_screenwidth()               
        height= root.winfo_screenheight()               
        root.geometry("%dx%d" % (width, height))

        # for maximize the window
        root.state('zoomed') 

        # root.attributes('-fullscreen', True)                      # for complete full screen view
        self.root.title("Face Recogniton System")

        # myfont = (family='Verdana', size=15, weight='bold')

        # bg image
        img3=Image.open(r"images\Subha.jpg")
        img3=img3.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl=ctk.CTkLabel( text="FACE RECOGNISED ATTENDANCE SOFTWARE")
        title_lbl.configure(font=("Lato",25))
        title_lbl.place(relx=0.5, rely=0.05, anchor=CENTER)

        # Student button
        img4=Image.open(r"images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        
        b1_1=ctk.CTkButton(text="Student Details", command=self.student_details, cursor="hand2")
        b1_1.place(relx=0.2, rely=0.5,width=220,height=60, anchor=CENTER)

        # Face Recognition button
        img4=Image.open(r"images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b2=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b2.place(x=650,y=100,width=220,height=220)

        b2_1=ctk.CTkButton( text="Face Detector", cursor="hand2")
        b2_1.place(relx=0.5, rely=0.5,width=220,height=60,  anchor=CENTER)

        # Attendance button
        img4=Image.open(r"images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b3=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b3.place(x=1100,y=100,width=220,height=220)

        b3_1=ctk.CTkButton(text="Attendance", cursor="hand2")
        b3_1.place(relx=0.8, rely=0.5,width=220,height=60,  anchor=CENTER)

        # Train Data button
        img4=Image.open(r"images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b4.place(x=200,y=400,width=220,height=220)

        b4_1=ctk.CTkButton(text="Train Data", cursor="hand2")
        b4_1.place(relx=0.2, rely=0.9,width=220,height=60,  anchor=CENTER)

        # Photos button
        img4=Image.open(r"images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b5=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b5.place(x=650,y=400,width=220,height=220)

        b5_1=ctk.CTkButton(text="Photos", cursor="hand2")
        b5_1.place(relx=0.5, rely=0.9,width=220,height=60,  anchor=CENTER)

        # Exit button
        img4=Image.open(r"images\Exit_Button.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b6=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b6.place(x=1100,y=400,width=220,height=220)

        

        b6_1=ctk.CTkButton(text="Exit", cursor="hand2",command = root.destroy, fg_color="red")
        b6_1.place(relx=0.8, rely=0.9,width=220,height=60,  anchor=CENTER)

        end_lbl=ctk.CTkLabel(text="Created By The Indian Coding Club")
        end_lbl.configure(font=("Helvetica", 10, "bold italic"), fg="grey")
        end_lbl.place(relx=0.5, rely=0.98, anchor=CENTER)

    #==========Functions buttons=======================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        









if __name__ == "__main__":
    root=ctk.CTk()
    obj=Face_Recognition_System(root)
    root.mainloop()
