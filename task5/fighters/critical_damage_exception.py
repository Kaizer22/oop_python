class CriticalDamageException(Exception):
    def __init__(self, damage_value):
        self.message = "Критический урон!"
        self.damage_value = damage_value
