# main.py
import mysql.connector
from flask import Flask, redirect, url_for, request, render_template, session, make_response

from datetime import datetime
now = datetime.now()
formatted_date = now.strftime('%Y-%d-%m %H:%M:%S')

mydb = mysql.connector.connect(
    host="hospital-lab.mysql.database.azure.com",
    user="lab_admin",
    passwd="tamerbasha.2024",  # write ur own password
    database="Laboratory_Department"  # here
)


# Enable cursor buffering
mycursor = mydb.cursor(buffered=True)
app = Flask(__name__)

# Session encryption key
app.config["SECRET_KEY"] = "uf_a0HhSlHAneZoA0Xe8Gw"

# Initialize navbar inheritance dictionary


@app.context_processor
def injectnavbarhtml():
    NavbarDict = {
        ('patient',): 'patient_navbar.html',
        ('labtechnician',): 'labtech_navbar.html',
        ('admin',): 'admin_navbar.html',
        ('employee',): 'hr_navbar.html',
        None: 'patient_navbar.html'
    }
    # print(NavbarDict[session.get("PERMISSION", None)])
    string = NavbarDict[session.get("PERMISSION", None)]
    return dict(navbarhtml=string)


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/Forgotpassword', methods=['POST', 'GET'])
def Forgotpassword():
    if request.method == 'POST':
        Email_check = request.form['Email_check']
        resp = make_response(redirect('/Newpassword'))
        resp.set_cookie('Email_check', Email_check)
        return resp
    else:
        return render_template('Forgotpassword.html')


@app.route('/Newpassword', methods=['POST', 'GET'])
def Newpassword():
    if request.method == 'POST':
        Email_check = request.cookies.get('Email_check')       
        newPass = request.form['newPass']  
        newPass2 = request.form['newPass2']
        if newPass == newPass2:
            sql = "UPDATE user SET Password=%s WHERE user.Email=%s"
            val = (newPass,Email_check)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('login.html', message= 'Your password has been reset succesfully')
        else:
            return render_template('NewPassword.html', error="Error! Passwords Do Not Match!" )
    else:
        #print(request.cookies.get('Email_check'))
        return render_template('Newpassword.html')


@app.route('/Home', methods=['POST', 'GET'])
def Home():
    # TODO: PASS USER INFORMATION THROUGH THIS ROUTE
    if request.method == 'GET':

        # patient
        # lab tech
        # admin and HR(employee)

        # TODO: fix this in frontend and HOME route
        # if permission == ('admin',):
        #     return render_template('admin_home.html', message="Welcome " + username, username=username)
        # if permission == ('employee',):
        #     return render_template('employee_home.html', message="Welcome " + username, username=username)
        # if permission == ('labtechnician',):
        #     return render_template('labtech_home.html', message="Welcome " + username, username=username)
        # if permission == ('patient',):
        #     return render_template('patient_home.html', message="Welcome " + username, username=username)

        permission = session.get("PERMISSION", None)

        print(permission)
        print("returned to homepage")

        if permission == ('labtechnician',):
            return render_template("Home_labtech.html")
        elif permission == ('employee',) or permission == ('admin',):
            return render_template("Home_admin.html")
        elif permission == ('patient',):
            return render_template("Home_patient.html")


@app.route('/View_lab_admin', methods=['POST', 'GET'])
def View_lab_admin():
    if request.method == 'GET':
        mycursor.execute("SELECT * FROM Lab")
        labinfo = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'labinfo': labinfo
        }
        return render_template('View_lab_admin.html', data=data)


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


@app.route('/View_lab_employee', methods=['POST', 'GET'])
def View_lab_employee():
    if request.method == 'GET':
        mycursor.execute("SELECT * FROM Lab")
        labinfo = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'labinfo': labinfo
        }
        return render_template('View_lab_employee.html', data=data)


@app.route('/View_lab_labtech', methods=['POST', 'GET'])
def View_lab_labtech():
    if request.method == 'GET':
        mycursor.execute("SELECT * FROM Lab")
        labinfo = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'labinfo': labinfo
        }
        return render_template('View_lab_labtech.html', data=data)


@app.route('/View_lab_patient', methods=['POST', 'GET'])
def View_lab_patient():
    if request.method == 'GET':
        mycursor.execute("SELECT * FROM Lab")
        labinfo = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'labinfo': labinfo
        }
        return render_template('View_lab_patient.html', data=data)


# TODO: CHECK REDIRECT MESSAGE

@app.route('/Add_lab_tech_admin', methods=['POST', 'GET'])
def Add_lab_tech_admin():
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
            print('Labtech added by')
            # TODO: Fix redirecting in /home route so it can send message or error
            return redirect('/Home', message=FirstName + ' ' + LastName + " has been succesfuly added to lab technicians.")
        except:
            return render_template('Add_lab_tech_admin.html', error="Invalid input!")
    else:
        return render_template('Add_lab_tech_admin.html')


