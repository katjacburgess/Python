#DATE: JULY 31, 2015
#AUTHOR: KATHLEENR
#DESRIPTION: Pick your favorite character from friends and see a quote of what they said on the show

question = raw_input("Who is your favorite character on friends?: ")
question = question.lower(); #makes the case, no matter what it is, lowercase
print question; #shows what ross is, you can comment this line out ;)

if question == "rachel": #changed all the if statements to lowercase versions
	print "quote: I mean isnt that just kick-you-in-the-crotch, spit on your-neck-fantastic (case insensitive)"

if question == "ross":
	print "quote: We Were On A BREAK!!!"

if question == "monica":
	print "quote: Ive got this uncontrollable need to please people"

if question == "phoebe":
	print "quote: See? Hes your lobster!"

if question == "joey":
	print "quote: JOEY DOESNT SHARE FOOD"

