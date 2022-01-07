# main.py
import mysql.connector
from flask import Flask, render_template, request
app = Flask(__name__)

mydb = mysql.connector.connect(
    host="hospital-lab.mysql.database.azure.com",
    user="lab_admin",
    passwd="tamerbasha.2024",  # write ur own password
    database="Laboratory_Department"  # here
)
mycursor = mydb.cursor()
mycursor1 = mydb.cursor()


@app.route('/')
def hello_name():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/Add_new_equipment')
def Add_new_equipment():
    return render_template('Add_new_equipment.html')


@app.route('/Edit_equipment')
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
            val = (FirstName, MiddleName, LastName, Birthdate, SSN, Salary,
                   Address, EmailAddress, SupervisorSSN, ID, Gender)
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

    else:
        return render_template('Add_employee.html')


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
        data = {
            'message': "data retrieved",
            'personalinfo': personalinfo,
            'basicinfo': basicinfo,
            'contactinfo': contactinfo,
            'superinfo': superinfo
        }
        return render_template('View_employee.html', data=data)


@app.route('/Add_lab_tech')
def Add_lab_tech():

    return render_template('Add_lab_tech.html')


@app.route('/Login')
def Login():
    return render_template('Login.html')


@app.route('/Forgot_login')
def Forgot_login():
    return render_template('Forgot_login.html')


@app.route('/Add_consumables')
def Add_consumables():
    return render_template('Add_consumables.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/Lab_guide')
def Lab_guide():
    return render_template('Lab_guide.html')


@app.route('/hr_navbar')
def hr_navbar():
    return render_template('hr_navbar.html')


@app.route('/admin_navbar')
def admin_navbar():
    return render_template('admin_navbar.html')


@app.route('/frontdesk_navbar')
def frontdesk_navbar():
    return render_template('frontdesk_navbar.html')


@app.route('/labtech_navbar')
def labtech_navbar():
    return render_template('labtech_navbar.html')


@app.route('/patient_navbar')
def patient_navbar():
    return render_template('patient_navbar.html')


@app.route('/temp_navbar')
def temp_navbar():
    return render_template('temp_navbar.html')


@app.route('/testing')
def testing():
    return render_template('testing.html')


@app.route('/llogin')
def llogin():
    return render_template('llogin.html')


if __name__ == '__main__':
    app.run(debug=True)
