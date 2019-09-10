class Item:
# class Item(name, description, health):
    def __init__(self, name, description, health):
        # super().__innit__(name, description, health)
        self.name = name
        self.description = description
        self.health = health

class Weapon(Item):
    def __init__(self, name, description, health):
        super().__init__(name, description, health)
        self.power = health
        # self.power = power

Stick = Weapon("stick", "A sharp stick that looks like it might hurt", 2)
Great_Sword = Weapon("Great Sword", "A gigantic sword", 5)
Flaming_Hammer = Weapon("Flaming Hammer", "Metal hammer that has some kind of flames surrounding it", 12)



#class Greatsword(Weapon):
    # def __init__(self):
    #     super().__init__(name="Greatsword",
    #                     description="A gigantic sword not many can hold.",
    #                     power=2)

class Armor(Item):
    def __init__(self, name, description, health):
        # self.health = health
        super().__init__(name, description, health)

Leather_body_armor = Armor("Leather Armor", "Armor made out of fine leather", 5)
Metal_body_armor = Armor("Metal Armor", "Solid metal armor", 14)
Gold_body_armor = Armor("Gold Armor", "Rare armor that shines bright", 10)


    

# class LeatherChestpiece(Armor):
#     def __init(self):
#         super().__innit__(name="LeatherChestpiece"
#                         description="Old Chestpiece made out of fine leather"
#                         health=2)


# shield = Armor('basic shield', 'description of shield',6)

class Misc(Item):
    def __innit__(self, name, description, health):
        super().__innit__(name, description, health)
       # self.health = health

Healing_Potion = ("Misc", "Potion that gains +25 health" 20)


# # this is your basic item class
# #weapons, armor are subclasses of Item
# class Item(name, description, health):
#     def __innit__(self, name, description, health):
#     # self.health = health
#         super().__innit__(name, description, health)
#     # self.description=description
#     # self.name=name


