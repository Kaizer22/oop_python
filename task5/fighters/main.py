# Настройка класса нового типа бойца
from threading import Thread

from task5.fighters.logger import Debugger

Debugger.DEBUG = False

from task5.fighters.custom_fighter_metaclass import CustomFighterMetaclass
from task5.fighters.fighters_game import FightersGame
from task5.fighters.stats_generator import generate_stats
from task5.fighters.warrior import Warrior
from task5.fighters.archer import Archer

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
fighter2 = Archer()

# Запуск генерации статистики по n поединкам
# Отчет записывается в файл stats.txt
generatorThread = Thread(target=generate_stats, args=("stats.txt", fighter1, fighter2
                                                      , 20))
generatorThread.start()

game = FightersGame(fighter1, fighter2)
game.start()

generatorThread.join()
