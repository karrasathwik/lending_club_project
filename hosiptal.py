from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hosiptal management system")
        self.root.geometry("1240x800+0+0")
        
        
        self.NAMES_OF_TABLET =StringVar()
        self.Refence_No=StringVar()
        self.Dose =StringVar()
        self.No_of_Tablets =StringVar()
        self.Lot=StringVar()
        self.Issue_Date =StringVar()
        self.Exp_Date =StringVar()
        self.Side_Effect =StringVar()
        self.Further_info=StringVar()
        self.Blood_Pressure=StringVar()
        self.Any_Allergy=StringVar()
        self.Medication=StringVar()
        self.PaientID=StringVar()
        self.NHS_number=StringVar()
        self.Patient_Name=StringVar()
        self.Date_Birth=StringVar()
        self.Address=StringVar()
        self.Postcode=StringVar()
        
        
            
        
        lbltitile = Label(self.root,bd=10,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",20,"bold"))
        lbltitile.pack(side=TOP,fill=X)
        
        
        #=========================Dataframe================================================
        Dataframe =Frame(self.root,bd=10,relief=RIDGE)
        Dataframe.place(x=5,y=60,width=1280,height=400)
        
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                                        font=("times new roman",15,"bold"),text="patient information")
        
        DataframeLeft.place(x=0,y=5,width=900,height=350)
        
        DataframeRight = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                                        font=("times new roman",15,"bold"),text="prescription")
        
        DataframeRight.place(x=935,y=10,width=320,height=350)
        
    #===============================button frame==================================================================
    
        Buttonframe =Frame(self.root,bd=10,relief=RIDGE)
        Buttonframe.place(x=0,y=470,width=1280,height=60)
    #================================detailframe====================================================================
    
        
        Detailframe =Frame(self.root,bd=8,relief=RIDGE)
        Detailframe.place(x=0,y=535,width=1280,height=109)
        
        #=====================================dataframe left=========================================================================================
        
        lblNameTablet = Label(DataframeLeft,text="NAMES OF TABLET",font=("times new roman",8,"bold"),padx=2,pady=5)
        lblNameTablet.grid(row=0,column=0)
        
        comNameTablet= ttk.Combobox(DataframeLeft,textvariable=self.NAMES_OF_TABLET,font=("times new roman",8,"bold"),
                                                                                    width=33)
        comNameTablet["values"]=("Nice","corna","tb","bisoprol","fourzomide","enstro")
        comNameTablet.grid(row=0,column=1)

        lblref = Label(DataframeLeft,font=("arial",10,"bold"),text="Refence No",padx=2,pady=6)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,textvariable=self.Refence_No,font=("arial",10,"bold"),width=33)
        txtref.grid(row=1,column=1) 
        
        lblDose = Label(DataframeLeft,font=("arial",10,"bold"),text="Dose:",padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,textvariable=self.Dose,font=("arial",10,"bold"),width=33)
        txtDose.grid(row=2,column=1)
        
        lblTablet = Label(DataframeLeft,font=("arial",10,"bold"),text="No of Tablets:",padx=2,pady=6)
        lblTablet.grid(row=3,column=0,sticky=W)
        txtTablet=Entry(DataframeLeft,textvariable=self.No_of_Tablets,font=("arial",10,"bold"),width=33)
        txtTablet.grid(row=3,column=1)
        
        lblLot = Label(DataframeLeft,font=("arial",10,"bold"),text="Lot:",padx=2,pady=4)
        lblLot.grid(row=4,column=0,sticky=W)
        lblLot=Entry(DataframeLeft,textvariable=self.Lot,font=("arial",10,"bold"),width=33)
        lblLot.grid(row=4,column=1)
        
        lblDate = Label(DataframeLeft,font=("arial",10,"bold"),text="Issue Date:",padx=2,pady=4)
        lblDate.grid(row=5,column=0,sticky=W)
        lblDate=Entry(DataframeLeft,textvariable=self.Issue_Date,font=("arial",10,"bold"),width=33)
        lblDate.grid(row=5,column=1)
        
        lblDateE = Label(DataframeLeft,font=("arial",10,"bold"),text="Exp Date:",padx=2,pady=4)
        lblDateE.grid(row=6,column=0,sticky=W)
        lblDateE=Entry(DataframeLeft,textvariable=self.Exp_Date,font=("arial",10,"bold"),width=33)
        lblDateE.grid(row=6,column=1)
        
        
        lblSideEffect  = Label(DataframeLeft,font=("arial",10,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        lblSideEffect=Entry(DataframeLeft,textvariable=self.Side_Effect,font=("arial",10,"bold"),width=33)
        lblSideEffect.grid(row=8,column=1)
        
        lblFurtherinfo = Label(DataframeLeft,font=("arial",10,"bold"),text="Further info:",padx=2,pady=6)
        lblFurtherinfo.grid(row=9,column=0,sticky=W)
        lblFurtherinfo=Entry(DataframeLeft,textvariable=self.Further_info,font=("arial",10,"bold"),width=33)
        lblFurtherinfo.grid(row=9,column=1)
        
        lblBloodpressure = Label(DataframeLeft,font=("arial",10,"bold"),text="Blood Pressure",padx=4,pady=6)
        lblBloodpressure.grid(row=0,column=2,sticky=W)
        lblBloodpressure=Entry(DataframeLeft,textvariable=self.Blood_Pressure,font=("arial",10,"bold"),width=33)
        lblBloodpressure.grid(row=0,column=3)
        
        
        
        lblAllergy = Label(DataframeLeft,font=("arial",10,"bold"),text="Any Allergy",padx=4,pady=6)
        lblAllergy.grid(row=1,column=2,sticky=W)
        comNameAllergy= ttk.Combobox(DataframeLeft,textvariable=self.Any_Allergy,font=("arial",8,"bold"),
                                                                                    width=35)
        comNameAllergy["values"]=("yes","no")
        comNameAllergy.grid(row=1,column=3)
        
        
        lblMedication = Label(DataframeLeft,font=("arial",10,"bold"),text="Medication",padx=4,pady=6)
        lblMedication.grid(row=2,column=2,sticky=W)
        lblMedication=Entry(DataframeLeft,textvariable=self.Medication,font=("arial",10,"bold"),width=33)
        lblMedication.grid(row=2,column=3)
        
    
        lblPatient = Label(DataframeLeft,font=("arial",10,"bold"),text="PaientID",padx=4,pady=6)
        lblPatient.grid(row=3,column=2)
        lblPatient = Entry( DataframeLeft,textvariable=self.PaientID,font=("arial",10,"bold"),width=33)
        lblPatient.grid(row=3,column=3)
        
        lblNumber = Label(DataframeLeft,font=("arial",10,"bold"),text = "NHS number",padx=4,pady=6)
        lblNumber.grid(row=4,column=2)
        lblNumber = Entry(DataframeLeft,textvariable=self.NHS_number,font=("arial",10,"bold"),width=33)
        lblNumber.grid(row=4,column=3)
                
        lblPatientName = Label(DataframeLeft,font=("arial",10,"bold"),text ="Patient Name",padx=4,pady=6)
        lblPatientName.grid(row=5,column=2)
        lblPatientName = Entry(DataframeLeft,textvariable=self.Patient_Name,font=("arial",10,"bold"),width=33)
        lblPatientName.grid(row=5,column=3)
        
        lblDateBirth = Label(DataframeLeft,font=("arial",10,"bold"),text="Date&Birth",padx=4,pady=6)
        lblDateBirth.grid(row=6,column=2,)
        lblDateBirth = Entry(DataframeLeft,textvariable=self.Date_Birth,font=("arial",10,"bold"),width=33)
        lblDateBirth.grid(row=6,column=3)
        
        
        lblAddres = Label(DataframeLeft,font=("arial",10,"bold"),text = "Address",padx=4,pady=6)
        lblAddres.grid(row=8,column=2)
        lblAddres = Entry(DataframeLeft,textvariable=self.Address,font=("arial",10,"bold"),width=33)
        lblAddres.grid(row=8,column=3)
        
        lblPostcode = Label(DataframeLeft,font=("arial",10,"bold"),text="Postcode",padx=4,pady=6)
        lblPostcode.grid(row=9,column=2)
        lblPostcode = Entry(DataframeLeft,textvariable=self.Postcode,font=("arial",10,"bold"),width=33)
        lblPostcode.grid(row=9,column=3)
#===============================Dataframeright==================
        self.txtPrescription = Text(DataframeRight,font=("arial",10,"bold"),width=40,height=18,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        #=======================buttona=============================
        btnPrescription = Button(Buttonframe,text="prescription",bg="blue",fg="white",font=("arial",10,"bold"),width=25,height=1,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)
        
        btnPrescriptionData = Button(Buttonframe,text="prescriptionData",bg="Blue",fg="white",font=("arial",10,"bold"),width=25,height=1,padx=8,pady=6)
        btnPrescriptionData.grid(row=0,column=3)
        #update,delete,reset,exit
        
        btnUpdate = Button(Buttonframe,text = "update",background ="blue",fg="white",font=("arial",10,"bold"),height=1,width=25,padx=2,pady=6)
        btnUpdate.grid(row=0,column=4)
        
        btnDelete = Button(Buttonframe,text="Delete",bg="blue",fg="white",font=("arial",10,"bold"),width=25,height=1,padx=2,pady=6)
        btnDelete.grid(row=0,column=5)
        
        btnReset = Button(Buttonframe,text="Reset",bg="blue",fg="WHITE",font=("arial",10,"bold"),height=1,width=25,padx=2,pady=6)
        btnReset.grid(row=0,column=6)        
        
        btnExit = Button(Buttonframe,text="Reset",bg="blue",fg="white",font=("arial",10,"bold"),height=1,width=22,padx=2,pady=6)
        btnExit.grid(row=0,column=7)   
#=======================Tablescroll=====================================
        scroll_x=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailframe,orient=VERTICAL)
        
        # Fixing the column names to match exactly
        self.hospital_table = ttk.Treeview(Detailframe, 
                                            columns=("NAMES OF TABLET", "Refence No", "Dose", "No of Tablets", "Lot",
                                                    "Issue Date", "Exp Date", "Side Effect", "Further info", "Blood Pressure",
                                                    "Any Allergy", "Medication", "Patient ID", "NHS number", "Date of Birth", 
                                                    "Patient Name", "Address", "Postcode"), 
                                            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        # Ensure the headings match exactly the column names
        self.hospital_table.heading("NAMES OF TABLET", text="Names of Tablets")
        self.hospital_table.heading("Refence No", text="Reference No")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("No of Tablets", text="No of Tablets")
        self.hospital_table.heading("Lot", text="Lot")
        self.hospital_table.heading("Issue Date", text="Issue Date")
        self.hospital_table.heading("Exp Date", text="Exp Date")
        self.hospital_table.heading("Side Effect", text="Side Effect")
        self.hospital_table.heading("Further info", text="Further Info")
        self.hospital_table.heading("Blood Pressure", text="Blood Pressure")
        self.hospital_table.heading("Any Allergy", text="Any Allergy")
        self.hospital_table.heading("Medication", text="Medication")
        self.hospital_table.heading("Patient ID", text="Patient ID")
        self.hospital_table.heading("NHS number", text="NHS Number")
        self.hospital_table.heading("Date of Birth", text="Date of Birth")
        self.hospital_table.heading("Patient Name", text="Patient Name")
        self.hospital_table.heading("Address", text="Address")
        self.hospital_table.heading("Postcode", text="Postcode")

        self.hospital_table["show"] = "headings"

        
        self.hospital_table.pack(fill=BOTH,expand=1)
        
        self.hospital_table.column("NAMES OF TABLET",width=80)
        self.hospital_table.column("Refence No",width=80)
        self.hospital_table.column("Dose",width=80)
        self.hospital_table.column("No of Tablets",width=80)
        self.hospital_table.column("Lot",width=80)
        self.hospital_table.column("Issue Date",width=80)
        self.hospital_table.column("Exp Date",width=80)
        self.hospital_table.column("Side Effect",width=80)
        self.hospital_table.column("Further info",width=80)
        self.hospital_table.column("Blood Pressure",width=80)
        self.hospital_table.column("Any Allergy",width=80)
        self.hospital_table.column("Medication",width=80)
        self.hospital_table.column("Patient ID",width=80)
        self.hospital_table.column("NHS number",width=80)
        self.hospital_table.column("Date of Birth",width=80)
        self.hospital_table.column("Patient Name",width=80) 
        self.hospital_table.column("Address",width=80)
        self.hospital_table.column("Postcode",width=80)
        
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        
#=======================functionality Declaration=======================
    def iprescriptionData(self):
        if self.NAMES_OF_TABLET.get()==""or self.Refence_No.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = mysql.connector.connect(host=" 127.0.0.1",Username="root",password="XAMPP",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values=(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                            self.NAMES_OF_TABLET.get(),
                                                                                                                            self.Refence_No.get(),
                                                                                                                            self.Dose.get(),
                                                                                                                            self.NAMES_OF_TABLET(),
                                                                                                                            self.Lot.get(),
                                                                                                                            self.Issue_Date.get(),
                                                                                                                            self.Exp_Date.get(),
                                                                                                                            self.Side_Effect.get(),
                                                                                                                            self.Any_Allergy.get(),
                                                                                                                            self.NHS_number.get(),
                                                                                                                            self.Patient_Name.get(),
                                                                                                                            self.Date_Birth.get(),
                                                                                                                            self.Address.get(),
                                                                                                                            self.Postcode.get()
                                                                                                                            
                                                                                                                            ))
            conn.commit()
            conn.close(
            messagebox.showinfo("success","record insereted")
            )
root = Tk()
ob=Hospital(root)
root.mainloop()
#adding new_feature - feature1
        self.hospital_table = ttk.Treeview(Detailframe, 
                                            columns=("NAMES OF TABLET", "Refence No", "Dose", "No of Tablets", "Lot",
                                                    "Issue Date", "Exp Date", "Side Effect", "Further info", "Blood Pressure",
                                                    "Any Allergy", "Medication", "Patient ID", "NHS number", "Date of Birth", 
                                                    "Patient Name", "Address", "Postcode"), 
                                            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) 