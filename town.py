from rpg import hero

def town():#The currently broken structure of which to access the town interface
    print("You can see familliar structures in the distance and start off toward them.")
    input("Press \'Return'")
    exploration = 0
    quit = False

    while not quit:
        print("You\'re at Rie.")
        print("1. Meander for a while.")
        print("2. Visit Bender\'s Tavern.")
        print("3. Visit The Jester\'s Emporium.")
        print("4. Visit inn.")
        print("5. leave this place")
        print("\n")
        print("Now, what would you like to do?\n ")
        decision = input("")
        
        if decision == "1":#Option to speak with villagers| hopefully also, events to get items and gil
            fork = input("You arrive at the Rie Square! There is a boy on a soap-box that\'s grabbed your attention. \n1. Interact\n Return. Continue strolling\n ")
            if fork == "1":
                exploration +=1
                print("You argue passionately until a crowd forms. Then knock over the box and in the confusion \'borrowed\' some loose change.\n ") # {name.gil} += 21 print("you now have %s gil!")
                hero.inv["Gil"] += 21
                print(f"You stole 21 gil, giving you a total of {hero.inv['Gil']} Gil.\n\n")
            else:
                print("You decide to keep wandering around..\n")
                town()#Should return to town
        
        if decision == "2":#Second option to interact with townspeople| maybe also, play Blackjack cardgame for gil??
            print("You arrive at the tavern of which sign depicts some strange grid-mouthed wooden man only having a barrel-like torso with ribbed appendages, \nonly 3 digits on each hand, hooves and some manner of sprout on his head..\n")
            print("Inside you spot a table of people playing a card game while one suddenly jumps up and exclaims \"BLACKJACK!! \nIll clad individuals beckon passersby in a seedy corner and at the far end the Barkeep. ")
            fork = input("You shrug and head inside. \n1.Sit and play cards \nReturn. Approach Barkeep\n ")
            if fork == "1":
                print("You sit and make outlandish taunts and brags to the VERY visibly champion; challenging him to a one on one.\n ")
                #blackjack()
                #town()
            else:
                print("You have a seat and the Barkeep introduces himself as \"B.B Rodriguez\" named after the Tavern\'s founder. Maximo, grimaces and does the same then proceeds sit upon the stool.\n  After getting a drink, he begins to spin tales; \'alternative\' versions of your recent events. A enamored crowd draws story, after story. Now, after several drinks being filled to satisfaction,\n You \'accidentally\' knock over your drink starting a quarrel that erupts into a brawl!\n You slip out during the confusion with a smirk on your face then snicker and mubble to yourself \'Heh, heh... every time.")
                town()#Should return to town
        
        if decision == "3":#Shop choice
            print("You wander inside where you see a varied pathora of items adorning the shelves when burly man adorned in a Jester\'s costume with a strange momochrome palette calls you to the counter.")
            print("He looks you up and down and proceeds to flip the open/closed sign and draws the curtians. He then states \"I may be a fool but, business is business.\" as he pulls out a rather large chest from under the counter")
            tree = input("Now, what're ya buyin?\n 1. Potion\n Return. Leave shop\n ")
            if tree == "1":#and gil > item price
                print("Is that all, Stanger?\n") #item += inv| print("obtained {name.item} you now have %s of them") need dictionary of items to add
            #elif tree == "1": #and gil < item price
                #print("Not enough gil, Stranger!\n") # stops item from being perchased| allows more item selection
            
                print("Heh, heh, heh... Thank you!!\n")
                town()#Should return to town
        
        if decision == "4":
            print("The sign on the door reads: \"Closed for revnovations\" You scoffed and barge in anyway.\n Oh,! I'm terribly sorry sir, we\'re currently spring cleaning and updating rooms! You stare back blankly.")
            fork = input("1. To Save \n Return. Take a hint")
            if fork == "1":
                print("You decide to ignore them and push past locking yourself into a freshly remade room.\n")
                hero.health = 100
                pickle.dump(hero, open("sav.dat", "wb"))#HERO STATUS REPLACES "BLANK!!"
                input("...\n")
                print("Ahhh..! You slept like a log!\n")
                hero.print_status()
            
            else:
                print("You silently turn around and leave..\n")
                town()
        if decision == "5":
            print("You decide to head back out.")
            quit = True