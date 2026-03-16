import time
import random

knows_license_plate = False
license_plate = ""

print("You are a teenager in the United States walking home when suddently a white van aproach you")
time.sleep(2)

name = input("Enter your name: ")

print("Stranger: Hello kid, what is your name?")
time.sleep(2)

print(name + ": im " + name)
time.sleep(2)

print("Stranger: I have candies and puppies. Want to enter my van?")
time.sleep(2)

while True:

    options = ["1. Tell him no", "2. Tell him yes"]
    for opt in options:
        print(opt)
        time.sleep(2)

    try:

        choice = input("Choose 1 or 2: ")
    except:

        print("something failed")
        time.sleep(2)

        continue

    if choice == "1":
        print("You said no so he had not choice but force you forces you.")
        time.sleep(2)

        break

    elif choice == "2":
        print("You said yes you said yes so you follow the stranger")
        time.sleep(2)

        break

    else:
        print("Type 1 or 2 only")
        time.sleep(2)

print("suddenly everything goes black")
time.sleep(2)

print("You wake up being dragged by the stranger.")
time.sleep(2)

while True:

    options = ["1. Scream for help", "2. Stay silent and watch your nearbys", "3. Attack the stranger"]
    for opt in options:

        print(opt)
        time.sleep(2)

    try:

        wake = input("Choose 1, 2, or 3: ")

    except:

        print("something failed")
        time.sleep(2)

        continue

    if wake == "1":

        print("You scream and the stranger with a liquid smell he put you uncuncious.")
        time.sleep(2)
    
        print("then when you are concious because of your bad behavior he ties you 10 times harder than he was about to")
        time.sleep(3)
        
        print("ultimately you cant escape.")
        time.sleep(2)

        print("you lose")

        quit()
    elif wake == "2":

        print("You stay silent and see the license plate. it was JAM607")
        time.sleep(2)

        knows_license_plate = True
        license_plate = "JAM607"

        break

    elif wake == "3":

        print("You attack but he remains firm and with the smell of a liquid he puts you unconcious.")
        time.sleep(3)

        print("because of your bad behaviour he decided to yie you 10x harder and have more vigilance on you.")

        print("ultimately you cant escape")

        print("you lose.")
        quit()

    else:

        print("only thoes number")
        time.sleep(2)

print("You wake up tied in a room.")
time.sleep(2)

print("you notice that the ties are not hard and you know you can escape")
time.sleep(3)

print("you notice that you can escape")
time.sleep(2)

print("what are you doing now")
time.sleep(2)
while True:

    for opt in ["1. Pretend tied and make a plan", "2. run and try to escape the stranger "]:
        time.sleep(3)

        print(opt)
        time.sleep(2)

    try:

        escape = input("Choose 1 or 2: ")

    except:

        print("something failed")
        time.sleep(2)

        continue

    if escape == "1":

        print("You wait patiently and make a plan.")
        time.sleep(2)

        break

    elif escape == "2":

        print("you trie to escape but the stranger finds you and catch you")
        time.sleep(2)

        print("you lose")
        time.sleep(3)
        quit()

    else:

        print("Only 1 or 2")
        time.sleep(2)
print("eventualy he comes towards you")
time.sleep(3)

print("He gives you food, a knife, and a fork.")
time.sleep(2)

print("what do you take")
time.sleep(3)
while True:
    
    for opt in ["1. Take fork", "2. Take knife"]:
        print(opt)
        time.sleep(2)

    try:

        weapon = input("Choose 1 or 2: ")
    except:

        print("something failed")
        time.sleep(2)

        continue

    if weapon == "1":

        print("You hide the fork inside your pocket.")
        time.sleep(2)

        break

    elif weapon == "2":

        print("You cut yourself with the knife and you start screaming in pain")
        time.sleep(2)

        print("you lose")
        quit()

    else:

        print("invalid")
        time.sleep(2)
