from hero import Hero

class Assassin(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp, lane="Assassin")

    def ultimate(self, enemy):
        damage = 200
        print(f"\n🌟 {self.name} menggunakan ULTIMATE : Shadow Strike!")
        enemy.take_damage(damage)

    def stealth_attack(self, enemy):
        dmg = 50
        total = dmg * 2
        print(f"\n🌟 {self.name} menggunakan Stealth Attack!")
        print("⚡ Serangan mengenai musuh 2x!")
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        print(f"💥 Total damage: {total} DMG")
