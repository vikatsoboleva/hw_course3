class Character:
    def __init__(self, character_name, health_points):
        self.character_name = character_name
        self.health_points = health_points

    def attack_description(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе.")


class Warrior(Character):
    def __init__(self, character_name, health_points, strength):
        super().__init__(character_name, health_points)
        self.strength = strength

    def attack_description(self):
        return f"{self.character_name} атакует противника силой удара {self.strength} единиц."


class Wizard(Character):
    def __init__(self, character_name, health_points, magic_power):
        super().__init__(character_name, health_points)
        self.magic_power = magic_power

    def attack_description(self):
        return f"{self.character_name} накладывает заклинание с мощностью магии {self.magic_power} единиц."


# Пример использования:
warrior = Warrior("Эрагон", 100, 25)
wizard = Wizard("Геральд", 80, 40)

print(warrior.attack_description())
print(wizard.attack_description())
