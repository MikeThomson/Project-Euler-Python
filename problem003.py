#!/usr/bin/python
def firstFactor(num):
	i = 2
	while i < num :
		if(num % i == 0) :
			return i
		i += 1
	return num

factors = []
num = 600851475143
while num != 1 :
	factor = firstFactor(num)
	factors.append(factor)
	num /= factor

maxFactor = 1
for fac in factors :
	if(fac > maxFactor) :
		maxFactor = fac

print maxFactor
