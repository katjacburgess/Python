#DATE: AUGUST 2, 2015
#AUTHOR: CAMERON

number = 1
#print number

while number < 100:
#	print "Enter Loop"
#	number = number + number**number
	number = number + number #*number
	print number
	c = number
	dotGraph = ""
	while c > 0:
		dotGraph += "*"
		c = c - 1
	print dotGraph	
	print ""