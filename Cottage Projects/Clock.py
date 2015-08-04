### python /Users/supercgeek/Desktop/Start/Clock.py
import time
#import os
import datetime

now = datetime.datetime.now()



#YEARS
pre_years = ""
years = now.year

#DAYS
pre_days = ""
days = 215

#HOURS
pre_hours = ""
hours = now.hour

#MINS
pre_mins = ""
mins = now.minute

#SECS
pre_secs = ""
secs = now.second

#MILISECS
pre_milisecs = ""
milisecs = (now.microsecond/1000)

#LEGEND: Y:D:H:M:S:MS
#FORM:                       0000:          000:           00:            00:           00:          0000
#PRINT-STRING FORM: PRE-YEAR+YEARS+PRE-DAYS+DAYS+PRE-HOURS+HOURS+PRE-MINS+MINS+PRE-SECS+SECS+PREMILI+MILI
while secs < 60: 
	
	while milisecs != 1000:    
		milisecs = milisecs + 1
		#FORM PARSE LOGIC
		
		#PRE-YEARS LOGIC
		if years == 0:
			pre_years = "000"
		if years >= 1 and years <= 9:
			pre_years = "000"
		if years >= 10 and years <= 99:
			pre_years = "00"
		if years >= 100 and years <= 999:
			pre_years = "0"
		if years > 999:
			pre_years = ""
		
		#PRE-DAYS LOGIC
		if days == 0:
			pre_days = "00"
		if days >= 1 and days <= 9:
			pre_days = "00"
		if days >= 10 and days <= 99:
			pre_days = "0"
		if days > 99:
			pre_days = ""
		#PRE-HOURS LOGIC
		if hours == 0:
			pre_hours = "0"
		if hours >= 1 and days <= 9:
			pre_hours = "0"
		if hours > 9:
			pre_hours = ""
		#PRE-MINS LOGIC 
		if mins == 0:
			pre_mins = "0"
		if mins >= 1 and mins <= 9:
			pre_mins = "0"
		if mins > 9:
			pre_mins = ""
		#PRE-SECS LOGIC
		if secs == 0:
			pre_secs = "0"
		if secs >= 1 and secs <= 9:
			pre_secs = "0"
		if secs > 9:
			pre_secs = ""
		#PRE-MILI LOGIC
		if milisecs == 0:
			pre_milisecs = "000"
		if milisecs >= 1 and milisecs <= 9:
			pre_milisecs = "000"
		if milisecs >=10 and milisecs <= 99:
			pre_milisecs = "00"
		if milisecs >= 100 and milisecs <= 999:
			pre_milisecs = "0"
		if milisecs > 999:
			pre_milisecs = ""
		
#		os.system('clear')
		print ""
		print "YEARS : DAYS : HOURS : MINUTES : SECONDS : MILISECONDS"
			
		print str(pre_years) + str(years) +str(" : ") + str(pre_days) + str(days) + str(" : ") + str(pre_hours) + str(hours) + str(" : ") + str(pre_mins) + str(mins) + str(" : ") + str(pre_secs) + str(secs) +str(" : ") + str(pre_milisecs) + str(milisecs)
			
		time.sleep(0.0004)
	
	milisecs = 0
	secs = secs + 1

	if secs == 60:
		secs = 0
		mins = mins + 1
	
	if mins == 60:
		mins = 0
		hours = hours + 1
		
	if hours == 24:
		hours = 0
		days = days + 1 
		
	if days == 365:
		days = 0
		years = years + 1