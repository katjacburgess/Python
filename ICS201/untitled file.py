import random
numbers = []
for counter in range(0,10):
	
	numbers.append(random.randint(20,50))
	print numbers[::-1]
	
	
letters = ['a','b']
if 'a' in letters:
	print "found 'a' in letters"
	print letters.remove('a')
	print letters
else:
	print "didn't find 'a' in letters"
	
word = ['mental','health']
for c in range(len(word)):
	print c, word[c]     
	
letters.append('f') 
print letters
print letters.insert(1,9)
print letters
print letters[::1]