import abc
from abc import ABCMeta
from functools import wraps

from task5.fighters.critical_damage_exception import CriticalDamageException

CRITICAL_DAMAGE_BORDER = 1000


def attack_decorator(attack):
    @wraps(attack)
    def attack_wrapper(self, enemy):
        hp_before = enemy.hp
        attack(self, enemy)
        hp_after = enemy.hp
        damage = hp_before - hp_after
        try:
            if damage >= CRITICAL_DAMAGE_BORDER:
                raise CriticalDamageException(damage)
        except CriticalDamageException as cde:
            print(cde.message + " " + str(cde.damage_value))

    return attack_wrapper


class Fighter(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.hp = 10
        self.armor = 10
        self.agility = 10
        self.luck = 10
        self.base_attack = 2
        self.is_in_block = False

    def init_fighter(self, hp, armor, agility, luck, base_attack, is_in_block):
        self.hp = hp
        self.armor = armor
        self.agility = agility
        self.luck = luck
        self.base_attack = base_attack
        self.is_in_block = False

    @abc.abstractmethod
    @attack_decorator
    def attack(self, enemy):
        """Удар"""
        self.child_attack(enemy)

    @abc.abstractmethod
    def block(self, enemy):
        """Блок"""
        self.child_block(enemy)
