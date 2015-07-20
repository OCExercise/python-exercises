from sys import argv
# ok we're good, I think I get it.
# so, argv exists in python at large
# we imported it to use it
# it allows us to use command line arguments  
script, first, second, third, fourth = argv
#it takes 4 in this script
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
#all we're doing with them though is printing them in place
fifth = raw_input("How old are you? ")
print "you are %r years old" % fifth

