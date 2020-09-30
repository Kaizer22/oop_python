from enum import Enum


class Cell(Enum):
    EMPTY_CELL = 0

    WHITE_KING = 1
    WHITE_BISHOP = 2
    WHITE_KNIGHT = 3
    WHITE_PAWN = 4
    WHITE_QUEEN = 5
    WHITE_ROOK = 6

    BLACK_KING = -1
    BLACK_BISHOP = -2
    BLACK_KNIGHT = -3
    BLACK_PAWN = -4
    BLACK_QUEEN = -5
    BLACK_ROOK = -6


'''Класс, реализующий общий функционал всех клеток 
    шахматной доски. Все клетки обладают кодом состояния Cell(Enum)'''


class ICellState:
    def __init__(self, code):
        self._code = code

    @property
    def code(self):
        return self._code
