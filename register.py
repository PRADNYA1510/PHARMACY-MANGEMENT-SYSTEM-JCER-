from tkinter import *
from tkinter import ttk
import random
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1260x800+0+0")

        lbtitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=5,relief=RIDGE
                         ,bg='white',fg="green",font=("times new roman",45,"bold"),padx=2,pady=4)

        lbtitle.pack(side=TOP,fill=X)

        self.img2=ImageTk.PhotoImage(file=r"C:\project\background.jpeg")


        
        lblimg2=Label(self.root,image=self.img2)
        lblimg2.place(x=30,y=100,width=470,height=500)
        #==============================variables======================
        self.var_fname=StringVar()
        self.var_Lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_conpass=StringVar()
        
        
        
        
        
        
        #=================main frame===================
        frame=Frame(self.root,bg="lightgreen")
        frame.place(x=500,y=120,width=720,height=450)

        Register=Label(frame,font=("times new roman",25,"bold"),text="REGISTER HERE",fg="red",bg="Lightgreen")
        Register.place(x=20,y=20)
        
        #===============label and entry==============
        #1
        fname=Label(frame,font=("times new roman",15,""),text="First Name",fg="black",bg="Lightgreen")
        fname.place(x=30,y=80)

        self.Fname_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.var_fname)
        self.Fname_entry.place(x=190,y=80,width=250)
        
        Lname=Label(frame,font=("times new roman",15,""),text="Last Name",fg="black",bg="Lightgreen")
        Lname.place(x=30,y=120)

        self.Lname_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.var_Lname)
        self.Lname_entry.place(x=190,y=120,width=250)

        contactno=Label(frame,font=("times new roman",15,""),text="Contact No",fg="black",bg="Lightgreen")
        contactno.place(x=30,y=160)

        self.contactno_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.var_contact)
        self.contactno_entry.place(x=190,y=160,width=250)

        email=Label(frame,font=("times new roman",15,""),text="Email Id",fg="black",bg="Lightgreen")
        email.place(x=30,y=200)

        self.email_entry=ttk.Entry(frame,font=("arial",15,""),textvariable=self.var_email)
        self.email_entry.place(x=190,y=200,width=250)


        security=Label(frame,font=("times new roman",15,""),text="Security Question",fg="black",bg="Lightgreen")
        security.place(x=30,y=320)

        sec_combo=ttk.Combobox(frame,font=("arial",15,""),state="readonly",textvariable=self.var_securityQ)
        sec_combo.place(x=190,y=320)
        sec_combo["values"]=("select","your birth place","your pet name","favorite teacher")
        sec_combo.current(0)


        


        
        passward=Label(frame,font=("times new roman",15,""),text="Password",fg="black",bg="lightgreen")
        passward.place(x=30,y=240)

        self.passward_entry=ttk.Entry(frame,font=("arial",17,""),textvariable=self.var_pass)
        self.passward_entry.place(x=190,y=240,width=250)

        confirm_passward=Label(frame,font=("times new roman",15,""),text="Confirm Password",fg="black",bg="lightgreen")
        confirm_passward.place(x=30,y=280)

        self.cpassward_entry=ttk.Entry(frame,font=("arial",17,""),textvariable=self.var_conpass)
        self.cpassward_entry.place(x=190,y=280,width=250)

        #=====================check box===============
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,text="I agree to terms & condition",variable=self.var_check,font=("arial",10,""),bg="lightgreen",onvalue=1,offvalue=0)
        checkbtn.place(x=30,y=390)

        img1=Image.open("C:\project\logos9.jpeg")
        img1=img1.resize((100,30),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimg1,borderwidth=0,command=self.register_data)
        b1.place(x=250,y=410)
        
        #img3=Image.open("C:\project\logos8.jpeg")
        #img3=img3.resize((100,30),Image.LANCZOS)
        #self.photoimg3=ImageTk.PhotoImage(img3)
        #b2=Button(frame,image=self.photoimg3,borderwidth=0)
        #b2.place(x=350,y=410)

        secans=Label(frame,font=("times new roman",15,""),text="Security Answer",fg="black",bg="Lightgreen")
        secans.place(x=30,y=360)

        self.semail_entry=ttk.Entry(frame,font=("arial",15,""),textvariable=self.var_securityA)
        self.semail_entry.place(x=190,y=360,width=250)

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()==""or self.var_securityQ.get()=="select":
            messagebox.showerror("error","All fields requrired" )

        elif self.var_pass.get()!=self.var_conpass.get():
             messagebox.showerror("error","password and confirm password must be same")

        elif self.var_check.get()==0:
             messagebox.showerror("error","please agree our terms and conditions")
        else:
            messagebox.showinfo("success","welcome")
            conn=mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
            my_cursor=conn.cursor()
            query=("select * from registers where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("error","user alredy exixts,please try another email")
            else:
                my_cursor.execute("insert into registers values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),
                                                                                         self.var_Lname.get(),
                                                                                         self.var_contact.get(),
                                                                                         self.var_email.get(),
                                                                                         self.var_pass.get(),
                                                                                         self.var_securityQ.get(),
                                                                                         self.var_securityA.get(),
                                                                                        ))   
                     
            conn.commit()
            conn.close()
            messagebox.showinfo("success","Registered succesfully")
        

if __name__=='__main__':
    
    root=Tk()        
    app=Register(root)
    root.mainloop()        