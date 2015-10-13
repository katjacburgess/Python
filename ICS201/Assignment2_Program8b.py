#DATE: OCT 11TH, 2015
#AUTHOR: KATHLEEN
#Grade 10, Assignment 2, question 8, part b
#DESRIPTION: this program is a Guessing game between the computer and user. 

import random #add import to define random
number = random.randint(1, 100) #randomely generates number between 1 and 100
player = int(raw_input("Guess a number between 1 and 100: "))
print 
#add if stms, to tell user if number is to high, low, or is correct
if player > number:
	print "You guessed to high, guess lower."
elif player < number:
	print "You guessed to low, guess higher."
elif player == number:
	print "You guessed right! Congrats!"