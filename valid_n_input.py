#!/usr/bin/python

import commands
y=[]
while(x!='e'):
	x=raw_input("Enter the input {} :")
	y.append(x)
	
#for i in range(1,6):
#	x=raw_input("Enter the input {} :".format(str(i)))
#	y.append(x)
#for i in y:
#	z=commands.getoutput('ls /usr/bin/ | grep -w {}'.format(i))
#	if z == i:
#		print(commands.getoutput('{}'.format(i)))
#	else:
#		print('{}'.format(i))

for i in y:
	print (y[i])
