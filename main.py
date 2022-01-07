# main.py
import mysql.connector
from flask import Flask, redirect, url_for, request, render_template

from datetime import datetime
now = datetime.now()
formatted_date = now.strftime('%Y-%d-%m %H:%M:%S')

mydb = mysql.connector.connect(
    host="hospital-lab.mysql.database.azure.com",
    user="lab_admin",
    passwd="tamerbasha.2024",  # write ur own password
    database="Laboratory_Department"  # here
)
mycursor = mydb.cursor()
app = Flask(__name__)


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/Add_lab_tech', methods=['POST', 'GET'])
def Add_lab_tech():
    if request.method == 'POST':
        Username = request.form['Username']
        EmailAddress = request.form['EmailAddress']
        Password = request.form['Password']
        FirstName = request.form['FirstName']
        MiddleName = request.form['MiddleName']
        LastName = request.form['LastName']
        Sex = request.form['Sex']
        formatted_date = request.form['Birthdate']
        SSN = request.form['SSN']
        ManagerSSN = request.form['ManagerSSN']
        Salary = request.form['Salary']
        Address = request.form['Address']
        PhoneNumber = request.form['PhoneNumber']
        CV = request.form['CV']
        try:
            sql = "INSERT INTO Lab_Technician (SSN,First_Name,Middle_Name,Last_Name,SEX,Birthdate,Salary,Email,Address,Manager_SSN) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (SSN, FirstName, MiddleName, LastName, Sex,
                   formatted_date, Salary, EmailAddress, Address, ManagerSSN)
            mycursor.execute(sql, val)
            sql = "INSERT INTO LabTechPhoneNumber (LabTechSSN, PhoneNumber) VALUES (%s,%s)"
            val = (SSN, PhoneNumber)
            mycursor.execute(sql, val)
            sql = "INSERT INTO LabTechQualifications (LabTechSSN, Qualifications) VALUES (%s,%s)"
            val = (SSN, CV)
            mycursor.execute(sql, val)
            sql = "INSERT INTO User(User_SSN,Username,Password,Permission_Level,Email,LabTechSSN) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (SSN, Username, Password, "labtechnician", EmailAddress, SSN)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('Add_lab_tech.html', message=FirstName + ' ' + LastName + " has been succesfuly added to lab technicians.")
        except:
            return render_template('Add_lab_tech.html', error="Invalid input!")
    else:
        return render_template('Add_lab_tech.html')


@app.route('/View_report_patient', methods=['POST', 'GET'])
def View_report_patient():
    if request.method == 'GET':
        mycursor.execute(
            "SELECT  Publish_Date, ReportID, Name FROM report JOIN patient WHERE Patient_SSN = SSN")
        reportinfo = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'reportinfo': reportinfo
        }
        return render_template('View_report_patient.html', data=data)
    else:
        return render_template('View_report_post_OK.html')


