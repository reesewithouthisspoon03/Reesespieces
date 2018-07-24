#reese's pieces's first python code, I'll be testing and learning generic python stuff here
for x in range(1, 100):
    if x %5 == 0 and x % 3 == 0:
        print ("FuzzBuzz")
    elif x %3 == 0 : 
        print ("Fuzz")
    elif x %5 == 0: 
        print ("Buzz")
    else:
        print x
