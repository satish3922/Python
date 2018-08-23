#!/usr/bin/env python2
import cgitb,cgi,os,commands,mysql.connector

# Getting FieldValue From HTML Page
cgitb.enable()
data = cgi.FieldStorage()  # Create object of cgitb
username = data.getvalue('username')
password = data.getvalue('password')

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
def valid_password(password):
    name = "select Password from register where Password='{}';".format(password)
    cursor.execute(name)
    cursor.fetchall()
    name = cursor.rowcount
    return name

p = valid_password(password)
u = valid_username(username)
if(p == 0 and u == 0):
    print "<script>"
    print "alert('Incorrect Password & Username')"
    print "</script>"
    print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/index.html'>".format(ip)
elif(p == 1 and u == 0):
    print "<script>"
    print "alert('Incorrect Password')"
    print "</script>"
    print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/index.html'>".format(ip)
elif(p == 0 and u == 1):
    print "<script>"
    print "alert('Incorrect Username')"
    print "</script>"
    print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/index.html'>".format(ip)
else:
    commands.getoutput('echo {}:{} >> cookies'.format(username,password))
    print "<script>"
    print "alert('Welcome to Infinity')"
    print "</script>"
    print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/cloud.html'>".format(ip)