@app.route('/Add_Report', methods=['POST', 'GET'])
def Add_Report():
    if request.method == 'POST':
        ReportID = request.form['ReportID']
        Name = request.form['Name']
        Publish_Date = request.form['Publish_Date']
        Reffered_By = request.form['Reffered_By']
        Comments = request.form['Comments']
        Patient_SSN = request.form['Patient_SSN']
        try:
            sql = "INSERT INTO report(ReportID,Name,Publish_Date,Referred_By,Comments,Patient_SSN) VALUES(%s, %s, %s, %s, %s, %s)"
            val = (ReportID, Name, Publish_Date,
                   Reffered_By, Comments, Patient_SSN)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('index.html', message=ReportID + " has been successfully added to the database")
        except:
            return render_template('Add_Report.html', error="Invalid input!")

    else:
        return render_template('Add_Report.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    return render_template('signup.html')


@app.route('/View_report_labtech', methods=['POST', 'GET'])
def View_report_labtech():
    if request.method == 'POST':
        PatientNumber = request.form['PatientNumber']
        ReportID = request.form['ReportID']
        mycursor.execute("SELECT Test_Name, Value, Reference_Range FROM report AS R JOIN patient JOIN test WHERE R.Patient_SSN = SSN AND ReportID = Report_ID AND Patient_Number=%s AND ReportID=%s", (PatientNumber, ReportID))
        reportinfo = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'reportinfo': reportinfo
        }
        mycursor.execute(
            "SELECT Name FROM report JOIN patient WHERE Patient_SSN = SSN AND Patient_Number=%s AND ReportID=%s", (PatientNumber, ReportID))
        x = mycursor.fetchone()
        ReportName = x[0]
        mycursor.execute(
            "SELECT Publish_Date FROM report JOIN patient WHERE Patient_SSN = SSN AND Patient_Number=%s AND ReportID=%s", (PatientNumber, ReportID))
        x = mycursor.fetchone()
        PublishDate = x[0]
        mycursor.execute(
            "SELECT Referred_By FROM report JOIN patient WHERE Patient_SSN = SSN AND Patient_Number=%s AND ReportID=%s", (PatientNumber, ReportID))
        x = mycursor.fetchone()
        Referred = x[0]
        mycursor.execute(
            "SELECT Comments FROM report JOIN patient WHERE Patient_SSN = SSN AND Patient_Number=%s AND ReportID=%s", (PatientNumber, ReportID))
        x = mycursor.fetchone()
        Comments = x[0]
        # ReportName=ReportName #data=data
        return render_template('View_report_post_OK.html', data=data, ReportName=ReportName, PublishDate=PublishDate, Referred=Referred, Comments=Comments)
    else:
        return render_template('View_report_labtech.html')


@app.route('/View_report_post_OK', methods=['POST', 'GET'])
def View_report_post_OK():
    return render_template('View_report_post_OK.html')


@app.route('/Add_new_equipment', methods=['POST', 'GET'])
def Add_new_equipment():
    return render_template('Add_new_equipment.html')


@app.route('/Edit_equipment', methods=['POST', 'GET'])
def Edit_equipment():
    return render_template('Edit_equipment.html')


@app.route('/Add_employee', methods=['POST', 'GET'])
def Add_employee():
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        MiddleName = request.form['MiddleName']
        LastName = request.form['LastName']
        Birthdate = request.form['Birthdate']
        SSN = request.form['SSN']
        Salary = request.form['Salary']
        Address = request.form['Address']
        if request.form['SupervisorSSN'] == (''):
            SupervisorSSN = None
        else:
            SupervisorSSN = request.form['SupervisorSSN']
        EmailAddress = request.form['EmailAddress']
        Gender = request.form['Gender']
        ID = request.form['ID']
        PhoneNumber = request.form['PhoneNumber']
        Qualifications = request.form['Qualifications']
        Username = request.form['Username']
        Password = request.form['Password']
        PermissionLevel = request.form['PermissionLevel']
        try:
            sql = "INSERT INTO employee(First_Name, Middle_Name, Last_Name, Birthdate, SSN, Salary, Address, Email, Supervisor_SSN, ID, SEX) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (FirstName, MiddleName, LastName, Birthdate, SSN,
                   Salary, Address, EmailAddress, SupervisorSSN, ID, Gender)
            mycursor.execute(sql, val)

            sql = "INSERT INTO employeephonenumber(PhoneNumber, EmployeeSSN) VALUES(%s, %s)"
            val = (PhoneNumber, SSN)
            mycursor.execute(sql, val)

            sql = "INSERT INTO employeequalifications(CV, EmployeeSSN) VALUES(%s, %s)"
            val = (Qualifications, SSN)
            mycursor.execute(sql, val)

            sql = "INSERT INTO User(User_SSN, Username, Password, Permission_Level, Email, EmpSSN) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (SSN, Username, Password, PermissionLevel, EmailAddress, SSN)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('index.html', message=FirstName + ' ' + LastName + " has been successfully added to the database")
        except:
            return render_template('Add_employee.html', error="Invalid input!")


