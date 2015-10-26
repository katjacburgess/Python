#DATE: OCT 12TH, 2015
#AUTHOR: KATHLEEN BURGESS
#ASSIGNMENT: 3, question 5/b
#DESRIPTION: aks for 3 numbers, and prints the numbers, the sum and the average
number1 = -1 #cannot be 0 because that is used to end the loop
while number1 != 0:
	number1 = int(raw_input("Please enter a number. Enter 0 to end: "))
	if number1 != 0: #use if sts, so once 0 is entred the program will stop immediately 
		number2 = int(raw_input("Please enter a second number: "))
		number3 = int(raw_input("Please enter a third number: "))
		print number1,",", number2, ",", number3
		sum = number1 + number2 + number3
		print sum
		average = (number1 + number2 + number3)/3
		print average