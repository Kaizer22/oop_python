from task2.chess.game_logic.base_elements.empty_cell import EmptyCell
from task2.chess.game_logic.base_elements.interface_cell_state import Cell
from task2.chess.game_logic.figures.figure_bishop import Bishop
from task2.chess.game_logic.figures.figure_king import King
from task2.chess.game_logic.figures.figure_knight import Knight
from task2.chess.game_logic.figures.figure_pawn import Pawn
from task2.chess.game_logic.figures.figure_queen import Queen
from task2.chess.game_logic.figures.figure_rook import Rook

'''Класс, реализующий шахматную доску'''


class Board:

    def __init__(self, field_height=8, field_width=8, placement='standard'):
        # Параметры шахматной доски
        self._field_height = field_height
        self._field_width = field_width

        # Шахматное поле;
        # представлено 2D массивом объектов ICellState
        self._field = list()

        # Создание пустых клеток
        for i in range(0, field_height):
            buf = list()
            for j in range(0, field_width):
                buf.append(EmptyCell(0))
            self._field.append(buf)

        # Расстановка фигур в соответсвии с заданной схемой placement
        # Доступны: standard и reverse
        self._place_figures(placement)

    @property
    def field_width(self):
        return self._field_width

    @property
    def field_height(self):
        return self._field_height

    # Получение кода состояния клетки доски
    def get_cell(self, x, y):
        return self._field[y][x].code

    # Расстановка фигур на доске в зависимости от входного параметра
    def _place_figures(self, placement):
        # В качестве аналога switch был использован одноразовый словарь
        {
            'standard': self._place_standard,
            'reverse': self._place_reverse_
        }[placement]()

    # Стандартная расстановка фигур
    def _place_standard(self):
        # При данной расстановке: белые - сверху доски, черные снизу
        # Если ширина доски нечентая, то игроки получают по дополнительной королеве
        # При расстановке остальных фигур происходит повторение станадртного порядка расстановки

        # Расставляем пешки
        self._place_pawns_in_line(self._field_height - 2, 1)

        # Расставляем остальные фигуры, подбирая их количество под масштаб
        # шахматной доски
        black_line = self._field_height - 1
        white_line = 0
        self._place_other_figures_in_standard_line(black_line, False)
        self._place_other_figures_in_standard_line(white_line, True)

    # Обратная расстановка фигур
    def _place_reverse_(self):
        # Отличие от стандартонго порядка - пешки следуют вторым рядом
        # Расставляем пешки
        self._place_pawns_in_line(self._field_height - 1, 0)

        # Расставляем остальные фигуры, подбирая их количество под масштаб
        # шахматной доски
        black_line = self._field_height - 2
        white_line = 1
        self._place_other_figures_in_standard_line(black_line, False)
        self._place_other_figures_in_standard_line(white_line, True)

    # Обработка следующего хода и проверка корректности
    # в рамках доски на такие случаи как:
    #  - для хода выбрана пустая клетка
    #  - для хода выбрана фигура другого игрока или на конечных координатах расположена
    #  дружественная фигура
    #  А корректность конечных координат каждая фигура проверяяет самостоятельно
    def next_turn(self, old_x, old_y, new_x, new_y, is_white_turn):
        old_cell_code = self._field[old_y][old_x].code
        new_cell_code = self._field[new_y][new_x].code
        if old_cell_code == Cell.EMPTY_CELL.value:
            print("empty")
            return False
        elif is_white_turn and (old_cell_code < 0 or new_cell_code > 0):
            print("<0")
            print(old_cell_code)
            return False
        elif not is_white_turn and (old_cell_code > 0 or new_cell_code < 0):
            print(">0")
            return False
        else:
            if self._field[old_y][old_x].move_to(new_x, new_y):
                buf = self._field[old_y][old_x]
                self._field[old_y][old_x] = EmptyCell(0)
                self._field[new_y][new_x] = buf
                return True
            else:
                print("moveto")
                return False

    # Расположить пешки в линию
    def _place_pawns_in_line(self, black_line, white_line):
        for i in range(0, self._field_width):
            self._field[white_line][i] = Pawn(i, white_line, Cell.WHITE_PAWN.value)
            self._field[black_line][i] = Pawn(i, black_line, Cell.BLACK_PAWN.value)

    # Расположить остальные фигуры в линию стандартного порядка
    def _place_other_figures_in_standard_line(self, line, is_white):
        if is_white:
            queen = Cell.WHITE_QUEEN.value
            king = Cell.WHITE_KING.value
            rook = Cell.WHITE_ROOK.value
            bishop = Cell.WHITE_BISHOP.value
            knight = Cell.WHITE_KNIGHT.value
        else:
            queen = Cell.BLACK_QUEEN.value
            king = Cell.BLACK_KING.value
            rook = Cell.BLACK_ROOK.value
            bishop = Cell.BLACK_BISHOP.value
            knight = Cell.BLACK_KNIGHT.value
        queen_pos = int(self._field_width / 2 - 1)
        king_pos = int(self._field_width / 2)
        if self._field_width % 2 == 0:
            self._field[line][queen_pos] = Queen(queen_pos,
                                                 line, queen)
            self._field[line][king_pos] = King(king_pos, line, king)

        else:
            self._field[line][queen_pos] = Queen(queen_pos, line, queen)
            self._field[line][king_pos] = King(king_pos, line, king)
            self._field[line][queen_pos + 2] = Queen(queen_pos + 2, line, queen)

        for i in range(0, queen_pos - 2):
            self._field[line][i] = Rook(i, line, rook)
            self._field[line][i + 1] = Knight(i + 1, line, knight)
            self._field[line][i + 2] = Bishop(i + 2, line, bishop)

            self._field[line][self._field_width - i - 1] = Rook(self._field_width - i - 1,
                                                                line, rook)
            self._field[line][self._field_width - i - 2] = Knight(self._field_width - i - 2,
                                                                  line, knight)
            self._field[line][self._field_width - i - 3] = Bishop(self._field_width - i - 3,
                                                                  line, bishop)
