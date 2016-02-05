#Random Die Generator
import random

def d20():
    x = (random.randint(1,20))
    if (x < 11):
        print (x)
        print ("You miss!")
    elif (x < 19):
        print (x)
        print ("You Hit!")
    else:
        print (x)
        print ("Crit hit!")

def d12():
    x = (random.randint(1,12))
    if (x == 1):
        print (x)
        print ("Minimum Damage")
    elif (x < 11):
        print (x)
        print ("Average Damage")
    else:
        print (x)
        print ("Maximum Damage")

def d10():
    x = (random.randint(1,10))
    if (x == 1):
        print (x)
        print ("Minimum damage")
    elif (x < 9):
        print (x)
        print ("Average damage")
    else:
        print (x)
        print ("Maximum damage")
		
def d8():
    x = (random.randint(1,8))
    if (x == 1):
        print (x)
        print ("Minimum damage")
    elif (x < 7):
        print (x)
        print ("Average damage")
    else:
        print (x)
        print ("Maximum damage")
		
def d6():
    x = (random.randint(1,6))
    if (x == 1):
        print (x)
        print ("Minimum damage")
    elif (x < 5):
        print (x)
        print ("Average damage")
    else:
        print (x)
        print ("Maximum damage")
		
def d4():
    x = (random.randint(1,4))
    if (x == 1):
        print (x)
        print ("Minimum damage")
    elif (x < 3):
        print (x)
        print ("Average damage")
    else:
        print (x)
        print ("Maximum damage")

def roll(prompt, terminate='Thank you, goodbye'):
    while True:
        print ("Rolling d20: ")
        d20()
        print ("\n")
        print ("Rolling d12: ")
        d12()
        print ("\n")
        print ("Rolling d10: ")
        d10()
        print ("\n")
        print ("Rolling d8: ")
        d8()
        print ("\n")
        print ("Rolling d6: ")
        d6()
        print ("\n")
        print ("Rolling d4: ")
        d4()
        print ("\n")
        print ("Do you wish to roll again?: ")
        print ("\n")
        rolls = input()
        if rolls in ('y', 'ye', 'yes'):
            True
        if rolls in ('n', 'no'):
            return False
            print (terminate)


prompt =('y', 'ye', 'yes', 'n', 'no')
print ("\n")
roll(prompt, terminate='Thank you, goodbye')


