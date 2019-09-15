import random
from items import *
import pickle
import os
class Character:
    def __init__(self, name, health, power, stats, inv):
        self.name = name
        self.health = health
        self.stats = stats
        self.inv = inv
        self.power = round(power + (stats["Strength"] * .5)) + (self.inv["Weapon"]) #Takes base power and adds half of strength stat and damage value of weapon
        self.defense = round((stats["Constitution"] * .25) + (self.inv["Armor"] / 2))
        self.evasion = (stats["Agility"] * .25) / 10
        

    def dealdamage(self, enemy):
        #factors in evasion, power, and defense to calculate if an attack hit, and how much damage it does
        evade = random.random()
        dmg_amount = self.power - enemy.defense
        if dmg_amount < 0:
                dmg_amount = 0
                
        if evade <= enemy.evasion:
            dmg_amount = 0
            enemy.health = enemy.health
            print(f"{enemy.name} dodged the attack!")
            return dmg_amount

        else:
            enemy.health -= dmg_amount
        return dmg_amount

    def print_status(self):
        print(f"{self.name} has {self.health} health, {self.power} power, and {self.defense} defense.")

    def alive(self):
        if self.health <= 0:
            return True
    
    def defeated(self,enemy): #If the enemy's weapon is stronger than yours, takes enemy's weapon. Same thing for armor. Inherits gil amount.
        if self.inv["Weapon"] > enemy.inv["Weapon"]:
            pass
        else:
            self.power += enemy.inv["Weapon"]

        if self.inv["Armor"] > enemy.inv["Armor"]:
            pass
        else:
            self.inv["Armor"] += enemy.inv["Armor"]
        self.inv["Gil"] += enemy.inv["Gil"]

    def use_potion(self):
        self.health += 25
        print("You've recovered 25 health, you wimp. What, can't beat your enemy without healing? Disgusting.")

class Hero(Character):
        def dealdamage(self,enemy):
            evade = random.random()
            dmg_amount = self.power - enemy.defense
            
            if enemy == shadow:
                enemy.evasion = .9
                if evade <= enemy.evasion:
                    dmg_amount = 0
                    enemy.health = enemy.health
                    print(f"{enemy.name} dodged {self.name}'s attack!")
                    return dmg_amount
                else:
                    if dmg_amount < 0:
                        dmg_amount = 0
                    critical_hit = random.random()
                    if critical_hit <= .20:
                        critical = (self.power * 2) - enemy.defense
                        enemy.health -= critical            
                        print("CRITICAL HIT!")
                        return critical

                    elif critical_hit > .20:
                        enemy.health -= dmg_amount
                        return dmg_amount

            elif evade <= enemy.evasion:
                dmg_amount = 0
                enemy.health = enemy.health
                print(f"{enemy.name} dodged {self.name}'s attack!")
                return dmg_amount

            else:
                if dmg_amount < 0:
                    dmg_amount = 0
                critical_hit = random.random()
                if critical_hit <= .20:
                    critical = (self.power * 2) - enemy.defense
                    enemy.health -= critical            
                    print("CRITICAL HIT!")
                    return critical

                elif critical_hit > .20:
                    enemy.health -= dmg_amount
                    return dmg_amount

class Berserker(Character):
    def dealdamage(self, enemy):
        evade = random.random()
        dmg_amount = self.power - enemy.defense
        if dmg_amount < 0:
                dmg_amount = 0    
        if evade <= enemy.evasion:
            dmg_amount = 0
            enemy.health = enemy.health
            print(f"{enemy.name} dodged {self.name}'s attack!")
            return dmg_amount

        else:
            if self.health < 10:
                berserking = round(self.power * 1.25)
                #Increases Berserker's damage when his health goes below 10
                enemy.health -= berserking
                print("Oh God the Berserker has lost too much health and is going nuts! His damage has increased by 25%!\n")
                return berserking
            else:
                enemy.health -= dmg_amount
                return dmg_amount

class Centaur(Character):
    def dealdamage(self, enemy):
        evade = random.random()
        dmg_amount = self.power - enemy.defense
        if dmg_amount < 0:
                dmg_amount = 0    
        if evade <= enemy.evasion:
            dmg_amount = 0
            enemy.health = enemy.health
            print(f"{enemy.name} dodged {self.name}'s attack!")
            return dmg_amount
        else:
            #Centaur has a 20% chance to use a special skill
            trample = random.random()
            if trample <= .20:
                trample_damage = self.power * 1.5
                enemy.health -= trample_damage
                print("The Centaur charges at you!")
                return trample_damage
            else:
                enemy.health -= dmg_amount
                return dmg_amount

