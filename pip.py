
from tkinter import *
import tkinter
import random
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox



class PharmacyManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1260x800+0+0")
        self.root.resizable(False, False)
       
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

        self.txt = "PHARMACY MANAGEMENT SYSTEM"
        self.count = 0
        self.text = ""
        self.color = ["green"]
        self.heading = Label(self.root, text=self.txt, font=(
            "times new roman", 45, "bold"), fg="blue", bd=9, relief=RIDGE)
        self.heading.pack(side=TOP, fill=X)
        self.slider()
        self.heading_color()


        
        #lbtitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE
                         #,bg='white',fg="blue",font=("times new roman",45,"bold"),padx=2,pady=4)

        #lbtitle.pack(side=TOP,fill=X)

        img1=Image.open("C:\project\logos1.jpeg")
        img1=img1.resize((60,60),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=20,y=15)
        #______________________DATA FRAME_________________________________


        Dataframe=Frame(self.root,bd=12,relief=RIDGE,padx=20)
        Dataframe.place(x=0,y=100,width=1260,height=380)

        DataframeLeft=LabelFrame(Dataframe,bd=7,relief=RIDGE,padx=20,
                    text="Medicine information",fg="red",font=("arial",12,"bold"))
        DataframeLeft.place(x=0,y=5,width=680,height=350)
        
        DataframeRight=LabelFrame(Dataframe,bd=7,relief=RIDGE,padx=20,text="Medicine_Add Dept"
        ,fg="red",font=("arial",12,"bold"))
        DataframeRight.place(x=690,y=5,width=500,height=350)

        #______________________BUTTON FRAME__________________________________

        ButtonDataframe=Frame(self.root,bd=12,relief=RIDGE,padx=20)
        ButtonDataframe.place(x=0,y=470,width=1260,height=50)        
        #_____________________main button_____________________________________

        btnadddata=Button(ButtonDataframe,command=self.add_data,text="MED_ADD"
        ,bg="darkgreen",fg="white",font=("arial",10,"bold"),width=13)
        btnadddata.grid(row=0,column=0)

        btndeletedata=Button(ButtonDataframe,text="DELETE",command=self.Delete_info,
        bg="red",fg="white",font=("arial",10,"bold"),width=13)
        btndeletedata.grid(row=0,column=1)

        btnupdatedata=Button(ButtonDataframe,text="UPDATE",command=self.update_new
        ,bg="darkgreen",fg="white",font=("arial",10,"bold"),width=13)
        btnupdatedata.grid(row=0,column=2)
        
        btnresetdata=Button(ButtonDataframe,text="RESET", command=self.clear_new,bg="darkgreen",fg="white",font=("arial",10,"bold"),width=13)
        btnresetdata.grid(row=0,column=3)

        btnexitdata=Button(ButtonDataframe,text="SHOWALL", command=self.root.quit
        ,bg="darkgreen",fg="white",font=("arial",10,"bold"),width=13)
        btnexitdata.grid(row=0,column=4)

        #________________________SERACH_BY________________________________________     


        lblsearch=Label(ButtonDataframe,text="SEARCH_BY",bg="red",fg="white",font=("arial",10,"bold"),padx=2)
        lblsearch.grid(row=0,column=5,sticky=W)

        self.search_combo=ttk.Combobox(ButtonDataframe,width=12, textvariable=self.search_by,font=("arial",13,"bold"),state="readonly")
        self.search_combo.grid(row=0,column=6)
        self.search_combo["values"] = ("Select options", "ref")
        self.search_combo.current(0)
        
        txtsearch=Entry(ButtonDataframe,bd=3, textvariable=self.search_txt,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtsearch.grid(row=0,column=7)

        btnsearch=Button(ButtonDataframe,text="SEARCH",command=self.search_data,
        bg="darkgreen",fg="white",font=("arial",10,"bold"),width=12)
        btnsearch.grid(row=0,column=8)

        btnshowall=Button(ButtonDataframe,text="EXIT"
        ,bg="darkgreen",fg="white",font=("arial",10,"bold"),width=12)
        btnshowall.grid(row=0,column=9)

        #__________________________label and entry__________________________

        lblrefno=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)

        
        conn=mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
        my_cursor=conn.cursor()
        my_cursor.execute("select ref from pharma ")
        row_01=my_cursor.fetchall()

        self.ref_combo=ttk.Combobox(DataframeLeft,textvariable=self.refno_var,width=25,font=("arial",13,"bold"),state="readonly")
        self.ref_combo.grid(row=0,column=1)
        self.ref_combo["values"]=('Select',row_01,)
        self.ref_combo.current(0)
        


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

        self.typemedname_combo=ttk.Combobox(DataframeLeft,textvariable=self.Med_name,width=25,font=("arial",13,"bold"),state="readonly")
        self.typemedname_combo.grid(row=3,column=1)
        self.typemedname_combo["values"]=('Select',medi)
        self.typemedname_combo.current(0)


        lbllotno=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot no:",padx=2,pady=6)
        lbllotno.grid(row=4,column=0,sticky=W)

        self.txtlotno=Entry(DataframeLeft,textvariable=self.lotno_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        self.txtlotno.grid(row=4,column=1)
        

        lblissue=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue date:",padx=2,pady=6)
        lblissue.grid(row=5,column=0,sticky=W)

        self.txtissue=Entry(DataframeLeft,textvariable=self.issuedt_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        self.txtissue.grid(row=5,column=1)


        lblexp=Label(DataframeLeft,font=("arial",12,"bold"),text="Expiry date:",padx=2,pady=6)
        lblexp.grid(row=6,column=0,sticky=W)

        self.txtexp=Entry(DataframeLeft,textvariable=self.expdt_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        self.txtexp.grid(row=6,column=1)


        lbluser=Label(DataframeLeft,font=("arial",12,"bold"),text="Users:",padx=2,pady=6)
        lbluser.grid(row=7,column=0,sticky=W)

        self.txtuser=Entry(DataframeLeft,textvariable=self.uses_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        self.txtuser.grid(row=7,column=1)

        
        lblsdf=Label(DataframeLeft,font=("arial",12,"bold"),text="Side_effect:",padx=2,pady=6)
        lblsdf.grid(row=8,column=0,sticky=W)

        self.txtsdf=Entry(DataframeLeft,textvariable=self.sideeffect_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=27)
        self.txtsdf.grid(row=8,column=1)

        
        lblPW=Label(DataframeLeft,font=("arial",12,"bold"),text="Prec warning",padx=2,pady=6)
        lblPW.grid(row=0,column=2,sticky=W)

        self.txtPW=Entry(DataframeLeft,textvariable=self.warning_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        self.txtPW.grid(row=0,column=3)

        lbldosage=Label(DataframeLeft,font=("arial",12,"bold"),text="Dosage:",padx=2,pady=6)
        lbldosage.grid(row=1,column=2,sticky=W)

        self.txtdosage=Entry(DataframeLeft,textvariable=self.dosage_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        self.txtdosage.grid(row=1,column=3)

        
        lblprice=Label(DataframeLeft,font=("arial",12,"bold"),text="Price:",padx=2,pady=6)
        lblprice.grid(row=2,column=2,sticky=W)

        self.txtprice=Entry(DataframeLeft,textvariable=self.price_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        self.txtprice.grid(row=2,column=3)
         

        lblproduct=Label(DataframeLeft,font=("arial",12,"bold"),text="Product QT",padx=2,pady=6)
        lblproduct.grid(row=3,column=2,sticky=W)

        self.txtproduct=Entry(DataframeLeft,textvariable=self.quantity_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        self.txtproduct.grid(row=3,column=3)

        
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

        self.txtrefno=Entry(DataframeRight,textvariable=self.Refno_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=15)
        self.txtrefno.place(x=100,y=10)
        

        lblmednm=Label(DataframeRight,font=("arial",12,"bold"),text="Med_name",padx=15,pady=6)
        lblmednm.place(x=-5,y=50)

        self.txtmednm=Entry(DataframeRight,textvariable=self.Med_name,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=15)
        self.txtmednm.place(x=100,y=50)

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
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("successfully", "medicine added")  
        
    def fetch_datamed(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        row = my_cursor.fetchall()

        if len(row) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())

            for i in row:
                self.medicine_table.insert("", END, values=i)

            conn.commit()
            conn.close()    

    def Medget_cursor(self, event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.Refno_var.set(row[0])
        self.Med_name.set(row[1])


    def Update_med(self):
        
        if self.Refno_var.get() == "" or self.Med_name.get()=="":

            messagebox.showerror("Error", "Ref No. and med name is required")
        else:
            try:
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
            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)    

    
    def Delete_med(self):
        if self.Refno_var.get()=="":
            messagebox.showerror("Error","Ref no is required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
                my_cursor = conn.cursor()

            
                my_cursor.execute("Delete from pharma where Ref=%s ",(self.Refno_var.get(),))
                conn.commit()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
                self.fetch_datamed()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)
    
           

        

    def clear_med(self):
        self.Med_name.set("")
        self.Refno_var.set("")

    #*********************Main Table*********************

    def add_data(self):
        if self.refno_var.get() == "" or self.lotno_var.get() == "" or self.typemed_var.get() == "":
            messagebox.showerror("Error","All fields are required")
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
            messagebox.showinfo("Success","Successfully added")                                  

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
            my_cursor.execute("Update meddetails set compname=%s,typemed, medname=%s,lot_no =%s,issuedate=%s,expdate=%s,uses=%s,sideff=%s,precwarn=%s,dosage=%s, tabletprice=%s,productQT=%s where ref_no=%s",(
                                                                                                                                                                                                                 
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
            messagebox.showinfo("Success","Successfully updated") 

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
          
    def search_data(self):

        conn = mysql.connector.connect(host='localhost',username='root',password='Pradnya',database='mydata',port='3306')
        new_cursor=conn.cursor()
        selected = self.search_combo.get()
        if selected == "Select Options":
            messagebox.showerror("Error","You have to choose an option")

        else:

            new_cursor.execute("Select * from meddetails where ref_no=?",(self.search_txt.get(),))
            row=new_cursor.fetchone()

            if len(row)!=0:
                self.Pharmacy_table.delete(*self.Pharmacy_table.get_children())

                for i in row:
                    self.Pharmacy_table.insert("",END,values=i)

                conn.commit()
        
    def slider(self):
        if self.count>=len(self.txt):
            self.count=-1
            self.text=""
            self.heading.config(text=self.text)
        else:
            self.text=self.text+self.txt[self.count]
            self.heading.config(text=self.text)
        self.count+=1
        self.heading.after(200,self.slider)
    def heading_color(self):
        fg=random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(100,self.heading_color)
    
            
            

    
        

        

    

      




if __name__=="__main__":
    root=tkinter.Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()       