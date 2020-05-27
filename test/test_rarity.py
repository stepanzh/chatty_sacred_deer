import unittest

from lib.core.rarity import RarityLevels
from lib.core.colors import Colors

for l in RarityLevels:
    print(Colors.colorise(l, l.c))
