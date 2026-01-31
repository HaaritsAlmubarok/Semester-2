from hero import Hero

class Support(Hero):
    def __init__(self, name, hp):
        # super() mengakses parent class (Hero)
        super().__init__(name, hp, job="Support")

    def ultimate(self, enemy):
        damage = 50
        print()
        print(f"🌟 {self.name} menggunakan skill 1 : Healing Wave!")
        enemy.take_damage(damage)

    def combo(self, enemy):
        dmg = 10
        print()
        print(f"🌟 {self.name} menggunakan skill combo : Serangan Lembut! {dmg} DMG!")
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)