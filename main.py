#main.py
import mysql.connector
from flask import Flask, render_template, request
app = Flask(__name__)

mydb = mysql.connector.connect(
  host="hospital-lab.mysql.database.azure.com",
  user="lab_admin",
  passwd="tamerbasha.2024", #write ur own password
  database="Laboratory_Department" #here 
)
mycursor = mydb.cursor()

@app.route('/')
def hello_name():

   return render_template('index.html')


@app.route('/View_report_patient', methods=['POST','GET'])
def View_report_patient():
   if request.method =='GET':
      mycursor.execute("SELECT  Publish_Date, ReportID, Name FROM report JOIN patient WHERE Patient_SSN = SSN")
      reportinfo = mycursor.fetchall()
      data = {
            'message': "data retrieved",
            'reportinfo': reportinfo
         }
      return render_template('View_report_patient.html', data=data)
   else:
      return render_template('View_report_post_OK.html')


@app.route('/signup', methods=['POST','GET'])
def signup():
   return render_template('signup.html')

@app.route('/View_report_labtech', methods=['POST','GET'])
def View_report_labtech():
   if request.method=='POST':
      PatientNumber=request.form['PatientNumber']
      ReportID=request.form['ReportID']
      mycursor.execute("SELECT Test_Name, Value, Reference_Range FROM report AS R JOIN patient JOIN test WHERE R.Patient_SSN = SSN AND ReportID = Report_ID AND Patient_Number=%s AND ReportID=%s", (PatientNumber, ReportID))
      reportinfo = mycursor.fetchall()
      data = {
            'message': "data retrieved",
            'reportinfo': reportinfo
        }
      mycursor.execute("SELECT Name FROM report JOIN patient WHERE Patient_SSN = SSN AND Patient_Number=%s AND ReportID=%s", (PatientNumber, ReportID))
      x = mycursor.fetchone()
      ReportName = x[0]
      mycursor.execute("SELECT Publish_Date FROM report JOIN patient WHERE Patient_SSN = SSN AND Patient_Number=%s AND ReportID=%s", (PatientNumber, ReportID))
      x = mycursor.fetchone()
      PublishDate = x[0]
      mycursor.execute("SELECT Referred_By FROM report JOIN patient WHERE Patient_SSN = SSN AND Patient_Number=%s AND ReportID=%s", (PatientNumber, ReportID))
      x = mycursor.fetchone()
      Referred = x[0]
      mycursor.execute("SELECT Comments FROM report JOIN patient WHERE Patient_SSN = SSN AND Patient_Number=%s AND ReportID=%s", (PatientNumber, ReportID))
      x = mycursor.fetchone()
      Comments = x[0]
      return render_template('View_report_post_OK.html', data=data, ReportName=ReportName, PublishDate=PublishDate, Referred=Referred, Comments=Comments ) #ReportName=ReportName #data=data
   else:
      return render_template('View_report_labtech.html')

@app.route('/View_report_post_OK', methods=['POST','GET'])
def View_report_post_OK():
   return render_template('View_report_post_OK.html')

@app.route('/Add_new_equipment', methods=['POST','GET'])
def Add_new_equipment():
   return render_template('Add_new_equipment.html')

@app.route('/Edit_equipment', methods=['POST','GET'])
def Edit_equipment():
   return render_template('Edit_equipment.html')

@app.route('/Add_employee', methods=['POST','GET'])
def Add_employee():
    if request.method=='POST':
        FirstName=request.form['FirstName']
        MiddleName=request.form['MiddleName']
        LastName=request.form['LastName']
        Birthdate=request.form['Birthdate']
        SSN=request.form['SSN']
        Salary=request.form['Salary']
        Address=request.form['Address']
        if request.form['SupervisorSSN'] ==(''):
         SupervisorSSN= None
        else:
         SupervisorSSN = request.form['SupervisorSSN']
        EmailAddress=request.form['EmailAddress']
        Gender=request.form['Gender']
        ID=request.form['ID']
        PhoneNumber=request.form['PhoneNumber']
        Qualifications=request.form['Qualifications']
        Username=request.form['Username']
        Password=request.form['Password']
        PermissionLevel=request.form['PermissionLevel']
        try:
         sql= "INSERT INTO employee(First_Name, Middle_Name, Last_Name, Birthdate, SSN, Salary, Address, Email, Supervisor_SSN, ID, SEX) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
         val = (FirstName, MiddleName, LastName, Birthdate, SSN, Salary, Address, EmailAddress, SupervisorSSN, ID, Gender)
         mycursor.execute(sql, val)

         sql= "INSERT INTO employeephonenumber(PhoneNumber, EmployeeSSN) VALUES(%s, %s)"
         val= (PhoneNumber, SSN)
         mycursor.execute(sql, val)

         sql= "INSERT INTO employeequalifications(CV, EmployeeSSN) VALUES(%s, %s)"
         val= (Qualifications, SSN)
         mycursor.execute(sql, val)

         sql = "INSERT INTO User(User_SSN, Username, Password, Permission_Level, Email, EmpSSN) VALUES (%s,%s,%s,%s,%s,%s)"
         val = (SSN, Username, Password, PermissionLevel, EmailAddress, SSN)
         mycursor.execute(sql, val)


         mydb.commit()
         return render_template('index.html', message= FirstName + ' ' + LastName + " has been successfully added to the database") 
        except:   
            return render_template('Add_employee.html', error= "Invalid input!") 

    else: 
         return render_template('Add_employee.html')

