from tank import Tank
from fighter import Fighter
from assassin import Assassin
from mage import Mage
from marksman import Marksman
from support import Support

from goblin import Goblin
from rajanaga import RajaNaga

print("\n📖 === LEGENDA PAHLAWAN ELDORITA === 📖\n")
print("🌍 Di benua Eldorita, kedamaian telah lama sirna.")
print("🌙 Di malam yang gelap, pasukan goblin menyerang desa-desa kecil.")
print("👥 Pasukan Goblin yang kejam mengancam desa-desa kecil.")
print("👹 Goblin menguasai desa-desa kecil.")
print("🐲 Dan di puncak Gunung Api, Raja Naga Kuno tertidur menunggu mangsa...\n")

# ===============================
# 🧙‍♂️ PEMANGGILAN PAHLAWAN
# ===============================
tank = Tank("Tigreal", 300)
fighter = Fighter("Zilong", 220)
assassin = Assassin("Hayabusa", 180)
mage = Mage("Eudora", 170)
marksman = Marksman("Claude", 190)
support = Support("Rafaela", 200)
team = [tank, fighter, assassin, mage, marksman, support]

print("\n🗣️  Tigreal: Demi Eldorita, aku akan berdiri di garis depan!")
print("🗣️  Zilong: Pedangku takkan ragu!")
print("🗣️  Rafaela: Cahaya suci akan melindungi kita...\n")

# ===============================
# 🟢 PHASE 1 — SERANGAN GOBLIN
# ===============================
print("\n👹 === SERANGAN GOBLIN DI DESA UTARA === 👹\n")

goblin = Goblin()

print("📜 Di tengah desa yang terbakar, Goblin muncul dengan tawa mengerikan.")
print("🗣️  Goblin: HEHE! EMAS! DARAH! SEMUANYA MILIK KAMI!\n")

fighter.combo(goblin)

print("\n🗣️  Zilong: Serangan pertamaku mengenai sasaran!")
assassin.stealth_attack(goblin)

print("\n🗣️  Hayabusa: Bayangan tak pernah meleset...")

print("\n👹 Goblin yang terluka membalas dengan brutal!")
goblin.attack(tank)

print("\n🗣️  Tigreal: Seranganku tidak akan goyah!")
tank.fortify()

mage.fireball(goblin)

print("\n🗣️  Eudora: Rasakan murka petir!")

marksman.rapid_fire(goblin)
marksman.satuhit(goblin)

print("\n🗣️  Claude: Target dijatuhkan!")

print("\n📜 Goblin tumbang. Desa terselamatkan.")
print("📜 Namun… dari kejauhan, tanah mulai bergetar.\n")

# ===============================
# 🔥 PHASE 2 — KEBANGKITAN RAJA NAGA
# ===============================
print("\n🔥 === GUNUNG API — SARANG RAJA NAGA === 🔥\n")

dragon = RajaNaga()

print("📜 Langit menggelap. Lava mengalir di sela bebatuan.")
print("🐲 Raja Naga: MAKHLUK KECIL...")
print("🐲 Raja Naga: KALIAN TELAH MEMBANGUNKANKU!\n")

tank.fortify()
print("\n🗣️  Tigreal: Aku akan menahan serangannya! MAJU!")

fighter.ultimate(dragon)

print("\n🗣️  Zilong: Demi kehormatan!")

mage.ultimate(dragon)

print("\n📜 Raja Naga mengaum keras, mengguncang gunung!")
dragon.attack(tank)

print("\n🗣️  Rafaela: Jangan menyerah! Cahaya, sembuhkan mereka!")
support.heal_team(team)

assassin.ultimate(dragon)

print("\n🗣️  Hayabusa: Satu tebasan terakhir dari bayangan!")

# ===============================
# 😡 CUTSCENE — MODE BRUTAL
# ===============================
print("\n📜 Di tengah pertarungan sengit...")
print("📜 Darah Raja Naga menipis.")
print("📜 Nafasnya membara, matanya menyala merah.\n")

print("🐲 Raja Naga: CUKUP!!!")
print("🐲 Raja Naga: AKU AKAN MEMUSNAHKAN KALIAN SEMUA!!!")

dragon.fire_breath(team)

print("\n🗣️  Claude: Kita hampir kehabisan waktu!")
marksman.rapid_fire(dragon)

print("\n🗣️  Eudora: Ini kesempatan terakhir!")
mage.ultimate(dragon)

print("\n📜 Raja Naga terhuyung...")
print("📜 Sayapnya terbakar, tubuhnya mulai runtuh.\n")

marksman.ultimate(dragon)

# ===============================
# 🏆 ENDING
# ===============================
print("\n🏆 === RAJA NAGA TELAH DIKALAHKAN === 🏆")
print("🌅 Api padam, gunung kembali tenang.")
print("📜 Nama Tigreal, Zilong, Hayabusa, Eudora, Claude, dan Rafaela")
print("📜 akan dikenang sebagai PAHLAWAN ELDORITA SELAMANYA.\n")
