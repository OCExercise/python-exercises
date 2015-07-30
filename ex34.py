animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

#Zero indexing!
#The animal at 1. python
#The third (3rd) animal. @ 2, peacock
#The first (1st) animal. @ 0, bear
#The animal at 3. kangaroo
#The fifth (5th) animal. @ 4, whale
#The animal at 2. peacock
#The sixth (6th) animal. platypus
#The animal at 4.

print animals
python = animals[1]
print "the animal at 1 is 2nd, a %r" % python
peacock = animals[2]
print "the third animal has index 2 and is a %r" % peacock
bear = animals[0]
print "the first animal has index 0 and is a %r" % bear
kangaroo = animals[3]
print "the animal at 3 is 4th, a %r" % kangaroo
whale = animals[4]
print "the fifth animal has index 4 and is a %r" % whale
print "the animal at 2 is 3rd, a %r" % peacock
platypus = animals[5]
print "the sixth animal has index 5 and is a %r" % platypus
print "the animal at 4 is 5th, a %r" % whale
#i rewrote this like an idiot several times because I didn't realize
#i should have been using brackets instead of parens.
#it probably would have worked in single declarative lines instead of
#bothering with variables if I could've managed to choose correctly between
#commas/semicolons and brackets/parens.