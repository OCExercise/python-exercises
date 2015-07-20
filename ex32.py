the_count = [1, 2, 3, 4, 5] 
#a list, which looks suspiciously like a vector in R
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	#funtion var assigned from list argument
    print "This is count %d" % number


for fruit in fruits:
    print "A fruit of type: %s" % fruit

#mixed list changes to %r
for i in change:
    print "I got %r" % i

elements = []

#range is a built in that will interval expand and create list 
for i in range(0, 6): #you get one less than the last so you need n+1
    print "Adding %d to the list." % i
    elements.append(i)

# yes, could've said simply elements = range(0,6)

for i in elements:
    print "Element was: %d" % i

#other list ops: 
#list.append(x)
#Add an item to the end of the list; equivalent to a[len(a):] = [x].

#list.extend(L)
#Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.

#list.insert(i, x)
#Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

#list.remove(x)
#Remove the first item from the list whose value is x. It is an error if there is no such item.

#list.pop([i])
#Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

#list.index(x)
#Return the index in the list of the first item whose value is x. It is an error if there is no such item.

#list.count(x)
#Return the number of times x appears in the list.

#list.sort(cmp=None, key=None, reverse=False)
#Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

#list.reverse()
#Reverse the elements of the list, in place.