import mysql.connector

mydb = mysql.connector.connect(
    host="lab-hcis.mysql.database.azure.com",
    user="lab_admin@lab-hcis",
    passwd="tamerbasha.2024"
)

print(mydb)
