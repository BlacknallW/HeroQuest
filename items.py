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
Spooky_Hands = Weapon("Spooky Hands", "infected Hands", 10)
Shadow_Blade = Weapon("Shadow Blade", "The blade isn't even there ?!", 13)
Excalibur = Weapon("Excalibur", "Legendary Sword", 20)




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

    




health_potion = Item("Health Potion", "This tastes like the blood of the innocent. Yummy!", 25, 0)
