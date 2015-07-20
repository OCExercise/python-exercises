name = 'Alexander David McMath'
age = 30
height = 67.0
weight = 265.0
eyes = 'brown'
teeth = 'white'
hair = 'nonexistent'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He weighs %d pounds." % weight
print "Damn that's one fat motherfucker."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s if he brushes them." % teeth
#HRRRRRR
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

metric_height = height * 2.54
metric_weight = weight / 2.2
print "He's %d cm tall." % metric_height
print "He weighs %d kilos." % metric_weight