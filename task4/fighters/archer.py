from task3.fighters.fighter import Fighter
from task3.fighters.inventory import Inventory
from task3.fighters.item import Item, Quality
from task3.fighters.long_range_combat_mixin import LongRangeCombatMixin
from task4.fighters.logger import log_method_calls


@log_method_calls("%H:%M:%S")
class Archer(Fighter, Inventory, LongRangeCombatMixin):

    def __init__(self):
        super(Inventory, self).__init__()
        super(LongRangeCombatMixin, self).__init__()
        super(Fighter, self).__init__()
        self.init_fighter(1000, 10, 3, 3, 5, False)
        self.init_long_range_combat(20)
        self.put_item(Item("Доспех лучника", 10, 10, 1, 2, 0, 10, Quality.ORDINARY))
        self.put_item(Item(" Лук и стрелы", 0, 0, 10, 2, 8, 40, Quality.ORDINARY))

        self.update_stats()

    def update_stats(self):
        effect_hp, effect_armor, effect_agility, effect_luck, effect_attack = self.use_inventory()
        self.hp += effect_hp
        self.armor += effect_armor
        self.agility += effect_agility
        self.luck += effect_luck
        self.base_attack += effect_attack

    def update_items(self):
        delta_hp, delta_armor, delta_agility, delta_luck, delta_attack = self.use_inventory()
        self.hp += delta_hp
        self.armor += delta_armor
        self.agility += delta_agility
        self.luck += delta_luck
        self.base_attack += delta_attack

    def attack(self, enemy):
        self.update_items()
        if self.is_in_block:
            self.is_in_block = False
        attack = (self.base_attack * (self.agility / (2 - self.luck/10))) - (enemy.armor/10)
        print("Лучник ({0:.2f}HP) атаковал . Нанесено урона: {1:.2f} ".format(self.hp, attack))
        enemy.hp -= attack
        pass

    def block(self, enemy):
        print("Лучник ({0:.2f}HP) - блок".format(self.hp))
        self.update_items()
        if not self.is_in_block:
            self.is_in_block = True
            self.armor = self.armor * 2
