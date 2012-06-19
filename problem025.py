#!/usr/bin/python

a = 1
b = 1
count = 2 # a is the 2nd term
while len(str(a)) < 1000 :
	a,b = a+b, a
	count += 1
print count
