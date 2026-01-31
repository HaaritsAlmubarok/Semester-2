from hero import Hero

class Fighter(Hero):
    def __init__(self, name, hp):
        # super() mengakses parent class (Hero)
        super().__init__(name, hp, job="Fighter")

    def ultimate(self, enemy):
        damage = 150
        print()
        print(f"🌟 {self.name} menggunakan skill 1 : Spear Flip!")
        enemy.take_damage(damage)

    def combo(self, enemy):
        dmg = 30
        print()
        print(f"🌟 {self.name} menggunakan skill combo : Serangan Bertubi-tubi! {dmg} DMG!")
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        