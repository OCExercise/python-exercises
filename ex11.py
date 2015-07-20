print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
#using %r rather than type dependent numerical input
#raw_input() is like %r, input() will run like code, 
#int() will convert the input to
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)