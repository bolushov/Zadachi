import random

class Boss:
    def __init__(self):
        self.health = 250
        self.damage = 50

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_damage(self):
        return self.damage

    def set_damage(self, damage):
        self.damage = damage

class Player:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.is_alive = True

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_damage(self):
        return self.damage

    def is_alive(self):
        return self.is_alive

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False

# Добавление новых игроков
players = ["Ilim"]
players.append(Player("Warrior", 100, 20))
players.append(Player("Mage", 80, 30))
players.append(Player("Archer", 90, 25))

# Golem
class Golem(Player):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def take_damage(self, damage):
        # Golem принимает 1/5 часть урона от босса
        super().take_damage(damage + damage // 5)

players.append(Golem("Golem", 150, 15))

# Lucky
class Lucky(Player):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def take_damage(self, damage):
        # Lucky имеет шанс уклонения
        if random.choice([True, False]):
            print(self.get_name() + " уклонился от удара босса!")
        else:
            super().take_damage(damage)

players.append(Lucky("Lucky", 70, 40))

# Berserk
class Berserk(Player):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.blocked_damage = 0

    def take_damage(self, damage):
        # Berserk блокирует часть удара босса и прибавляет заблокированный урон к своему урону
        self.blocked_damage += damage // 3
        super().take_damage(damage - self.blocked_damage)

    def get_blocked_damage(self):
        return self.blocked_damage

players.append(Berserk("Berserk", 120, 20))

# Thor
class Thor(Player):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def take_damage(self, damage):
        # Thor с шансом оглушает босса
        if random.choice([True, False]):
            print(self.get_name() + " оглушил босса на 1 раунд!")
            return
        super().take_damage(damage)

players.append(Thor("Thor", 90, 35))

boss = Boss()

while boss.get_health() > 0:
    for player in players:
        if player.is_alive():
            player_damage = player.get_damage()
            boss_damage = boss.get_damage()

            player.take_damage(boss_damage)
            if isinstance(player, Berserk):
                blocked_damage = player.get_blocked_damage()
                player_damage += blocked_damage
                player.take_damage(-blocked_damage)  # Возврат заблокированного урона боссу

            print(player.get_name() + " нанес " + str(player_damage) + " урона боссу.")
            
    if boss.get_health() > 0:
        for player in players:
            if player.is_alive():
                boss_damage = boss.get_damage()
                player.take_damage(boss_damage)
        
        print("Босс нанес " + str(boss_damage) + " урона игрокам.")

print("Босс повержен!")