@app.route('/Add_empdependents', methods=['POST','GET'])
def Add_empdependents():
   if request.method=='POST':
      FirstName=request.form['FirstName']
      MiddleName=request.form['MiddleName']
      LastName=request.form['LastName']
      Birthdate=request.form['Birthdate']
      SSN=request.form['SSN']
      Gender=request.form['Gender']
      Address=request.form['Address']
      Relationship=request.form['Relationship']
      EmployeeSSN=request.form['EmployeeSSN']

      try:
         sql = "INSERT INTO dependents_employee(Dependent_SSN, First_Name, Middle_Name, Last_Name, Birthdate, SEX, Address, Relationship, ESSN ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
         val = (SSN, FirstName, MiddleName, LastName, Birthdate, Gender, Relationship, Address, EmployeeSSN)
         mycursor.execute(sql, val)
         mydb.commit()
         return render_template('index.html', message= FirstName + ' ' + LastName + " has been successfully added to the database") 
      except:
         return render_template('Add_empdependents', error= "Invalid input!")

   else: 
       return render_template('Add_empdependents.html')


@app.route('/View_employee', methods=['POST','GET'])
def View_employee():
   if request.method == 'GET':
      # Personal info
        mycursor.execute("SELECT ID, SSN, First_Name, Middle_Name, Last_Name, SEX, Birthdate, Salary, Supervisor_SSN FROM employee")
        personalinfo = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute("SELECT SSN, First_Name,Last_Name,Username,Password, user.Email FROM employee JOIN user WHERE SSN = EmpSSN ")
        basicinfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute("SELECT SSN, First_Name,Last_Name,Address,PhoneNumber FROM employee JOIN employeephonenumber WHERE SSN = EmployeeSSN  ")
        contactinfo = mycursor.fetchall()
        # Supervisor Table
        mycursor.execute("SELECT S.ID,S.SSN,S.First_Name,S.Middle_Name,S.Last_Name,S.SEX, S.Birthdate,S.Salary FROM employee AS E JOIN employee AS S WHERE E.Supervisor_SSN = S.SSN ")
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
      EmployeeSSN=request.form['EmployeeSSN']
      # Personal info
      mycursor.execute("SELECT E.ID, E.SSN, E.First_Name, E.Middle_Name, E.Last_Name, E.SEX, E.Birthdate, E.Salary, E.Supervisor_SSN FROM employee AS E WHERE E.SSN=%s",(EmployeeSSN,))
      personalinfo = mycursor.fetchall()
      # Basic Info Button
      mycursor.execute("SELECT E.SSN, E.First_Name,E.Last_Name,Username,Password, user.Email FROM employee AS E JOIN user WHERE E.SSN = user.EmpSSN AND E.SSN=%s",(EmployeeSSN,))
      basicinfo = mycursor.fetchall()
      # Contact Info Button
      mycursor.execute("SELECT E.SSN, E.First_Name,E.Last_Name,E.Address,PhoneNumber FROM employee AS E JOIN employeephonenumber WHERE E.SSN = EmployeeSSN AND E.SSN=%s",(EmployeeSSN,))
      contactinfo = mycursor.fetchall()
      # Supervisor Table
      mycursor.execute("SELECT S.ID,S.SSN,S.First_Name,S.Middle_Name,S.Last_Name,S.SEX, S.Birthdate,S.Salary FROM employee AS E JOIN employee AS S WHERE E.Supervisor_SSN = S.SSN AND E.SSN=%s",(EmployeeSSN,))
      superinfo = mycursor.fetchall()
      # Dependents Table
      mycursor.execute("SELECT Dependent_SSN, D.First_Name, D.Middle_Name, D.Last_Name, D.SEX, D.Birthdate, D.Address, Relationship FROM employee AS E JOIN dependents_employee AS D WHERE E.SSN = D.ESSN AND D.ESSN=%s",(EmployeeSSN,))
      depinfo = mycursor.fetchall()
      # Supervised Table
      mycursor.execute("SELECT S.ID, S.SSN, S.First_Name, S.Middle_Name, S.Last_Name, S.SEX, S.Birthdate, S.Salary FROM employee AS E JOIN employee AS S ON E.Supervisor_SSN = S.SSN AND E.SSN=%s",(EmployeeSSN,))
      supervisedinfo = mycursor.fetchall()
      # Supervises Table
      mycursor.execute("SELECT S.ID, E.SSN, E.First_Name, E.Middle_Name, E.Last_Name, E.SEX, E.Birthdate, E.Salary FROM employee AS E JOIN employee AS S ON E.Supervisor_SSN = S.SSN AND S.SSN=%s",(EmployeeSSN,))
      supervisesinfo = mycursor.fetchall()

      data={
         'message': "data retrieved",
         'personalinfo': personalinfo,
         'basicinfo': basicinfo,
         'contactinfo': contactinfo,
         'superinfo': superinfo,
         'depinfo': depinfo,
         'supervisedinfo':supervisedinfo,
         'supervisesinfo':supervisesinfo
      }
      return render_template('View_employee.html', data=data)
      

