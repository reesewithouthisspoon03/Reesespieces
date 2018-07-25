import random
import time
def play():
    print ("Want to do some Madlibs?")
    time.sleep(2)
    print ("That's what I thought, let's get started")
    time.sleep(3)
    prob = random.random()
    noun1 = raw_input("enter your first noun  ")
    noun2 = raw_input("enter your second noun  ")
    smell = raw_input("enter a scent  ")
    madlib1 = random.randrange(1,4)
    madlib2 = random.randrange(1,4)
    madlib3 = random.randrange(1,4)
    if madlib1 == 1:
        print "My favorite part of coding is,", noun1
    if madlib1 == 2:
        print "when I ", noun1
    if madlib1 == 3:
        print "I hate", noun1
    if madlib2 == 1:
        print "My favorite part of coding is", noun2
    if madlib2 == 2:
        print "i love", noun2
    if madlib2 == 3:
        print "I hate", noun2
    if madlib1 == 1:
        print "My favorite part of coding is,", smell
    if madlib3 == 2:
        print "i love", smell
    if madlib3 == 3:
        print "I hate", smell
while True:
    restart = raw_input("wanna play again?")
    print"restarting"
    time.sleep(1)
    print"3"
    time.sleep(1)
    print"2"
    time.sleep(1)
    print"1"
    time.sleep(2)
    print "restart complete"
    time.sleep(1)
    print '''starting "madlibs"'''
    time.sleep(1)
    play()