@app.route('/Add_lab_tech_emp', methods=['POST', 'GET'])
def Add_lab_tech_emp():
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
            # TODO: Fix redirecting in /home route so it can send message or error
            return render_template('/Home', message=FirstName + ' ' + LastName + " has been succesfuly added to lab technicians.")
        except:
            return render_template('Add_lab_tech_emp.html', error="Invalid input!")
    else:
        return render_template('Add_lab_tech_emp.html')


@app.route('/Add_patient_admin', methods=['POST', 'GET'])
def Add_patient_admin():
    if request.method == 'POST':
        Username = request.form['Username']
        Email = request.form['Email']
        Password = request.form['Password']
        FirstName = request.form['FirstName']
        MiddleName = request.form['MiddleName']
        LastName = request.form['LastName']
        Gender = request.form['Gender']
        formatted_date = request.form['Birthdate']
        SSN = request.form['SSN']
        Insurance = request.form['Insurance']
        Address = request.form['Address']
        PhoneNumber = request.form['PhoneNumber']
        MedicalHistory = request.form['MedicalHistory']
        try:
            sql = "INSERT INTO Patient(SSN,First_Name, Middle_Name, Last_Name, SEX, Birthdate, Insurance,Address, Email) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (SSN, FirstName, MiddleName, LastName, Gender,
                   formatted_date, Insurance, Address, Email)
            mycursor.execute(sql, val)
            sql = "INSERT INTO User(User_SSN,Username,Password,Permission_Level,Email,PatientSSN) VALUES(%s, %s, %s, %s, %s, %s)"
            val = (SSN, Username, Password, "patient", Email, SSN)
            mycursor.execute(sql, val)
            sql = "INSERT INTO PatientPhoneNumber(PatientSSN, PhoneNumber) VALUES(%s, %s)"
            val = (SSN, PhoneNumber)
            mycursor.execute(sql, val)
            sql = "INSERT INTO PatientMedicalHistory(PatientSSN, MedicalHistory) VALUES(%s, %s)"
            val = (SSN, MedicalHistory)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('/Home', message=FirstName + LastName+" has been successfully added to the database")
        except:
            return render_template('Add_patient_admin.html', error="Invalid input!")

    else:
        return render_template('Add_patient_admin.html')


@app.route('/View_report_admin', methods=['POST', 'GET'])
def View_report_admin():
    if request.method == 'POST':
        PatientNumber = request.form['PatientNumber']
        ReportID = request.form['ReportID']
        mycursor.execute("SELECT Test_Name, Value, Reference_Range FROM report AS R JOIN patient JOIN test WHERE R.Patient_SSN = SSN AND ReportID = Report_ID AND SSN=%s AND ReportID=%s", (PatientNumber, ReportID))
        reportinfo = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'reportinfo': reportinfo
        }
        mycursor.execute(
            "SELECT Name FROM report JOIN patient WHERE Patient_SSN = SSN AND SSN=%s AND ReportID=%s", (PatientNumber, ReportID))
        x = mycursor.fetchone()
        ReportName = x[0]
        mycursor.execute(
            "SELECT Publish_Date FROM report JOIN patient WHERE Patient_SSN = SSN AND SSN=%s AND ReportID=%s", (PatientNumber, ReportID))
        x = mycursor.fetchone()
        PublishDate = x[0]
        mycursor.execute(
            "SELECT Referred_By FROM report JOIN patient WHERE Patient_SSN = SSN AND SSN=%s AND ReportID=%s", (PatientNumber, ReportID))
        x = mycursor.fetchone()
        Referred = x[0]
        mycursor.execute(
            "SELECT Comments FROM report JOIN patient WHERE Patient_SSN = SSN AND patient.SSN=%s AND ReportID=%s", (PatientNumber, ReportID))
        x = mycursor.fetchone()
        Comments = x[0]
        return render_template('View_report_post_OK.html', data=data, ReportName=ReportName, PublishDate=PublishDate, Referred=Referred, Comments=Comments)
    else:
        mycursor.execute(
            "SELECT ReportID,SSN,Name FROM report JOIN patient ON Patient_SSN = SSN")
        All_reports = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'All_reports': All_reports
        }
        return render_template('View_report_admin.html', data=data)


@app.route('/View_report_patient', methods=['POST', 'GET'])
def View_report_patient():
    if request.method == 'GET':
        print(session.get("USERSSN", None))
        mycursor.execute(
            "SELECT Publish_Date, ReportID, Name FROM report JOIN patient ON Patient_SSN = SSN  WHERE Patient_SSN = %s", (session.get("USERSSN", None),))
        reportinfo = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'reportinfo': reportinfo
        }
        # TODO: user session variable in queries
        return render_template('View_report_patient.html', data=data)
    else:

        ReportID = request.form['ReportID']
        print(ReportID)
        mycursor.execute(
            "SELECT Test_Name, Value, Reference_Range FROM report AS R JOIN test ON ReportID = Report_ID WHERE ReportID=%s", (ReportID,))
        reportinfo = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'reportinfo': reportinfo
        }
        mycursor.execute(
            "SELECT Name FROM report WHERE ReportID=%s", (ReportID,))
        x = mycursor.fetchone()
        ReportName = x[0]
        mycursor.execute(
            "SELECT Publish_Date FROM report WHERE ReportID=%s", (ReportID,))
        x = mycursor.fetchone()
        PublishDate = x[0]
        mycursor.execute(
            "SELECT Referred_By FROM report WHERE ReportID=%s", (ReportID,))
        x = mycursor.fetchone()
        Referred = x[0]
        mycursor.execute(
            "SELECT Comments FROM report WHERE ReportID=%s", (ReportID,))
        x = mycursor.fetchone()
        Comments = x[0]
        return render_template('View_report_post_OK.html', data=data, ReportName=ReportName, PublishDate=PublishDate, Referred=Referred, Comments=Comments)


