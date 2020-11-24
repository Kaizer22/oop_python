import random
from datetime import datetime
import time
from functools import wraps

from task4.fighters.custom_fighter_metaclass import CustomFighterMetaclass
from task4.fighters.logger import Debugger

Debugger.DEBUG = True

from task4.fighters.warrior import Warrior
from task4.fighters.long_range_combat_mixin import LongRangeCombatMixin


def game_decorator(start):
    def get_current_time():
        return datetime.now()

    @wraps(start)
    def game_wrapper(self):
        time_start = str(get_current_time())
        start(self)
        time.sleep(2)
        time_end = str(get_current_time())
        print("Партия началась - " + time_start + "\n" +
              "Партия закончилась - " + time_end)

    return game_wrapper


def turn_decorator(make_turn):
    @wraps(make_turn)
    def turn_wrapper(self, fighter, enemy):
        rand_val = random.randrange(1, 6, 1)
        print("RAND:", rand_val)
        print("[Боец {} ]: ".format(1 if self.is_fighter_1_turn else 2))
        make_turn(self, fighter, enemy, rand_val)

    return turn_wrapper


class FightersGame:

    def __init__(self, fighter1, fighter2):
        self.is_fighter_1_turn = True
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    @turn_decorator
    def make_turn(self, fighter, enemy, rand_val=1):
        if rand_val < 3:
            fighter.block(enemy)
        elif rand_val >= 5 and isinstance(fighter, LongRangeCombatMixin):
            fighter.shoot(enemy)
        else:
            fighter.attack(enemy)

    @game_decorator
    def start(self):
        print("Welcome to Fighters")
        while self.fighter1.hp > 0 and self.fighter2.hp > 0:
            if self.is_fighter_1_turn:
                self.make_turn(self.fighter1, self.fighter2)
                print("________________________")
                self.is_fighter_1_turn = not self.is_fighter_1_turn
            else:
                self.make_turn(self.fighter2, self.fighter1)
                print("________________________")
                self.is_fighter_1_turn = not self.is_fighter_1_turn

        if self.fighter1.hp < 0:
            print("Выиграл боец номер 2")
        else:
            print("Выиграл боец номер 1")




# Настройка класса нового типа бойца
CustomFighterMetaclass \
    .set_name("NewCustomFighter") \
    .set_inventory() \
    .set_long_range_combat_mixin() \
    .set_standard_specifications()
# Создание объекта сконструированного класса
custom = CustomFighterMetaclass.get_type()()
print(type(custom))
print(dir(type(custom)))

# custom.shoot(fighter1)
fighter1 = Warrior()
fighter2 = Warrior()

game = FightersGame(fighter1, fighter2)

game.start()
