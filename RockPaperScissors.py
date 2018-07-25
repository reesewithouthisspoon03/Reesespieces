import random
prob = random.random()
player_rps = raw_input ("Pick: rock paper, or scissors  ")
print player_rps

rock = 1
paper = 2
scissors = 3
cpu_rps = random.randrange(1, 4)
if cpu_rps == rock:
        print "rock"
elif cpu_rps == paper:
        print "paper"
elif cpu_rps == scissors:
        print "scissors"
else:
    player_rps = rock
if player_rps == cpu_rps:
    print ("tie")
elif player_rps == "paper" and cpu_rps == "rock":
    print ("You win! Paper covers rock")
elif player_rps == "paper" and cpu_rps == "scissors" :
    print ("You Lose, scissors cuts paper")
elif player_rps == "rock" and cpu_rps == "scissors":
    print ("You win! rock smashes scissors") 
elif player_rps == "rock" and cpu_rps == "paper":
    print ("You lose! Paper covers Rock")
elif player_rps == "scissors" and cpu_rps == "rock":
    print "You lose! Rock smashes scissors"
elif player_rps == "scissors" and cpu_rps == "paper":
    print "You win! Scissors cuts paper"    
    
