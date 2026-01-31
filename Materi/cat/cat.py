# di awali class namaClas
class Cat:
    # self = dirinya sendiri / internal class
    # __init__ = constructor
    # fungsi yg pertama kari di panggil
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    # method = fungsi di dalam class
    def sleep(self, duration):
        print(f"turu {duration} menit")

# buat objek dari class cat
belang = Cat ("mix", 5)
oyen = Cat ("orange",3)
# print("obj belang:", belang)
# print("obj oyen:", oyen)
print()
belang.sleep(10)
oyen.sleep(5)
print()
print(f"warna si belang: {belang.color}")
print(f"berat si belang: {belang.weight} kg")
print()
print(f"warna si oyen: {oyen.color}")
print(f"berat si oyen: {oyen.weight} kg")
print()