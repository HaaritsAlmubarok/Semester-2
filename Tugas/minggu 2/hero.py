class Hero:
    def __init__(self, name, hp, lane):
        self.name = name
        self.lane = lane
        self.max_hp = hp
        self.hp = hp
        self.shield = 0   # ✅ WAJIB
        print(f"✨ [{self.lane}] {self.name} telah di summon!")

    def receive_shield(self, amount):
        self.shield += amount
        print(f"🛡️ {self.name} mendapat shield +{amount} | Shield: {self.shield}")

    def heal(self):
        heal_amount = 20
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"💖 {self.name} healing | HP: {self.hp}")

    def take_damage(self, damage):
        if self.shield > 0:
            absorbed = min(self.shield, damage)
            self.shield -= absorbed
            damage -= absorbed
            print(f"🛡️  Shield menyerap {absorbed} damage!")

        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

        print(f"💥 {self.name} terkena {damage} damage | HP: {self.hp}")

        if self.hp == 0:
            print(f"☠️ {self.name} tereliminasi!")

    def attack(self, enemy, damage):
        print(f"\n⚔️ {self.name} menyerang {enemy.name}!")
        enemy.take_damage(damage)

    def ultimate(self, target):
        print(f"{self.name} belum memiliki ultimate khusus")

    def __str__(self):
        status = "Hidup"
        if self.hp <= 0:
            status = "☠️ Tereliminasi"
        return f"{self.name} [{self.lane}] | HP: {self.hp}/{self.max_hp} | Shield: {self.shield} | Status: {status}"
