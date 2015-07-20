#set some variables to have string values, using % to insert values (including vars set to strings) into strings
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#what do you think is gonna happen? it tells the joke when you execute the file.
print x
print y
#the % operator inserts the var, which is a string
print "I said: %r." % x
print "I also said: '%s'." % y
#it continues
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#this is gay
print joke_evaluation % hilarious
#more strings
w = "This is the left side of..."
e = "a string with a right side."
#the + operator, when receiving strings for input, concatenates them. HRRRR
print w + e
#I count 5 strings inside other strings
#noting that %r is different from %d and %s