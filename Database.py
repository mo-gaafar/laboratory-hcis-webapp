import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="", #write ur own password
  database="Laboratory_Department" #here
)
mycursor = mydb.cursor()

#Creating the database. Run this one first instead of this  line above database="Laboratory_Department"
#mycursor.execute("CREATE DATABASE Laboratory_Department")


#Uncomment the Employee first, then run each one while commenting the others.

#Creating Lab Tech table
##mycursor.execute("CREATE TABLE Lab_Technician (SSN VARCHAR(255) NOT NULL, First_Name VARCHAR(255) NOT NULL, Middle_Name VARCHAR(255) NOT NULL, Last_Name VARCHAR(255) NOT NULL, SEX ENUM('male', 'female') NOT NULL, Birthdate DATE NOT NULL, Salary INT NOT NULL, Email VARCHAR(255) NOT NULL, Address TEXT NOT NULL, Manager_SSN VARCHAR(255) NOT NULL, PRIMARY KEY(SSN), FOREIGN KEY (Manager_SSN) REFERENCES Employee(SSN))")
#Creating LabTechAddress table
##mycursor.execute("CREATE TABLE LabTechAddress (LabTechSSN VARCHAR(255) NOT NULL, Address VARCHAR(255) NOT NULL,PRIMARY KEY(LabTechSSN, Address), FOREIGN KEY (LabTechSSN) REFERENCES Lab_Technician(SSN))")
#Creating LabTechQualifications table
##mycursor.execute("CREATE TABLE LabTechQualifications (LabTechSSN VARCHAR(255) NOT NULL, Qualifications VARCHAR(255) NOT NULL,PRIMARY KEY(LabTechSSN, Qualifications), FOREIGN KEY (LabTechSSN) REFERENCES Lab_Technician(SSN))")
#Creating LabTechPhoneNumber table
##mycursor.execute("CREATE TABLE LabTechPhoneNumber (LabTechSSN VARCHAR(255) NOT NULL, PhoneNumber VARCHAR(255) NOT NULL,PRIMARY KEY(LabTechSSN, PhoneNumber), FOREIGN KEY (LabTechSSN) REFERENCES Lab_Technician(SSN))")

#Creating Employee table
##mycursor.execute("CREATE TABLE Employee (SSN VARCHAR(255) NOT NULL, ID INT NOT NULL, First_Name VARCHAR(255) NOT NULL, Middle_Name VARCHAR(255) NOT NULL, Last_Name VARCHAR(255) NOT NULL, SEX ENUM('male', 'female') NOT NULL, Birthdate DATE NOT NULL, Salary INT NOT NULL, Email VARCHAR(255) NOT NULL, Address TEXT NOT NULL, Supervisor_SSN VARCHAR(255) , PRIMARY KEY(SSN), FOREIGN KEY ( Supervisor_SSN) REFERENCES Employee(SSN))")
#Creating EmployeeQualifications table
##mycursor.execute("CREATE TABLE EmployeeQualifications (EmployeeSSN VARCHAR(255) NOT NULL, Qualifications VARCHAR(255) NOT NULL,PRIMARY KEY(EmployeeSSN, Qualifications), FOREIGN KEY (EmployeeSSN) REFERENCES Employee(SSN))")
#Creating EmployeePhoneNumber table
##mycursor.execute("CREATE TABLE EmployeePhoneNumber (EmployeeSSN VARCHAR(255) NOT NULL, PhoneNumber VARCHAR(255) NOT NULL,PRIMARY KEY(EmployeeSSN, PhoneNumber), FOREIGN KEY (EmployeeSSN) REFERENCES Employee(SSN))")