print("after the stranger left you decide to explore")
time.sleep(3)

print("after some explore you find somw items that can be useful for the future")

print(" you can only use 3 items, not 2 or more same items and there is an incorrect one so be aware of the things you choose.")
time.sleep(4)
print("Items available:")
time.sleep(2)

items = ["dog food", "sharp pencil", "ruler", "flute"]
for i in items:

    print(i)
    time.sleep(2)

items_picked = 0

bad_flute = False

picked_items = ""

while True:

    try:

        item = input("Pick item or q: ").lower()

    except:

        print("something failed")
        time.sleep(2)

        continue

    if item == "q":

        break

    if item in picked_items:

        print("You already picked that item")
        time.sleep(2)

        continue

    if item == "flute":

        bad_flute = True
    elif item not in items:

        print("That item doesn't exist")
        time.sleep(2)

        continue

    picked_items = picked_items + item
    items_picked = items_picked + 1

    print("Item picked")
    time.sleep(2)

    if items_picked > 3:
        print("Too many items. Something bad will happen.")
        time.sleep(2)

if items_picked != 3:
    print("You did not pick exactly 3 items and you are lacking of material to win or you choose more items than you should. you lose.")
    time.sleep(4)
    quit()

if bad_flute:
    print("The flute makes noise. You lose.")
    time.sleep(2)
    quit()

print("Night falls. You use your fork to make a hole in the door and escape")
time.sleep(2)

print("you escape the basement")
print("A guard dog blocks your path.")
time.sleep(2)

while True:

    for opt in ["1. Attack the dog in order to escape", "2. Use dog food to distract the dog and escape"]:

        print(opt)
        time.sleep(2)

    try:

        dog = input("Choose 1 or 2: ")

    except:
        print("something failed")
        time.sleep(2)

        continue

    if dog == "1":

        print(" the dog barks and the stranger hears that and catches you.")
        time.sleep(3)
        quit()

    elif dog == "2":

        print("Dog eats the food and he is distracted. You sneak past the dog without noises.")
        time.sleep(2)

        break

    else:
        print("choose 1 or 2")
        time.sleep(2)

print("Final boss appears")
time.sleep(2)

while True:

    for opt in ["1. Hide around the house", "2. Stab the stranger with the sharp pencil"]:

        print(opt)
        time.sleep(2)

    try:

        final = input("Choose 1 or 2: ")

    except:
        print("something failed")
        time.sleep(2)

        continue

    if final == "1":

        print("you find a good spot but is not useful because the stranger knows all the spots and he eventually finds you. You lose.")
        time.sleep(4)
        quit()
    elif final == "2":

        print("You stab him and run the exit")
        time.sleep(2)

        break

    else:

        print("invalid")
        time.sleep(2)
print("then when you are about to exit the stranger tries to grab you")
time.sleep(3)

print("you are going to press 'ENTER' in order to roll a number and if you get from 1 to 2 you get fails but if you get from 3 to 6 you get some doges and ultimately escaping.")
time.sleep(5)
dodges = 0
fails = 0

while True:

    input("Press 'ENTER' to dodge")

    roll = random.randint(1, 6)

    print("Roll:", roll)
    time.sleep(2)

    if roll <= 2:

        fails += 1

        print("Fail")
    else:
        dodges += 1
        print("Dodge")

    time.sleep(2)
    print("Dodges:", dodges, "/4 | Fails:", fails, "/2")
    time.sleep(2)

    if fails == 2:

        print("He catches you and drag you to the basement.")
        time.sleep(2)

        print("you lose.")
        quit()

    if dodges == 4:

        break

print("You reach the police station.")
time.sleep(2)

if knows_license_plate:

    print("then you report the license plate:", license_plate)
    time.sleep(2)

    print("Good ending")

else:

    print("No evidence.")
    time.sleep(2)

    print("unsatisfied ending")
time.sleep(2)

print("Congrats, you win.")
time.sleep(2)
