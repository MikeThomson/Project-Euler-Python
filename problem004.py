#!/usr/bin/python
def isPalindrome(word) :
	wordString = str(word)
	if wordString == wordString[::-1] :
		return True
	return False
currentMax = 0
for i in range(100, 1000) :
	for j in range(100, 1000) :
		if isPalindrome(i*j) and i*j > currentMax :
			currentMax = i*j

print currentMax
