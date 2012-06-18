#!/usr/bin/python

def isPrime(num) :
	i = 2
	while i<num:
		if num % i == 0:
			return False
		i += 1
	return True

primeCount = 0
i = 2
lastPrime = 0
while primeCount != 10001:
	if(isPrime(i)):
		lastPrime = i
		primeCount += 1
		print "Found prime " + str(i) + " which is number "+str(primeCount)+"\n"
	i += 1

print lastPrime
