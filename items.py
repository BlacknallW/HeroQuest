

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

        # self.power = power

Stick = Weapon("stick", "A sharp stick that looks like it might hurt", 2)
Great_Sword = Weapon("Great Axe", "A gigantic axe", 5)
Flaming_Hammer = Weapon("Flaming Hammer", "Metal hammer that has some kind of flames surrounding it", 15)



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
        

Leather_body_armor = Armor("Leather Armor", "Armor made out of fine leather", 5)
Metal_body_armor = Armor("Metal Armor", "Solid metal armor", 14)
Gold_body_armor = Armor("Gold Armor", "Rare armor that shines bright", 20)


    

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