@app.route('/View_labtech_admin', methods=['POST', 'GET'])
def View_labtech_admin():
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
        return render_template('View_labtech_admin.html', data=data)
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
        return render_template('View_labtech_admin.html', data=data)


@app.route('/View_labtech_employee', methods=['POST', 'GET'])
def View_labtech_employee():
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
        return render_template('View_labtech_employee.html', data=data)
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
        return render_template('View_labtech_employee.html', data=data)


@app.route('/View_labtech_labtech', methods=['POST', 'GET'])
def View_labtech_labtech():
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
        return render_template('View_labtech_labtech.html', data=data)
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
        return render_template('View_labtech_labtech.html', data=data)


@app.route('/View_employee_emp', methods=['POST', 'GET'])
def View_employee_emp():
    if request.method == 'GET':
        # Personal info
        mycursor.execute(
            "SELECT ID, SSN, First_Name, Middle_Name, Last_Name, SEX, Birthdate, Supervisor_SSN FROM employee")
        personalinfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute(
            "SELECT SSN, First_Name,Last_Name,Address,PhoneNumber, Email FROM employee JOIN employeephonenumber WHERE SSN = EmployeeSSN  ")
        contactinfo = mycursor.fetchall()
        # Supervisor Table
        mycursor.execute(
            "SELECT S.ID,S.SSN,S.First_Name,S.Middle_Name,S.Last_Name,S.SEX, S.Birthdate,S.Salary FROM employee AS E JOIN employee AS S WHERE E.Supervisor_SSN = S.SSN ")
        superinfo = mycursor.fetchall()

        data = {
            'message': "data retrieved",
            'personalinfo': personalinfo,
            'contactinfo': contactinfo,
            'superinfo': superinfo
        }
        return render_template('View_employee_emp.html', data=data)
    else:
        EmployeeSSN = request.form['EmployeeSSN']
        # Personal info
        mycursor.execute(
            "SELECT E.ID, E.SSN, E.First_Name, E.Middle_Name, E.Last_Name, E.SEX, E.Birthdate, E.Supervisor_SSN FROM employee AS E WHERE E.SSN=%s", (EmployeeSSN,))
        personalinfo = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute(
            "SELECT E.SSN, E.First_Name,E.Last_Name,Username,Password, user.Email FROM employee AS E JOIN user WHERE E.SSN = user.EmpSSN AND E.SSN=%s", (EmployeeSSN,))
        basicinfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute(
            "SELECT E.SSN, E.First_Name,E.Last_Name,E.Address,PhoneNumber, E.Email FROM employee AS E JOIN employeephonenumber WHERE E.SSN = EmployeeSSN AND E.SSN=%s", (EmployeeSSN,))
        contactinfo = mycursor.fetchall()
        # Supervisor Table
        mycursor.execute("SELECT S.ID,S.SSN,S.First_Name,S.Middle_Name,S.Last_Name,S.SEX, S.Birthdate,S.Salary FROM employee AS E JOIN employee AS S WHERE E.Supervisor_SSN = S.SSN AND E.SSN=%s", (EmployeeSSN,))
        superinfo = mycursor.fetchall()
        # Dependents Table
        mycursor.execute("SELECT Dependent_SSN, D.First_Name, D.Middle_Name, D.Last_Name, D.SEX, D.Birthdate, D.Address, Relationship FROM employee AS E JOIN dependents_employee AS D WHERE E.SSN = D.ESSN AND D.ESSN=%s", (EmployeeSSN,))
        depinfo = mycursor.fetchall()
        # Supervised Table
        mycursor.execute(
            "SELECT S.ID, S.SSN, S.First_Name, S.Middle_Name, S.Last_Name, S.SEX, S.Birthdate FROM employee AS E JOIN employee AS S ON E.Supervisor_SSN = S.SSN AND E.SSN=%s", (EmployeeSSN,))
        supervisedinfo = mycursor.fetchall()
        # Supervises Table
        mycursor.execute(
            "SELECT S.ID, E.SSN, E.First_Name, E.Middle_Name, E.Last_Name, E.SEX, E.Birthdate  FROM employee AS E JOIN employee AS S ON E.Supervisor_SSN = S.SSN AND S.SSN=%s", (EmployeeSSN,))
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
        return render_template('View_employee_emp.html', data=data)


