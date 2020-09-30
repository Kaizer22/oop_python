from task2.chess.game_logic.base_elements.interface_cell_state import ICellState

'''Пустая клетка. Не является шахматной фигурой, 
    но описывает состояние клетки доски'''
class EmptyCell(ICellState):
   def __init__(self, code):
       super().__init__(code)

