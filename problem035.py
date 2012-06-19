#!/usr/bin/python
from MyMath import *

def isCircularPrime(num, primes) :
	strNum = str(num)
	l = len(strNum)
	for i in range(0,l) :
		strNum = strNum[-1:] + strNum[:-1]
		if not int(strNum) in primes :
			return False
	return True

primes = erat_sieve(1000000)

count = 0
for prime in primes :
	if isCircularPrime(prime, primes) :
		count += 1

print count
