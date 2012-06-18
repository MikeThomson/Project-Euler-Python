from math import fabs
def isPrime(num):
	num = fabs(num)
	if num < 2:
		return False
	biggestTest = int(num/2)
	i = 3;
	if(num == 2) :
		return True
	if(num % 2 == 0) :
		return False
	while i < biggestTest :
		if num % i == 0 :
			return False
		i += 2

	return True

def getDivisors(num) :
	i = 1
	divisors = []
	while i < num :
		if num % i == 0 :
			divisors.append(i)
	return divisors

# Don'e want to make a sieve, this is borrowed
def erat_sieve(bound):
	if bound < 2:
		return []
	max_ndx = (bound - 1) / 2
	sieve = [True] * (max_ndx + 1)
	#loop up to square root
	for ndx in range(int(bound ** 0.5) / 2):
		# check for prime
		if sieve[ndx]:
			# unmark all odd multiples of the prime
			num = ndx * 2 + 3
			sieve[ndx+num:max_ndx:num] = [False] * ((max_ndx-ndx-num-1)//num + 1)
	# translate into numbers
	return [2] + [ndx * 2 + 3 for ndx in range(max_ndx) if sieve[ndx]]