@app.route('/Login', methods=['POST', 'GET'])
def Login():
    if request.method == 'POST':
        Email = request.form['Email']
        Password = request.form['Password']
        mycursor.execute(
            "SELECT Permission_Level FROM User WHERE Email=%s AND Password=%s", (Email, Password))
        permission = mycursor.fetchone()
        if permission:
            mycursor.execute(
                "SELECT Username FROM User WHERE Email=%s AND Password=%s", (Email, Password))
            x = mycursor.fetchone()
            username = x[0]
            if permission == ('admin',):
                return render_template('admin_home.html', message="Welcome " + username, username=username)
            if permission == ('employee',):
                return render_template('employee_home.html', message="Welcome " + username, username=username)
            if permission == ('labtechnician',):
                return render_template('labtech_home.html', message="Welcome " + username, username=username)
            if permission == ('patient',):
                return render_template('patient_home.html', message="Welcome " + username, username=username)
        else:
            return render_template('Login.html', error="Incorrect Email or Password!")
    else:
        return render_template('Login.html')


@app.route('/Add_labtech_dependents', methods=['POST', 'GET'])
def Add_labtech_dependents():
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        MiddleName = request.form['MiddleName']
        LastName = request.form['LastName']
        Birthdate = request.form['Birthdate']
        SSN = request.form['SSN']
        Gender = request.form['Gender']
        Address = request.form['Address']
        Relationship = request.form['Relationship']
        LabtechSSN = request.form['LabtechSSN']

        try:
            sql = "INSERT INTO Dependents_LabTech(Dependent_SSN, First_Name, Middle_Name, Last_Name, Birthdate, SEX, Address, Relationship, Lab_Tech_SSN ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (SSN, FirstName, MiddleName, LastName, Birthdate,
                   Gender, Address, Relationship, LabtechSSN)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('admin_home.html', message=FirstName + ' ' + LastName + " has been successfully added to the database")
        except:
            return render_template('Add_labtech_dependents.html', error="Invalid input!")

    else:
        return render_template('Add_labtech_dependents.html')


@app.route('/Add_empdependents', methods=['POST', 'GET'])
def Add_empdependents():
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        MiddleName = request.form['MiddleName']
        LastName = request.form['LastName']
        Birthdate = request.form['Birthdate']
        SSN = request.form['SSN']
        Gender = request.form['Gender']
        Address = request.form['Address']
        Relationship = request.form['Relationship']
        EmployeeSSN = request.form['EmployeeSSN']

        try:
            sql = "INSERT INTO dependents_employee(Dependent_SSN, First_Name, Middle_Name, Last_Name, Birthdate, SEX, Address, Relationship, ESSN ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (SSN, FirstName, MiddleName, LastName, Birthdate,
                   Gender, Relationship, Address, EmployeeSSN)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('index.html', message=FirstName + ' ' + LastName + " has been successfully added to the database")
        except:
            return render_template('Add_empdependents', error="Invalid input!")

    else:
        return render_template('Add_empdependents.html')


