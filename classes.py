# Описание классов

from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Класс меча
class Sword(Weapon):
    def attack(self):
        return "Меч: мощный удар!"

# Класс лука
class Bow(Weapon):
    def attack(self):
        return "Лук: точный выстрел!"

# Класс магического посоха
class MagicStaff(Weapon):
    def attack(self):
        return "Посох: магическая атака!"

# Класс игрока
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбрал оружие: {type(weapon).__name__}")

    def attack(self):
        if self.weapon:
            return f"{self.name} атакует: {self.weapon.attack()}"
        else:
            return f"{self.name} не имеет оружия для атаки."

# Класс монстра
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        return f"{self.name} получил урон! Осталось здоровья: {self.health}"
