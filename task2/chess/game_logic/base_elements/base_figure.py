from abc import abstractmethod

from task2.chess.game_logic.base_elements.interface_cell_state import ICellState

'''Абстрактный класс фигуры, определяющий общий функционал
    шахматных фигур и реализующий состояние клетки доски'''
class BaseFigure(ICellState):

    def __init__(self, pos_x, pos_y, code):
        super().__init__(code)
        self.x = pos_x
        self.y = pos_y

    # Реализация перемещения фигуры по доске
    def move_to(self, new_x, new_y):
        if self.check(new_x, new_y):
            self.x = new_x
            self.y = new_y
            return True
        else:
            return False
        pass

    # Абстрактный метод, реализуемый каждой конкретной фугурой
    # Проверка возможности соверешния хода для данной конкретной фигуры
    @abstractmethod
    def check(self, new_x, new_y):
        pass