@app.route('/View_employee_admin', methods=['POST', 'GET'])
def View_employee_admin():
    if request.method == 'GET':
        # Personal info
        mycursor.execute(
            "SELECT ID, SSN, First_Name, Middle_Name, Last_Name, SEX, Birthdate, Supervisor_SSN FROM employee")
        personalinfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute(
            "SELECT SSN, First_Name,Last_Name,Address,PhoneNumber, Email FROM employee JOIN employeephonenumber WHERE SSN = EmployeeSSN  ")
        contactinfo = mycursor.fetchall()
        # Supervisor Table
        mycursor.execute(
            "SELECT S.ID,S.SSN,S.First_Name,S.Middle_Name,S.Last_Name,S.SEX, S.Birthdate,S.Salary FROM employee AS E JOIN employee AS S WHERE E.Supervisor_SSN = S.SSN ")
        superinfo = mycursor.fetchall()

        data = {
            'message': "data retrieved",
            'personalinfo': personalinfo,
            'contactinfo': contactinfo,
            'superinfo': superinfo
        }
        return render_template('View_employee_admin.html', data=data)
    else:
        EmployeeSSN = request.form['EmployeeSSN']
        # Personal info
        mycursor.execute(
            "SELECT E.ID, E.SSN, E.First_Name, E.Middle_Name, E.Last_Name, E.SEX, E.Birthdate, E.Supervisor_SSN FROM employee AS E WHERE E.SSN=%s", (EmployeeSSN,))
        personalinfo = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute(
            "SELECT E.SSN, E.First_Name,E.Last_Name,Username,Password, user.Email FROM employee AS E JOIN user WHERE E.SSN = user.EmpSSN AND E.SSN=%s", (EmployeeSSN,))
        basicinfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute(
            "SELECT E.SSN, E.First_Name,E.Last_Name,E.Address,PhoneNumber, E.Email FROM employee AS E JOIN employeephonenumber WHERE E.SSN = EmployeeSSN AND E.SSN=%s", (EmployeeSSN,))
        contactinfo = mycursor.fetchall()
        # Supervisor Table
        mycursor.execute("SELECT S.ID,S.SSN,S.First_Name,S.Middle_Name,S.Last_Name,S.SEX, S.Birthdate,S.Salary FROM employee AS E JOIN employee AS S WHERE E.Supervisor_SSN = S.SSN AND E.SSN=%s", (EmployeeSSN,))
        superinfo = mycursor.fetchall()
        # Dependents Table
        mycursor.execute("SELECT Dependent_SSN, D.First_Name, D.Middle_Name, D.Last_Name, D.SEX, D.Birthdate, D.Address, Relationship FROM employee AS E JOIN dependents_employee AS D WHERE E.SSN = D.ESSN AND D.ESSN=%s", (EmployeeSSN,))
        depinfo = mycursor.fetchall()
        # Supervised Table
        mycursor.execute(
            "SELECT S.ID, S.SSN, S.First_Name, S.Middle_Name, S.Last_Name, S.SEX, S.Birthdate FROM employee AS E JOIN employee AS S ON E.Supervisor_SSN = S.SSN AND E.SSN=%s", (EmployeeSSN,))
        supervisedinfo = mycursor.fetchall()
        # Supervises Table
        mycursor.execute(
            "SELECT S.ID, E.SSN, E.First_Name, E.Middle_Name, E.Last_Name, E.SEX, E.Birthdate  FROM employee AS E JOIN employee AS S ON E.Supervisor_SSN = S.SSN AND S.SSN=%s", (EmployeeSSN,))
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
        return render_template('View_employee_admin.html', data=data)


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
            return render_template('/Home', message=FirstName + ' ' + LastName + " has been succesfuly added to lab technicians.")
            #TODO: redirect('/Home') +messsages or errors
        except:
            return render_template('Add_lab_tech.html', error="Invalid input!")
    else:
        return render_template('Add_lab_tech.html')


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
            # TODO: Fix redirecting in /home route so it can send message or error
            return render_template('/Home', message=ReportID + " has been successfully added to the database")
        except:
            return render_template('Add_Report.html', error="Invalid input!")

    else:
        return render_template('Add_Report.html')


