#This is where my final game will lie
import
import random
prob = random.random()
loading_screen = random.randrange(0,5)

start = raw_input("press X to start")
if loading_screen == "0":
    print "creating goblins"
if loading_screen == (1):
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
print "downloading fun"
print loading_screen
print loading_screen

print ("A message from the Developer:")
print ('''Hi thanks for playing my game, most likely you'll be seeing 
    my game while it's still very early and far from complete ''')  
name = raw_input("What's your name?")
if name == "Reese":
    print ("Welcome Home")
else:
    print ("hi", name)
age = raw_input("How old are you?")
print ("Oh", age, "thats an exciting year isn't it?")
