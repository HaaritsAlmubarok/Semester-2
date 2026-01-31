from hero import Hero

class Tank(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp, lane="Tank")

    # skill biasa: perkuat diri sendiri
    def fortify(self):
        shield = 60
        print(f"\n🛡️  {self.name} menggunakan Fortify!")
        self.receive_shield(shield)

    # ultimate: lindungi satu tim
    def ultimate(self, team):
        shield = 80
        print(f"\n🌟 {self.name} menggunakan ULTIMATE : Iron Wall!")
        print("🛡️  Seluruh tim mendapat shield!")

        for hero in team:
            hero.receive_shield(shield)
