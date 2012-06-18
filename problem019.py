#!/usr/bin/python
import datetime

myDate = datetime.date(1901, 1, 1)
finalDate = datetime.date(2001,1,1)

count = 0
while myDate < finalDate :
	if(myDate.weekday() == 6 and myDate.day == 1) :
		count += 1
	myDate = myDate + datetime.timedelta(days=1)
print count
