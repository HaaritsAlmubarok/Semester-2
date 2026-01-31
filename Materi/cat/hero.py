print()
print("================== Hero Module ==================\n")

class Hero :
    # pertama kali di panggil (summon)
    # self = dirinya sendiri / internal
    def __init__(self, name, job, hp):
        self.name = name
        self.job = job
        self.hp = hp
        print(f"✨ {self.name} telah di summon!")

    def heal(self):
        print(f"💖 {self.name} healing")
        heal_amount = 20
        self.hp += heal_amount
        print(f"💊 HP {self.name} bertambah + {heal_amount}")

    def take_damage(self, damage):
        # self.hp = self.hp - damage (aslinya)
        self.hp -= damage
        print(f"💥 {self.name} terkena {damage} damage")
        print(f"🩸 Sisa HP : {self.hp}\n")
        if self.hp == 0:
            print(f"☠️ {self.name} tereliminasi!")

    def attack(self, enemy, damage):
        print()
        print(f"⚔️  {self.name} menyerang {enemy.name}!")
        # panggil method dari method lain
        enemy.take_damage(damage)

    def __str__(self):
        status = "Hidup"
        if self.hp <= 0:
            status = "☠️  Tereliminasi"
        return f"{self.name} {self.job} | HP: {self.hp} | Status: {status}"



# buat objek / summon hero-hero ke loby
zilong = Hero("Zilong", "Fighter", 100)
aurora = Hero("Aurora", "Mage", 100)
zilong.attack(aurora, 30)
print(aurora)
aurora.attack(zilong, 5)
aurora.attack(zilong, 5)
aurora.attack(zilong, 5)
aurora.heal()
print(aurora)
print()
print('Skill 1 : Spear Flip!')
zilong.attack(aurora, 70)
zilong.heal()
print(zilong)
print()