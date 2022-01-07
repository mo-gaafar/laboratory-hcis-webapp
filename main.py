import mysql.connector
from flask import Flask, redirect, url_for, request,render_template

from datetime import datetime
now = datetime.now()
formatted_date = now.strftime('%Y-%d-%m %H:%M:%S')

mydb = mysql.connector.connect(
   host="hospital-lab.mysql.database.azure.com",
   username="lab_admin",
   password="tamerbasha.2024",
   database="Laboratory_Department"
)
mycursor = mydb.cursor()
app = Flask(__name__)

@app.route('/')
def hello_name():
   return render_template('Add_labtech_dependents.html')

@app.route('/Add_lab_tech',methods = ['POST', 'GET'])
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
         val = (SSN,FirstName,MiddleName,LastName,Sex,formatted_date,Salary,EmailAddress,Address,ManagerSSN)
         mycursor.execute(sql, val)
         sql = "INSERT INTO LabTechPhoneNumber (LabTechSSN, PhoneNumber) VALUES (%s,%s)"
         val= (SSN,PhoneNumber)
         mycursor.execute(sql, val)
         sql = "INSERT INTO LabTechQualifications (LabTechSSN, Qualifications) VALUES (%s,%s)"
         val = (SSN,CV)
         mycursor.execute(sql, val)
         sql = "INSERT INTO User(User_SSN,Username,Password,Permission_Level,Email,LabTechSSN) VALUES (%s,%s,%s,%s,%s,%s)"
         val = (SSN,Username,Password,"labtechnician",EmailAddress,SSN)
         mycursor.execute(sql, val)
         mydb.commit()
         return render_template('Add_lab_tech.html',message=FirstName + ' ' + LastName+ " has been succesfuly added to lab technicians.")
      except:
         return render_template('Add_lab_tech.html', error="Invalid input!")
   else:
      return render_template('Add_lab_tech.html')

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
            return render_template('admin_home.html', message=FirstName + ' ' + LastName + " has been successfully added to the database")
        except:
            return render_template('Add_employee.html', error="Invalid input!")

    else:
        return render_template('Add_employee.html')

@app.route('/Login',methods = ['POST', 'GET'])
def Login():
   if request.method == 'POST':
      Email = request.form['Email']
      Password = request.form['Password']
      mycursor.execute("SELECT Permission_Level FROM User WHERE Email=%s AND Password=%s", (Email, Password))
      permission = mycursor.fetchone()
      if permission:
          mycursor.execute("SELECT Username FROM User WHERE Email=%s AND Password=%s", (Email, Password))
          x = mycursor.fetchone()
          username = x[0]
          if permission==('admin',):
           return render_template('admin_home.html', message="Welcome "+ username, username=username)
          if permission == ('employee',):
             return render_template('employee_home.html', message="Welcome "+ username, username=username)
          if permission == ('labtechnician',):
             return render_template('labtech_home.html', message="Welcome "+ username, username=username)
          if permission == ('patient',):
             return render_template('patient_home.html', message="Welcome "+ username, username=username)
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
           val = (SSN, FirstName, MiddleName, LastName, Birthdate,Gender, Address, Relationship, LabtechSSN)
           mycursor.execute(sql, val)
           mydb.commit()
           return render_template('admin_home.html',message=FirstName + ' ' + LastName + " has been successfully added to the database")
       except:
           return render_template('Add_labtech_dependents.html', error="Invalid input!")

   else:
       return render_template('Add_labtech_dependents.html')

if __name__ == '__main__':
   app.run(debug=True)
