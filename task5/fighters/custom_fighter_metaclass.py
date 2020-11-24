from task5.fighters.fighter import Fighter
from task5.fighters.inventory import Inventory
from task5.fighters.long_range_combat_mixin import LongRangeCombatMixin


class CustomFighterMetaclass(type):
    __name = ''
    __bases = list()
    __namespace = dict()

    @classmethod
    def set_name(mcs, name):
        mcs.__name = name
        return CustomFighterMetaclass

    @classmethod
    def set_standard_specifications(mcs):
        # Добавление полей характеристик в класс бойца
        return CustomFighterMetaclass

    @classmethod
    def set_long_range_combat_mixin(mcs):
        mcs.__bases.append(LongRangeCombatMixin)
        return CustomFighterMetaclass

    @classmethod
    def set_inventory(mcs):
        # Установка наследования от Inventory
        mcs.__bases.append(Inventory)
        return CustomFighterMetaclass

    @classmethod
    def get_type(mcs):
        return type(CustomFighterMetaclass.__name,
                    tuple(CustomFighterMetaclass.__bases),
                    CustomFighterMetaclass.__namespace)

    #def __new__(cls, name, bases, namespace):
        #print()
        #return type(CustomFighterMetaclass.__name,
                    #tuple(CustomFighterMetaclass.__bases), namespace)
