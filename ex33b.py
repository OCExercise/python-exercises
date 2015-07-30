#implement ex. 33 with for-loop instead of while-loop
def for_great_justice (start, stop, step):
	istart = int(start); istop = int(stop); istep = int(step)
	values = range(istart, istop, istep)
	for n in values:
		display = []
		print "At the top i is %d" % n
		display = display.append(n)
		bottom = n + istep
		print "Numbers now: ", display
		print "At the bottom i is %d" % bottom 
		#there's an edge case where the last iteration of bottom goes
		#over the istop value, but the previous was written the same.
	print "The numbers: "
	for num in values: 
	#display in the for-loop is already just a reproduction of the values var,
	#so I guess I don't feel bad not using display in favor of values.
	#I do feel some "hard-coding" or "lack of abstraction" guilt.
	#I suppose I could make the for-loop into its own for_mini function 
	#so that it would return its local variable for future use.
	#but anyway, it works.
		print num

begin = raw_input("Minimum value? ")
end = raw_input("Maximum value? ")
interval = raw_input("Increment? ")

for_great_justice(begin, end, interval)