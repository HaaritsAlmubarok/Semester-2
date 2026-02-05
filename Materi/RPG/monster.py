# return type data suatu fungsi / method
# tambahkan di akhir ->  'def namaFungsi(self) -> tipeData:'
class Monster:
    def __init__(self, name : str, hp : int):
        self.name = name
        self.hp = hp
        print(f"🐉 Monster {self.name} telah summon!")

    def take_damage(self, damage : int):
        self.hp -= damage
        print(f"💥 {self.name} menerima {damage} damage")
        print(f"🩸 Sisa hp: {self.hp}\n")
        if self.hp <= 0:
            print(f"☠️  Monster {self.name} telah tereliminasi!")
            return False # Gagal
        return True  # Berhasil

    def attack(self, enemy, damage : int):
        print()
        print(f"⚔️  {self.name} menyerang {enemy.name}!")
        # panggil method dari method lain
        enemy.take_damage(damage)

    # fungsi untuk menampilkan informasi monster
    def __str__(self) -> str:
        status = "Hidup"
        if self.hp <= 0:
            status = "☠️  Tereliminasi"
        return f"{self.name} | HP: {self.hp} | Status: {status}"
