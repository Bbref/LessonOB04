from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    @abstractmethod
    def attack(self):
        pass

class Mech(Weapon):
    def __init__(self):
        super().__init__("меч", 60)

    def attack(self):
        print("Боец наносит удар мечом.")

class Luk(Weapon):
    def __init__(self):
        super().__init__("лук", 30)

    def attack(self):
        print("Боец наносит удар из лука.")

class Bulava(Weapon):
    def __init__(self):
        super().__init__("булава", 50)

    def attack(self):
        print("Боец наносит удар булавой.")

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.name}.")

    def attack(self):
        if self.weapon:
            self.weapon.attack()
            return self.weapon.damage
        else:
            print(f"{self.name} не имеет оружия.")
            return 0

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} побежден!")
        else:
            print(f"У {self.name} осталось {self.health} здоровья.")

def main():
    fighter = Fighter("Герой")
    monster = Monster("Дракон", 100)

    mech = Mech()
    luk = Luk()
    bulava = Bulava()

    # Боец выбирает меч и атакует
    fighter.change_weapon(mech)
    damage = fighter.attack()
    monster.take_damage(damage)

    # Боец выбирает лук и атакует
    fighter.change_weapon(luk)
    damage = fighter.attack()
    monster.take_damage(damage)

    # Боец выбирает булаву и атакует
    fighter.change_weapon(bulava)
    damage = fighter.attack()
    monster.take_damage(damage)

if __name__ == "__main__":
    main()
