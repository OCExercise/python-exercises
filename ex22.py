#pythagorean expectation, from some guy on github
RS = float(raw_input("My crap team has scored this many runs: "))
RA = float(raw_input("My crap team has allowed this many runs: "))
pynum = RS**2
print pynum
pyden = (pynum+RA**2)
print pyden
pyth = pynum/pyden
print pyth
print "This should be your crap team\'s win ratio: %.3f" % pyth
