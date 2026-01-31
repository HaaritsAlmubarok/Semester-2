print()
print("================== Hero Module ==================\n")

class Hero :
    # pertama kali di panggil (summon)
    # self = dirinya sendiri / internal
    def __init__(self, name, hp, job):
        self.name = name
        self.job = job
        # __namaAtribut = private attribut
        self.__hp = hp
        print(f"✨ [{self.job}] {self.name} telah di summon!")

    # gatter (ambil data attribut private)
    def get_hp(self):
        return self.__hp
    
    # setter (update data attribut private)
    def set_hp(self, number):
        self.__hp += number

    def heal(self):
        print(f"💖 {self.name} healing")
        heal_amount = 20
        self.__hp += heal_amount
        print(f"💊 HP {self.name} bertambah + {heal_amount}")

    def take_damage(self, damage):
        # self.__hp = self.__hp - damage (aslinya)
        self.__hp -= damage
        print(f"💥 {self.name} terkena {damage} damage")
        print(f"🩸 Sisa HP : {self.__hp}\n")
        if self.__hp == 0:
            print(f"☠️ {self.name} tereliminasi!")

    def attack(self, enemy, damage):
        print()
        print(f"⚔️  {self.name} menyerang {enemy.name}!")
        # panggil method dari method lain
        enemy.take_damage(damage)

    def ultimate(self, enemy, damage):
        print()
        print(f"🌟 {self.name} menggunakan ultimate!")


    # fungsi untuk menampilkan informasi hero
    def __str__(self):
        status = "Hidup"
        if self.__hp <= 0:
            status = "☠️  Tereliminasi"
        return f"{self.name} {self.job} | HP: {self.__hp} | Status: {status}"

