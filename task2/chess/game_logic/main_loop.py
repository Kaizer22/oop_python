from task2.chess.draw_manager.impl.console_drawer import ConsoleDrawer
from task2.chess.game_logic.base_elements.board import Board
from task2.chess.game_logic.input_handler_impl.console_input_handler import ConsoleInputHandler

'''Класс, отвечающий за игровой цикл и
    содержащий в себе все основные упраляющие 
    сущности и логику игры'''
class MainLoop:
    # В конструкторе создается экземпляр класс InputHandler
    # (в данном случае - конкретная реализация для обработки консольного ввода)
    # Затем создается экземпляр класса DrawManager, ответсвенного за отрисовку
    # графики (в данном случае - конкретная реализация для консольного вывода)
    # Также в конструкторе происходит вызов отрисовки приветственного экрана
    # и обработка ввода параметров предстоящей игры. Если параметров не получено,
    # то запускается игра со стандартныйми параметрами ( доска 8x8 со стандартной
    # расстановкой фигур)
    def __init__(self):
        self.input_handler = ConsoleInputHandler()
        self.drawer = ConsoleDrawer()

        self.drawer.draw_start_screen()
        args = self.input_handler.get_game_attributes()
        if args is not None:
            self.board = Board(args[0], args[1], args[2])
        else:
            self.board = Board()

    # Метод, содержащий основной игровой цикл
    # Флаги контролируют игровые состояния: какая сторона ходит,
    # продолжать ли игру, завершен ли ход (или ход был некорректным
    # и нужно попросить пользователя походить по-другому)
    def loop(self):
        is_game_playing = True
        is_white_turn = True
        while is_game_playing:
            self.drawer.show_current_player(is_white_turn)
            self.drawer.draw(board=self.board)
            self.drawer.show_hint()
            old_x, old_y, new_x, new_y, is_continue = self.input_handler.get_next_turn()
            if not is_continue:
                break
            is_turn_finished = self.board\
                .next_turn(old_x, old_y, new_x, new_y, is_white_turn)

            if is_turn_finished:
                is_white_turn = not is_white_turn
            else:
                self.drawer.show_warning()
        pass
