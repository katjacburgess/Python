#DATE: NOV 11TH, 2015
#AUTHOR: KATHLEEN BURGESS
#T6:LISTS, Exercise 4
#DESRIPTION: this program is exercise 3 but also prints the highest mark out of the marks list at the end
	

names = ["Jordon","Conner","Ethan","Megan","Lynsie","Ryan","Kevin"]
marks = [80,95,70,75,85,90,82]
print names[0],",",marks[0]
print names[1],",",marks[1]
print names[2],",",marks[2]
print names[3],",",marks[3]
print names[4],",",marks[4]
print names[5],",",marks[5]
print names[6],",",marks[6]
average = 0
sum = 0    
for n in marks: #use a for loop so it looks though every number in the list indivisually
    sum = sum + n #sum adds the numbers in the list
average = sum / len(marks) #divide by length of list, use len()
print "Average:", average

#find the highest mark
print "The highest mark is",max(marks) #max is a funtion that find the highest number