class Zombie(Character):
    def alive(self):
        if self.health <= 0:
            return False

Humans = {"Strength" : 7, "Agility" : 7, "Constitution" : 7}
Goblins = {"Strength" : 3, "Agility" : 7, "Constitution": 5 }
Demons = {"Strength" : 5, "Agility" : 5, "Constitution" : 0}
Centaurs = {"Strength" : 8, "Agility" : 8, "Constitution" : 5}
Undead = {"Strength" : 2, "Agility" : 5, "Constitution" : 0}
Amorphous = {"Strength" : 5, "Agility" : 30, "Constitution" : 5}
Ogres = {"Strength" : 10, "Agility" : 3, "Constitution" : 8}

hero = Hero("Maximo", 100, 10, Humans, {"Weapon": Unarmed.attack, "Armor": Leather_Jerkin.defense, "Gil": 999})
goblin = Character("Goblin", 20, 2, Goblins, {"Weapon": Stick.attack, "Armor": Tattered_Cloth.defense, "Gil": 8})
medic = Character("Medic", 25, 3, Humans, {"Weapon": Scalpel.attack, "Armor": Medical_Garb.defense, "Gil": 75})
shadow = Character("Shadow", 1, 10, Demons, {"Weapon": Shadow_Blade.attack, "Armor": Fortified_Darkness.defense, "Gil":177})
zombie = Zombie("Zombie", 10, 1, Undead, {"Weapon": Spooky_Hands.attack, "Armor": Tattered_Cloth.defense, "Gil":10})
berserker = Berserker("Berserker", 30, 8, Humans, {"Weapon": Great_Axe.attack, "Armor": Iron_Pauldrons.defense,"Gil":82})
centaur = Centaur("Centaur", 50, 8, Centaurs, {"Weapon": Bladed_Spear.attack, "Armor": Iron_Pauldrons.defense,"Gil":78})
ogre = Character("Ogre", 80, 15, Ogres, {"Weapon": Flaming_Hammer.attack, "Armor": Iron_Pauldrons.defense, "Gil":95})
slime = Character("Slime", 25, 5, Amorphous, {"Weapon": Slimy_Tendrils.attack, "Armor": Slime.defense, "Gil":143})
frank = Character("Humans", 100, 15, Humans, {"Weapon": Excalibur.attack, "Armor": Gold_Body_Armor.defense,"Gil":1000})

