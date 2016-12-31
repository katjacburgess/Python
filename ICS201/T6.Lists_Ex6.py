#DATE: NOV 11TH, 2015
#AUTHOR: KATHLEEN BURGESS
#T6:LISTS, Exercise 6
#DESRIPTION:   
	
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = 0
import random
licensePlate = []
licensePlate_lists = []
        
for counter in range (0,3):
	licensePlate.append(random.randint(1,9))
import random
for counter in range (0,3):
	numbers= random.randint(0,26)
	alphabetPlate = alphabets[numbers]
	licensePlate.append(alphabetPlate)
#licensePlate.insert(3," ")

for counter in range (0,10):
	licensePlate_lists.append(licensePlate)
print licensePlate_lists
#print licensePlate

	  
                                                                                                    
	
	
	
	#numbers.insert(1, 9) 
	#The ministry of transportation is looking for a programmer who can create a program to randomly generate license plates. Your license plates will contain three numbers followed by a space and followed by three letters. An example of a license plate will be 123 XYZ.
	#Here is the algorithm for how to do this:
	#Create a string variable of alphabets A..Z. Call it alphabets.
	#Randomly generate six numbers. In doing this, be as efficient as you can.
	#Use three of these numbers as the index values of the letters in the alphabet string to retrieve those letters. Once the three letters are put together with the remaining three numbers, you create a license plate number. Generate 10 of these plate numbers. Add them to a list. At the end, print these license plate numbers to the screen.