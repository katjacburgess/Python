#DATE: NOV 7TH, 2015
#AUTHOR: KATHLEEN BURGESS
#T5:STRINGS PART 2, Exercise 6
#DESRIPTION: this program asked for words from the user and at the end prints the total number of words of each length
	
word = 1
wordEqual5 = 0
wordUnder5 = 0
wordEqual6 = 0
wordOver6 = 0
while word != "done":
	word = raw_input("Enter a word, enter done to end. ")
	length_ofWord = len(word) #len counts the number od characters in each word
	if word != "done":
		print word
		if length_ofWord == 5:
			wordEqual5 = wordEqual5 + 1
		
		elif length_ofWord <5:
			wordUnder5 = wordUnder5 + 1
		
		elif length_ofWord ==6:
			wordEqual6 = wordEqual6 + 1
		
		elif length_ofWord >6:
			wordOver6 = wordOver6 + 1

print "Words of 5 characters:"
print wordEqual5
print "Words under 5 characters:"
print wordUnder5
print "Words of 6 characters:"
print wordEqual6
print "Words more than 6 characters:"
print wordOver6



#under 5 characters____words
#of 5 characters____words
#of 6 characters____words
#of more than 6 characters____words


