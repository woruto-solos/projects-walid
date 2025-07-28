class fortnite:  
    def __init__(self,rarity, skin, gun):
        self.rarity =rarity
        self.skin = skin
        self.gun = gun

    def describe_fortnite(self):
        print(f"This is a {self.rarity} {self.skin}, which is a {self.fortnite_type}")
first_fortnite=fortnite("legendary","renegade raider","scar")
second_fortnite=fortnite("rare","naruto","pump")
print(first_fortnite.rarity)
print(second_fortnite.skin)
print(first_fortnite.gun)