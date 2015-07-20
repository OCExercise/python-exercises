# this one is like your scripts with argv
def print_two(*args): #name function, type the arguments
    arg1, arg2 = args #unpack them
    print "arg1: %r, arg2: %r" % (arg1, arg2) #this is what it does

def print_two_again(arg1, arg2): #good to know I can skip straight to the set of args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1): #I get it
    print "arg1: %r" % arg1

def print_none(): #HRRRR
    print "I got nothin'."


print_two("your","gay")
print_two_again("nigger","ware")
print_one("FFS")
print_none()