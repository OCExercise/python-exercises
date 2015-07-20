#use \ to "escape in" problematic characters like a single or double quote
#use """ similarly
tabby_cat = "\tI'm tabbed in." #tab
persian_cat = "I'm split\non a line." #newline
backslash_cat = "I'm \\ a \\ cat." #backslash character

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
""" #literal formatting above

hrrr = '''what exactly
does this
single quote
do?'''
print hrrr

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
#I see how the while loop nested in the for loop caused it to run indefinitely
#the \r and the , made it repeat in place
#while True:
 #   for i in ["/","-","|","\\","|"]:
  #      print "%s\r" % i,
 