@app.route('/View_employee', methods=['POST', 'GET'])
def View_employee():
    if request.method == 'GET':
        # Personal info
        mycursor.execute(
            "SELECT ID, SSN, First_Name, Middle_Name, Last_Name, SEX, Birthdate, Salary, Supervisor_SSN FROM employee")
        personalinfo = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute(
            "SELECT SSN, First_Name,Last_Name,Username,Password, user.Email FROM employee JOIN user WHERE SSN = EmpSSN ")
        basicinfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute(
            "SELECT SSN, First_Name,Last_Name,Address,PhoneNumber FROM employee JOIN employeephonenumber WHERE SSN = EmployeeSSN  ")
        contactinfo = mycursor.fetchall()
        # Supervisor Table
        mycursor.execute(
            "SELECT S.ID,S.SSN,S.First_Name,S.Middle_Name,S.Last_Name,S.SEX, S.Birthdate,S.Salary FROM employee AS E JOIN employee AS S WHERE E.Supervisor_SSN = S.SSN ")
        superinfo = mycursor.fetchall()

        data = {
            'message': "data retrieved",
            'personalinfo': personalinfo,
            'basicinfo': basicinfo,
            'contactinfo': contactinfo,
            'superinfo': superinfo
        }
        return render_template('View_employee.html', data=data)
    else:
        EmployeeSSN = request.form['EmployeeSSN']
        # Personal info
        mycursor.execute(
            "SELECT E.ID, E.SSN, E.First_Name, E.Middle_Name, E.Last_Name, E.SEX, E.Birthdate, E.Salary, E.Supervisor_SSN FROM employee AS E WHERE E.SSN=%s", (EmployeeSSN,))
        personalinfo = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute(
            "SELECT E.SSN, E.First_Name,E.Last_Name,Username,Password, user.Email FROM employee AS E JOIN user WHERE E.SSN = user.EmpSSN AND E.SSN=%s", (EmployeeSSN,))
        basicinfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute(
            "SELECT E.SSN, E.First_Name,E.Last_Name,E.Address,PhoneNumber FROM employee AS E JOIN employeephonenumber WHERE E.SSN = EmployeeSSN AND E.SSN=%s", (EmployeeSSN,))
        contactinfo = mycursor.fetchall()
        # Supervisor Table
        mycursor.execute("SELECT S.ID,S.SSN,S.First_Name,S.Middle_Name,S.Last_Name,S.SEX, S.Birthdate,S.Salary FROM employee AS E JOIN employee AS S WHERE E.Supervisor_SSN = S.SSN AND E.SSN=%s", (EmployeeSSN,))
        superinfo = mycursor.fetchall()
        # Dependents Table
        mycursor.execute("SELECT Dependent_SSN, D.First_Name, D.Middle_Name, D.Last_Name, D.SEX, D.Birthdate, D.Address, Relationship FROM employee AS E JOIN dependents_employee AS D WHERE E.SSN = D.ESSN AND D.ESSN=%s", (EmployeeSSN,))
        depinfo = mycursor.fetchall()
        # Supervised Table
        mycursor.execute("SELECT S.ID, S.SSN, S.First_Name, S.Middle_Name, S.Last_Name, S.SEX, S.Birthdate, S.Salary FROM employee AS E JOIN employee AS S ON E.Supervisor_SSN = S.SSN AND E.SSN=%s", (EmployeeSSN,))
        supervisedinfo = mycursor.fetchall()
        # Supervises Table
        mycursor.execute("SELECT S.ID, E.SSN, E.First_Name, E.Middle_Name, E.Last_Name, E.SEX, E.Birthdate, E.Salary FROM employee AS E JOIN employee AS S ON E.Supervisor_SSN = S.SSN AND S.SSN=%s", (EmployeeSSN,))
        supervisesinfo = mycursor.fetchall()

        data = {
            'message': "data retrieved",
            'personalinfo': personalinfo,
            'basicinfo': basicinfo,
            'contactinfo': contactinfo,
            'superinfo': superinfo,
            'depinfo': depinfo,
            'supervisedinfo': supervisedinfo,
            'supervisesinfo': supervisesinfo
        }
        return render_template('View_employee.html', data=data)


@app.route('/Add_test', methods=['POST', 'GET'])
def Add_test():
    if request.method == 'POST':
        Test_ID = request.form['Test_ID']
        Test_Name = request.form['Test_Name']
        Category = request.form['Category']
        Value = request.form['Value']
        Start_Date = request.form['Start_Date']
        End_Date = request.form['End_Date']
        Reference_Range = request.form['Reference_Range']
        Cost = request.form['Cost']
        Patient_SSN = request.form['Patient_SSN']
        Report_ID = request.form['Report_ID']
        Lab_No = request.form['Lab_No']
        # try:
        sql = "INSERT INTO test(Test_ID,Test_Name,Category,Value,Start_Date,End_Date,Reference_Range,Cost,Patient_SSN,Report_ID,Lab_No) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (Test_ID, Test_Name, Category, Value, Start_Date, End_Date,
               Reference_Range, Cost, Patient_SSN, Report_ID, Lab_No)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('index.html', message=Test_ID + " has been successfully added to the database")
        # # except:
        #       return render_template('Add_test.html', error= "Invalid input!")

    else:
        return render_template('Add_test.html')


