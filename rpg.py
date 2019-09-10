import random
from items import *


class Character:
    def __init__(self, name, health, power, stats, inv, gil):
        self.name = name
        self.power = power
        self.stats = stats
        self.power = round(power + (stats["Strength"] * .5)) 
        self.defense = round((stats["Constitution"] * .25))
        self.evasion = (stats["Agility"] * .25) / 10

    def dealdamage(self, enemy):
        evade = random.random()
        dmg_amount = self.power - enemy.defense
        


    def attack(self, power, enemy):
        starting_health = enemy.health
        if "weapon" in self.inv.keys():
            weapon = self.inv.get("weapon")
        else:
            weapon = 0
        if enemy == medic:
            recover_health = random.random()
            if recover_health <= .20:
                enemy.health -= (power + weapon.power) - 2
                print("The Medic injects herself with a syringe, which is definitely not usually a good idea, and recovered 2 health!")
            else:
                enemy.health -= (power + weapon.power)
        elif enemy == shadow:
            null_damage = random.random()
            if null_damage <= .10:
                enemy.health -= (power + weapon.power)
                print(f"{shadow.name} took no damage from that attack!")
            else:
                enemy.health -= (power + weapon.power)
        else:    
            enemy.health -= (power + weapon.power)
            return starting_health - enemy.health
    
    def alive(self, health):
        if self.health <= 0:
            return True
    
    def print_status(self, name, health, power):
        print(f"{name} has {health} health and {power} power.")

class Hero(Character):
    def attack(self, power, enemy, inv):
        starting_health = enemy.health
        if "weapon" in inv.keys():
            weapon = self.inv.get("weapon")
        else:
            weapon = 0
        double_damage = random.random()
        if double_damage <= .20:
            critical_hit = power * 2
            enemy.health = enemy.health - critical_hit - weapon.power
            print("CRITICAL HIT!")
            return starting_health - enemy.health
        else:
            enemy.health -= (power + weapon.power)
            return starting_health - enemy.health

class Berserker(Character):
    def dealdamage(self, enemy):
        evade = random.random()
        dmg_amount = self.power - enemy.defense
            
        if evade <= enemy.evasion:
            dmg_amount = 0
            enemy.health = enemy.health
            print(f"{enemy.name} dodged {self.name}'s attack!")
            return dmg_amount

        else:
            if self.health < 15:
                berserking = self.power * 2
                enemy.health -= berserking
                print("Oh God the Berserker has lost too much health and is going nuts! His damage has been doubled!\n")
                return berserking
            else:
                enemy.health -= dmg_amount
                return dmg_amount

hero = Hero("Maximo", 50, 100, 9999, {})
goblin = Character("Goblin", 2, 200, 5,{"weapon": Stick})
medic = Character("Medic", 3, 25, 20, {}) 
shadow = Character("Shadow", 10, 1, 100, {})
zombie = Character("Zombie", 1, 10, 40, {})
berserker = Berserker("Berserker", 10, 30, 70, {})

class Centaur(Character):
    def dealdamage(self, enemy):
        evade = random.random()
        dmg_amount = self.power - enemy.defense
            
        if evade <= enemy.evasion:
            dmg_amount = 0
            enemy.health = enemy.health
            print(f"{enemy.name} dodged {self.name}'s attack!")
            return dmg_amount
        else:
            trample = random.random()
            if trample <= .20:
                trample_damage = self.power * 1.5
                enemy.health -= trample_damage
                print("The Centaur charges at you!")
                return trample_damage
            else:
                enemy.health -= dmg_amount
                return dmg_amount

Humans = {"Strength" : 7, "Agility" : 7, "Constitution" : 7}
Goblins = {"Strength" : 3, "Agility" : 7, "Constitution": 5 }
Demons = {"Strength" : 5, "Agility" : 5, "Constitution" : 0}
Centaurs = {"Strength" : 8, "Agility" : 8, "Constitution" : 5}
Undead = {"Strength" : 2, "Agility" : 5, "Constitution" : 0}
Amorphous = {"Strength" : 5, "Agility" : 30, "Constitution" : 5}
Ogres = {"Strength" : 10, "Agility" : 3, "Constitution" : 8}

