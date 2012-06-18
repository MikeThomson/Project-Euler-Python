#!/usr/bin/python
import MyMath

i=3
total = 0
primes = MyMath.erat_sieve(2000000);
for x in primes :
	total += x
print total
