import random

from task3.fighters.archer import Archer
from task3.fighters.fighter import Fighter
from task3.fighters.long_range_combat_mixin import LongRangeCombatMixin
from task3.fighters.warrior import Warrior

""" Основной исполняемы скрипт игры"""


# Седующий ход определяется "броском кубика"
def make_turn(fighter, enemy):
    rand_val = random.randrange(1, 6, 1)
    print("RAND:", rand_val)
    if rand_val < 3:
        fighter.block(enemy)
    elif rand_val >= 5 and isinstance(fighter, LongRangeCombatMixin):
        fighter.shoot(enemy)
    else:
        fighter.attack(enemy)


print("Welcome to Fighters")
fighter1 = Archer()
fighter2 = Warrior()
is_fighter_1_turn = True

# Пока показатели жизней обоих бойцов больше нуля - битва продолжается
while fighter1.hp > 0 and fighter2.hp > 0:
    if is_fighter_1_turn:
        make_turn(fighter1, fighter2)
        print("________________________")
        is_fighter_1_turn = not is_fighter_1_turn
    else:
        make_turn(fighter2, fighter1)
        print("________________________")
        is_fighter_1_turn = not is_fighter_1_turn

if fighter1.hp < 0:
    print("Выиграл боец номер 2")
else:
    print("Выиграл боец номер 1")
