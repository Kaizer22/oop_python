from task2.chess.draw_manager.draw_manager import DrawManager
from task2.chess.game_logic.base_elements.interface_cell_state import Cell

'''Реализация класса DrawManager для консольного вывода'''
class ConsoleDrawer(DrawManager):

    def show_current_player(self, is_white_turn):
        if is_white_turn:
            current_player = "White's"
        else:
            current_player = "Black's"
        print(current_player + " turn")

    def draw_start_screen(self):
        print("Welcome to Chess. Press Enter to start a standard game \n"
              "or type \"[NUMBER] [NUMBER] [POSITIONING]\" to start a game on \n"
              "custom board and with non standard figures positioning.")

    def draw(self, board):
        buf_str = ""
        pattern = "{0}"
        info = "  "
        for i in range(0, board.field_width ):
            info += str(i + 1) + "  "
        print(info)
        for i in range(0, board.field_height):
            for j in range(0, board.field_width):
                buf_str += pattern \
                    .format(self._get_char(
                    board.get_cell(j, i), j, i))
            print(str(i + 1) + "|" + buf_str + "|" + str(i + 1))
            buf_str = ""
        print(info)

    # Получение спец шахматного символа utf  по коду
    def _get_char(self, code, x, y):
        # Фигуры
        if code != Cell.EMPTY_CELL.value:
            return {Cell.WHITE_KING.value: "\u2654\u00a0",
                    Cell.WHITE_BISHOP.value: "\u2657\u00a0",
                    Cell.WHITE_KNIGHT.value: "\u2658\u00a0",
                    Cell.WHITE_PAWN.value: "\u2659\u00a0",
                    Cell.WHITE_QUEEN.value: "\u2655\u00a0",
                    Cell.WHITE_ROOK.value: "\u2656\u00a0",
                    Cell.BLACK_KING.value: "\u265A\u00a0",
                    Cell.BLACK_BISHOP.value: "\u265D\u00a0",
                    Cell.BLACK_KNIGHT.value: "\u265E\u00a0",
                    Cell.BLACK_PAWN.value: "\u265F\u00a0",
                    Cell.BLACK_QUEEN.value: "\u265B\u00a0",
                    Cell.BLACK_ROOK.value: "\u265C\u00a0"
                    }.get(code)
        else:
            # Пустые клетки: черные и белые
            if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
                return "\u25A0\u1160"
            else:
                return "\u25A1\u1160"

    def show_hint(self):
        print("Enter your turn like that:"
              " \"[CHOSEN FIGURE X] [Y]   [NEW X] [Y]\" "
              "or type \"q\" to exit the game ")
        pass

    def show_warning(self):
        print("Something wrong. Please check your input")
