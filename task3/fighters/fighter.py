from abc import abstractmethod, ABC

"""
Абстрактный класс бойца 
"""


class Fighter(ABC):

    def __init__(self):
        self.hp = 10
        self.armor = 10
        self.agility = 10
        self.luck = 10
        self.base_attack = 2
        self.is_in_block = False

    # Инициализация экземпляра бойца происходит посредством этого метода
    def init_fighter(self, hp, armor, agility, luck, base_attack, is_in_block):
        self.hp = hp
        self.armor = armor
        self.agility = agility
        self.luck = luck
        self.base_attack = base_attack
        self.is_in_block = False

    # Метод, реализующий атаку. Каждый класс-наследник реализует его по-своему
    @abstractmethod
    def attack(self, enemy):
        """Удар"""

    # Метод, реализующий блок. Каждый класс-наследник реализует его по-своему
    @abstractmethod
    def block(self, enemy):
        """Блок"""
