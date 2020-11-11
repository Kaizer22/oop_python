from enum import Enum


class Item:

    def __init__(self, name, armor_effect, hp_effect,
                 agility_effect, luck_effect, attack_bonus, strength, quality):
        self.name = name
        self.armor_effect = armor_effect
        self.hp_effect = hp_effect
        self.agility_effect = agility_effect
        self.luck_effect = luck_effect
        self.attack_bonus = attack_bonus
        self.strength = strength
        self.quality = quality

    def use(self):
        self.strength -= self.quality


class Quality(Enum):
    BAD = 5
    ORDINARY = 4
    GOOD = 3
    BEST = 2
    LEGENDARY = 1
