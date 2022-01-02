from flask import Flask, render_template
app = Flask(__name__)

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

@app.route('/Add_employee')
def Add_employee():
   return render_template('Add_employee.html')

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
   

if __name__ == '__main__':
   app.run()
