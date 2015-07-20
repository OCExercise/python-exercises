def while_away(length, increment): #forgot the goddamn colon
	#length = int(raw_input("What is the limit? ")) 
	#delete "length" from def line and above is how the func was taking args
	i = 0
	end = int(length)
	jump = int(increment)
	numbers = []
	while i < end:
		print "At the top i is %d" % i
		numbers.append(i)
		i = i + jump
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	print "The numbers: "
	for num in numbers:
		print num

criterion = raw_input("What is the limit? ")
interval = raw_input("What is the increment? ")
while_away(criterion, interval) 
#at present it takes arguments like a regular function
#i feel as though there was some benefit to the no-args way I had it
#would I ever do that?
