#!/usr/bin/python
lastX = 1
x = 2
total = 0
while x < 4000000 :
	if x % 2 == 0:
		total += x
	tmp = x
	x = x+lastX
	lastX = tmp
print total
