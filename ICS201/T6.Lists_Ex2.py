#DATE: NOV 11TH, 2015
#AUTHOR: KATHLEEN BURGESS
#T6:LISTS, Exercise 2
#DESRIPTION: this program uses the built in function len, it prints the number of characters in a name
	
name = raw_input("Please enter a name ")
for c in range(len(name)):
	print c, name[c]

