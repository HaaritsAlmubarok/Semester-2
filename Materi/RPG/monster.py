class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print(f"🐉 Monster {self.name} telah summon!")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"💥 {self.name} menerima {damage} damage")
        print(f"🩸 Sisa hp: {self.hp}\n")
        if self.hp <= 0:
            print(f"☠️  Monster {self.name} telah tereliminasi!")

    def attack(self, enemy, damage):
        print()
        print(f"⚔️  {self.name} menyerang {enemy.name}!")
        # panggil method dari method lain
        enemy.take_damage(damage)


    # fungsi untuk menampilkan informasi monster
    def __str__(self):
        status = "Hidup"
        if self.hp <= 0:
            status = "☠️  Tereliminasi"
        return f"{self.name} | HP: {self.hp} | Status: {status}"
