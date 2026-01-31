from hero import Hero

class Marksman(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp, lane="Marksman")

    def ultimate(self, enemy):
        damage = 170
        print(f"\n🌟 {self.name} menggunakan ULTIMATE : Bullet Storm!")
        enemy.take_damage(damage)

    def rapid_fire(self, enemy):
        dmg = 15
        hit = 9
        total = dmg * hit

        print(f"\n🔫 {self.name} menggunakan Rapid Fire!")
        print(f"🔫 Menembak musuh {hit}x!")

        for i in range(hit):
            enemy.take_damage(dmg)

        print(f"💥 Total damage yang diterima musuh: {total} DMG!")

    def satuhit(self, enemy):
        damage = 5
        print(f"\n🌟 {self.name} menggunakan peluru terakhir untuk mengeliminasi goblin!")
        enemy.take_damage(damage)
