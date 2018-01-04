#!/usr/bin/python
import commands
n=int(raw_input("Enter the no of IP to show :"))

#taking out of ip of all system
result=(commands.getoutput('arp-scan -I wlp6s0 --localnet | grep -i 192.168')).splitlines()
l=len(result)

#define tuple
y=[]
for i in result:
	y.append(i.split('\t'))

#printing ip list
print("    IP's are :")
if n <= l:
	n = n
else:
	n = l
for i in range(0,n):
	print("\t\t"+y[i][0]) 
