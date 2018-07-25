#This is where my final game will lie
import random
import time
prob = random.random()
loading_screen = random.randrange(0,5)
def skyrim():
    if loading_screen == 0:
        print "creating goblins"
    if loading_screen == 1:
        print "Learning spells"
    if loading_screen == 2:
        print "fighting skeletons"
    if loading_screen == 3: 
        print "finding artifacts"
    if loading_screen == 4:
        print "creating quests"
    if loading_screen == 5:
        print "Look out for Easter Eggs"
    print "Initializing data"
    time.sleep(1)
    print "downloading fun"
    time.sleep(1)
    print loading_screen
    time.sleep(1)
    print loading_screen
    time.sleep(1)
    print ("A message from the Developer:")
    print ('''Hi thanks for playing my game, most likely you'll be seeing 
        my game while it's still very early and far from complete ''')  
    name = raw_input("What's your name?")
    if name == "Reese":
        print ("Welcome Home")
    else:
        print ("hi", name)
    time.sleep(1)
    age = raw_input("How old are you?")
    print ("Oh", age, "thats an exciting year isn't it?")
while True:
    start = raw_input("press X to start")
    if start == "x":
        skyrim()
    else:
        print "press X to start"
    start = raw_input("press X to start")

