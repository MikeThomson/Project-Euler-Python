#!/usr/bin/python
def checkDivisible(num) :
	for i in range(1,21) :
		if(num % i != 0) :
			return False
	return True

i = 20
while(not checkDivisible(i)) :
	i += 1

print i
