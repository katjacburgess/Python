#DATE: NOV 11TH, 2015
#AUTHOR: KATHLEEN BURGESS
#T6:LISTS, Exercise 5
#DESRIPTION: this program takes postal codes from a list and prints and counts the postal codes that start with "L"

total = 0
postalCodes = ['LOR1V0','L7N1S3','MORT23','LB9R0P','PS6K90','V0RC5L']

print postalCodes[0].startswith("L")
if postalCodes[0].startswith("L") == True:
	total = total + 1
	print postalCodes[0]
	
print postalCodes[1].startswith("L")
if postalCodes[1].startswith("L") == True:
	total = total + 1
	print postalCodes[1]
		
print postalCodes[2].startswith("L")
if postalCodes[2].startswith("L") == True:
	total = total + 1
	print postalCodes[2]

print postalCodes[3].startswith("L")
if postalCodes[3].startswith("L") == True:
	total = total + 1
	print postalCodes[3]
		
print postalCodes[4].startswith("L")
if postalCodes[4].startswith("L") == True:
	total = total + 1
	print postalCodes[4]
		
print postalCodes[5].startswith("L")
if postalCodes[5].startswith("L") == True:
	total = total + 1
	print postalCodes[5]
print total,"postal codes start with the letter L."