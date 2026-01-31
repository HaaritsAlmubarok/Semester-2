from hero import Hero

class Support(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp, lane="Support")

    # heal diri sendiri (opsional)
    def heal(self):
        heal_amount = 20
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"💖 {self.name} menyembuhkan diri | HP: {self.hp}")

    # 🔥 HEAL SATU TIM (INI YANG DIPANGGIL DI main.py)
    def heal_team(self, team):
        heal_amount = 30
        print("\n✨ Rafaela mengangkat tongkat suci!")
        print("💖 Cahaya suci menyembuhkan seluruh tim!")

        for hero in team:
            hero.hp += heal_amount
            if hero.hp > hero.max_hp:
                hero.hp = hero.max_hp
            print(f"💊 {hero.name} pulih +{heal_amount} HP | HP: {hero.hp}")
