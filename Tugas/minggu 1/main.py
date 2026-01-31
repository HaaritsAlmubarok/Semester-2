data = []


# ===== Menu Pertama =====

def tambah_data():
    id_data = int(input("Masukkan ID: "))
    nama = input("Masukkan Nama: ")
    kelas = input("Masukkan Kelas: ")
    hobi = input("Masukkan Hobi: ")

    data.append({
        "id": id_data,
        "nama": nama,
        "kelas": kelas,
        "hobi": hobi
    })
    print()
    print("=============================")
    print("✅ Data berhasil ditambahkan")
    print("=============================\n")



# ===== Menu Kedua =====

def tampil_data():
    if len(data) == 0:
        print()
        print("=====================")
        print("⚠️ Data masih kosong")
        print("=====================\n")
        return

    print("\nID\tNama\tKelas\tHobi")
    for d in data:
        print(f"{d['id']}\t{d['nama']}\t{d['kelas']}\t{d['hobi']}")
    print()



# ===== Menu Ketiga =====

def ubah_data():
    id_cari = int(input("Masukkan ID yang ingin diubah: "))
    for d in data:
        if d["id"] == id_cari:
            d["nama"] = input("Nama baru: ")
            d["kelas"] = input("Kelas baru: ")
            d["hobi"] = input("Hobi baru: ")
            print()
            print("========================")
            print("✅ Data berhasil diubah")
            print("========================\n")
            return
    print()
    print("=======================")
    print("❌ Data tidak ditemukan")
    print("=======================\n")



# ===== Menu Keempat =====

def hapus_data():
    id_cari = int(input("Masukkan ID yang ingin dihapus: "))
    for d in data:
        if d["id"] == id_cari:
            data.remove(d)
            print()
            print("=========================")
            print("✅ Data berhasil dihapus")
            print("=========================\n")
            return
    print()
    print("=======================")
    print("❌ Data tidak ditemukan")
    print("=======================\n")

# =========================
# MENU UTAMA
# =========================
while True:
    print()
    print("====== MENU ======\n")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("0. Keluar\n")

    pilihan = input("Pilih menu: ")
    print()

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampil_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "0":
        print()
        print("==============================")
        print("===== 👋 Program selesai =====")
        print("==============================")
        break
    else:
        print()
        print("=======================")
        print("⚠️ Pilihan tidak valid")
        print("=======================\n")
