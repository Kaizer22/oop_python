from task2.chess.game_logic.main_loop import MainLoop


class Chess:
    # Конструктор, в котором создается экзмпляр игрового цикла
    def __init__(self):
        self._main_loop_ = MainLoop()
        pass

    # Запуск игрового цикла
    def start_game(self):
        self._main_loop_.loop()
        pass


# Создание экземпляра шахмат и запуск игры в консоли
game = Chess()
game.start_game()
