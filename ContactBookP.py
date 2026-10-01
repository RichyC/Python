#Introduction
print('Welcome to your personal contact book.\nSelect an operation')

#Get Input
operation = input()

#Provides 3 operations
#   1.list - lists contacts
#   2. add - adds new contacts
#   3. delete - deletes contacts
if operation == 'list':
    sql = "SELECT * FROM ContactBook"
elif operation == 'add':
    firstName = input('Enter First Name: ')
    lastName = input('Enter Last Name: ')
    phoneNumber = input('Enter Phone Number: ')
    email = input('Enter Email: ')
    address = input('Enter Address: ')
    city = input('Enter City: ')
    state = input('Enter State: ')
    zipCode = input('Enter Zip: ')
    sql = f"INSERT INTO ContactBook (FirstName, LastName, PhoneNumber, Email, Address, City, StateOrProvince, Zip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (firstName, lastName, phoneNumber, email, address, city, state, zipCode)
elif operation == 'delete':
     name = input('Enter First Name and Last Name: ')
     name = name.split(" ")
     sql = "DELETE FROM ContactBook WHERE FirstName = %s AND LastName = %s"
     values = (name[0], name[1])

#Connects to mysql database
import mysql.connector
conn = mysql.connector.connect(host=host,user=user, password=password, database=database)
cur = conn.cursor()

try:
    values 
except NameError:
    cur.execute(sql)
    rowcount = cur.rowcount
    if operation == 'list':
        if rowcount == 0:
            print('Your contacts are empty')
        else:
            rows = cur.fetchall()
else:
    cur.execute(sql,values)
    conn.commit()
    if operation == 'add':
        print('Successfully added contact')
    elif operation == 'delete':
        print('Successfully deleted contact')
