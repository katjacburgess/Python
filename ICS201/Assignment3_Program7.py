#DATE: OCT 11TH, 2015
#AUTHOR: KATHLEEN BURGESS
#Grade 10, Assignment 3, question 7
#DESRIPTION: calculates the amount of money(donation), Mr. Ford would have donated after the x amount of days entered by the user

days = float(raw_input("After how many days of donation? "))
if days >1:
	firstday = 0.01
	subday = 0
	value = float(firstday)
	subday = value*(2**days)-value
	donation = subday
	print "After", days, "day(s) of donation, Mr. Ford will have donated",donation, "to his favourite charity."
	print
elif days == 1:
	donation = 0.1
	print 
	print "After", days, "day(s) of donation, Mr. Ford will have donated",donation, "to his favourite charity."
	
#not pritning right number
#can you make the code run until it reaches certain amount of days entered
	