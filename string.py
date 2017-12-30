#!/usr/bin/env python
text1=str(raw_input("Enter the first string : "))
text2=str(raw_input("Enter the second string : "))
t=[]
s=[]
print("matched string are :")
for i in text1:
    for j in text2:
        if (i==j):
	    if i in t:
		break
            elif (i==' '):
		break
	    else:
		t.append(i)
	    break
#	else:
#	    if i in s:
#	    	s.append(i)
print (t)
#print ("not matched string are: ")
#print (s)
