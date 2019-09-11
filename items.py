class Item():
# class Item(name, description, health):
    def __init__(self, name, description, health, damage):
        # super().__innit__(name, description, health)
        self.name = name
        self.description = description
        self.health = health
        self.damage = damage

    def __str__(self):
        return self.__str__()
    
    def use_item(self,user,enemy):
        if self.health == 0:
            enemy.health -= self.damage
        if self.damage == 0:
            user.health += self.health

            

class Weapon():
    def __init__(self, name, description, attack):
        self.name = name
        self.description = description
        self.attack = attack

Unarmed = Weapon("Unarmed","Holy crap man you're going at this bare-handed? Absolute savage, bro.", 0)
Stick = Weapon("Stick", "A sharp stick that looks like it might hurt", 5)
Great_Axe = Weapon("Great Axe", "A gigantic Axe", 7)
Flaming_Hammer = Weapon("Flaming Hammer", "Metal hammer that has some kind of flames surrounding it", 15)
Scalpel = Weapon("Scalpel", "Doctors tool", 5)
Bladed_Spear = Weapon("Bladed Spear", "Sharp stick with a blade on the end of it", 8)
Slimy_Tendrils = Weapon("Slimy Tendrils", "goooooeeeyyy", 5)
Spooky_Hands = Weapon("Spooky Hands", "infected Hands", 1)
Shadow_Blade = Weapon("Shadow Blade", "The blade isn't even there ?!", 13)
Excalibur = Weapon("Excalibur", "Legendary Sword", 20)


#class Greatsword(Weapon):
    # def __init__(self):
    #     super().__init__(name="Greatsword",
    #                     description="A gigantic sword not many can hold.",
    #                     power=2)

class Armor():
    def __init__(self, name, description, defense):
        self.name = name
        self.description = description
        self.defense = defense
        

Leather_Jerkin = Armor("Leather Jerkin", "Armor made out of fine leather", 5)
Tattered_Cloth = Armor("Tattered Cloth", "Cloth with rips in it", 3)
Gold_Body_Armor = Armor("Gold Armor", "Rare armor that shines bright", 20)
Iron_Pauldrons = Armor("Iron Pauldrons", "Iron Armor", 8)
Medical_Garb = Armor("Medical Garb", "Clothes for Medical staff", 7)
Slime = Armor("Slime", "Goo", 4)
Fortified_Darkness = Armor("Fortified Darkness", "Almost invisible type of darkness", 5)

    

# class LeatherChestpiece(Armor):
#     def __init(self):
#         super().__innit__(name="LeatherChestpiece"
#                         description="Old Chestpiece made out of fine leather"
#                         health=2)


# shield = Armor('basic shield', 'description of shield',6)

#class Misc(Item):
    #def __innit__(self, name, description, health):
        #super().__innit__(name, description, health)
    # self.health = health

#Healing_Potion = Misc("Misc", "Potion that gains +25 health", 20)

health_potion = Item("Health Potion", "This tastes like the blood of the innocent. Yummy!", 25, 0)
# # this is your basic item class
# #weapons, armor are subclasses of Item
# class Item(name, description, health):
#     def __innit__(self, name, description, health):
#     # self.health = health
#         super().__innit__(name, description, health)
#     # self.description=description
#     # self.name=name

health_potion = Item("Health_Potion", "This potion taste like the blood of the innocent. Yummy", 25, 0)
