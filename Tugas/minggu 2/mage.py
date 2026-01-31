from hero import Hero

class Mage(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp, lane="Mage")

    def ultimate(self, enemy):
        damage = 180
        print(f"\n🌟 {self.name} menggunakan ULTIMATE : Arcane Blast!")
        enemy.take_damage(damage)

    def fireball(self, enemy):
        dmg = 10
        total = dmg * 7
        print(f"\n🔥 {self.name} menggunakan Fireball!")
        print("🔥 Bola api mengenai musuh 7x!")
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        enemy.take_damage(dmg)
        print(f"💥 Total damage yang diterima musuh: {total} DMG!")
