from enum import Enum

"""Класс предмета. Предметы располагаются в инвентаре бойца
и усиливают его боевые показатели"""
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

    # Каждое использование предмета снижает его прочность
    # на величину, определяемую качеством предмета
    def use(self):
        self.strength -= self.quality

# Качество предмета. Чем хуже - тем большая величина прочности тратиться за
# ход
class Quality(Enum):
    BAD = 5
    ORDINARY = 4
    GOOD = 3
    BEST = 2
    LEGENDARY = 1
