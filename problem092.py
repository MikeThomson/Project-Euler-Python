#!/usr/bin/python
from collections import defaultdict

def chainEndsIn89(num, hits) :
	if(num in hits) :
		return hits[num]
	if(num == 89) :
		hits[num] = True
		return True
	if(num == 1) :
		hits[num] = False
		return False
	else :
		strNum = str(num)
		total = 0
		digits = list(strNum)
		for i in digits :
			total += int(i) * int(i)
		return chainEndsIn89(total, hits)

count = 0
hits = defaultdict(bool)
for i in range(1,10000000) :
	if chainEndsIn89(i,hits) :
		hits[i] = True
		count += 1
print count