@app.route('/View_lab_tech', methods=['POST', 'GET'])
def View_lab_tech():
    if request.method == 'GET':
        # Personal info
        mycursor.execute(
            "SELECT SSN, First_Name, Middle_Name, Last_Name, SEX, Birthdate, Salary, Manager_SSN FROM lab_technician")
        PersonalInfo = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute(
            "SELECT SSN, First_Name,Last_Name,Username,Password, user.Email FROM lab_technician JOIN user WHERE SSN = LabTechSSN ")
        BasicInfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute(
            "SELECT SSN, First_Name,Last_Name,Address,PhoneNumber FROM lab_technician JOIN LabTechPhoneNumber WHERE SSN = LabTechSSN  ")
        ContactInfo = mycursor.fetchall()
        # # Manager Table
        # mycursor.execute("SELECT E.ID,E.SSN,E.First_Name,E.Middle_Name,E.Last_Name,E.SEX, E.Birthdate,E.Salary FROM lab_technician JOIN employee AS E WHERE  Manager_SSN= E.SSN ")
        # Manager = mycursor.fetchall()

        data = {
            'message': "data retrieved",
            'PersonalInfo': PersonalInfo,
            'BasicInfo': BasicInfo,
            'ContactInfo': ContactInfo,
            # 'Manager': Manager
        }
        return render_template('View_lab_tech.html', data=data)
    else:
        LabtechSSN = request.form['LabtechSSN']
        # Personal info
        mycursor.execute(
            "SELECT SSN, First_Name, Middle_Name, Last_Name, SEX, Birthdate, Salary, Manager_SSN FROM lab_technician WHERE SSN=%s", (LabtechSSN,))
        PersonalInfo = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute(
            "SELECT SSN, First_Name,Last_Name,Username,Password, user.Email FROM lab_technician JOIN user WHERE SSN = LabTechSSN  AND SSN=%s", (LabtechSSN,))
        BasicInfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute(
            "SELECT SSN, First_Name,Last_Name,Address,PhoneNumber FROM lab_technician JOIN LabTechPhoneNumber WHERE SSN = LabTechSSN AND SSN=%s", (LabtechSSN,))
        ContactInfo = mycursor.fetchall()
        # Manager Table
        mycursor.execute("SELECT E.ID,E.SSN,E.First_Name,E.Middle_Name,E.Last_Name,E.SEX, E.Birthdate,E.Salary FROM lab_technician AS L JOIN employee AS E WHERE  L.Manager_SSN= E.SSN AND L.SSN=%s", (LabtechSSN,))
        Manager = mycursor.fetchall()
        # Dependents Table
        mycursor.execute("SELECT SSN, Dependent_SSN, D.First_Name, D.Middle_Name, D.Last_Name, D.SEX, D.Birthdate, D.Address, Relationship FROM lab_technician JOIN Dependents_LabTech AS D WHERE SSN = D.Lab_Tech_SSN AND D.Lab_Tech_SSN=%s", (LabtechSSN,))
        Dependents = mycursor.fetchall()

        data = {
            'message': "data retrieved",
            'PersonalInfo': PersonalInfo,
            'BasicInfo': BasicInfo,
            'ContactInfo': ContactInfo,
            'Manager': Manager,
            'Dependents': Dependents,
        }
        return render_template('View_lab_tech.html', data=data)


@app.route('/View_lab', methods=['POST', 'GET'])
def View_lab():
    if request.method == 'GET':
        mycursor.execute("SELECT * FROM Lab")
        labinfo = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'labinfo': labinfo
        }
        return render_template('View_lab.html', data=data)


@app.route('/Add_lab', methods=['POST', 'GET'])
def Add_lab():
    if request.method == 'POST':
        labnum = request.form['labnum']
        labname = request.form['labname']
        labtype = request.form['labtype']
        lablocation = request.form['lablocation']
        try:
            sql = "INSERT INTO lab(Lab_Number,Lab_Name,Lab_Type,Lab_Location) VALUES (%s,%s,%s,%s)"
            val = (labnum, labname, labtype, lablocation)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('Add_lab.html', message="Lab " + labname + " has been successfully added to the labs table.")
        except:
            return render_template('Add_lab.html', error="Invalid input!")

    else:
        return render_template('Add_lab.html')


if __name__ == '__main__':
    app.run(debug=True)
