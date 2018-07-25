import random
def play():
    prob = random.random()
    eightball_answer = random.randrange(1,16)
    player_input = raw_input ("Ask the magic 8 ball a question  ")
    print player_input
    if eightball_answer == 1:
        print "I don't know, ask me later"
    elif eightball_answer == 2:
        print "Most likely"
    elif eightball_answer == 3:
        print "Without a doubt"
    elif eightball_answer == 4:
        print "Better not tell you now"
    elif eightball_answer == 5:
        print "definitely"
    elif eightball_answer == 6:
        print "absolutely not"
    elif eightball_answer == 7:
        print "outlook not so good"
    elif eightball_answer == 8:
        print "Totally!"
    elif eightball_answer == 9:
        print "yes"
    elif eightball_answer == 10:
        print "no"
    elif eightball_answer == 11:
        print "yes"
    elif eightball_answer == 12:
        print "no"
    elif eightball_answer == 13:
        print "ask me again"
    elif eightball_answer == 14:
        print "not in a million years"
    elif eightball_answer == 15:
        print "stop asking me questions"
        
while True:
    answer = raw_input("Do you want to ask the magic 8 ball another question?  ")
    if answer == 'yes':
        play()
    elif answer == 'no':
        sure = raw_input("are you sure you want to quit?") 
        if sure == 'yes':
            break
    else:
        print ("say 'yes' or 'no'")