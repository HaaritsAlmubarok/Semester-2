from enemy import Enemy
import random

class Goblin(Enemy):
    def __init__(self):
        super().__init__(
            name="Goblin Warrior",
            hp=400,
            damage=25
        )

    def attack(self, hero):
        print(f"\n👹 {self.name} menyerang {hero.name}!")

        damage = self.damage

        # mode mengamuk
        if self.hp < self.max_hp * 0.4:
            print("😡 Goblin mengamuk! Damage meningkat!")
            damage += 15

        hero.take_damage(damage)

        # serangan cepat
        if random.random() < 0.3:
            print("⚡ Goblin menyerang cepat!")
            hero.take_damage(15)
