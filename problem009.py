#!/usr/bin/python
def isTriplet(a,b,c):
	return (a*a + b*b == c*c)

done = False
for a  in range(1,999) :
	for b in range(a, 999) :
		c = 1000 - a - b
		if isTriplet(a,b,c) :
			done = True
			break
	if done :
		break
print a*b*c
