from abc import abstractmethod

'''Класс, представляющий общий функционал 
    для классов, работающих с графикой'''
class DrawManager:
    def __init__(self):
        pass

    @abstractmethod
    def draw_start_screen(self):
        """" Абстрактный метод для реализации полиморфизма
                Отрисовка приветсвенного экрана"""

    @abstractmethod
    def draw(self, board):
        """" Абстрактный метод для реализации полиморфизма
                Отрисовка текущего состояния доски"""

    @abstractmethod
    def show_current_player(self, is_white_turn):
        """" Абстрактный метод для реализации полиморфизма
                Показ подсказки о том, чья очередь ходить"""

    @abstractmethod
    def show_hint(self):
        """" Абстрактный метод для реализации полиморфизма
                Показ подсказки о том, как ходить"""

    @abstractmethod
    def show_warning(self):
        """" Абстрактный метод для реализации полиморфизма
                Показ предостережения - ход не может быть осуществлен"""
