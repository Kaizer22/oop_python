"""Миксин предоставляющий бойцу возможность проводить
дальнобойную атаку"""


class LongRangeCombatMixin:

    def __init__(self):
        self.power = 0

    def init_long_range_combat(self, power):
        self.power = power

    def shoot(self, enemy):
        attack = self.power - enemy.armor / 2
        print("Выстрел.Нанесено урона: {0:.2f} ".format(attack))
        enemy.hp -= attack
