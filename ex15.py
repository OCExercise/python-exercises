from sys import argv
script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
#We call a function on txt named read. 
#What you get back from open is a file, 
#and it also has commands you can give it. 
#You give a file a command by using the . (dot or period), 
#the name of the command, and parameters.
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()
# close -- Closes the file. Like File->Save.. in your editor.
# read -- Reads the contents of the file. You can assign the result to a variable.
# readline -- Reads just one line of a text file.
# truncate -- Empties the file. Watch out if you care about the file.
# write('stuff') -- Writes "stuff" to the file.