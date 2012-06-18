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
