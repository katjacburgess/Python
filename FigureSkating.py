#DATE: JULY 31, 2015
#AUTHOR: KATHLEEN
#DESRIPTION: This code will calculate your points based on the figure skating spins and jumps you exceute.

#points system executed elements

#jumps
_1A = 1.10
_2S = 1.30
_2T = 1.30
_2Lo = 1.80
_2F = 1.80
_2Lz = 2.10
_2A = 3.30
_3S = 4.20
_3T = 4.30
_3Lo = 5.10
_3F = 5.30
_3Lz = 6.00
_3A = 8.50
_4S = 10.50
_4T = 10.30

#spins
LSpB = 1.20
FSSpB = 1.70
FCCoSpB = 1.70
CCoSpB = 1.70

#step and choreography sequences
StSq_1 = 1.80
ChSqB = 2.00

#score definition
pointTalley = 0 

userInput = raw_input("Which elements did you excecute in your program? EG 'Sow Cow, Blab Blah, etc.': ")
#print userInput
userInput = userInput.lower()
#print userInput	

if userInput == "single axel":
#	print "test"
	pointTalley = pointTalley + _1A
#	print _1A
#	print pointTalley




print "Total Score = ", pointTalley 

#string operator, seprator by commas, split qith commas phython 