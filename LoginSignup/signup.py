#!/usr/bin/env python2
import cgitb,cgi,os,commands,mysql.connector

# Getting FieldValue From HTML Page
cgitb.enable()
data = cgi.FieldStorage()  # Create object of cgitb
username = data.getvalue('username')
email = data.getvalue('email')
password = data.getvalue('password')
mobile = data.getvalue('mobile')

print "Content-type:text/html"
print ""

# Fetching System IP
ip = tuple(commands.getoutput('hostname -I').split(' ')[:-1])[0]

# Connecting to DataBase Mysql
connection = mysql.connector.connect(user='root', password='redhat', database='cloud')
cursor = connection.cursor() # Creating Cursor to Read DataBase Table

# Checking valid_email Details
def valid_username(username):
    name = "select Username from register where Username='{}';".format(username)
    cursor.execute(name)
    cursor.fetchall()
    name = cursor.rowcount
    return name
# Checking valid_Signup Details
def valid_email(email):
    name = "select Email from register where Email='{}';".format(email)
    cursor.execute(name)
    cursor.fetchall()
    name = cursor.rowcount
    return name

e = valid_email(email)
u = valid_username(username)

if(e == 1 and u == 1):
    print "<script>"
    print "alert('Email and Username Already Exists')"
    print "</script>"
    print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/signup.html'>".format(ip)
elif(e == 1 and u == 0):
    print "<script>"
    print "alert('Email Already Exists')"
    print "</script>"
    print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/signup.html'>".format(ip)
elif(e == 0 and u == 1):
    print "<script>"
    print "alert('Try Different Username')"
    print "</script>"
    print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/signup.html'>".format(ip)
else:
    data = "insert into register SET Email='{}',Password='{}',Mobile='{}',Username='{}'".format(email,password,mobile,username)
    cursor.execute(data)
    connection.commit()
    print "<script>"
    print "alert('Successfully Registered')"
    print "</script>"
    print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/index.html'>".format(ip)
