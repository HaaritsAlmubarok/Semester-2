# print = output data ke terminal
print("Hello World!")
print("=" * 40)
# tipe data python
name = "Made Suryana" # string (text)
age = 20 # intiger (number)
married = False # boolean (true/false)
print(f"{name}, umur {age} tahun")
namaBali = ["wayan","made","kadek","putu"]
print(namaBali)
print("=" * 40)
# fungsi di awali kata def
# def namaFungsi (parameter-parameter)
def halo(name, city):
    print(f"Halo {name}, asal {city}")
    print("-" * 35)
# panggil namaFungsi di luar def
halo("mas udin", "solo")
halo("mbak sinta", "sunda")