#Creating Patient table
##mycursor.execute("CREATE TABLE Patient (SSN VARCHAR(255) NOT NULL, Patient_Number INT NOT NULL, First_Name VARCHAR(255) NOT NULL, Middle_Name VARCHAR(255) NOT NULL, Last_Name VARCHAR(255) NOT NULL, SEX ENUM('male', 'female') NOT NULL, Birthdate DATE NOT NULL, Nantionality VARCHAR(255) NOT NULL, Insurance VARCHAR(255) , Address TEXT NOT NULL, PRIMARY KEY(SSN))")
#Creating PatientPhoneNumber table
##mycursor.execute("CREATE TABLE PatientPhoneNumber (PatientSSN VARCHAR(255) NOT NULL, PhoneNumber VARCHAR(255) NOT NULL,PRIMARY KEY(PatientSSN, PhoneNumber), FOREIGN KEY (PatientSSN) REFERENCES Patient(SSN))")
#Creating PatientMedicalHistory table
##mycursor.execute("CREATE TABLE PatientMedicalHistory (PatientSSN VARCHAR(255) NOT NULL, MedicalHistory VARCHAR(255) NOT NULL,PRIMARY KEY(PatientSSN, MedicalHistory), FOREIGN KEY (PatientSSN) REFERENCES Patient(SSN))")


#Creating Equipment table
##mycursor.execute("CREATE TABLE Equipment (Serial_Number VARCHAR(255) NOT NULL, Inventory_ID INT UNIQUE NOT NULL, Department VARCHAR(255) NOT NULL, Device_Name VARCHAR(255) NOT NULL, Test_Name VARCHAR(255) NOT NULL, Test_Type VARCHAR(255) NOT NULL, Status ENUM('available', 'not available') NOT NULL, IPMMaintenance VARCHAR(255) NOT NULL, Manufacturer_ID VARCHAR(255) NOT NULL, Model VARCHAR(255) NOT NULL, PRIMARY KEY(Serial_Number))")

#Creating Lab table
##mycursor.execute("CREATE TABLE Lab (Lab_Number INT NOT NULL, Lab_Name VARCHAR(255) NOT NULL, Lab_Type VARCHAR(255) NOT NULL, Lab_Location TEXT NOT NULL, PRIMARY KEY(Lab_Number))")

#Creating Consumables table
##mycursor.execute("CREATE TABLE Consumables (Name VARCHAR(255) NOT NULL, Stock INT NOT NULL, Supplier_Contact TEXT NOT NULL, PRIMARY KEY(Name))")

#Creating Test table
##mycursor.execute("CREATE TABLE Test (Test_ID INT NOT NULL, Test_Name VARCHAR(255) NOT NULL, Category VARCHAR(255) NOT NULL, Value INT NOT NULL, Start_Date DATE NOT NULL, End_Date DATE NOT NULL , Reference_Range INT NOT NULL, Cost INT NOT NULL, Patient_SSN VARCHAR(255) NOT NULL, Report_ID INT NOT NULL, Lab_No INT NOT NULL, PRIMARY KEY(Test_ID), FOREIGN KEY (Patient_SSN) REFERENCES Patient(SSN), FOREIGN KEY (Report_ID) REFERENCES Report(REPORTID), FOREIGN KEY (Lab_No) REFERENCES Lab(Lab_Number))")

#Creating Report table
##mycursor.execute("CREATE TABLE Report (ReportID INT NOT NULL, Name VARCHAR(255) NOT NULL, Publish_Date DATE NOT NULL, Referred_By VARCHAR(255) NOT NULL, Comments TEXT , Patient_SSN VARCHAR(255) NOT NULL, PRIMARY KEY(ReportID), FOREIGN KEY ( Patient_SSN) REFERENCES Patient(SSN))")

#Creating Dependents_Employee table
##mycursor.execute("CREATE TABLE Dependents_Employee(Dependent_SSN VARCHAR(255) NOT NULL, ESSN VARCHAR(255) , First_Name VARCHAR(255) NOT NULL, Middle_Name VARCHAR(255) NOT NULL, Last_Name VARCHAR(255) NOT NULL, Birthdate DATE NOT NULL, Address TEXT NOT NULL, Relationship VARCHAR(255) NOT NULL, PRIMARY KEY(Dependent_SSN, ESSN), FOREIGN KEY (ESSN) REFERENCES Employee(SSN))")
#Creating DependentsEmpPhoneNumber table
##mycursor.execute("CREATE TABLE DependentsEmpPhoneNumber (DependentSSN VARCHAR(255) NOT NULL, PhoneNumber VARCHAR(255) NOT NULL,PRIMARY KEY(DependentSSN, PhoneNumber), FOREIGN KEY (DependentSSN) REFERENCES Dependents_Employee(Dependent_SSN))")

