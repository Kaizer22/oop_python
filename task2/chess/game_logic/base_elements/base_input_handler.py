from abc import abstractmethod

''' Класс, описывающи общий функционал классов,
    обрабатывающих пользовательский ввод'''
class InputHandler:
    @abstractmethod
    def get_game_attributes(self):
        """" Абстрактный метод для реализации полиморфизма
                Обработка ввода начальных параметров игры"""

    @abstractmethod
    def get_next_turn(self):
        """" Абстрактный метод для реализации полиморфизма
                Обработка ввода следующего хода"""
