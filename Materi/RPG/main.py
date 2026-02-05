from colorama import Fore, Back, Style, init
from marksman import Marksman
from fighter import Fighter
from monster import Monster
from support import Support
from mage import Mage

# auto reset warna (biar gak ngefek ke print selanjutnya)
init(autoreset=True)
print(Fore.GREEN + Back.WHITE + Style.BRIGHT + "\n========== Selamat datang di Game RPG OOP ==========")
print()

zilong = Fighter("zilong", 100)
ewdora = Mage("Ewdora", 100)
estes = Support("Estes", 100)
dragon = Monster("dragon", 1000)
batrix = Marksman("Batrix", 100)

print(zilong)
print(ewdora)
print(estes)
print(batrix)
print(dragon)

# # zilong.ultimate(dragon)
# # print(f"ambil hp hero : {zilong.__hp()}")
# # zilong.set_hp(1000)
# ambil atribut private via gatter
print(f"HP Ewdora: {ewdora.hp}")
print(f"HP Zilong: {zilong.hp}")
# # ewdora.ultimate(dragon)
# zilong.combo(dragon)
# ewdora.combo(dragon)
# dragon.attack(zilong, 50)
# dragon.attack(ewdora, 70)
# dragon.attack(estes, 30)
# dragon.attack(batrix, 40)


# print(zilong)
# print(ewdora)
# print(estes)
# print(batrix)
# print(dragon)

running = True
while running:
    print("== Status Monster == ")
    print(dragon)
    print("\nPilih Aksi :")
    print("💠 1. Attack")
    print("💠 2. Ultimate")
    print("💠 3. Heal")
    print("💠 4. Exit\n")

    try:
    # ambil inputan user
        aksi = int(input("Aksi Mu : "))
    except ValueError:
        print("⚠️  Input tidak valid, masukkan angka woi..!\n")
        continue

    # buat list party
    raid_party = [zilong, ewdora, estes, batrix,]
    # attack_party = [20, 15, 10, 40] # damage masing-masing hero
    if aksi == 1:
        for party in raid_party:
            party.attack(dragon, 50)
        # cek aksi monster kalau 0 selesai
        if dragon.hp == 0:
            running = False
            print("🏆 Monster Telah Tereliminasi, Kamu Menang!\n")
            break

    elif aksi == 2:
        for party in raid_party:
            party.ultimate(dragon)
        # cek aksi monster kalau 0 selesai
        if dragon.hp == 0:
            running = False
            print("🏆 Monster Telah Tereliminasi, Kamu Menang!\n")
            break

    elif aksi == 3:
        for party in raid_party:
            party.heal()

    elif aksi == 4:
        running = False
        print("👋 Terima Kasih telah bermain!\n")

    else:
        print("⚠️  Aksi tidak tersedia\n")