@app.route('/Add_report_labtech', methods=['POST', 'GET'])
def Add_report_labtech():
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
            # TODO: Fix redirecting in /home route so it can send message or error
            #return render_template('/Home', message=ReportID + " has been successfully added to the database")
            return render_template('Home_labtech.html', message=ReportID + " has been successfully added to the database")
        except:
            return render_template('Add_report_labtech.html', error="Invalid input!")

    else:
        return render_template('Add_report_labtech.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        Username = request.form['Username']
        Email = request.form['Email']
        Password = request.form['Password']
        FirstName = request.form['FirstName']
        MiddleName = request.form['MiddleName']
        LastName = request.form['LastName']
        Gender = request.form['Gender']
        formatted_date = request.form['Birthdate']
        SSN = request.form['SSN']
        Insurance = request.form['Insurance']
        Address = request.form['Address']
        PhoneNumber = request.form['PhoneNumber']
        MedicalHistory = request.form['MedicalHistory']
        try:
            sql = "INSERT INTO Patient(SSN,First_Name, Middle_Name, Last_Name, SEX, Birthdate, Insurance,Address, Email) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (SSN, FirstName, MiddleName, LastName, Gender,
                   formatted_date, Insurance, Address, Email)
            mycursor.execute(sql, val)
            sql = "INSERT INTO User(User_SSN,Username,Password,Permission_Level,Email,PatientSSN) VALUES(%s, %s, %s, %s, %s, %s)"
            val = (SSN, Username, Password, "patient", Email, SSN)
            mycursor.execute(sql, val)
            sql = "INSERT INTO PatientPhoneNumber(PatientSSN, PhoneNumber) VALUES(%s, %s)"
            val = (SSN, PhoneNumber)
            mycursor.execute(sql, val)
            sql = "INSERT INTO PatientMedicalHistory(PatientSSN, MedicalHistory) VALUES(%s, %s)"
            val = (SSN, MedicalHistory)
            mycursor.execute(sql, val)
            mydb.commit()
            return render_template('login.html', message="You now can login to your account!")
        except:
            return render_template('signup.html', error="Invalid input!")

    else:
        return render_template('signup.html')


@app.route('/View_report_labtech', methods=['POST', 'GET'])
def View_report_labtech():
    if request.method == 'POST':
        # TODO: make lab tech view the reports they participate in only
        # session.get('USERSSN',None)
        PatientNumber = request.form['PatientNumber']
        ReportID = request.form['ReportID']
        mycursor.execute("SELECT Test_Name, Value, Reference_Range FROM report AS R JOIN patient JOIN test WHERE R.Patient_SSN = SSN AND ReportID = Report_ID AND SSN=%s AND ReportID=%s", (PatientNumber, ReportID))
        reportinfo = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'reportinfo': reportinfo
        }
        mycursor.execute(
            "SELECT Name FROM report JOIN patient WHERE Patient_SSN = SSN AND SSN=%s AND ReportID=%s", (PatientNumber, ReportID))
        x = mycursor.fetchone()
        ReportName = x[0]
        mycursor.execute(
            "SELECT Publish_Date FROM report JOIN patient WHERE Patient_SSN = SSN AND SSN=%s AND ReportID=%s", (PatientNumber, ReportID))
        x = mycursor.fetchone()
        PublishDate = x[0]
        mycursor.execute(
            "SELECT Referred_By FROM report JOIN patient WHERE Patient_SSN = SSN AND SSN=%s AND ReportID=%s", (PatientNumber, ReportID))
        x = mycursor.fetchone()
        Referred = x[0]
        mycursor.execute(
            "SELECT Comments FROM report JOIN patient WHERE Patient_SSN = SSN AND patient.SSN=%s AND ReportID=%s", (PatientNumber, ReportID))
        x = mycursor.fetchone()
        Comments = x[0]
        return render_template('View_report_post_OK.html', data=data, ReportName=ReportName, PublishDate=PublishDate, Referred=Referred, Comments=Comments)
    else:
        mycursor.execute(
            "SELECT ReportID,SSN,Name FROM report JOIN patient ON Patient_SSN = SSN")
        All_reports = mycursor.fetchall()
        data = {
            'message': "data retrieved",
            'All_reports': All_reports
        }
        return render_template('View_report_labtech.html', data=data)


@app.route('/View_report_post_OK', methods=['POST', 'GET'])
def View_report_post_OK():
    return render_template('View_report_post_OK.html')


@app.route('/Add_new_equipment', methods=['POST', 'GET'])
def Add_new_equipment():
    if request.method == 'POST':
        Serial_Number = request.form['Serial_Number']
        Device_Name = request.form['Device_Name']
        Model = request.form['Model']
        ManufacturerName = request.form['ManufacturerName']
        Manufacturer_ID = request.form['Manufacturer_ID']
        ManufacturingDate = request.form['ManufacturingDate']
        Department = request.form['Department']
        Inventory_ID = request.form['Inventory_ID']
        Status = request.form['Status']
        IPMMaintenance = request.form['IPMMaintenance']
        Test_Name = request.form['Test_Name']
        Test_Type = request.form['Test_Type']
       
        
        # try:
        sql = "INSERT INTO equipment (Serial_Number,Inventory_ID,Department,Device_Name,Test_Name,Test_Type,Status,IPMMaintenance,Manufacturer_ID,Model,ManufacturerName,ManufacturingDate) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val= (Serial_Number,Inventory_ID,Department,Device_Name,Test_Name,Test_Type,Status,IPMMaintenance,Manufacturer_ID,Model,ManufacturerName,ManufacturingDate)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('Add_new_equipment.html', message=Device_Name  + " has been succesfuly added to new equipment.")
        # except:
            # return render_template('Add_new_equipment.html', error="Invalid input!")
    else:
        return render_template('Add_new_equipment.html')

