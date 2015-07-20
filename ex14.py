from sys import argv
#seems like script always has to be there and will be the filename every time
script, user_name = argv
prompt = '(god you\'re a cocksucker) ' #simple enough

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt) #been there done that

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer) 
# the %r passes in sequence from the set into the """