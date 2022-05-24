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

        # code for full screen height and width --------------------
        width= root.winfo_screenwidth()               
        height= root.winfo_screenheight()               
        # root.geometry("%dx%d" % (width, height))

        # for maximize the window ---------------------------
        # root.state('zoomed') 

        # for complete full screen view ----------------------
        root.attributes('-fullscreen', True)
        self.root.title("Face Recogniton System")

        # bg image
        img3=Image.open(r"images\bgimg.jpg")

        img3=img3.resize((width, height), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(width=width,height=height)

        #Title label
        title_lbl=ctk.CTkLabel(root,text="FACE RECOGNISED ATTENDANCE SOFTWARE")
        title_lbl.configure(font=("Lato",25))
        title_lbl.place(relx=0.5, rely=0.05, anchor=CENTER)

        # Student button
        b1_1=ctk.CTkButton(text="Student Details", command=self.student_details, text_font=("Verdana", 12), cursor="hand2")
        b1_1.place(relx=0.2, rely=0.4,width=320,height=80, anchor=CENTER)

        # Face Recognition button
        b2_1=ctk.CTkButton(text="Face Detector", cursor="hand2", text_font=("Verdana", 12))
        b2_1.place(relx=0.5, rely=0.4,width=320,height=80,  anchor=CENTER)

        # Attendance button
        b3_1=ctk.CTkButton(text="Attendance", cursor="hand2", text_font=("Verdana", 12))
        b3_1.place(relx=0.8, rely=0.4,width=320,height=80,  anchor=CENTER)

        # Train Data button
        b4_1=ctk.CTkButton(text="Train Data", cursor="hand2", text_font=("Verdana", 12))
        b4_1.place(relx=0.2, rely=0.8,width=320,height=80,  anchor=CENTER)

        # Photos button
        b5_1=ctk.CTkButton(text="Photos", cursor="hand2", text_font=("Verdana", 12))
        b5_1.place(relx=0.5, rely=0.8,width=320,height=80,  anchor=CENTER)

        # Exit button        
        b6_1=ctk.CTkButton(text="Exit", cursor="hand2", command = root.destroy, fg_color="red", text_font=("Verdana", 12))
        b6_1.place(relx=0.8, rely=0.8,width=320,height=80,  anchor=CENTER)

        # End Label
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
