#file object = open("hello.txt")
#helloFile.write("Testing... 1 2 3") #prints to end of file
#helloFile.write("") #makes a line space

import time

for i in range(0, 50):
	print ""
	helloFile = open("hello.txt")
	readString = helloFile.read()
	timeString = time.strftime("%I:%M:%S")
	print "FILE CONTENTS @ " + str(timeString) + " :"
	print ""
	print readString
	helloFile.close()
	time.sleep(1)