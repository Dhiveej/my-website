import random
while True:
    try:
        choice =int(input("GUESS THE NUMBER BETWEEN 1 AND 100 : "))
    except ValueError :
        print ("INVALID OUTPUT")
        continue
    c1=random.randint(1,100)
    if choice - c1 > 25 :
        print ("TOO HIGH")
    elif c1 - choice > 25:
        print ("TOO LOW ")
    elif c1 - choice > 10:
        print (" HIGH")
    elif choice -c1 > 10:
        print ("LOW")
    else :
        print ("CONGRATULATIONS ! U HAVE GUESSED THE NUMBER")
        break