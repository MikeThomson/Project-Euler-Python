#!/usr/bin/python

from collections import defaultdict

def evenFunc(n) :
	return n/2

def oddFunc(n) : 
	return 3*n + 1

def chainLength(n, count, hits) :
	if(n in hits) :
		return count + hits[n]
	if(n == 1) :
		return count + 1
	if(n%2 == 0) :
		return chainLength(evenFunc(n), count +1, hits)
	else :
		return chainLength(oddFunc(n), count +1, hits)

maxChain = 0
maxNum = 0
hits = defaultdict(int)
for i in range(1,1000000) :
	l = chainLength(i,0, hits)
	hits[i] = l
	if(l > maxChain) :
		maxChain = l
		maxNum = i
print maxNum