@app.route('/Add_lab_tech', methods=['POST','GET'])
def Add_lab_tech():
   
   return render_template('Add_lab_tech.html')

@app.route('/Login', methods=['POST','GET'])
def Login():
   return render_template('Login.html')

@app.route('/Forgot_login', methods=['POST','GET'])
def Forgot_login():
   return render_template('Forgot_login.html')

@app.route('/Add_consumables', methods=['POST','GET'])
def Add_consumables():
   return render_template('Add_consumables.html')

@app.route('/test', methods=['POST','GET'])
def test():
   return render_template('test.html')

@app.route('/Lab_guide', methods=['POST','GET'])
def Lab_guide():
   return render_template('Lab_guide.html')

@app.route('/hr_navbar', methods=['POST','GET'])
def hr_navbar():
   return render_template('hr_navbar.html')

@app.route('/admin_navbar', methods=['POST','GET'])
def admin_navbar():
   return render_template('admin_navbar.html')

@app.route('/frontdesk_navbar', methods=['POST','GET'])
def frontdesk_navbar():
   return render_template('frontdesk_navbar.html')

@app.route('/labtech_navbar', methods=['POST','GET'])
def labtech_navbar():
   return render_template('labtech_navbar.html')

@app.route('/patient_navbar', methods=['POST','GET'])
def patient_navbar():
   return render_template('patient_navbar.html')

@app.route('/temp_navbar', methods=['POST','GET'])
def temp_navbar():
   return render_template('temp_navbar.html')

@app.route('/testing', methods=['POST','GET'])
def testing():
   return render_template('testing.html')

@app.route('/llogin', methods=['POST','GET'])
def llogin():
   return render_template('llogin.html')
@app.route('/View_lab_tech', methods=['POST','GET'])
def View_lab_tech():
   if request.method == 'GET':
      # Personal info
        mycursor.execute("SELECT SSN, First_Name, Middle_Name, Last_Name, SEX, Birthdate, Salary, Manager_SSN FROM lab_technician")
        PersonalInfo = mycursor.fetchall()
        # Basic Info Button
        mycursor.execute("SELECT SSN, First_Name,Last_Name,Username,Password, user.Email FROM lab_technician JOIN user WHERE SSN = LabTechSSN ")
        BasicInfo = mycursor.fetchall()
        # Contact Info Button
        mycursor.execute("SELECT SSN, First_Name,Last_Name,Address,PhoneNumber FROM lab_technician JOIN LabTechPhoneNumber WHERE SSN = LabTechSSN  ")
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
      LabtechSSN=request.form['LabtechSSN']
      # Personal info
      mycursor.execute("SELECT SSN, First_Name, Middle_Name, Last_Name, SEX, Birthdate, Salary, Manager_SSN FROM lab_technician WHERE SSN=%s",(LabtechSSN,))
      PersonalInfo = mycursor.fetchall()
      # Basic Info Button
      mycursor.execute("SELECT SSN, First_Name,Last_Name,Username,Password, user.Email FROM lab_technician JOIN user WHERE SSN = LabTechSSN  AND SSN=%s",(LabtechSSN,))
      BasicInfo = mycursor.fetchall()
      # Contact Info Button
      mycursor.execute("SELECT SSN, First_Name,Last_Name,Address,PhoneNumber FROM lab_technician JOIN LabTechPhoneNumber WHERE SSN = LabTechSSN AND SSN=%s",(LabtechSSN,))
      ContactInfo = mycursor.fetchall()
      # Manager Table
      mycursor.execute("SELECT E.ID,E.SSN,E.First_Name,E.Middle_Name,E.Last_Name,E.SEX, E.Birthdate,E.Salary FROM lab_technician AS L JOIN employee AS E WHERE  L.Manager_SSN= E.SSN AND L.SSN=%s",(LabtechSSN,))
      Manager = mycursor.fetchall()
      # Dependents Table
      mycursor.execute("SELECT SSN, Dependent_SSN, D.First_Name, D.Middle_Name, D.Last_Name, D.SEX, D.Birthdate, D.Address, Relationship FROM lab_technician JOIN Dependents_LabTech AS D WHERE SSN = D.Lab_Tech_SSN AND D.Lab_Tech_SSN=%s",(LabtechSSN,))
      Dependents = mycursor.fetchall()

      data={
         'message': "data retrieved",
         'PersonalInfo': PersonalInfo,
         'BasicInfo': BasicInfo,
         'ContactInfo': ContactInfo,
         'Manager': Manager,
         'Dependents': Dependents,
      }
      return render_template('View_lab_tech.html', data=data)





if __name__ == '__main__':
   app.run(debug = True)
