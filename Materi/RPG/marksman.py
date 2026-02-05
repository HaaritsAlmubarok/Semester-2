from monster import Monster
from hero import Hero

class Marksman(Hero):
    def __init__(self, name : str, hp : int):
        # super() mengakses parent class (Hero)
        super().__init__(name, hp, job="Marksman")

    def ultimate(self, enemy : Monster):
        damage = 120
        print()
        print(f"🌟 {self.name} menggunakan skill 1 : Piercing Arrow!")
        enemy.take_damage(damage)

    def rapid_fire(self, enemy : Monster):
        dmg = 25
        print()
        print(f"🌟 {self.name} menggunakan skill rapid fire : Serangan Cepat! {dmg} DMG!")
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)