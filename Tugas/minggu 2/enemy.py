class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.damage = damage
        print(f"👹 Musuh {self.name} muncul! HP: {self.hp}/{self.max_hp}")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

        print(f"⚔️  {self.name} menerima {damage} damage | HP: {self.hp}/{self.max_hp}")

        if self.hp == 0:
            print(f"💀 {self.name} telah dikalahkan!")

    def attack(self, hero):
        print(f"👹 {self.name} menyerang {hero.name}!")
        hero.take_damage(self.damage)
