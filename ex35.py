from sys import exit 
# I commented in the entire section from python.org here, because I didn't quite
# get it at first. Now I get it.

# In this case, we imported and used exit so that each of these functions could
# work with each other without having to nest perfectly.

def gold_room():
    print "This room is full of gold.  How much do you take?"

    choice = raw_input("> ") #choice in this and subsequent are local vars
    if "0" in choice or "1" in choice: 
    # binary is going to have one of these two values in any string
        how_much = int(choice) # passes to next if
    else:
        dead("Man, learn to type a number.") 
        # the only way out from previous would be to hit return w/o typing
        # dead will print a message and exit
        # next, needs type check & retry/dead if other than number is entered

    if how_much < 50: #hey, it was a number! passed down here from first if
        print "Nice, you're not greedy, you win!"
        #well, pretty obvious what's happening here
        exit(0)
    else: 
        dead("You greedy bastard!")


def bear_room(): # takes no arguments
    print "There is a bear here." # for user's benefit
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False # interesting to set this up thusly, see below

    while True: #bear_moved will = false at start, so not bear_moved = true
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.") #womp womp
        elif choice == "taunt bear" and not bear_moved: #True at outset
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True 
            # punt to prompt, now bear has moved due to True and True in elif
            # incidentally local vars named same as higher vars = not cool, Bob
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
            # don't gratuitously taunt the bear
        elif choice == "open door" and bear_moved: # true if bear taunted once
            #lack of condition for trying to open door with bear in way is dumb 
            gold_room() # moving right along
        else:
            print "I got no idea what that means." 
            # related to need for type check in gold_room function


def cthulhu_room(): # anyway
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice: # obvious
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else: #you will answer to cthulhu
        cthulhu_room()


def dead(why): 
# the lone thing in here that has an argument, because other funcs tell it why
    print why, "Good job!"
    exit(0)

def start(): # handles initial prompt and sends you to other rooms
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ") # choice is always local to funcs

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start() # enter the flowchart