hero = Hero("Maximo", 100, 5, Humans, {}, 999)
goblin = Character("Goblin", 20, 2, Goblins, {}, 8)
medic = Character("Medic", 25, 3, Humans, {},75)
shadow = Character("Shadow", 1, 10, Demons, {}, 177)
zombie = Zombie("Zombie", 10, 1,Undead, {}, 10)
berserker = Berserker("Berserker", 30, 10, Humans, {}, 82)
centaur = Centaur("Centaur", 50, 8, Centaurs, {}, 74)
ogre = Character("Ogre", 80, 15, Ogres, {}, 95)
slime = Character("Slime", 25, 5, Amorphous, {}, 143)
frank = Character("Humans", 100, 15, Humans, {}, 1000)

def main():
    print("Welcome to the world of...Frank. Yeah, just Frank. He's some guy. I guess he owns the world or something? Wild. \n\nAnyway. Your name is Maximo. I don't care what it was before, you're 'Maximo now. Hello, Maximo! \n\nOh no! A goblin is minding his own business somewhere. ASSAULT IT!!!\n\n")

    def goblin_battle():    
        while hero.health > 0 and goblin.health > 0:
            goblin.print_status(goblin.name, goblin.health, goblin.power)
            hero.print_status(hero.name, hero.health, hero.power)
            print("")
            print("Type the number of the action you wish to take.")
            print("1. Attack")
            print("2. Wait")
            print("3. Flee")
            print("4. Inventory")
            user_input = input("")
        
            if user_input == "1":
                damage = hero.attack(hero.power, goblin, hero.inv)
                print(f"You've dealt {damage} damage to the {goblin.name}.")
                if goblin.alive(goblin.health):
                    print("The goblin has been murdered. His only crime was being a goblin.")
                    for item in goblin.inv.keys():
                    self.inv.update(Weapon[
                        # update the hero's inventory with that item
                        # this means you need to check for an item of that type (ie "weapon", "armor", etc)
                        # and add/replace that item in the hero's inventory
                        # hero.inv ....
            
            if user_input == "2":
                print(f"You stare at the goblin. Menacingly. You even throw up a gang sign or two. He freaks the fudge out and attacks you out of sheer terror.")
            
            if user_input == "3":
                print(f"Seriously? You're just going to run away? Coward. COWAAAAAAAAAAAAAAAAARD!!!")
                break

            if user_input == "4":
                for item in hero.inv.keys():
                    print(f"{item} : {hero.inv.get(item)}") 

            
            if goblin.health > 0:
                damage = goblin.attack(goblin.power, hero)
                print(f"The goblin does {damage} damage to you!")

    goblin_battle()

    print("-" * 10)

    print("Phew that was a close one. Great job viciously murdering that innocent goblin. He might have a family around here somewhere so let's go tie up loose ends. OH SWEET LORD THERE'S A BERSERKER OVER THERE!\n")
    print("Like...he's not really 'Berserking' right now, but...you know...what if he does? Like yeah, he's gardening *right now*, but when he's finished gardening, then what? You know what I mean? Better kill him to make sure, right? Yeah...yeah...\n")

    # def berserker_battle():
    #     while hero.health > 0 and berserker.health > 0:
    #         berserker.print_status(berserker.name, berserker.health, berserker.power)
    #         hero.print_status(hero.name, hero.health, hero.power)
    #         print("")
    #         print("Type the number of the action you wish to take.")
    #         print("1. Attack")
    #         print("2. Wait")
    #         print("3. Flee")
    #         print("4. Inventory")
    #         user_input = input("")

    #         if user_input == "1":
    #             hero.attack(hero.power, berserker)
    #             print(f"You've dealt {hero.power} to the {berserker.name}.")
    #             if berserker.alive(berserker.health):
    #                 print("The berserker has been slain!")
    #         if user_input == "2":
    #             print("You insult the Berserker's mother and start stomping on his flowers while, for some reason, throwing up gang signs. Unprovoked, the Berserker attacks!")

    #         if user_input == "3":
    #             print("Oh, oh, what?! You murder a goblin in cold blood without a problem but now all of a sudden you have a problem -DEFENDING YOURSELF- against a Berserker? Seriously? What are you, racist against goblins? I don't have time for bigots. Get out of here.")
    #             break
            
    #         if berserker.health > 0:
    #             berserker.attack(berserker.power, hero)
    #             print(f"The {berserker.name} deals {berserker.power} damage to you. ")

    # # berserker_battle()
    
    print("-" * 10)
    print("Oh man that got really scary in the end, huh? Like you could have died, man. I wonder what his problem was, attacking you like that. Good thing you defended yourself and did nothing wrong! \n\nHey, look. A medic. \n\n... \n\n...I -SAID- : \"HEY, LOOK. A MEDIC\". \n\n")

    # def medic_battle():
    #     while hero.health > 0 and medic.health > 0:
    #         medic.print_status(medic.name, medic.health, medic.power)
    #         hero.print_status(hero.name, hero.health, hero.power)
    #         print("")
    #         print("Type the number of the action you wish to take.")
    #         print("1. Attack")
    #         print("2. Wait")
    #         print("3. Flee")
    #         print("4. Inventory")
    #         user_input = input("")

            if user_input == "1":
                print(f"You've dealt {hero.dealdamage(medic)} damage to the {medic.name}.")
                if medic.alive():
                    print("Oh wow you killed her.")
            elif user_input == "2":
                print("Your eyes roll to the back of your head, you start foaming at the mouth and making demonic screeches while walking like a crab and snapping your imaginary claws. The Medic tries to exorcise you, horrified, which is interesting because medics don't typically do exorcism.\n\n")

    #         if user_input == "3":
    #             print("You try to flee like a small, worthless child but the medic tranquilizes you with...a tranquilizer...gun? What time period is this game set in? Let's say it was a dart. Anyway, she hits you with it and then you go to jail or something. Lawyer up, my man.")
    #             break
            
            else:
                print("Nah don't do that. Press 1, 2, or 3.")

            if medic.health > 0:
                print(f"The {medic.name} deals {medic.dealdamage(hero)} damage to you.")
                if hero.alive():
                    print("")
                    print("After finally managing to subdue you, the medic sits on the ground and breathes heavily, unsure of how she actually managed to defeat you. Before she can say anything, you use one last burst of strength to shove her backwards while also stealing her medical bag. Without hesitation, you swallow every pill, potion, and tonic in her inventory, desperate to recover your health. She stares at you in a mixture of horror and intrigue as all your wounds heal and your skin changes a multitude of colors.\n\n'...Are you oka-'\n\nBefore she can finish her inquiry, you explode into glitter and confetti. While a fun and festive display, you are still very much dead. \n")
                    exit()

    medic_battle()

    print("-" *10)
    print("Oh man! What did you do?! No one told you to do that! She's dead, bro! You're a monster! Oh sweet she has some healing potions on her.\n\nYou've stolen...well, can it really be called stealing if it's a corpse? Legally, I think the answer is no. Anywho, 3 healing potions aquired!\n")

    #Add healing potions to inventory, probably with hero.inventory.update({"Potion": Healing Potion}) or something to that effect.
    print("You know what pairs well with senseless murder? Going into town to buy equipment with all that gil you looted from those folks who attacked you. Let's keep it civil for the moment, and put away our weapons. Well, your weapons. I'm a disembodied voice that tells you to do things, so I need weapons about as much as you need psychiatric help. Which is to say, not at all! Onward!")
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
                else:
                    print("You decide to keep wandering around..\n")
                    town()#Should return to town
            
            if decision == "2":#Second option to interact with townspeople| maybe also, play Blackjack cardgame for gil??
                print("You arrive at the tavern of which sign depicts some strange grid-mouthed wooden man only having a barrel-like torso with ribbed appendages, \nonly 3 digets on each hand, hooves and some manner of sprout on his head..\n")
                print("Inside you spot a table of people playing a card game while one suddenly jumps up and exclaims \"BLACKJACK!! \nIll clad individuals beckon passersby in a seedy corner and at the far end the Barkeep. ")
                fork = input("You shrug and head inside. \n1.Approach Barkeep \nReturn. Sit and play cards\n ")
                if fork == "1":
                    exploration +=1
                    print("You have a seat and chat with the Barkeep a while.\n ")
                else:
                    print("You sit and play cards for a while then leave.\n ")
                    town()#Should return to town
            
            if decision == "3":#Shop choice
                print("You wander inside where you see a varied pathora of items adorning the shelves when burly man adorned in a Jester\'s costume with a strange momochrome palette calls you to the counter.")
                print("He looks you up and down and proceeds to flip the open/closed sign and draws the blinds. He then states \"I may be a fool but, business is business.\" as he pulls out a rather large chest from under the counter")
                tree = input("Now, what're ya buyin?\n 1. Potion\n Return. Leave shop\n ")
                if tree == "1":#and gil > item price
                    print("Is that all, Stanger?\n") #item += inv| print("obtained {name.item} you now have %s of them") need dictionary of items to add
                #elif tree == "1": #and gil < item price
                    print("Not enough gil, Stranger!\n") # stops item from being perchased| allows more item selection
                
                    print("Heh, heh, heh... Thank you!!\n")
                    town()#Should return to town
            
            if decision == "4":
                print("Closed for revnovations\n")#Could be used for save feature| try: f = open("sav.txt") print(f.(write()) finally: f.close()
            
            if decision == "5":
                print("You decide to head back out.")
                quit = True
                
            
    # town()#Calls town to open up and be interacted with
                
    #Add healing potions to inventory, probably with hero.inventory.update({"Potion": Healing Potion}) or something to that effect.

    #Town function goes here. Swiggity swooty.
    print("Golly gee, look at you! (assumedly) Armed to the teeth and a thousand-yard stare that'd petrify Medusa herself. Now we can keep venturing forth without worrying about all of the pychopaths on the road who keep attacking you.\n\nWait, wait! Ssssshhhh! Do you hear that? \n\nSounds like a horse...or maybe...A CENTAUR!!! \n\nWATCH OUT! THAT COMPLETELY STATIONARY CENTAUR IS CHARGING RIGHT AT YOU!\n\n")
    
    def centaur_battle():
        while hero.health > 0 and centaur.health > 0:
            print("")
            centaur.print_status()
            hero.print_status()
            print("")
            print("Type the number of the action you wish to take.")
            print("1. Attack")
            print("2. Wait")
            print("3. Flee")
            print("4. Items")
            print(">")
            user_input = input("")

            if user_input == "1":
                print(f"You've dealt {hero.dealdamage(centaur)} damage to the {centaur.name}.")
                if centaur.alive():
                    print("HNNNNGH FEEL THAT ADRENALINE. DRINK HIS BLOOD.")
            elif user_input == "2":
                print("You start screaming. Like, at the top of your lungs, like an absolute lunatic. The centaur tries to run away but you chase him down, still screaming and ripping out clumps of your hair. Like a fugitive on bath salts, you are somehow faster than the horse-person, who has no choice but to attack you.\n\n")

            elif user_input == "3":
                print("")
                print("You walk away. Yeah, man. No surprise twist this time, you just walk away and the battle ends. You return home and put your keys on the table. You kiss your wife on the cheek and ask your daughter how her day at school was. They both scream, which is perfectly reasonable considering you don't have a home, that isn't your wife, and you don't have kids. A large, burly man kicks in the door and demands to know what you're doing there, sword in hand. Curiously, this isn't his house either. A third man comes in through the window and shouts at you both while dual-wielding scimitars. The woman and her daughter stop screaming at this point and look around in confusion, as this third man also doesn't live there. In fact, the woman isn't married and that little girl isn't her daughter. Not only that, but neither of them live in the house. So...whose house is this? Find out in the DLC!")
                exit()
            
            elif user_input == "4":
                #This should be a function that opens the inventory or something.
                pass
            
            else:
                print("Nah don't do that. Press 1, 2, 3, or 4. Yeah, you can press 4 now, so that's nice.")

            if centaur.health > 0:
                print(f"The {centaur.name} deals {centaur.dealdamage(hero)} damage to you.")
                if hero.alive():
                    print("")
                    print("Despite all the gear you (should have) bought, you fall to one knee in defeat. The centaur strides up to your kneeling form, looking into your darkened eyes while calling for medical assistance. His wife and children are watching in the distance, quite disturbed at how this picnic turned out. Yes, you interrupted a picnic. \n\nAs he turns to address them, you remember a fun fact about how if you pull a horse's tail, it will kick you. You reason that while centaurs have many of the same features as horses, they are not the same creatures. Kicking must be the reaction of an animal that reacts purely on instinct, whereas a centaur capable of speech and thought would be able to resist the urge, yes? Tis a shame you left your lab coat and clipboard at home. \n\nIn the pursuit of science, you pull the tail of the centaur, who promptly kicks you in the chin, loudly snapping your neck. As you stare at the scenery behind you and listen to the screams around you, you feel a sense of fulfillment. Science will never forget your sacrifice.")
                    exit()

    centaur_battle()

main()