from tkinter import *
from tkinter import ttk
import random
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()






class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("login")
        self.root.geometry("1260x800+0+0")
        self.root.configure(bg="light blue")

        
        
        frame=Frame(self.root,bg="green")
        frame.place(x=450,y=100,width=320,height=450)

        img1=Image.open("C:\project\logo4.jpeg")
        img1=img1.resize((60,60),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=570,y=110)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="green")
        get_str.place(x=85,y=70)

        username=Label(frame,font=("arial",12,"bold"),text="Username",fg="black",bg="green")
        username.place(x=70,y=140)

        self.username_entry=ttk.Entry(frame,font=("arial",12,""))
        self.username_entry.place(x=40,y=170,width=250)

        passward=Label(frame,font=("arial",12,"bold"),text="Passward",fg="black",bg="green")
        passward.place(x=70,y=210)

        self.passward_entry=ttk.Entry(frame,font=("arial",12,""))
        self.passward_entry.place(x=40,y=240,width=250)


        #===================icon image==================

        img2=Image.open("C:\project\logos5.jpeg")
        img2=img2.resize((20,20),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2,bg="green",borderwidth=0)
        lblimg2.place(x=490,y=245,width=20,height=20)

        img3=Image.open("C:\project\logos6.jpeg")
        img3=img3.resize((20,20),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimg3,bg="green",borderwidth=0)
        lblimg3.place(x=490,y=310,width=20,height=20)
        #===================login button===============
        login=Button(frame,text="LOGIN",command=self.login,bg="RED",fg="white",font=("arial",10,"bold"),width=12,relief=RIDGE,activeforeground="white",activebackground="red")
        login.place(x=100,y=310,width=120,height=30)
                

        register=Button(frame,text=" New Register",bg="green",command=self.register_window,fg="white",font=("arial",10,"bold"),width=12,border=0,activeforeground="white",activebackground="green")
        register.place(x=3,y=350,width=120)
                        
        forgot=Button(frame,text="Forgot Passward..?",command=self.forgot_pass,bg="green",fg="white",font=("arial",10,"bold"),width=12,border=0,activeforeground="white",activebackground="green")
        forgot.place(x=20,y=380,width=120)
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)   

    def login(self):
        if self.username_entry.get()==""or self.passward_entry.get()=="":
              messagebox.showerror("error","All fields are required")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from registers where email=%s and passward=%s",(self.username_entry.get(),self.passward_entry.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and passwords")
            else:
                open_main=messagebox.askyesno("Yes-No","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=PharmacyManagementSystem(self.new_window)  
                else:
                    if not open_main:
                        return
        conn.commit()
        conn.close()

    def forgot_pass(self):
        if self.username_entry.get()=="":
            messagebox.showerror("Error","please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
            my_cursor=conn.cursor()
            query1=("select * from registers where email=%s")
            value=(self.username_entry.get(),)
            my_cursor.execute(query1,value)
            row=my_cursor.fetchone()
            print(row)

            if row==None:
                messagebox.showerror("My error","please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                self.root2.configure(bg="white")

                
                l=Label(self.root2,text="Forgot Password",font=("times new roman",25,"bold"),fg="red",bg="white")
                l.place(x=0,y=5,relwidth=1)

                security=Label(self.root2,font=("times new roman",15,"bold"),text="Security Question",fg="black",bg="white")
                security.place(x=50,y=50)

                self.sec_combo=ttk.Combobox(self.root2,font=("arial",10,""),state="readonly")
                self.sec_combo.place(x=50,y=90,width=250)
                self.sec_combo["values"]=("select","your birth place","your pet name","favorite teacher")
                self.sec_combo.current(0)

                secans=Label(self.root2,font=("times new roman",15,"bold"),text="Security Answer",fg="black",bg="white")
                secans.place(x=50,y=140)

                self.semail_entry=ttk.Entry(self.root2,font=("arial",10,""))
                self.semail_entry.place(x=50,y=180,width=250)

                Pass=Label(self.root2,font=("times new roman",15,"bold"),text="New Password",fg="black",bg="white")
                Pass.place(x=50,y=230)

                self.Pass_entry=ttk.Entry(self.root2,font=("arial",10,""))
                self.Pass_entry.place(x=50,y=270,width=250)

                img1=Image.open("C:\project\logos10.jpeg")
                img1=img1.resize((100,30),Image.LANCZOS)
                self.photoimg1=ImageTk.PhotoImage(img1)
                b1=Button(self.root2,image=self.photoimg1,borderwidth=0,command=self.reset_pass)
                b1.place(x=50,y=300)
    
    def reset_pass(self):
        if self.sec_combo.get()== "select":
            messagebox.showerror("error","select the security question",parent=self.root2)

        elif self.semail_entry.get()=="":
            messagebox.showerror("error","please enter the answer",parent=self.root2)

        elif self.Pass_entry.get()=="":
            messagebox.showerror("error","please enter the new password",parent=self.root2)

        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
            my_cursor=conn.cursor()
            query2=("select * from registers where email=%s and securityQ=%s and securityA=%s")  
            values=(self.username_entry.get(),self.sec_combo.get(),self.Pass_entry.get())
            my_cursor.execute(query2,values)
            rows=my_cursor.fetchone()
            if rows==None:
                messagebox.showerror("Error","please enter the correct answer",parent=self.root2)
            else:
                query3=("update registers set passward=%s where email=%s")
                valuess=(self.Pass_entry.get(),self.username_entry.get()) 
                my_cursor.execute(query3,valuess)   

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset",parent=self.root2)
                self.root2.destroy()






            

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

        self.sec_combo=ttk.Combobox(frame,font=("arial",15,""),state="readonly",textvariable=self.var_securityQ)
        self.sec_combo.place(x=190,y=320)
        self.sec_combo["values"]=("select","your birth place","your pet name","favorite teacher")
        self.sec_combo.current(0)


        


        
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
        

                                 



class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1260x800+0+0")

        #========add med variale=========
        self.Refno_var=StringVar()
        self.Med_name=StringVar()
        #=============main variable==========
        self.refno_var = StringVar()
        self.companyname_var = StringVar()
        self.typemed_var = StringVar()
        self.medicine_var = StringVar()
        self.lotno_var = StringVar()
        self.issuedt_var = StringVar()
        self.expdt_var = StringVar()
        self.uses_var = StringVar()
        self.sideeffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.quantity_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()


        
        lbtitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE
                         ,bg='white',fg="blue",font=("times new roman",45,"bold"),padx=2,pady=4)

        lbtitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\project\logos1.jpeg")
        img1=img1.resize((60,60),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=30,y=20)
        #______________________DATA FRAME_________________________________


        Dataframe=Frame(self.root,bd=12,relief=RIDGE,padx=20)
        Dataframe.place(x=0,y=100,width=1260,height=380)

        DataframeLeft=LabelFrame(Dataframe,bd=7,relief=RIDGE,padx=20,
                    text="Medicine information",fg="red",font=("arial",12,"bold"))
        DataframeLeft.place(x=0,y=5,width=680,height=350)
        
        DataframeRight=LabelFrame(Dataframe,bd=7,relief=RIDGE,padx=20,text="Medicine Add Dept"
        ,fg="red",font=("arial",12,"bold"))
        DataframeRight.place(x=690,y=5,width=500,height=350)

        #______________________BUTTON FRAME__________________________________

        ButtonDataframe=Frame(self.root,bd=12,relief=RIDGE,padx=20)
        ButtonDataframe.place(x=0,y=470,width=1260,height=50)        
        #_____________________main button_____________________________________

        btnadddata=Button(ButtonDataframe,command=self.add_data,text="INSERT"
        ,bg="darkgreen",fg="white",font=("arial",10,"bold"),width=13)
        btnadddata.grid(row=0,column=0)

        btndeletedata=Button(ButtonDataframe,text="DELETE",command=self.Delete_info
        ,bg="red",fg="white",font=("arial",10,"bold"),width=13)
        btndeletedata.grid(row=0,column=1)

        btnupdatedata=Button(ButtonDataframe,text="UPDATE",command=self.update_new
        ,bg="darkgreen",fg="white",font=("arial",10,"bold"),width=13)
        btnupdatedata.grid(row=0,column=2)
        
        btnresetdata=Button(ButtonDataframe,text="RESET",command=self.clear_new,bg="darkgreen",fg="white",font=("arial",10,"bold"),width=13)
        btnresetdata.grid(row=0,column=3)

        btnexitdata=Button(ButtonDataframe,text="EXIT",command=self.root.quit
        ,bg="darkgreen",fg="white",font=("arial",10,"bold"),width=13)
        btnexitdata.grid(row=0,column=4)

        #________________________SERACH_BY________________________________________     


        #lblsearch=Label(ButtonDataframe,text="SEARCH_BY",bg="red",fg="white",font=("arial",10,"bold"),padx=2)
        #lblsearch.grid(row=0,column=5,sticky=W)

        #self.search_combo=ttk.Combobox(ButtonDataframe,textvariable=self.search_by,width=12,font=("arial",13,"bold"),state="readonly")
        #self.search_combo.grid(row=0,column=6)
        #self.search_combo["values"]=("ref","medicine","lot")
        #self.search_combo.current(0)
        
        #txtsearch=Entry(ButtonDataframe,bd=3,textvariable=self.search_txt,relief=RIDGE,width=12,font=("arial",17,"bold"))
        #txtsearch.grid(row=0,column=7)

        btnsearch=Button(ButtonDataframe,text="Pharmacist are first aid for society"
        ,bg="white",fg="magenta",font=("arial",10,"bold"),width=30)
        btnsearch.grid(row=0,column=8)

        #btnshowall=Button(ButtonDataframe,text="SHOWALL"
        #,bg="darkgreen",fg="white",font=("arial",10,"bold"),width=12)
        #btnshowall.grid(row=0,column=9)

        #__________________________label and entry__________________________

        lblrefno=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)

        
        conn=mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
        my_cursor=conn.cursor()
        my_cursor.execute("select ref from pharma ")
        row=my_cursor.fetchall()

        ref_combo=ttk.Combobox(DataframeLeft,textvariable=self.refno_var,width=25,font=("arial",13,"bold"),state="readonly")
        ref_combo.grid(row=0,column=1)
        ref_combo["values"]=row
        ref_combo.current(0)
        


        lblcmp=Label(DataframeLeft,font=("arial",12,"bold"),text="Company name:", padx=2)
        lblcmp.grid(row=1,column=0,sticky=W)

        txtcmp=Entry(DataframeLeft,textvariable=self.companyname_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        txtcmp.grid(row=1,column=1)

        

        lblmed=Label(DataframeLeft,font=("arial",12,"bold"),text="Type of medicine:",padx=2)
        lblmed.grid(row=2,column=0,sticky=W)

        typemed_combo=ttk.Combobox(DataframeLeft,textvariable=self.typemed_var,width=25,font=("arial",13,"bold"),state="readonly")
        typemed_combo.grid(row=2,column=1)
        typemed_combo["values"]=("Tablet","Liquid","Capsule","Drops","Inhale","injections","Topical Medicines")
        typemed_combo.current(0)


        #===================add medicine===============================
        lblmedname=Label(DataframeLeft,font=("arial",12,"bold"),text="Medicine name:",padx=2,pady=6)
        lblmedname.grid(row=3,column=0,sticky=W)

        
        conn=mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
        my_cursor=conn.cursor()
        my_cursor.execute("select Medname from pharma")
        medi=my_cursor.fetchall()

        typemedname_combo=ttk.Combobox(DataframeLeft,textvariable=self.medicine_var,width=25,font=("arial",13,"bold"),state="readonly")
        typemedname_combo.grid(row=3,column=1)
        typemedname_combo["values"]=medi
        typemedname_combo.current(0)


        lbllotno=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot no:",padx=2,pady=6)
        lbllotno.grid(row=4,column=0,sticky=W)

        txtlotno=Entry(DataframeLeft,textvariable=self.lotno_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        txtlotno.grid(row=4,column=1)
        

        lblissue=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue date:",padx=2,pady=6)
        lblissue.grid(row=5,column=0,sticky=W)

        txtissue=Entry(DataframeLeft,textvariable=self.issuedt_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        txtissue.grid(row=5,column=1)


        lblexp=Label(DataframeLeft,font=("arial",12,"bold"),text="Expiry date:",padx=2,pady=6)
        lblexp.grid(row=6,column=0,sticky=W)

        txtexp=Entry(DataframeLeft,textvariable=self.expdt_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        txtexp.grid(row=6,column=1)


        lbluser=Label(DataframeLeft,font=("arial",12,"bold"),text="Users:",padx=2,pady=6)
        lbluser.grid(row=7,column=0,sticky=W)

        txtuser=Entry(DataframeLeft,textvariable=self.uses_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        txtuser.grid(row=7,column=1)

        
        lblsdf=Label(DataframeLeft,font=("arial",12,"bold"),text="Side_effect:",padx=2,pady=6)
        lblsdf.grid(row=8,column=0,sticky=W)

        txtsdf=Entry(DataframeLeft,textvariable=self.sideeffect_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        txtsdf.grid(row=8,column=1)

        
        lblPW=Label(DataframeLeft,font=("arial",12,"bold"),text="Prec warning",padx=2,pady=6)
        lblPW.grid(row=0,column=2,sticky=W)

        txtPW=Entry(DataframeLeft,textvariable=self.warning_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        txtPW.grid(row=0,column=3)

        lbldosage=Label(DataframeLeft,font=("arial",12,"bold"),text="Dosage:",padx=2,pady=6)
        lbldosage.grid(row=1,column=2,sticky=W)

        txtdosage=Entry(DataframeLeft,textvariable=self.dosage_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        txtdosage.grid(row=1,column=3)

        
        lblprice=Label(DataframeLeft,font=("arial",12,"bold"),text="Price:",padx=2,pady=6)
        lblprice.grid(row=2,column=2,sticky=W)

        txtprice=Entry(DataframeLeft,textvariable=self.price_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        txtprice.grid(row=2,column=3)
         

        lblproduct=Label(DataframeLeft,font=("arial",12,"bold"),text="Product QT",padx=2,pady=6)
        lblproduct.grid(row=3,column=2,sticky=W)

        txtproduct=Entry(DataframeLeft,textvariable=self.quantity_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        txtproduct.grid(row=3,column=3)

        
        img2=Image.open("C:\project\logos2.jpeg")
        img2=img2.resize((240,170),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b2=Button(self.root,image=self.photoimg2,borderwidth=0)
        b2.place(x=460,y=280)
       

        #============================data frame right==========================


        img3=Image.open("C:\project\logos3.jpeg")
        img3=img3.resize((200,170),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b3=Button(self.root,image=self.photoimg3,borderwidth=0)
        b3.place(x=1000,y=280)


        
        lblrefno=Label(DataframeRight,font=("arial",12,"bold"),text="Ref_no",padx=15,pady=6)
        lblrefno.place(x=-5,y=10)

        txtrefno=Entry(DataframeRight,textvariable=self.Refno_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=15)
        txtrefno.place(x=100,y=10)
        

        lblmednm=Label(DataframeRight,font=("arial",12,"bold"),text="Med name",padx=15,pady=6)
        lblmednm.place(x=-5,y=50)

        txtmednm=Entry(DataframeRight,textvariable=self.Med_name,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=15)
        txtmednm.place(x=100,y=50)

        #======================side frame=======================
        
        side_frame=Frame(DataframeRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=-5,y=150,width=250,height=160)


        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("Ref","Med-name"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)
        
        self.medicine_table.heading("Ref",text="Ref_no")
        self.medicine_table.heading("Med-name",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("Ref",width=150)
        self.medicine_table.column("Med-name",width=150)

        self.medicine_table.bind("<ButtonRelease-1>", self.Medget_cursor)
        self.fetch_datamed()

        #====================medicine add button==============
        
        medframe=Frame(DataframeRight,bd=6,relief=RIDGE,bg="pink")
        medframe.place(x=280,y=10,width=150,height=120)

        btnadddata=Button(medframe,text="ADD", command=self.AddMed
        ,bg="YELLOW",fg="BLACK",font=("arial",10,"bold"),width=16)
        btnadddata.grid(row=0,column=0)

        btnupdata=Button(medframe,text="UPDATE",command=self.Update_med,
        bg="YELLOW",fg="BLACK",font=("arial",10,"bold"),width=16)
        btnupdata.grid(row=1,column=0)

        btndeldata=Button(medframe,text="DELETE",command=self.Delete_med
        ,bg="YELLOW",fg="BLACK",font=("arial",10,"bold"),width=16)
        btndeldata.grid(row=2,column=0)

        btnclrdata=Button(medframe,text="CLEAR",command=self.clear_med
        ,bg="YELLOW",fg="BLACK",font=("arial",10,"bold"),width=16)
        btnclrdata.grid(row=3,column=0)
        
        #===============================frame details========================
        medframedetails=Frame(self.root,bd=6,relief=RIDGE,bg="pink")
        medframedetails.place(x=0,y=520,width=1260,height=150)
        

        tableframe=Frame(medframedetails,bd=6,relief=RIDGE,bg="pink")
        tableframe.place(x=0,y=1,width=1250,height=120)


        scrol_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y=ttk.Scrollbar(tableframe,orient=VERTICAL)
        scrol_y.pack(side=RIGHT,fill=Y)

        self.Pharmacy_table=ttk.Treeview(tableframe,column=("Ref","Companyname","type","tabletname","lotno","issuedate",
                                           "expdate","uses","sideeffect","warning","dosage","price","productqt"),
                                            xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)

        scrol_x.config(command=self.Pharmacy_table.xview)
        scrol_y.config(command=self.Pharmacy_table.yview)
        
        self.Pharmacy_table.heading("Ref",text="Ref_no",)
        self.Pharmacy_table.heading("Companyname",text="Company Name")
        self.Pharmacy_table.heading("type",text="Type of medicine")
        self.Pharmacy_table.heading("tabletname",text="Tablet name")
        self.Pharmacy_table.heading("lotno",text="Lot no")
        self.Pharmacy_table.heading("issuedate",text="Issue Date")
        self.Pharmacy_table.heading("expdate",text="Exp date")
        self.Pharmacy_table.heading("uses",text="Uses")
        self.Pharmacy_table.heading("sideeffect",text="Side Effect")
        self.Pharmacy_table.heading("warning",text="Warning")
        self.Pharmacy_table.heading("dosage",text="Dosage")
        self.Pharmacy_table.heading("price",text="Price")
        self.Pharmacy_table.heading("productqt",text="Product Qts")
        self.Pharmacy_table["show"]="headings"
        self.Pharmacy_table.pack(fill=BOTH,expand=1)

        self.Pharmacy_table.column("Ref",width=100)
        self.Pharmacy_table.column("Companyname",width=100)
        self.Pharmacy_table.column("type",width=100)
        self.Pharmacy_table.column("tabletname",width=100)
        self.Pharmacy_table.column("lotno",width=100)
        self.Pharmacy_table.column("issuedate",width=100)
        self.Pharmacy_table.column("expdate",width=100)
        self.Pharmacy_table.column("uses",width=100)
        self.Pharmacy_table.column("sideeffect",width=100)
        self.Pharmacy_table.column("warning",width=100)
        self.Pharmacy_table.column("dosage",width=100)
        self.Pharmacy_table.column("price",width=100)
        self.Pharmacy_table.column("productqt",width=100)
        self.Pharmacy_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_datamed()
        self.fetch_new()

    #===================add medicine functionality declarations=================
    def AddMed(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(Ref,Medname) values(%s,%s)",( self.Refno_var.get(),
                                                                             self.Med_name.get()
                                                                             ))
        conn.commit()
        self.fetch_datamed()
        
        messagebox.showinfo("successfully", "medicine added",parent=self.root)  
        self.get_cursor()
        conn.close()
         
        
    def fetch_datamed(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())

            for i in rows:
                self.medicine_table.insert("", END, values=i)

            conn.commit()
            conn.close()    

    def Medget_cursor(self,event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.refno_var.set(row[0])
        self.Med_name.set(row[1])

    def Update_med(self):
        
        if self.Refno_var.get() == "" or self.Med_name.get()=="":

            messagebox.showerror("Error", "Ref No. and med name is required",parent=self.root)
        else:
           
               conn = mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
               my_cursor = conn.cursor()

               my_cursor.execute("Update pharma set Medname=%s where Ref=%s", (  
                                                                               self.Med_name.get(),
                                                                                 self.Refno_var.get()
                                                                               
                                                                                ))

        conn.commit()
        messagebox.showinfo("Update", "Successfully Updated", parent=self.root)
        self.fetch_datamed()
        conn.close()

    
    def Delete_med(self):
        if self.Refno_var.get()=="":
            messagebox.showerror("Error","Ref no is required",parent=self.root)
        else:

        
            conn = mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
            my_cursor = conn.cursor()

            
            my_cursor.execute("Delete from pharma where Ref=%s ",(self.Refno_var.get(),))
        conn.commit()
        messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
        self.fetch_datamed()
        conn.close()
           

        

    def clear_med(self):
        self.Med_name.set(),
        self.Refno_var.set()

   

    #*********************Main Table*********************

    def add_data(self):
        if self.refno_var.get() == "" or self.lotno_var.get() == "" or self.typemed_var.get() == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
       
            conn = mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("insert into meddetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.refno_var.get(),
                                        self.companyname_var.get(),
                                        self.typemed_var.get(),
                                        self.medicine_var.get(),
                                        self.lotno_var.get(),
                                        self.issuedt_var.get(),
                                        self.expdt_var.get(),
                                        self.uses_var.get(),
                                        self.sideeffect_var.get(),
                                        self.warning_var.get(),
                                        self.dosage_var.get(),
                                        self.price_var.get(),
                                        self.quantity_var.get()
                                          ))

            conn.commit()
            self.fetch_new()
            conn.close()
            messagebox.showinfo("Success","Successfully added",parent=self.root)                                  

    def fetch_new(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from meddetails")
        row = my_cursor.fetchall()
        if len(row)!=0:
            self.Pharmacy_table.delete(*self.Pharmacy_table.get_children())

            for i in row:
                self.Pharmacy_table.insert("",END,values=i)

            conn.commit()
        conn.close()    
    def get_cursor(self,event=""):
        cursor_row=self.Pharmacy_table.focus()
        content=self.Pharmacy_table.item(cursor_row)
        row=content["values"]
        self.refno_var.set(row[0])
        self.companyname_var.set(row[1])
        self.typemed_var.set(row[2])
        self.medicine_var.set(row[3])
        self.lotno_var.set(row[4])
        self.issuedt_var.set(row[5])
        self.expdt_var.set(row[6])
        self.uses_var.set(row[7])
        self.sideeffect_var.set(row[8])
        self.warning_var.set(row[9])
        self.dosage_var.set(row[10])
        self.price_var.set(row[11])
        self.quantity_var.set(row[12])

    def update_new(self):
         if self.refno_var.get() == "" or self.lotno_var.get() == "" or self.typemed_var.get() == "":
            messagebox.showerror("Error","All fields are required")
         else:   
            conn = mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("Update meddetails set compname=%s,typemed=%s,medname=%s,lot_no=%s,issuedate=%s,expdate=%s,uses=%s,sideff=%s,precwarn=%s,dosage=%s,tabletprice=%s,productQT=%s where ref_no=%s",(
                                                                                                                                                                                                                 
                                                                                                                                                                                                                 self.companyname_var.get(),
                                                                                                                                                                                                                 self.typemed_var.get(),
                                                                                                                                                                                                                 self.medicine_var.get(),
                                                                                                                                                                                                                 self.lotno_var.get(),
                                                                                                                                                                                                                 self.issuedt_var.get(),
                                                                                                                                                                                                                 self.expdt_var.get(),
                                                                                                                                                                                                                 self.uses_var.get(),
                                                                                                                                                                                                                 self.sideeffect_var.get(),
                                                                                                                                                                                                                 self.warning_var.get(),
                                                                                                                                                                                                                 self.dosage_var.get(),
                                                                                                                                                                                                                 self.price_var.get(),
                                                                                                                                                                                                                 self.quantity_var.get(),
                                                                                                                                                                                                                 self.refno_var.get()
                                                                                                                                                                                                                ))
            conn.commit()
            self.fetch_new()
            
            self.clear_new()
            conn.close()
            messagebox.showinfo("Success","Successfully updated",parent=self.root) 

    def Delete_info(self):
        if self.refno_var.get()=="":
            messagebox.showerror("Error","Ref no is required",parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
            my_cursor = conn.cursor()

            
            my_cursor.execute("Delete from meddetails where ref_no=%s ",(self.refno_var.get(),))         
        conn.commit()
        messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
        self.fetch_new()
        conn.close()



    def clear_new(self):
        #self.refno_var.set("")
        self.companyname_var.set("")
        #self.typemed_var.set("")
        #self.medicine_var.set("")
        self.lotno_var.set("")
        self.issuedt_var.set("")
        self.expdt_var.set("")
        self.uses_var.set("")
        self.sideeffect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("")
        self.price_var.set("")
        self.quantity_var.set("")
          
    
                                 





if __name__=='__main__':
    
   main()