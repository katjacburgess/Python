#DATE: OCT 12TH, 2015
#AUTHOR: KATHLEEN BURGESS
#Grade 10, Assignment 3, question 5
#DESRIPTION:
number1 = 101
while number1 != 0:
	number1 = int(raw_input("Please enter a number. Enter 0 to end: "))
	number2 = int(raw_input("Please enter a second number: "))
	number3 = int(raw_input("Please enter a third number: "))
	print number1,",", number2, ",", number3
	sum = number1 + number2 + number3
	print sum
	average = (number1 + number2 + number3)/3
	print average