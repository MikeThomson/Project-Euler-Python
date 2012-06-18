#!/usr/bin/python
import math
def sumOfSquares():
	total = 0
	i = 1
	while i <= 100:
		total += math.pow(i,2)
		i += 1
	return total

def squareOfSums():
	total = 0
	i=1
	while i <=100:
		total += i
		i += 1
	return math.pow(total,2)

print squareOfSums() - sumOfSquares()
