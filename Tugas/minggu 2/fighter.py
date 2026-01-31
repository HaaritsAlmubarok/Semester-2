from hero import Hero

class Fighter(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp, lane="Fighter")

    def ultimate(self, enemy):
        damage = 150
        print(f"\n🌟 {self.name} menggunakan ULTIMATE: Hantaman Kapak!")
        enemy.take_damage(damage)

    def combo(self, enemy):
        dmg = 30
        total = dmg * 3
        print(f"\n🌟 {self.name} menggunakan Combo Attack!")
        print("⚔️  Serangan mengenai musuh 3x!")
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        print(f"💥 Total damage: {total} DMG")
