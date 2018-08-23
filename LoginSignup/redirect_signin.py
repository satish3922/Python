#!/usr/bin/env python2
import cgitb,cgi,commands
cgitb.enable()

print "Content-type:text/html"
print ""

# Fetching System IP
ip = tuple(commands.getoutput('hostname -I').split(' ')[:-1])[0]
print "<meta HTTP-EQUIV='refresh' content='0;url=http://{}/index.html'>".format(ip)
