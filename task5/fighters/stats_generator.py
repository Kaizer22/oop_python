import time

from task5.fighters.fighters_game import FightersGame
from task5.fighters.stats_generator_timeout_exception import StatsGeneratorTimeoutException

# Таймаут выполнения генерации отчета по статистике поединков
STATS_GENERATOR_TIMEOUT = 20


def generate_stats(filename, fighter1, fighter2, rounds):
    start_time = time.time()
    first_won = 0
    second_won = 0

    file = open(filename, 'w')
    file.write("Статистика " + str(rounds) + " поединков(-а) "
                                             "бойцов \n" + str(type(fighter1)) + " \n"
               + str(type(fighter2)) +
               "\n")
    for i in range(0, rounds):
        current_time = time.time()
        if current_time - start_time >= STATS_GENERATOR_TIMEOUT:
            raise StatsGeneratorTimeoutException
        fighter1 = type(fighter1)()
        fighter2 = type(fighter2)()
        game = FightersGame(fighter1, fighter2)
        game.start()
        if game.get_winner() == 1:
            first_won += 1
        else:
            second_won += 1

    file.write("Боец 1 победил в " + str((first_won / rounds * 100)) + "% поединков \n")
    file.write("Боец 2 победил в " + str((second_won / rounds * 100)) + "% поединков \n")
    file.close()
    print("Подсчет статистики успешно завершен")
