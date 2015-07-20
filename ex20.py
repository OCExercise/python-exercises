from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0) #goes to the 0 byte in file

def print_a_line(line_count, f):
    print line_count, f.readline() 
    #it would be great if I would stop getting tripped up
    #by lack of defined arguments WHILE STILL IN DEF
    #dumbass
    #however, this time you were somewhat right; readline
    #is connected to the file and not to the function argument

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line =+ 1 #increment the counter, slightly shorter
print_a_line(current_line, current_file)

current_line =+ 1
print_a_line(current_line, current_file)