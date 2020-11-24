import time
from functools import wraps

from task5.fighters.fighter import attack_decorator
from task5.fighters.fighter import Fighter
from task5.fighters.inventory import Inventory
from task5.fighters.item import Item, Quality
from task5.fighters.logger import log_method_calls


@log_method_calls("%H:%M:%S")
class Warrior(Fighter, Inventory):

    def __init__(self):
        super(Inventory, self).__init__()
        super(Fighter, self).__init__()
        super().init_fighter(1000, 20, 2, 1, 7, False)
        super().put_item(Item("Топор", 0, 0, 10, 3, 9, 10, Quality.ORDINARY))

    def update_stats(self):
        effect_hp, effect_armor, effect_agility, effect_luck = self.use_inventory()
        self.hp += effect_hp
        self.armor += effect_armor
        self.agility += effect_agility
        self.luck += effect_luck

    def update_items(self):
        delta_hp, delta_armor, delta_agility, delta_luck, delta_attack = self.use_inventory()
        self.hp += delta_hp
        self.armor += delta_armor
        self.agility += delta_agility
        self.luck += delta_luck
        self.base_attack += delta_attack

    def child_attack(self, enemy):
        self.update_items()
        if self.is_in_block:
            self.is_in_block = False
            self.armor /= 2
        attack = (self.base_attack * (self.agility / (2 - self.luck / 10))) - (enemy.armor / 5)
        print("Воин ({0:.2f}HP) атаковал . Нанесено урона: {1:.2f} ".format(self.hp, attack))
        enemy.hp -= attack

    def child_block(self, enemy):
        print("Воин ({0:.2f}HP) - блок".format(self.hp))
        self.update_items()
        if not self.is_in_block:
            self.is_in_block = True
            self.armor = self.armor * 2
