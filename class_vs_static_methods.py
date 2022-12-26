# Class vs static methods

class Monster:
    ARE_MONSTERS_EVIL = True

    def __init__(self, name, strength, defense):
        self.name = name
        self.strength = strength
        self.defense = defense

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def dragon(cls):
        return cls("Dragon", 90, 90)

    @classmethod
    def zombie(cls, strength=10):
        return cls("Zombie", strength, 10)

    @classmethod
    def make_monsters_good(cls):
        cls.ARE_MONSTERS_EVIL = False

    @staticmethod
    def fight(monster_one, monster_two):
        if monster_one.strength > monster_two.defense:
            print(f"{monster_one} wins!")
        elif monster_two.strength > monster_one.defense:
            print(f"{monster_two} wins!")
        else:
            print("No one won!")


dragon = Monster.dragon()
zombie = Monster.zombie(10)

print(Monster.ARE_MONSTERS_EVIL)
Monster.make_monsters_good()
print(Monster.ARE_MONSTERS_EVIL)

Monster.fight(dragon, zombie)
