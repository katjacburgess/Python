#DATE: JULY 22, 2015
#AUTHOR: KATHLEEN
#DESRIPTION: this code will show if two numbers when added together equal zero

#VARIABLES
var1 = raw_input("Enter the First Number: ")
var2 = raw_input("Enter the Second Number: ")
result = ""

# is (var1 + var2) equal to 0?
if (var1 + var2) == 0:
	# (var1 + var2) = 0
	print "( " + str(var1) + " + " + str(var2) + " ) = 0"
	print "the sum of these numbers equal zero"
else: 
	result = int(var1) + int(var2)
	# (var1 + var2) = result
	print "( (" + str(var1) + ") + (" + str(var2) + ") ) = " + str(result)
	print "the sum of these numbers do not equal zero"
	
	
	