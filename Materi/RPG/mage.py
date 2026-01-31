from hero import Hero

class Mage(Hero):
    def __init__(self, name, hp):
        # super() mengakses parent class (Hero)
        super().__init__(name, hp, job="Mage")

    def ultimate(self, enemy):
        damage = 100
        print()
        print(f"🌟 {self.name} menggunakan skill 1 : Setrum!")
        enemy.take_damage(damage)

    def combo(self, enemy):
        dmg = 20
        print()
        print(f"🌟 {self.name} menggunakan skill combo : Setrum berdahak! {dmg} DMG!")
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
