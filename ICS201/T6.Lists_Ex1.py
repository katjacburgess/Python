#DATE: NOV 10TH, 2015
#AUTHOR: KATHLEEN BURGESS
#T6:LISTS, Exercise 1
#DESRIPTION: this program takes 5 names from the user and adds them to a list then prints each name forwards and backwards

listofNames = []
reverseList = []
names= 0
while names<5:
	names = names + 1
	name1 = raw_input("Please enter a name. Enter stop to end. ")
	if name1 == "stop":
		names = 6
	if name1 != "stop":
		name2 = raw_input("Please enter a name ")
		name3 = raw_input("Please enter a name ")
		name4 = raw_input("Please enter a name ")
		name5 = raw_input("Please enter a name ")
		listofNames.append(name1)
		listofNames.append(name2)
		listofNames.append(name3)
		listofNames.append(name4)
		listofNames.append(name5)
		reverseList.append(name1[::-1])
		reverseList.append(name2[::-1])
		reverseList.append(name3[::-1])
		reverseList.append(name4[::-1])
		reverseList.append(name5[::-1])
		for i in range(0,5):
			print listofNames[i], reverseList[i]