def main():
    print("Welcome to the world of...Frank. Yeah, just Frank. He's some guy. I guess he owns the world or something? Wild. \n\nAnyway. Your name is Maximo. I don't care what it was before, you're 'Maximo now. Hello, Maximo! \n\nOh no! A goblin is minding his own business somewhere. ASSAULT IT!!!\n\n")

    def goblin_battle():    
        while hero.health > 0 and goblin.health > 0:
            print("")
            goblin.print_status()
            hero.print_status()
            print("\nType the number of the action you wish to take.")
            print("1. Attack")
            print("2. Wait")
            print("3. Flee")
            print("4. Use Health Potion")
            print(">")
            user_input = input("")
        
            if user_input == "1":
                print(f"You've dealt {hero.dealdamage(goblin)} damage to {goblin.name}.")
                if goblin.alive():
                    hero.defeated(goblin)
                    print("The goblin has been murdered. His only crime was being a goblin. You've picked up the Goblin's stick!" )
            
            elif user_input == "2":
                print(f"You stare at the goblin. Menacingly. You even throw up a gang sign or two. He freaks the fudge out and attacks you out of sheer terror.")
            
            elif user_input == "3":
                print(f"Seriously? You're just going to run away? Coward. COWAAAAAAAAAAAAAAAAARD!!!")
                exit()

            elif user_input == "4":
                hero.use_potion()

            else:
                print("Hey bud. That wasn't one of the options you were given. Learn the rules!")

            if goblin.health > 0:
                print(f"The goblin does {goblin.dealdamage(hero)} damage to {hero.name}!")
                if hero.alive():
                    print("")
                    print("Oh wow you died. No one could have seen that coming. That's actually pretty amazing considering this is the first encounter.\n I guess you wanted to see all the different dialogue. Never forget that you deserve to be happy. If you're not happy now, I hope you will be one day.")
                    exit()
    

    goblin_battle()

    print("-" * 10)

    print("Phew that was a close one. Great job viciously murdering that innocent goblin. He might have a family around here somewhere so let's go tie up loose ends. OH SWEET LORD THERE'S A BERSERKER OVER THERE!\n")
    print("Like...he's not really 'Berserking' right now, but...you know...what if he does? Like yeah, he's gardening *right now*, but when he's finished gardening, then what? You know what I mean? Better kill him to make sure, right? Yeah...yeah...\n")

    def berserker_battle():
        while hero.health > 0 and berserker.health > 0:
            print("")
            berserker.print_status()
            hero.print_status()
            print("\nType the number of the action you wish to take.")
            print("1. Attack")
            print("2. Wait")
            print("3. Flee")
            print("4. Use Health Potion")
            print(">")
            user_input = input("")

            if user_input == "1":
                print(f"You've dealt {hero.dealdamage(berserker)} damage to the {berserker.name}.")
                if berserker.alive():
                    hero.defeated(berserker)
                    print("The berserker has been slain!")
            elif user_input == "2":
                print("You insult the Berserker's mother and start stomping on his flowers while, for some reason, throwing up gang signs. Unprovoked, the Berserker attacks!")

            elif user_input == "3":
                print("Oh, oh, what?! You murder a goblin in cold blood without a problem but now all of a sudden you have a problem -DEFENDING YOURSELF- against a Berserker? Seriously? What are you, racist against goblins? I don't have time for bigots. Get out of here.")
                exit()

            elif user_input == "4":
                hero.use_potion()

            else:
                print("Oh boy. That's not one of the options you were given and yet you did it anyway. So uh...don't do that.")

            if berserker.health > 0:
                print(f"The {berserker.name} deals {berserker.dealdamage(hero)} damage to you. ")
                if hero.alive():
                    print("")
                    print("\nWith your health depleted, the Berserker goes to help you up in hopes that you will explain any misunderstandings. Unfortunately he trips over one of the holes in his garden and decapitates you with his axe as he falls. So uh...yeah, you dead.")
                    exit()
                    


    berserker_battle()
    
    print("-" * 10)
    print("Oh man that got really scary in the end, huh? Like you could have died, man. I wonder what his problem was, attacking you like that. Good thing you defended yourself and did nothing wrong! \n\nHey, look. A medic. \n\n... \n\n...I -SAID- : \"HEY, LOOK. A MEDIC\". \n\n")

    def medic_battle():
        while hero.health > 0 and medic.health > 0:
            print("")
            medic.print_status()
            hero.print_status()
            print("\nType the number of the action you wish to take.")
            print("1. Attack")
            print("2. Wait")
            print("3. Flee")
            print("4. Use Health Potion")
            print(">")
            user_input = input("")

            if user_input == "1":
                print(f"You've dealt {hero.dealdamage(medic)} damage to the {medic.name}.")
                if medic.alive():
                    hero.defeated(medic)
                    print("Oh wow you killed her.")
            elif user_input == "2":
                print("Your eyes roll to the back of your head, you start foaming at the mouth and making demonic screeches while walking like a crab and snapping your imaginary claws. The Medic tries to exorcise you, horrified, which is interesting because medics don't typically do exorcism.\n\n")

            elif user_input == "3":
                print("\nYou try to flee like a small, worthless child but the medic tranquilizes you with...a tranquilizer...gun? What time period is this game set in? Let's say it was a dart. Anyway, she hits you with it and then you go to jail or something. Lawyer up, my man.")
                exit()

            elif user_input == "4":
                hero.use_potion()

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
            decicion = input("")
            
            if decicion == "1":#Option to speak with villagers| hopefully also, events to get items and gil
                fork = input("You arrive at the Rie Square! There is a boy on a soap-box that\'s grabbed your attention. \n1. Interact\n Return. Continue strolling\n ")
                if fork == "1":
                    exploration +=1
                    print("You argue passionately until a crowd forms. Then knock over the box and in the confusion \'borrowed\' some loose change.\n ") # {name.gil} += 21 print("you now have %s gil!")
                else:
                    print("You decide to keep wandering around..\n")
                    town()#Should return to town
            
            if decicion == "2":#Second option to interact with townspeople| maybe also, play Blackjack cardgame for gil??
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
                           
            if decicion == "3":#Shop choice
                print("You wander inside where you see a varied pathora of items adorning the shelves when burly man adorned in a Jester\'s costume with a strange momochrome palette calls you to the counter.")
                print("He looks you up and down and proceeds to flip the open/closed sign and draws the curtians. He then states \"I may be a fool but, business is business.\" as he pulls out a rather large chest from under the counter")
                tree = input("Now, what're ya buyin?\n 1. Potion\n Return. Leave shop\n ")
                if tree == "1":#and gil > item price
                    print("Is that all, Stanger?\n") #item += inv| print("obtained {name.item} you now have %s of them") need dictionary of items to add
                #elif tree == "1": #and gil < item price
                    print("Not enough gil, Stranger!\n") # stops item from being perchased| allows more item selection
                
                    print("Heh, heh, heh... Thank you!!\n")
                    town()#Should return to town
            
            if decicion == "4":
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
            
            if decicion == "5":
                print("You decide to head back out.")
                quit = True
                main()
            
    town()#Calls town to open up and be interacted with
                
                
    #Add healing potions to inventory, probably with hero.inventory.update({"Potion": Healing Potion}) or something to that effect.

    #Town function goes here. Swiggity swooty.
    print("\nGolly gee, look at you! (assumedly) Armed to the teeth and a thousand-yard stare that'd petrify Medusa herself. Now we can keep venturing forth without worrying about all of the pychopaths on the road who keep attacking you.\n\nWait, wait! Ssssshhhh! Do you hear that? \n\nSounds like a horse...or maybe...A CENTAUR!!! \n\nWATCH OUT! THAT COMPLETELY STATIONARY CENTAUR IS CHARGING RIGHT AT YOU!\n\n")
    
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
            print("4. Use Health Potion")
            print(">")
            user_input = input("")

            if user_input == "1":
                print(f"You've dealt {hero.dealdamage(centaur)} damage to the {centaur.name}.")
                if centaur.alive():
                    hero.defeated(centaur)
                    print("HNNNNGH FEEL THAT ADRENALINE. DRINK HIS BLOOD.")
            elif user_input == "2":
                print("You start screaming. Like, at the top of your lungs, like an absolute lunatic. The centaur tries to run away but you chase him down, still screaming and ripping out clumps of your own hair. Like a fugitive on bath salts, you are somehow faster than the horse-person, who has no choice but to attack you.\n\n")

            elif user_input == "3":
                print("")
                print("You walk away. Yeah, man. No surprise twist this time, you just walk away and the battle ends. You return home and put your keys on the table. You kiss your wife on the cheek and ask your daughter how her day at school was. They both scream, which is perfectly reasonable considering you don't have a home, that isn't your wife, and you don't have kids. A large, burly man kicks in the door and demands to know what you're doing there, sword in hand. Curiously, this isn't his house either. A third man comes in through the window and shouts at you both while dual-wielding scimitars. The woman and her daughter stop screaming at this point and look around in confusion, as this third man also doesn't live there. In fact, the woman isn't married and that little girl isn't her daughter. Not only that, but neither of them live in the house. So...whose house is this? Find out in the DLC!")
                exit()
            
            elif user_input == "4":
                hero.use_potion()
                
            
            else:
                print("Nah don't do that. Press 1, 2, 3, or 4.")

            if centaur.health > 0:
                print(f"The {centaur.name} deals {centaur.dealdamage(hero)} damage to you.")
                if hero.alive():
                    print("")
                    print("Despite all the gear you (should have) bought, you fall to one knee in defeat. The centaur strides up to your kneeling form, looking into your darkened eyes while calling for medical assistance. His wife and children are watching in the distance, quite disturbed at how this picnic turned out. Yes, you interrupted a picnic. \n\nAs he turns to address them, you remember a fun fact about how if you pull a horse's tail, it will kick you. You reason that while centaurs have many of the same features as horses, they are not the same creatures. Kicking must be the reaction of an animal that reacts purely on instinct, whereas a centaur capable of speech and thought would be able to resist the urge, yes? Tis a shame you left your lab coat and clipboard at home. \n\nIn the pursuit of science, you pull the tail of the centaur, who promptly kicks you in the chin, loudly snapping your neck. As you stare at the scenery behind you and listen to the screams around you, you feel a sense of fulfillment. Science will never forget your sacrifice.")
                    exit()

    centaur_battle()

    print("\n\n With a swift swing of your...whatever weapon you're using at this point, the Centaur draws his last breath. His screaming family flee the scene...screaming. You're doing great, Maximo! All these demented subhumans keep attacking you and you're just putting them down, bro. You know what this calls for? A stroll into the local cementary! Let's geddit!\n\nYou enter the cementary, listening to me without question for some strange reason. Probably because I'm your only ally in this cruel world, right? We've got each other's backs, you and I. Although I have no back, being a disembodied voice and all.\n\nLOOK OVER THERE! IT'S...oh it's just a zombie. I mean, it's already dead and quite unintelligent so there's no real need to-")
    print("\n\"Good day ol' chaps! I say, what a marvelous day it is for a stroll! I should visit Reginald and his marvelous garden!\"")
    print("\nOH NO! This zombie is sentient, intelligent, and most digustingly of all, British! Or whatever this world's equivalent of British is. Does everyone here speak some variation of like, Old English or something? Doesn't matter. KILL IT!")

    def zombie_battle():
        while hero.health > 0 and zombie.health != 0:
            print("")
            zombie.print_status()
            hero.print_status()
            print("\nType the number of the action you wish to take.")
            print("1. Attack")
            print("2. Wait")
            print("3. Flee")
            print("4. Use Health Potion")
            print("5. Throw Health Potion at Zombie")
            print(">")
            user_input = input("")
        
            if user_input == "1":
                print(f"You've dealt {hero.dealdamage(zombie)} damage to {zombie.name}.")
            
            elif user_input == "2":
                print(f"You start doing whatever the dance from the Thriller video is called. In zombie culture, this is considered appropriation or something, and is one of the most offensive things you, as a flesh-person, can do toward the undead. With renewed vigor, the zombie attacks you like he means it.")
            
            elif user_input == "3":
                print(f"You turn to run, but you have the ankles of a player in the NBA so the aforementioned ankles snap. As you fall to the ground, you try to catch yourself with your hands out, but that NBA player bone structure strikes again, so both of your wrists snap. Offended by your lack of calcium, a skellington bursts out of the ground and starts extracting your skeleton from your body, desperate to save your bones from your abusive flesh. I won't go into detail as to how painful it is, but man is it painful. In a strange turn of events, however, you're not dead. Like, you're undead, yeah, but you're still like...moving around. Just, as a skellington. Which is honestly not bad since you have all the support of your skelly bros. For once in your miserable life, you've found a group of...creatures, that care about you.")
                exit()

            elif user_input == "4":
                hero.use_potion()
            
            elif user_input == "5":
                zombie.health = 0
                hero.defeated(zombie)
                print("You douse the zombie with a health potion. He stares at you in shock, or maybe it just appears that way because his jaw unhinges itself. His skin starts to bubble and smoke,and a puddle of melted, rotten flesh begins to form below him. He's actually quite pleasant throughout the entire process, reasoning that this misunderstanding of hostility was probably his fault, and this is only to be expected. How disgustingly British of him.")
            else:
                print("Hey bud. That wasn't one of the options you were given. Learn the rules!")

            if zombie.health != 0:
                print(f"The zombie does {zombie.dealdamage(hero)} damage to {hero.name}!")
                if hero.alive():
                    print("")
                    print("You lost to a zombie. How does one lose to a zombie? And not just any zombie, but a -BRITISH- zombie? Ugh. \n\nThe zombie strolls up to you in his tattered British attire, and produces a pipping hot cuppa. For you non-Brits, I think that's what they call cups of tea. It's abbreviated out of sheer laziness and selfishness. Your nationality is a mystery, but you refuse the cuppa, slapping it out of his rotting hands.\n\n\"How dare you?! How...DARE YOU?! HOW DARE YOU?!\"\n\nThe posh zombie begins to foam at the mouth, his eyes glowing with a crimson mist. He tackles you to the ground and sinks his yellowed teeth into your jugular before ripping it out entirely. As your drown from your own blood filling your lungs, the last thing you hear is him apologizing. Maybe he was Canadian?\n\n")
                    exit()
    zombie_battle()

    print("Before you have a moment to recover from your most recent spat, you are surrounded by pitch darkness. No matter how hard you stare into the abyss, you can't make out any figures. However...you feel the abyss stare back.\n\nA patch of obsidian shadow erupts with power, 'lighter' shadows coalescing at its 'feet' while piercing white eyes glow from the 'head' of this spectral pillar. Your surroundings are still pitch black, but this figure is inexplicably darker, with an emanating aura of dread that chills your very soul. A wicked blade of shadow forms in the creatures 'hands', seconds before it springs to attack.")

    def shadow_battle():
        while hero.health > 0 and shadow.health > 0:
            print("")
            shadow.print_status()
            hero.print_status()
            print("\nType the number of the action you wish to take.")
            print("1. Attack")
            print("2. Wait")
            print("3. Flee")
            print("4. Use Health Potion")
            print(">")
            user_input = input("")
        
            if user_input == "1":
                print(f"You've dealt {hero.dealdamage(shadow)} damage to {shadow.name}.")
                if shadow.alive():
                    hero.defeated(shadow)
                    print("No matter how many times you strike at the Shadow, your blade seems to glide through it's aetherial form. It is almost as if the Shadow is dispersing at the beginning of your strike, and reforming as it passes. Your attacks become uncoordinated and desperate while your body becomes bloodied and bruised, your veins turning black each time the spectral blade lands. In fact, it seems like the horrifying being's weapon is the only definite part of its anatomy. With your mind racing and not a second to spare, you leap backwards as the creature strikes horizontally at you. Mustering up your remaining strength, you bring your weapon down as hard you can on its blade as the attack passes you. With a sharp crack, the Shadow's sword splits in two. Tormented souls scream forth from the cracks as they travel along the blade, creating light on the otherwise obsidian surface. The Shadow itself howls in agony as the cracks continue to travel across the surface of the otherworldly horror's 'body'. Finally, the pressure of the exiting souls becomes too great, and the entire pitch black area around you shatters into luminous light.")
            
            elif user_input == "2":
                print(f"There is no humor to be had in this bout. Your very existence is on the line. The Shadow takes advantage of your faltering willpower and attacks.")
            
            elif user_input == "3":
                print(f"Run? And where, pray tell, are you running? You are surrounded by infinite darkness. The moment it takes to ponder this causes you to drop your defenses, leaving ample time for the Shadow to run you through with its blade. The shadows of the blade spread through your veins, consuming your very soul and converting your physical essence into darkness. With its blade now stronger, the Shadow vanishes as quickly as it came, leaving no trace of the battle that occured, nor the poor soul who fell as a result.")
                exit()

            elif user_input == "4":
                hero.use_potion()

            else:
                print("Hey bud. That wasn't one of the options you were given. Learn the rules!")

            if shadow.health > 0:
                print(f"The {shadow.name} does {shadow.dealdamage(hero)} damage to {hero.name}!")
                if hero.alive():
                    print("")
                    print("The Shadow disarms you, quite literally. The severed limb immediately turns into a shadowy mist that melds into the spectral being before you. The pain from the missing limb is muted by the sheer terror spreading through your chest. The Shadow raises its blade again, bringing it down on your remaining arm as you attempt to defend yourself. With no way to shield your vision, you have no choice but to stare at the imposing mass as it takes your head in both of its 'hands', forcing you to stare into its 'eyes'. What comes next is unspeakable pain. It feels as if your soul is slowly being torn into the smallest of pieces. You open your mouth to scream, but no sound comes out. Your vision changes, and you are now staring directly into your own petrified eyes. Your existence merges with the Shadow's as your body breaks down into spectral mist. You spend the rest of the Shadow's 'life' staring through its eyes as it grows its power, adding more victims to its ranks. The pain never subsides. Your existence is torment.")
                    exit()

    shadow_battle()

main()
"""def loader():
        load = input("Would you like to load your data?\n 1.Load Save \n Return. To continue.")
    if load == "1":
        try:
            hero = pickle.load(open("sav.dat", "rb"))
            town()#yes should trigger a try block for saved data returning a message of "no save data found!" if none exists. if data is present do town()
        except:
            print("No save data found!")
    else:
        main()"""