@app.route('/Add_consumables', methods=['POST', 'GET'])
def Add_consumables():
    if request.method == 'POST':
        Name = request.form['Name']
        Stock = request.form['Stock']
        InventoryID = request.form['InventoryID']
        SupplierContact = request.form['SupplierContact']
        EquipSSN = request.form['EquipSSN']
       
        try:
            sql = "INSERT INTO consumables (Name,Stock,InventoryID,SupplierContact) VALUES(%s,%s,%s,%s)"
            val = (Name, Stock,InventoryID,SupplierContact)
            mycursor.execute(sql, val)
            mydb.commit()
            sql = "INSERT INTO uses (Consumables_Name,EquipmentSerialNUmber) VALUES(%s,%s)"
            val = (Name,EquipSSN)
            mycursor.execute(sql, val)
            return render_template('Add_consumables.html', message=  Name + " has been successfully added to the consumables table.")
        except:
            return render_template('Add_consumables.html', error="Invalid input!")

    else:
        return render_template('Add_consumables.html')
    
@app.route('/viewequipment', methods=['POST', 'GET'])
def viewequipment():
     if request.method == 'GET':
        # Personal info
        mycursor.execute("SELECT Serial_Number, Device_Name,Model FROM equipment")
        DeviceInformation = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute("SELECT ManufacturerName, Manufacturer_ID,ManufacturingDate FROM equipment")
        ManufacturerInformation = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute("SELECT Department, Inventory_ID,Status,IPMMaintenance FROM equipment")
        InstitutionalInformation = mycursor.fetchall()
        # Supervisor Table
        mycursor.execute("SELECT Test_Name, Test_Type FROM equipment")
        TestInformation = mycursor.fetchall()
        mycursor.execute("SELECT Device_Name, Serial_Number FROM equipment")
        EquipmentList = mycursor.fetchall()
       



        data = {
            'message': "data retrieved",
            'DeviceInformation': DeviceInformation,
            'ManufacturerInformation': ManufacturerInformation,
            'InstitutionalInformation': InstitutionalInformation,
            'TestInformation': TestInformation,
            'EquipmentList': EquipmentList
            }
        
        return render_template('viewequipment.html', data=data)
     else:
        Serial_Number = request.form['Serial_Number']
        # Personal info
        mycursor.execute("SELECT Serial_Number, Device_Name,Model FROM equipment WHERE Serial_Number=%s", (Serial_Number,))
        DeviceInformation = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute("SELECT ManufacturerName, Manufacturer_ID,ManufacturingDate FROM equipment WHERE Serial_Number=%s", (Serial_Number,))
        ManufacturerInformation = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute("SELECT Department, Inventory_ID,Status,IPMMaintenance FROM equipment WHERE Serial_Number=%s", (Serial_Number,))
        InstitutionalInformation = mycursor.fetchall()
        # Supervisor Table
        mycursor.execute("SELECT Test_Name, Test_Type FROM equipment WHERE Serial_Number=%s", (Serial_Number,))
        TestInformation = mycursor.fetchall()
        # Dependents Table
        mycursor.execute("SELECT Device_Name, Serial_Number FROM equipment WHERE Serial_Number=%s", (Serial_Number,))
        EquipmentList = mycursor.fetchall()
        # Supervised Table
       


        data = {
            'message': "data retrieved",
            'DeviceInformation': DeviceInformation,
            'ManufacturerInformation': ManufacturerInformation,
            'InstitutionalInformation': InstitutionalInformation,
            'TestInformation': TestInformation,
            'EquipmentList': EquipmentList
        }
        return render_template('viewequipment.html', data=data)
    
    
    
