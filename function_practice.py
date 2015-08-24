#DATE: JULY 26, 2015
#AUTHOR: KATHLEEN
#DESRIPTION: This is "Functions" practice.

###OLD MANUAL WAY:
print "Hello Joe, My name is Kathleen."
print "Hello Chris, My name is Kathleen."
print "Hello Bob, My name is Kathleen."


##BREAK##
print ""										

###NEW FUNCTION WAY:
#Declaring a Function
def nameOw(name):
	print "Hello " + str(name) + ", My name is Kathleen."

#Calling a Function

nameOw("Joe")
nameOw("Xander")
nameOw("Lili")


#Call a function & Pass a variable differently
myName = "Superman";
nameOw(myName) #as long as the variable is in the same place, the function will treat it the same way