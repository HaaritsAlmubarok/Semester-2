# type hinting -> memberi tahu tipe data apa yang akan di gunakan
from __future__ import annotations


from monster import Monster


class Hero :
    # pertama kali di panggil (summon)
    # self = dirinya sendiri / internal
    def __init__(self, name : str, hp : int, job : str):
        self.name = name
        self.job = job
        # __namaAtribut = private attribut
        self.__hp = hp
        print(f"✨ [{self.job}] {self.name} telah di summon!")

    # @property = gatter versi modern
    @property
    def hp(self):
        return self.__hp
    
    #  @namaGatterNya.satter = setter versi modern
    @hp.setter
    def hp(self, value : int):
        if value < 0:
            value = 0
        self.__hp += value  

    # gatter (ambil data attribut private)
    # def get_hp(self):
    #     return self.__hp
    
    # setter (update data attribut private)
    # def set_hp(self, number):
    #     self.__hp += number

    def heal(self):
        print(f"💖 {self.name} healing")
        heal_amount = 20
        self.__hp += heal_amount
        print(f"💊 HP {self.name} bertambah + {heal_amount}")

    def take_damage(self, damage : int):
        # self.__hp = self.__hp - damage (aslinya)
        self.__hp -= damage
        print(f"💥 {self.name} terkena {damage} damage")
        print(f"🩸 Sisa HP : {self.__hp}\n")
        if self.__hp == 0:
            print(f"☠️ {self.name} tereliminasi!")

    def attack(self, enemy : Monster, damage : int):
        print()
        print(f"⚔️  {self.name} menyerang {enemy.name}!")
        # panggil method dari method lain
        enemy.take_damage(damage)

    def ultimate(self, enemy : Monster, damage : int):
        print()
        print(f"🌟 {self.name} menggunakan ultimate!")


    # fungsi untuk menampilkan informasi hero
    def __str__(self) -> str:
        status = "Hidup"
        if self.__hp <= 0:
            status = "☠️  Tereliminasi"
        return f"{self.name} {self.job} | HP: {self.__hp} | Status: {status}"

