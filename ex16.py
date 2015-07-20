#close -- Closes the file. Like File->Save.. in your editor.
#read -- Reads the contents of the file. You can assign the result to a variable.
#readline -- Reads just one line of a text file.
#truncate -- Empties the file. Watch out if you care about the file.
#write('stuff') -- Writes "stuff" to the file.
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#this functionality is actually the built-in keyboard interrupt
#and the raw_input is still 'dumb'...but who's keeping score
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
#notably the file contents are assigned to a variable, in this case target
#but this is discrete from actually writing to the file
print "Truncating the file.  Goodbye!"
target.truncate()
#dead-ed
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write('%r \n %r \n %r \n' % (line1, line2, line3))

print "And finally, we close it."
target.close() #this saves it too
#open and read are not the same
#open with no arguments defaults to read