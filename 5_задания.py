class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Damage: {self.damage}"

class Main:
    @staticmethod
    def createHeroes():
        heroes = []
        heroes.append(Hero("Warrior", 100, 20))
        heroes.append(Hero("Mage", 80, 30))
        heroes.append(Hero("Archer", 90, 25))
        return heroes

    @staticmethod
    def main():
        heroes = Main.createHeroes()
        for hero in heroes:
            print(hero)

if __name__ == "__main__":
    Main.main()






