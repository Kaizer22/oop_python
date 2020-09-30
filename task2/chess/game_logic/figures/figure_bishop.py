from task2.chess.game_logic.base_elements.base_figure import BaseFigure

'''Фигура Слон '''
class Bishop(BaseFigure):
    def __init__(self, pos_x, pos_y, code):
        super().__init__(pos_x, pos_y, code)

    def check(self, new_x, new_y):
        pass