from lib.core.colors import color, Colors


class Rarity:
    def __init__(self, w=None, c=color(15)):
        self.w = w
        self.c = c

    def __str__(self):
        return 'Rarity({w})'.format(w=self.w)

    def c(self):
        if self.c is not None:
            return self.c
        else:
            raise Exception('Must specify color!')
    
    def w(self):
        return self.w


Normal = Rarity(10, color(15))
Rare = Rarity(8, color(10))
VRare = Rarity(6, color(33))
Extreme = Rarity(4, color(200))
Legend = Rarity(2, color(208))
Unique = Rarity(1)

RarityLevels = (Normal, Rare, VRare, Extreme, Legend, Unique)
