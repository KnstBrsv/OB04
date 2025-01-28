from classes import Fighter, Sword, Bow, MagicStaff, Monster

# Создание игрока и оружия
player = Fighter("Боец")
sword = Sword()
bow = Bow()
magic_staff = MagicStaff()

# Создание монстра
monster = Monster("Гоблин", 100)

# Экипировка оружия
player.equip_weapon(sword)
print(player.attack())
print(monster.take_damage(10))

player.equip_weapon(bow)
print(player.attack())
print(monster.take_damage(10))

player.equip_weapon(magic_staff)
print(player.attack())
print(monster.take_damage(10))
