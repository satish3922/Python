#!/usr/bin/python

''' take 5 input from user and check whether is command or not if yes then execute the command else simply print the vlaue '''

import commands
y=[]
for i in range(1,6):
	x=raw_input("Enter the input {} :".format(str(i)))
	y.append(x)
for i in y:
	z=commands.getoutput('ls /usr/bin/ | grep -w {}'.format(i))
	if z == i:
		print(commands.getoutput('{}'.format(i)))
	else:
		print('{}'.format(i))
