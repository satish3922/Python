#!/usr/bin/python
 
''' write a program to print all the ip of working system in your network (locally) with fixed no of ip'''

import commands
n=int(raw_input("Enter the no of IP to show :"))

# Taking out of ip of all system
# ------------------------------
result=(commands.getoutput('arp-scan -I wlp6s0 --localnet | grep -i 192.168 > /root/ip.txt; cat /root/ip.txt')).split('\t')

k=commands.getoutput('wc -l /root/ip.txt')
k=((k[0]).split(' ')[0])
l=int(k)

# checking condition for no of ip requseted or we have
# ----------------------------------------------------
if n <= l:
	n=n*2+1
else:
	n=l*2+1

# define tuple
# ------------
y=[]
z=[]
y.append(result[0])
for i in range(2,n,2):
	a=result[i]
	z=a.split('\n')
	y.append(z[-1])

# printing ip list
# ----------------
print("    IP's are :")
for i in y:
	print("\t\t"+i) 