@app.route('/viewconsumables', methods=['POST', 'GET'])
def viewconsumables():
     if request.method == 'GET':
        # Personal info
        mycursor.execute("SELECT Name, Stock,SupplierContact,InventoryID FROM consumables")
        ConsumableInformation = mycursor.fetchall()
       
        # Basic Info Button
  
    
        data = {
            'message': "data retrieved",
            'ConsumableInformation': ConsumableInformation
            }
        
        return render_template('viewconsumables.html', data=data)
     else:
        InventoryID = request.form['InventoryID']
        # Personal info
        mycursor.execute("SELECT Name, Stock,SupplierContact,InventoryID FROM consumables WHERE InventoryID=%s", (InventoryID,))
        ConsumableInformation = mycursor.fetchall()
    

        data = {
            'message': "data retrieved",
            'ConsumableInformation': ConsumableInformation
        }
        return render_template('viewconsumables.html', data=data)

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
            # TODO: Fix redirecting in /home route so it can send message or error
            return render_template('/Home', message=FirstName + ' ' + LastName + " has been successfully added to the database")
        except:
            return render_template('Add_employee.html', error="Invalid input!")
    else:
        return render_template('Add_employee.html')


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
            # print(username)
            mycursor.execute(
                "SELECT User_SSN FROM user WHERE Username = %s", (username,))
            x = mycursor.fetchone()
            userssn = x[0]
            # SETTING SESSION VARIABLES
            session["USERNAME"] = username
            session["PERMISSION"] = permission
            session["USERSSN"] = userssn
            print(session.get("USERNAME", None))
            print(session.get("PERMISSION", None))
            print(session.get("USERSSN", None))

            # TODO: SEND MESSAGE AND ERROR THROUGH REDIRECT
            # DERIVING NAME BASED ON USERPERMISSION VARIABLE
            return redirect('/Home')

            # TODO: fix this in frontend and HOME route
            # if permission == ('admin',):
            #     return render_template('admin_home.html', message="Welcome " + username, username=username)
            # if permission == ('employee',):
            #     return render_template('employee_home.html', message="Welcome " + username, username=username)
            # if permission == ('labtechnician',):
            #     return render_template('labtech_home.html', message="Welcome " + username, username=username)
            # if permission == ('patient',):
            #     return render_template('patient_home.html', message="Welcome " + username, username=username)
        else:
            return render_template('Login.html', error="Incorrect Email or Password!")
    else:
        return render_template('Login.html')


@app.route('/Logout', methods=['POST', 'GET'])
def Logout():
    # CLEARS SESSION ON LOGOUT
    session.pop("USERNAME", None)
    session.pop("PERMISSION", None)
    session.pop("USERSSN", None)

    return redirect(url_for("Login"))


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
            # TODO: Fix redirecting in /home route so it can send message or error
            return render_template('/Home', message=FirstName + ' ' + LastName + " has been successfully added to the database")
        except:
            return render_template('Add_labtech_dependents.html', error="Invalid input!")

    else:
        return render_template('Add_labtech_dependents.html')


@app.route('/Add_labtech_dependents_emp', methods=['POST', 'GET'])
def Add_labtech_dependents_emp():
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
            # TODO: Fix redirecting in /home route so it can send message or error
            return render_template('/Home', message=FirstName + ' ' + LastName + " has been successfully added to the database.")
        except:

            return render_template('Add_labtech_dependents_emp.html', error="Invalid input!")

    else:
        return render_template('Add_labtech_dependents_emp.html')


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
            # TODO: Fix redirecting in /home route so it can send message or error
            return render_template('/Home', message=FirstName + ' ' + LastName + " has been successfully added to Employee "+EmployeeSSN+"dependents.")
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


@app.route('/ContactUs', methods=['POST', 'GET'])
def ContactUs():
    if request.method == 'GET':
        return render_template("ContactUs.html")
    else:
        return redirect('/Home')


@app.route('/Add_test', methods=['POST', 'GET'])
def Add_test():
    if request.method == 'POST':

        Test_ID = request.form['Test_ID']
        Test_Name = request.form['Test_Name']
        Category = request.form['Category']
        Value = request.form['Value']
        Reference_Range = request.form['Reference_Range']
        Cost = request.form['Cost']
        Patient_SSN = request.form['Patient_SSN']
        Report_ID = request.form['Report_ID']
        Lab_No = request.form['Lab_No']

        LabtechSSN = session.get("USERSSN", None)
        try:
            sql = "INSERT INTO test(Test_ID,Test_Name,Category,Value,Reference_Range,Cost,Patient_SSN,Report_ID,Lab_No) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (Test_ID, Test_Name, Category, Value,
                   Reference_Range, Cost, Patient_SSN, Report_ID, Lab_No)
            mycursor.execute(sql, val)
            # TODO: ADD TO CONDUCTS RELATIONSHIP (testid and labtech id) using session cookies note:remember quotations in ssn

            sql = "INSERT INTO conducts(TestID,LabTechSSn) VALUES(%s, %s)"
            val = (Test_ID, LabtechSSN)
            mycursor.execute(sql, val)

            mydb.commit()
            # TODO: Fix redirecting in /home route so it can send message or error
            return render_template('Home_labtech.html', message="Test "+Test_ID + " has been successfully added to Report " + Report_ID)
        except:
            return render_template('Add_test.html', error="Invalid input!")

    else:
        return render_template('Add_test.html')


@app.route('/Add_test_admin', methods=['POST', 'GET'])
def Add_test_admin():
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
        try:
            sql = "INSERT INTO test(Test_ID,Test_Name,Category,Value,Start_Date,End_Date,Reference_Range,Cost,Patient_SSN,Report_ID,Lab_No) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (Test_ID, Test_Name, Category, Value, Start_Date, End_Date,
                   Reference_Range, Cost, Patient_SSN, Report_ID, Lab_No)
            mycursor.execute(sql, val)
            mydb.commit()
            # TODO: Fix redirecting in /home route so it can send message or error
            return render_template('/Home', message="Test "+Test_ID + " has been successfully added to Report " + Report_ID)
        except:
            return render_template('Add_test_admin.html', error="Invalid input!")

    else:
        return render_template('Add_test_admin.html')


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
            # TODO: Fix redirecting in /home route so it can send message or error
            return render_template('/Home', message="Lab " + labname + " has been successfully added to the labs table.")
        except:
            return render_template('Add_lab.html', error="Invalid input!")

    else:
        return render_template('Add_lab.html')


