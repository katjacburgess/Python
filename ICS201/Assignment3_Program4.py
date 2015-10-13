#DATE: OCT 11TH, 2015
#AUTHOR: KATHLEEN BURGESS
#Grade 10, Assignment 3, question 4
#DESRIPTION: extended version of the Guessing Game. It uses a loop, so you can guess multiple times until correct
	
import random
guess1 = 0
guesses_taken = 0
number = random.randint(1, 100) #generaate number here, so number stays the same every loop/guess
while guess1 != 101: #enter 101 to end loop

	guess1 = int(raw_input("Guess a number between 1 and 100. Enter 101 to end the game: "))
	guesses_taken = guesses_taken + 1 #will add 1 guess to tally, every time it runs the loop
	print #space
	if guess1 == 101:
		print "Thanks for playing :)" #add message after they are done playing
	elif guess1 == number:
		print "YOU GUESSED CORRECTLY! It took you", guesses_taken,"guesses." #prints how many guesses it took you
	elif guess1 > number:
		print "You guessed to high, guess lower."
	elif guess1 < number:
		print "You guessed to low, guess higher."
		
#how do i include a counter?
	



