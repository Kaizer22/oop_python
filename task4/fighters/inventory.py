
class Inventory:
    def __init__(self):
        self.items = []

    def put_item(self, item):
        self.items.append(item)

    def use_inventory(self):
        result_hp = 0
        result_armor = 0
        result_agility = 0
        result_luck = 0
        result_base_attack = 0
        for item in self.items:
            result_hp += item.hp_effect
            result_armor += item.armor_effect
            result_agility += item.agility_effect
            result_luck += item.luck_effect
            result_base_attack += item.attack_bonus
        return result_hp, result_armor, result_agility, result_luck, result_base_attack

    def update_items_strength(self):
        delta_hp = 0
        delta_armor = 0
        delta_agility = 0
        delta_luck = 0
        delta_base_attack = 0
        for item in self.items:
            item.use()
            if item.strength < 0:
                delta_hp -= item.hp_effect
                delta_armor -= item.armor_effect
                delta_agility -= item.agility_effect
                delta_luck -= item.luck_effect
                delta_base_attack -= item.attack_bonus
                self.items.remove(item)
                print("Сломан предмет: {0}", item.name)
        return delta_hp, delta_armor, delta_agility, delta_luck, delta_base_attack