@app.route('/View_patient_labtech', methods=['POST', 'GET'])
def View_patient_labtech():
    # TODO: view their own patients only (indirect relation :( ))
    if request.method == 'GET':
        # Personal info
        mycursor.execute(
            "SELECT SSN, First_Name, Middle_Name, Last_Name, SEX, Birthdate, Insurance  FROM patient")
        personalinfo = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute(
            "select SSN,First_Name,Last_Name,Username,Password, patient.Email from patient join user where SSN=User_SSN")
        basicinfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute(
            "select SSN,First_Name,Last_Name,Address,PhoneNumber from patient join patientphonenumber where SSN=PatientSSN")
        contactinfo = mycursor.fetchall()

        data = {
            'message': "data retrieved",
            'personalinfo': personalinfo,
            'basicinfo': basicinfo,
            'contactinfo': contactinfo,

        }
        return render_template('View_patient_labtech.html', data=data)
    else:
        PatientSSN = request.form['PatientSSN']
        # Personal info
        mycursor.execute(
            "SELECT p.SSN, p.First_Name, p.Middle_Name, p.Last_Name, p.SEX, p.Birthdate, p.Insurance FROM patient As p where p.SSN=%s",
            (PatientSSN,))
        personalinfo = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute(
            "SELECT p.SSN, p.First_Name,p.Last_Name,Username,Password, user.Email FROM patient AS p JOIN user WHERE p.SSN = user.PatientSSN AND p.SSN=%s",
            (PatientSSN,))
        basicinfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute(
            "SELECT p.SSN, p.First_Name,p.Last_Name,p.Address,PhoneNumber FROM patient AS p JOIN patientphonenumber WHERE p.SSN =patientSSN AND p.SSN=%s",
            (PatientSSN,))
        contactinfo = mycursor.fetchall()
        # Medical History
        mycursor.execute(
            "SELECT p.SSN, p.First_Name,p.Last_Name, MedicalHistory FROM patient AS p JOIN patientmedicalhistory WHERE p.SSN =patientSSN AND p.SSN=%s", (PatientSSN,))
        Medicalinfo = mycursor.fetchall()

        data = {
            'message': "data retrieved",
            'personalinfo': personalinfo,
            'basicinfo': basicinfo,
            'contactinfo': contactinfo,
            'Medicalinfo': Medicalinfo,

        }
        return render_template('View_patient_labtech.html', data=data)


@app.route('/View_patient', methods=['POST', 'GET'])
def View_patient():
    if request.method == 'GET':
        # Personal info
        mycursor.execute(
            "SELECT SSN, First_Name, Middle_Name, Last_Name, SEX, Birthdate, Insurance  FROM patient")
        personalinfo = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute(
            "select SSN,First_Name,Last_Name,Username,patient.Email,Password from patient join user where SSN=User_SSN")
        basicinfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute(
            "select SSN,First_Name,Last_Name,Address,PhoneNumber from patient join patientphonenumber where SSN=PatientSSN")
        contactinfo = mycursor.fetchall()

        data = {
            'message': "data retrieved",
            'personalinfo': personalinfo,
            'basicinfo': basicinfo,
            'contactinfo': contactinfo,

        }
        return render_template('View_patient.html', data=data)
    else:
        PatientSSN = request.form['PatientSSN']
        # Personal info
        mycursor.execute(
            "SELECT p.SSN, p.First_Name, p.Middle_Name, p.Last_Name, p.SEX, p.Birthdate, p.Insurance FROM patient As p where p.SSN=%s",
            (PatientSSN,))
        personalinfo = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute(
            "SELECT p.SSN, p.First_Name,p.Last_Name,Username,Password, user.Email FROM patient AS p JOIN user WHERE p.SSN = user.PatientSSN AND p.SSN=%s",
            (PatientSSN,))
        basicinfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute(
            "SELECT p.SSN, p.First_Name,p.Last_Name,p.Address,PhoneNumber FROM patient AS p JOIN patientphonenumber WHERE p.SSN =patientSSN AND p.SSN=%s",
            (PatientSSN,))
        contactinfo = mycursor.fetchall()
        # Medical History
        mycursor.execute(
            "SELECT p.SSN, p.First_Name,p.Last_Name, MedicalHistory FROM patient AS p JOIN patientmedicalhistory WHERE p.SSN =patientSSN AND p.SSN=%s", (PatientSSN,))
        Medicalinfo = mycursor.fetchall()

        data = {
            'message': "data retrieved",
            'personalinfo': personalinfo,
            'basicinfo': basicinfo,
            'contactinfo': contactinfo,
            'Medicalinfo': Medicalinfo,

        }
        return render_template('View_patient.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