#Creating Dependents_LabTech table
##mycursor.execute("CREATE TABLE Dependents_LabTech(Dependent_SSN VARCHAR(255) NOT NULL, Lab_Tech_SSN VARCHAR(255) , First_Name VARCHAR(255) NOT NULL, Middle_Name VARCHAR(255) NOT NULL, Last_Name VARCHAR(255) NOT NULL, Birthdate DATE NOT NULL, Address TEXT NOT NULL, Relationship VARCHAR(255) NOT NULL, PRIMARY KEY(Dependent_SSN, Lab_Tech_SSN), FOREIGN KEY (Lab_Tech_SSN) REFERENCES Lab_Technician(SSN))")
#Creating DependentsLabTechPhoneNumber table
##mycursor.execute("CREATE TABLE DependentsLabTechPhoneNumber (DependentSSN VARCHAR(255) NOT NULL, PhoneNumber VARCHAR(255) NOT NULL,PRIMARY KEY(DependentSSN, PhoneNumber), FOREIGN KEY (DependentSSN) REFERENCES Dependents_LabTech(Dependent_SSN))")


#Creating Works_On table
##mycursor.execute("CREATE TABLE Works_On (LabTechSSN VARCHAR(255) NOT NULL, Hours INT NOT NULL, EquipmentSerialNumber VARCHAR(255) NOT NULL, PRIMARY KEY(LabTechSSN, EquipmentSerialNumber), FOREIGN KEY (LabTechSSN) REFERENCES Lab_Technician(SSN), FOREIGN KEY (EquipmentSerialNumber) REFERENCES Equipment(Serial_Number))")

#Creating Uses table
##mycursor.execute("CREATE TABLE Uses (Consumables_Name VARCHAR(255) NOT NULL, EquipmentSerialNumber VARCHAR(255) NOT NULL,PRIMARY KEY(Consumables_Name, EquipmentSerialNumber), FOREIGN KEY (Consumables_Name) REFERENCES Consumables(Name), FOREIGN KEY (EquipmentSerialNumber) REFERENCES Equipment(Serial_Number))")

#Creating Contains table
##mycursor.execute("CREATE TABLE Contains (LabNumber INT NOT NULL, EquipmentSerialNumber VARCHAR(255) NOT NULL,PRIMARY KEY(LabNumber, EquipmentSerialNumber), FOREIGN KEY (LabNumber) REFERENCES Lab(Lab_Number), FOREIGN KEY (EquipmentSerialNumber) REFERENCES Equipment(Serial_Number))")

#Creating Conducts table
##mycursor.execute("CREATE TABLE Conducts (LabTechSSn VARCHAR(255) NOT NULL, TestID INT NOT NULL,PRIMARY KEY(LabTechSSn, TestID), FOREIGN KEY (LabTechSSn) REFERENCES Lab_Technician(SSN), FOREIGN KEY (TestID) REFERENCES Test(Test_ID))")

#Creating User table
##mycursor.execute("CREATE TABLE User (User_SSN VARCHAR(255) NOT NULL, Username VARCHAR(255) NOT NULL, Password VARCHAR(255) NOT NULL, Permission_Level INT NOT NULL, Email VARCHAR(255) NOT NULL, PatientSSN VARCHAR(255) , LabTechSSN VARCHAR(255) , EmpSSN VARCHAR(255) , PRIMARY KEY(User_SSN), FOREIGN KEY (PatientSSN) REFERENCES Patient(SSN), FOREIGN KEY (LabTechSSn) REFERENCES Lab_Technician(SSN), FOREIGN KEY (EmpSSN) REFERENCES Employee(SSN))")
