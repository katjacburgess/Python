#DATE: NOV 7TH, 2015
#AUTHOR: KATHLEEN BURGESS
#T5:STRINGS PART 2, Exercise 5
#DESRIPTION: this program prints a string forwards, backwards and part b checks if the word is a palindrome
	
word1 = raw_input("Enter a word ")
print word1[::], word1[::-1] #[::] outputs what is in the string
word2 = raw_input("Enter a word ")
print word2[::], word2[::-1] #[::-1] outputs the string backwards
word3 = raw_input("Enter a word ")
print word3[::], word3[::-1]
word4 = raw_input("Enter a word ")
print word4[::], word4[::-1]
print 

#b) modify the above program to check the word is a palindrome. A palindrome is a word that can be read the same way in either direction.
print "Now lets check if the words you enter are palindromes."
print 
word1 = raw_input("Enter a word ")
output = word1[::-1]
print word1[::], output
if word1 == output:
	print word1,"is a palindrome."
else: print word1,"is not a palindrome."

word2 = raw_input("Enter a word ")
output = word2[::-1]
print word2[::], output
if word2 == output:
	print word2,"is a palindrome."
else: print word2,"is not a palindrome."

word3 = raw_input("Enter a word ")
output = word3[::-1]
print word3[::], output
if word3 == output:
	print word3,"is a palindrome."
else: print word3,"is not a palindrome."

word4 = raw_input("Enter a word ")
output = word4[::-1]
print word4[::], output
if word4 == output:
	print word4,"is a palindrome."
else: print word4,"is not a palindrome."
