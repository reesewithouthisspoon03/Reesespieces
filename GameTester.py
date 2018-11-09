#This is the most stable updated version of the game
import random
import time
prob = random.random()
loading_screen = random.randrange(0,5)
loading_screen2 = random.randrange(0,5)
loading_screen3 = random.randrange(0,5)
random_encounter1 = random.randrange(10, 15)
random_encounter2 = random.randrange(13, 20)
random_encounter3 = random.randrange(17, 25)
#variables
global health 
health = 100
global strength 
strength = 10
global intelligence 
intelligence = 10
global agility 
agility = 10
global fun 
fun = 10
global gold
gold = 100
print ("Rever Monde presents...")
time.sleep(1)
print ("An Elder Scrolls parody...")
time.sleep(1)
print ("The Elder Scrolls 0: Adventurer")
time.sleep(1)
time.sleep(3.6)
def skyrim():
    global health 
    health = 100
    global strength 
    strength = 10
    global intelligence 
    intelligence = 10
    global agility 
    agility = 10
    global fun 
    fun = 10
    global gold
    gold = 100
    print "Launching skyrim_80.exe"
    print "Initializing data"
    time.sleep(1)
    print "installing fun.exe"
    time.sleep(2)
    print "executing fun.exe"
    time.sleep(1)
    print "loading graphics"
    time.sleep(3)
    print "G@F!C$ F@!iUR3 3J3CT!NG"
    time.sleep(5)
    print "error, graphics load attempt failed"
    time.sleep(1)
    print "continue loading skyrim_80.exe"
    time.sleep(2)
    print "Initializing world"
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
    time.sleep(1.3)
    if loading_screen2 == 0:
        print "forging swords"
    if loading_screen2 == 1:
        print "casting spells"
    if loading_screen2 == 2:
        print "Fighting giants"
    if loading_screen2 == 3: 
        print "summoning daedra"
    if loading_screen2 == 4:
        print "pillaging villages"
    if loading_screen2 == 5:
        print "Not being sued"
    time.sleep(1.7)
    if loading_screen3 == 0:
        print "still not being sued"
    if loading_screen3 == 1:
        print "Learning Shouts"
    if loading_screen3 == 2:
        print "Fus Roh Dah"
    if loading_screen3 == 3: 
        print "Climbing Mountains"
    if loading_screen3 == 4:
        print "Delving into dungeons"
    if loading_screen3 == 5:
        print "Look out for Easter Eggs"
    time.sleep(2.5)
    print "loading complete, launching game"
    time.sleep(2.9)
    print ("Just some background information, when giving user input, act like you're just talking, not of that Y/N crap, just talk normally.")
    print '''Hiding inside a fireplace was never on your to do list,
but your parents helped you in, and pushed a button and a stone slab slid under your feet.'''
    time.sleep(1)
    print '''You hear your mother whisper an enchantment and runes appear on the stone.
You beg them to come too, dispite them having explained that they have to protect you'''
    time.sleep(1)
    print '''We'd seen trouble from our windows, I only had a glance, and what I saw seemed like a nightmare
your parents assure you hadn't seen anything, but each passing second after only made the image more clear
a demonic horde, at least 2 dozen.
you heard them come in asking for you by name:'''
    global name
    name = raw_input("What's your name? ")
    if name == "Reese":
        print ("Return of the King")
    elif name == "tester":
        print ("Thanks for testing my game! (The usual line is Bring us ____, and we'll be on our way, the blank being a name that isn't secret, I have easter eggs hidden, this name is one of them.")
    elif name == "dovahkiin":
        print "FUS RO DAH"
    elif name == "Kimberly":
        print "Snack Time!!!"
    elif name == "Jordan":
        print "I sleep on the floor, like a puppy-dog"
    elif name == "silence my brother":
        print "Welcome home"
    elif name == "sanguine my brother":
        print "Welcome home"
    elif name == "innocence my brother":
        print "Welcome home"
    elif name == "Vahdeta":
        print "She didn't know what to say"
    else:
        fun = 10
        fun += 1
    print '''"You know why we're here. Bring us''', name, '''and we'll be on our way."'''
    time.sleep(1)
    print '''You hear your parents say together, "We'd die before we let that happen."
the reply was nothing except both of their dying breaths, let out in a shriek...
the trauma causes you to pass out'''
    time.sleep(3)
    def createrace():
        global name
        global health
        global strength
        global intelligence
        global agility
        global fun
        global gold
        print "CREATE YOUR CHARACTER"
        time.sleep(1)
        global race
        if race == "Orc":
            print "Orcs have brute strength, they are the most physically rigorous. +50 HEALTH!, + 25 strength -2 agility, -7 intelligence"
            race_sure = raw_input("Are you sure you want to be this race?")
            if race_sure == "yes":
                health += 25
                strength += 15
                intelligence -= 7
                agility -= 2
            elif race_sure == "Yes":
                health += 25
                strength += 15
                intelligence -= 7
                agility -= 2
            elif race_sure == "Y":
                health += 25
                strength += 15
                intelligence -= 7
                agility -= 2
            elif race_sure == "y":
                health += 25
                strength += 15
                intelligence -= 7
                agility -= 2
            elif race_sure == "No":
                createrace()
            elif race_sure == "no":
                createrace()
            elif race_sure == "N":
                createrace()
            elif race_sure == "n":
                createrace()
        elif race == "Redguard":
            print "Redguards are physically fit and agile, making them most useful as swordsmen +20 health +10 strength, +10 agility"
            race_sure = raw_input("Are you sure you want to be this race?")
            if race_sure == "yes":
                health += 20
                strength += 10
                agility += 10
            elif race_sure == "Yes":
                health += 20
                strength += 10
                agility += 10
            elif race_sure == "Y":
                health += 20
                strength += 10
                agility += 10
            elif race_sure == "y":
                health += 20
                strength += 10
                agility += 10
            elif race_sure == "No":
                createrace()
            elif race_sure == "no":
                createrace()
            elif race_sure == "N":
                createrace()
            elif race_sure == "n":
                createrace()
        elif race == "Imperial":
            print "Imperials conquered the tamrielic empire. They are very diplomatic as well +7.5 to all stats!"
            race_sure = raw_input("Are you sure you want to be this race?")
            if race_sure == "yes":
                health += 7.5
                intelligence += 7.5
                strength += 7.5
                agility += 7.5
            elif race_sure == "Yes":
                health += 7.5
                intelligence += 7.5
                strength += 7.5
                agility += 7.5
            elif race_sure == "Y":
                health += 7.5
                intelligence += 7.5
                strength += 7.5
                agility += 7.5
            elif race_sure == "y":
                health += 7.5
                intelligence += 7.5
                strength += 7.5
                agility += 7.5
            elif race_sure == "No":
                createrace()
            elif race_sure == "no":
                createrace()
            elif race_sure == "N":
                createrace()
            elif race_sure == "n":
                createrace()
            else:
                print "wow, you happened to pick some kind of affirmative that I didn't include, try again buddy"
                createrace()
        race = raw_input("Choose your race (Orc, Redguard, Argonian, Breton, HighElf, DarkElf, WoodElf, Khajiit, Nord, Imperial) If you want extra info on each race, type 'info') FYI, the canon race is Imperial ")
        if race == "Orc":
            print "Orcs have brute strength, they are the most physically rigorous race of tamriel. +20 HEALTH!, + 25 strength -2 agility, -7 intelligence"
            health += 20
            strength += 15
            intelligence -= 7
            agility -= 2
        elif race == "Redguard":
            print "Redguards are physically fit and agile, making them most useful as swordsmen +15 health +10 strength, +10 agility"
            health += 15
            strength += 10
            agility += 10
        elif race == "Imperial":
            print "Imperials conquered the tamrielic empire. They are very diplomatic as well. +7.5 to all stats!"
            health += 7.5
            intelligence += 7.5
            strength += 7.5
            agility += 7.5
        elif race == "Khajiit":
            print "Khajiits are witty and agile. They make great warriors, thieves and assassins. +15 agility, +10 strength, +7 health, +7 intelligence"
            health +=7
            agility += 15
            intelligence += 7
            strength += 10
        elif race == "Breton":
            print "Bretons are derived from human and elven ancestry. They possess great intelligence and are abstract thinkers, +25 intelligence, +5 strenth"
            intelligence += 25
            strength += 5
        elif race == "HighElf":
            print "High Elves are naturally gifted in the arcane. They make the best mages in Tamriel. Arrogent pricks who think they're better than other races as well. +30 Intelligence, + 2 agility -5 health - 5 strength"
            health -= 5
            intelligence += 30
            agility += 5
        elif race == "Nord":
            print "Nord are tall, pale humans that have incredible resistance and strength. Racist against all other races +5 agility +8 health +20 strength"
            health += 8
            agility += 5
            strength += 20
        elif race == "DarkElf":
            print "Dark Elves are dark-skinned elves that are often targeted because of their status. They are historically good assasins in the Morag Tong nd wizards like House Telvanni -5 health +30 intelligence, +10 agility"
            health -= 5
            intelligence += 30
            agility += 10
        elif race == "WoodElf":
            print "Wood Elves live in the forests of Valenwood. They make excellent rangers +5 health +5 intelligence +20 agility +5 strength"
            health += 5
            intelligence += 5
            agility += 20
            strength += 5
        elif race == "Argonian":
            print "Argonians are reptilian people that can breathe underwater and a resistant to many human diseases. +10 health +10.5 strength, agility +7"
            health += 10
            strength += 10.5
            agility += 7
        elif race == "info":
            print "Argonians are waterbreathing reptillian people, they have a longstanding and mutual hatred with Dark Elves, Nords are very strong and cold resistant and are often critisized as barbaric and racist, Imperials are well rounded as any class they have been reguarded as great scholars, warriors, as well as thieves however their biggest trump card is diplomacy. Redguards are well rounded in combat as anything but a mage they hail from Hammerfell, which is dominated by the Alik'r Desert, as such they are resistant to heat and poison of some creatures. Khajiit are nimble feline humanoids, they get bad reputations as thieves and pickpockets, however many outside of their homeland of Elsweyr are members of caravans, they have a weakness to moonsugar and skooma, the cocaine of Tamriel. Bretons are half-elves who make naturally good magic users their mixed blood makes them good spellswords, they are also splendid cooks. High Elves AKA Altmer are the most magically gifted of the races of tamriel, they are also pompous people seeing themselves as gods among men. Woodelves, AKA Bosmer hail from Valenwood, a forest sanctuary untouched by most men, beast and other mer races. Orcs, or Orsimer are simillar to Nords, scorned and seen as barbaric, they are seen as savage by most elves. Known mostly for their brute strength and smithing skills. They Hail from the Wrothgarian Mountains in the borders of High Rock and Skyrim, there are also several settlements in Skyrim. Dark Elves or Dunmer are a mystical race of elves hailing from Morrowind, with the Red Mountain at its central island of Vvardenfell. Nords have a special hatred for them. They are known to be great wizards, but as seen with the Morag Tong, they can be deadly assassins."
            createrace()
        else:
            print "please remember to spell it out correctly"
            createrace()
    createrace()
    def part2():
        global name
        global race
        global strength
        global health
        global intelligence
        global agility
        global fun
        global gold
        time.sleep(1)
        print '''ten years now, it's been ten years
since I lost my parents. Killed by bandits the townsfold said,
but I know it isn't true. I saw them with my own eyes. I've learned much since then...'''
        print '''I've read about them, now I know what they are, daedra, lead by a black robed figure, he seemed to be more human than the daedra.'''
        time.sleep(2)
        print '''"Who was the robed figure?" "Why would they come for me?", I thought "What could they possibly want?"
These answers never left my mind, they haunted my sleep, and I constantly pursued them. 
After that harrowing night, my great-uncle, Capitus took care of me.
A grey man, that I'd never met before. He had kind eyes, with a tiredness to them.'''
        time.sleep(4)
        print "You wake up from another nightmare about that night. They've been getting worse lately. It's your 18th birthday."
        stand = raw_input("press o to stand up ")
        if stand == "o":
            print "Bronze achievment unlocked! 'YOU HAVE LEGS'"
            time.sleep(1.5)
            print "you stand up and stretch your legs, you go into your chest and pick out your outfit"
        else:
            print "you fail to move your legs, YOU'RE PARALYZED"
            time.sleep(1)
            print "you died from paralysis"
            print "you got rekt"
            time.sleep(1)
            try_again = raw_input("wanna have another go at it?")
            if try_again == "yes":
                part2()
            else:
                print "why can't you type a simple 'yes'? you aren't worthy of my game"
                time.sleep(9999999999)
        def class_select():
            global name
            global race
            global strength
            global health
            global intelligence
            global agility
            global fun
            global gold
            global fight_class
            fight_class = raw_input("What equipment do you wear? (AKA, what's your class) (Warrior, Thief, Mage, Knight, Spellsword, Archer, Assassin, Adventurer, Too Swole To Control (2S2C), atronach, conjurer. And as with races, type 'info' for information on all classes ")
            if fight_class == "info":
                print "Warrior basic physical fighter. Thief, basic stealth fighter. Mage, basic magic/mental fighter. Knight, a highly defensive charachter, however not lacking in offense. Spellsword, a Warrior/Mage hybrid. Archer, an agility focused character"
                time.sleep(1)
                class_select()
            elif fight_class == "Warrior":
                print "A basic warrior +25 strength"
                strength += 20 
            elif fight_class == "Thief":
                print "Basic thief: +25 Agility"
                agility += 20
            elif fight_class == "Assassin":
                print "A cunning assassin, trained to kill targets +10 agility, +8 intelligence, +2 strength"
                strength += 2
                intelligence += 8
                agility += 15
            elif fight_class == "Mage":
                print "Mages have natural magical ability. +25 Intelligence"
                intelligence += 25
            elif fight_class == "Knight":
                print "Knights are strong in body and character, they also have some pretty sick looking armor. +5 agility, +12 strength, +75 health"
                agility += 5
                strength += 12
                health += 75
            elif fight_class == "Spellsword":
                print "Spellswords use both magic and combat. +15 intelligence, +15 strength"
                intelligence += 25
                strength += 25
            elif fight_class == "Archer":
                print "Archers use bow and arrows in battle. +5 health +10 strength, +15 agility"
                health += 5
                strength += 10
                agility += 15
            elif fight_class == "2S2C":
                print "Protein......... -25 intelligence, +75 strength, +25 health"
                intelligence -= 25
                strength += 75
                health += 25
            elif fight_class == "Adventurer":
                print "Adventurers explore territory and as is custom in RPGs, they take on quests. +10 to all stats"
                intelligence += 10
                strength += 10
                health += 10
                agility += 10
                fun += 10
            elif fight_class == "Atronach":
                print "Elemental beings brought forth from Oblivion. +15 intelligence"
                intelligence += 15
                fun += 5
            elif fight_class == "Conjurer":
                print "Conjurers are robed Mages who summon undead to fight against them. +5 agility, +5 health, +15 intelligence"
                intelligence += 15
                agility += 5
                health += 5
            else:
                print "Try capitalizing and checking spelling"
                class_select()
        class_select()
        def part3():
            global fight_class
            global strength
            global health
            global intelligence
            global agility
            global fun
            global gold
            print "Yes, your uncle taught you how to be a", fight_class, "but if you want to exact revenge, you'll need to be stronger."
            time.sleep(2)
            print "speaking of your uncle, you should go see him."
            first_quest = raw_input("talk to your great uncle? ")
            if first_quest == "yes":
                print "you apporoach Capitus"
            elif first_quest == "no":
                print "You decide to go out on your adventure without speaking to your uncle"
                time.sleep(1)
                print "You have no idea where you're going and you get lost."
                time.sleep(1)
                print "bandits pick you off within hours and loot your corpse"
                time.sleep(1)
                print "you got rekt"
                time.sleep(1)
                try_again = raw_input("wanna have another go at it? ")
                if try_again == "yes":
                    part2()
                else:
                    print "why can't you type a simple 'yes'? you aren't worthy of my game"
                    time.sleep(9999999)
            else:
                print("I said type 'yes' or 'no', follow directions next time")
                part2()
            print "He looks to you with weary eyes and says", name, "You are 18 now. Your time has come. Today is the day that you leave and fulfill your destiny"
            second_quest = raw_input("What do you think your destiny is?(To exact revenge! To find out who the black robed figure is, To forget about my past ")
            if second_quest == "To exact revenge!":
                print "You're a firey soul, be careful that the flame does not consume you... +5 strength"
                strength += 5
            elif second_quest == "To find out who the black robed figure is":
                print "You are inquisitive... I admire that. Remember that the truth is often obtained through great struggle, and it may not be what you except it to be. intelligence +5"
                intelligence += 5
            elif second_quest == "To forget about my past":
                print "So you wish to go rouge? Fate is strong, but if your will and intent is good and strong, you may overcome it. +5 agility"
                agility += 5
            else:
                print "Perhaps you will. I'm not a prophet you know, though I have great wisdom. In time you shall discover your destiny whatever it may be. +5 to a hidden stat"
                fun += 5
            print "You must go now, and discover your destiny, take this, it's quite dangerous to go alone."
            global first_weapon
            first_weapon = raw_input("What weapon do you recieve? (Sword + Shield, Warhammer, Bow and Quiver, Daggers, An enchanted staff{just type 'staff'.) your weapon's usefulness depends on your stats ")
            print "To give you a bit of an advantage, I'll give you one more stat bonus for your weapon to give you some extra edge"
            if first_weapon == "Sword + Shield":
                print "Achievement unlocked! Basic Warrior"
                time.sleep(1.7)
                print "Obtained Sword + Shield!  +5 strength, +5 health"
                strength += 5
                health += 5
            elif first_weapon == "Bow and Quiver":
                print "Achievement unlocked! 'Pointy Aren't They?'"
                time.sleep(1.7)
                print "Obtained Bow and Quiver! +5 agility, +3 strength"
                agility += 5
                strength += 3
            elif first_weapon == "Warhammer":
                print "Achievement unlocked! 'A blunt instrument'"
                time.sleep(1.7)
                print "Obtained Warhammer!, + 10 strength"
                strength += 10
            elif first_weapon == "Daggers":
                print "Achievement unlocked! 'stab time!!!'"
                time.sleep(1.7)
                print "Obtained daggers! + 5 strength, + 3 agility"
                strength += 5
                agility += 3
            elif first_weapon == "staff":
                print "Achievement unlocked! 'Magic stuff'"
                time.sleep(1.7)
                print "Obtained Enchanted Staff + 10 intelligence"
                intelligence += 10
            else:
                print "You chose 'nothing'!"
                time.sleep(1.2)
                print '''trash easter egg unlocked, "no hands"'''
                time.sleep(0.5)
                print "you go out into the world without a weapon"
                time.sleep(1.2)
                print "bandits assault you head on, with nothing to defend yourself, you are murdered in 30 seconds flat"
                time.sleep(1.2)
                print "GIT GUD!!!"
                time.sleep(0.5)
                print "try again"
                part2()
            print "Now go and discover your destiny"
            time.sleep(1.9)
            print "The tutorial is complete, welcome to The Elder Scrolls 0: Adventurer"
        part3()
        def part4():
            global fight_class
            global strength
            global health
            global intelligence
            global agility
            global fun
            global gold
            global first_weapon
            see_stats = raw_input("Would you like to see your stats? ")
            if see_stats == ("yes"):
                print "health is" + str(health)
                print "strength is" + str(strength)
                print "intelligence is" + str(intelligence)
                print "agility is" + str(agility)
                print "and you have" + str(gold), "gold"
                if see_stats == ("super"):
                    print "fun is" +str(fun)
                part4()
            print "A thief sneaks up behind you with a knife to your throat and demands your money"
            random_event1reaction = raw_input("How do you deal with the thief? Give in? Fight back? Pursuade?  ")
            if random_event1reaction =="Fight back":
                if fight_class == "Assassin":
                    time.sleep(1.75)
                    print "Little does this thief know that you're a trained assassin, you murder him to death and take his money + 80 gold"
                elif strength > 34:
                    print "You easily fight off the bandit! He runs off with grave wounds"
                elif strength > 24:
                    print "After a long fight you defeat the bandit, both of you are very hurt -100 health"
                    health -= 100
                    if health < 1:
                        print "you bled out from your injuries"
                        part4()
                elif agility > 34:
                    print "You happen to be quite the ninja, you quickly draw your", first_weapon, "and snatch the thief up quicker than a cake"
                elif agility > 20:
                    print "You make an attempt to quickly disarm the bandit, it works but you're injured (-10 health) you take the dagger and drive it into the thief's neck  -10 health"
                    health -= 10
                elif intelligence > 34:
                    print "You realize that there is a very steep hill just behind the thief, so you push him down"
                else:
                    print "You wet yourself and the bandit instantly slits your throat out of disgust"
                    time.sleep(1.5)
                    print "you're dead? And from wetting yourself? Get a hold of yourself!!! Go back and do things different!"
                    time.sleep(4)
                    createrace()
            elif random_event1reaction == "Give in":
                print "you were given some money by Capitus, the thief demands it all, you oblige -100 gold"
                gold -= 100
                time.sleep(1.75)
                if agility > 30:
                    print "but being an aspiring thief yourself, you pickpocket his money almost immediately after the thief turns around +250 gold"
                    gold += 250
                elif agility > 18:
                    print "after handing him only a few gold, you break free and sprint away. Good on you coward, but at least you didn't die. - 5 gold"
                else:    
                    print '''The thief says, "Did you really think I'd only ask for your money? No, I want your life as well." He proceeds to slit your throat'''
                    time.sleep(1)
                    print "You died? This was so easy though!!! oh well, go back and maybe you'll learn something useful"
                    time.sleep(4)
                    part4()
            elif random_event1reaction == "pursuade":
                if intelligence > 29:
                    print "You tell the thief about your fake cache of goods, since he's stupid he believes you"
                    time.sleep(0.8)
                    print "you take the opportunity to ambush the thief"
                    if strength > 14:
                        time.sleep(1.3)
                        print "you sucessfully defeat the thief! Nice job! + 20 gold"
                    else:
                        print "You botch the job, both of you go tumbling down a hill, the thief dies, since he landed on his head, you also took quite a bit of damage -40 health"
                else:
                    print "The thief doesn't believe you, so he pushes you down a large hill, lucky for you it's not a necessarily long fall -90 health"
                    if health > 0:
                        print "Even luckier, you survive it"
                    else:
                        print "But you aren't quite lucky enough, so you died"
            else:
                print "Your complicated action is too much for the thief to handle, his head implodes, leaving a mound where his head once was. +10 to a hidden stat."
                fun += 10
                time.sleep(1)
            print "Good job at completing your first random encounter, this one wasn't so random though, so you could go back and take differrent routes to learn more about how random events work."
            time.sleep(2)
            tutorial = raw_input("Would you like to go back? Warning, this will reset all the way back to before you created your race! ")
            if tutorial == ("yes"):
                createrace()
            elif tutorial == ("Yes"):
                createrace()
            elif tutorial == ("Y"):
                createrace()
            elif tutorial == ("No"):
                time.sleep(1)
            elif tutorial == ("no"):
                time.sleep(1)
            else:
                time.sleep(1)
        part4()
        def part5():
            global fight_class
            global strength
            global health
            global intelligence
            global agility
            global fun
            global gold
            global first_weapon
            print ("Having survived your encounter with the thief, you decide to save your progress here, because who wants to go back to the start?")
            time.sleep(1)
            print ("Being an adventurer, you decide you want to do some adventuring.")
            time.sleep(1)
            inventory1 = raw_input ("Before you continue would you like to check your inventory?")
            if inventory1 == "yes":
                print first_weapon
                print fight_class, "'s armor"
                print "you have", str(gold), "gold"
                print "Capitus' letter"
                time.sleep(1)
            elif inventory1 == "Yes":
                print first_weapon
                print fight_class, "'s armor"
                print "you have", str(gold), "gold"
                print "Capitus' letter"
            print ("You decide to read the letter:")
            time.sleep(1.4)
            if fight_class == "2S2C":
              print "You cannot read, however your muslces are able to absorb the knowledge of the letter."
              time.sleep (2)
              print ("Your muscles determine from the letter that your uncle Capitus knows more about your parents' death. He says you will learn more as you continue")
            elif intelligence > 0:
                print ("It says: I know more about your parents' death than I've let on, it was never safe to talk about it in the cabin, continue your path, and it shall be let known.")
            else:
                print "You're too stupid to read, so you continue walking blindly."
                time.sleep(1)
                print "I'm not even sure if this is possible without being 2S2C, and they have their own thing, props to you, so I'll give you a freebie, +10 intelligence"
                intelligence += 10
        part5()
        def part6():
            global fight_class
            global strength
            global health
            global intelligence
            global agility
            global fun
            global gold
            global first_weapon
            print ("part 6 coming soon")
            if random_encounter1 == 10:
                print "bear"
            if random_encounter1 == 11:
                print "EZ money"
            if random_encounter1 == 12:
                print "A new weapon"
            if random_encounter1 == 13:
                print "Training"
            if random_encounter1 == 14:
                print "Near instadeath"
            if random_encounter1 == 15:
                print "Tough bandits"    
            if random_encounter2 == 13:
                print "Training"
            if random_encounter2 == 14:
                print "Near instadeath"
            if random_encounter2 == 15:
                print "Tough bandits"
            if random_encounter2 == 16:
                print "New armor"
            if random_encounter2 == 17:
                print "New armor + gold"    
            if random_encounter2 == 18:
                print "Giant"
            if random_encounter2 == 19:
                print "Baby dragon"    
            if random_encounter2 == 20:
                print "Draugr crypt"
            if random_encounter3 == 17:
                print "New armor + gold"    
            if random_encounter3 == 18:
                print "Giant"
            if random_encounter3 == 19:
                print "Baby dragon"    
            if random_encounter3 == 20:
                print "Draugr Crypt"
            if random_encounter3 == 21:
                print "Portal to oblivion opens"    
            if random_encounter3 == 22:
                print "Dragon"
            if random_encounter3 == 23:
                print "3 Ogres"    
            if random_encounter3 == 24:
                print "Practical instadeath"
            if random_encounter3 == 25:
                print "Massive loot cache, followed by 5 werewolves."
            time.sleep(99999)
        part6()
    while True:
        part2()
while True:
    start = raw_input("press x to start ")
    if start == "x":
        skyrim()
    elif start == "Eseer":
        print "You found a platinum easter egg, Eseer is the greatest mortal being that we know of"
    elif start == "fus ro dah":
        print "Sweet! You found a bronze easter egg, good job! This one was easy, there are still many more"
    elif start == "Fus Ro Dah":
        print "Sweet! You found a bronze easter egg, good job! This one was easy, there are still many more"
    elif start == "sweet mother, sweet mother, send your child unto me, for the sins of the unworthy must be baptized in blood and fear":
        print "By Sithis, you've discovered a silver Easter Egg!" #Audience/others who read this, don't be alarmed, I'm not a murderer, thats a quote from the Dark Brotherhood, a band of assassins in Skyrim"
    elif start == "Sweet mother, sweet mother, send your child unto me, for the sins of the unworthy must be baptized in blood and fear":
        print "By Sithis, you've discovered a silver Easter Egg!"
    else:
        print " "