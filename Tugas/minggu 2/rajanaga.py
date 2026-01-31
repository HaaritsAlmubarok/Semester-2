class RajaNaga:
    def __init__(self):
        self.nama = "Raja Naga Kuno"
        self.max_hp = 1000
        self.health = 1000
        self.base_damage = 60
        self.rage = False
        self.phase2 = False

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

        print(f"💥 {self.nama} menerima {damage} damage")
        print(f"🩸 HP Raja Naga: {self.health}/{self.max_hp}")

        # 🔥 CUTSCENE 50%
        if self.health <= self.max_hp * 0.5 and not self.rage:
            self.rage = True
            print("\n😡 Raja Naga mengaum keras!")
            print("🔥 Raja Naga memasuki MODE BRUTAL!")
            self.base_damage += 30

        # 🔥 PHASE 2 < 30%
        if self.health <= self.max_hp * 0.3 and not self.phase2:
            self.phase2 = True
            print("\n💀 LANGIT MENJADI GELAP...")
            print("🔥 PHASE 2 — AMARAH NAGA TERLEPAS!")

        if self.health == 0:
            print(f"\n☠️ {self.nama} telah dikalahkan!")

    def attack(self, target):
        print(f"\n🐲 {self.nama} menyerang {target.name}!")
        target.take_damage(self.base_damage)

    # 🔥 SERANGAN KE SATU TIM
    def fire_breath(self, team):
        print("\n🔥 Raja Naga menyemburkan API KESELURUH TIM!")
        for hero in team:
            hero.take_damage(40)
