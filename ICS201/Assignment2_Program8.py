#DATE: OCT 7TH, 2015
#AUTHOR: KATHLEEN
#Grade 10, Assignment 2, question 8
#DESRIPTION: this program is a Guessing game. Player1 enters a number and player2 is asks to guess it. An appropiate comment is printed to player2 if the number is to high, to low or correct

player1 = int(raw_input("Player 1, enter a number between 1 and 100 "))
player2 = int(raw_input("Player 2, guess the number player 1 entered, it is between 1 and 100 "))
print 
if player2 > player1:
	print "You guessed to high, guess lower"
elif player2 < player1:
	print "You guessed to low, guess higher"
elif player2 == player1:
	print "You guessed right! Congrats!"