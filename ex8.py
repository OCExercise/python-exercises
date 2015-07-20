#assigning a string of string inputs to a variable is a little like a primitive function.
#the term formatter now has to, after the %, have "arguments" 
#in the form of a set of numbers or strings.
#it will take numbers or strings because it's %r
#the commas are separating the values and don't appear when executed
formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
) #noting that parens are immune to line breaks, making life easier
#Notice that the last line of output uses both single-quotes 
#and double-quotes for individual pieces. Why do you think that is?
#appearance of an apostrophe (') in the third string
#Wait...what is python 3 and why are we using 2.7 if there's a 3?