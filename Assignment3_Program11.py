#DATE: OCT 25TH, 2015
#AUTHOR: KATHLEEN BURGESS
#ASSIGNMENT: 3, problem 10, Group 14
#DESRIPTION:
	
additionalRoom = 0
while additionalRoom != "no":
	#ask for demensions of room
	"Welcome to Fern's Fine Flooring"
	width = float(raw_input("Please enter width of room. (m) "))
	length = float(raw_input("Please enter length of room. (m) "))
	#ask user to choose flooring type
	print 
	flooring_type = raw_input("""Flooring Types and Pricing: 
Tile $10/m^2
Linoleum $8/m^2
Carpeting (Indoor/Outdoor) $5/m^2

Please choose a floor type. """)
	#calculate price of flooring
#add funtion so code does not notice caps!!!
	if flooring_type == "Tile":
		cost_ofFlooring = 10*(width*length)
	elif flooring_type == "Linoleum":
		cost_ofFlooring = 8*(width*length)
	elif flooring_type == "Carpeting":
		cost_ofFlooring = 5*(width*length)
	#calculate subtotal
	subTotal = 0
	subTotal = subTotal + cost_ofFlooring
	print "SubTotal:$",subTotal,", not including tax."
	#ask user if they want flooring for another room
	additionalRoom = raw_input("Do you want flooring for another room? Answer yes or no: ")
	print
#print reciet for user
HST =cost_ofFlooring*0.13
totalCost = subTotal + HST
print "SubTotal:$",subTotal
print "HST:$",HST
print "Total:$",totalCost
print 
print "Thanks for shopping at Fern's Fine Flooring. Hope to see you again."



