from tkinter import*
import customtkinter as ctk
from PIL import Image, ImageTk
from student import Student
from tkinter import messagebox
import cv2
import os
import numpy as np
import mysql.connector

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
        b2_1=ctk.CTkButton(text="Face Detector", command=self.face_recog, cursor="hand2", text_font=("Verdana", 12))
        b2_1.place(relx=0.5, rely=0.4,width=320,height=80,  anchor=CENTER)

        # Attendance button
        b3_1=ctk.CTkButton(text="Attendance", cursor="hand2", text_font=("Verdana", 12))
        b3_1.place(relx=0.8, rely=0.4,width=320,height=80,  anchor=CENTER)

        # Train Data button
        b4_1=ctk.CTkButton(text="Train Data", command=self.train_data, cursor="hand2", text_font=("Verdana", 12))
        b4_1.place(relx=0.2, rely=0.8,width=320,height=80,  anchor=CENTER)

        # Photos button
        b5_1=ctk.CTkButton(text="Photos", command=self.open_photos, cursor="hand2", text_font=("Verdana", 12))
        b5_1.place(relx=0.5, rely=0.8,width=320,height=80,  anchor=CENTER)

        # Exit button        
        b6_1=ctk.CTkButton(text="Exit", cursor="hand2", command = root.destroy, fg_color="red", text_font=("Verdana", 12))
        b6_1.place(relx=0.8, rely=0.8,width=320,height=80,  anchor=CENTER)

        # # End Label
        # end_lbl=ctk.CTkLabel(text="Created By The Indian Coding Club")
        # end_lbl.configure(font=("Helvetica", 10, "bold italic"), fg="grey")
        # end_lbl.place(relx=0.5, rely=0.98, anchor=CENTER)

    #==========Functions buttons for Student=======================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    # =============Function button for Photos====================
    def open_photos(self):
        os.startfile("data")
        
    # =============Function button for Train Data====================
    def train_data(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #======Train the classifier And save=====
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets complete", parent=self.root)

    # ================Face Recognition=============================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf): 
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) 
                id,predict=clf.predict(gray_image[y:y+h,x:x+w]) 
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost", username="root", password="Subhadip@321#", database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select name from student where roll="+str(id)) 
                n=my_cursor.fetchone()
                n="+".join(n)

                # my_cursor.execute("select roll from student where Student_id="+str(id)) 
                # r=my_cursor.fetchone()
                # r="+".join(r)

                my_cursor.execute("select dept from student where roll="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                
                if confidence>77:
                    # cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0,8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3) 
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord

        def recognize(img,clf,faceCascade): 
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf) 
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome tO Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()





if __name__ == "__main__":
    root=ctk.CTk()
    obj=Face_Recognition_System(root)
    root.mainloop()
