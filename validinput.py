#!/usr/bin/python

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
