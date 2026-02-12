from admin import Admin
from santri import Santri
from barang import Barang
from keranjang import Keranjang


# ================= VALIDASI INPUT ANGKA =================
def input_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))
            if angka < 0:
                print("Angka tidak boleh negatif!")
            else:
                return angka
        except ValueError:
            print("Masukin angka woi!")


# ================= TAMPILKAN BARANG =================
def tampilkan_barang(daftar_barang):
    print("\n=== DAFTAR MAKANAN ===")
    for i, barang in enumerate(daftar_barang):
        print(f"{i+1}. {barang.nama} | Harga: {barang.harga} | Stok: {barang.stok}")


# ================= MENU ADMIN =================
def menu_admin(admin, daftar_barang):
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Tambah Makanan Baru")
        print("2. Tambah Stok")
        print("3. Lihat Daftar Makanan")
        print("4. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama makanan: ")
            harga = input_angka("Harga: ")
            stok = input_angka("Stok: ")

            makanan_baru = Barang(nama, harga, stok)
            admin.tambah_barang_baru(daftar_barang, makanan_baru)

            print("Makanan berhasil ditambahkan!")

        elif pilihan == "2":
            if not daftar_barang:
                print("Belum ada makanan!")
                continue

            tampilkan_barang(daftar_barang)
            index = input_angka("Pilih nomor makanan: ") - 1

            if 0 <= index < len(daftar_barang):
                jumlah = input_angka("Jumlah stok tambahan: ")
                admin.tambah_stok_barang(daftar_barang[index], jumlah)
                print("Stok berhasil ditambahkan!")
            else:
                print("Nomor tidak valid!")

        elif pilihan == "3":
            tampilkan_barang(daftar_barang)

        elif pilihan == "4":
            break

        else:
            print("Pilihan tidak valid!")


# ================= MENU SANTRI =================
def menu_santri(santri, daftar_barang):
    keranjang = Keranjang()

    while True:
        print("\n=== MENU SANTRI ===")
        print("1. Lihat Daftar Makanan")
        print("2. Tambah ke Keranjang")
        print("3. Checkout")
        print("4. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_barang(daftar_barang)

        elif pilihan == "2":
            if not daftar_barang:
                print("Belum ada makanan!")
                continue

            tampilkan_barang(daftar_barang)
            index = input_angka("Pilih nomor makanan: ") - 1

            if 0 <= index < len(daftar_barang):
                jumlah = input_angka("Jumlah beli: ")
                try:
                    keranjang.tambah_barang(daftar_barang[index], jumlah)
                    print("Berhasil ditambahkan ke keranjang!")
                except ValueError as e:
                    print(e)
            else:
                print("Nomor tidak valid!")

        elif pilihan == "3":
            total = keranjang.hitung_total()

            if total == 0:
                print("Keranjang masih kosong!")
                continue

            print(f"Total belanja: {total}")
            print(f"Saldo anda: {santri.saldo}")

            try:
                santri.kurangi_saldo(total)
                keranjang.checkout()
                print("Checkout berhasil!")
                print(f"Sisa saldo: {santri.saldo}")
                break
            except ValueError as e:
                print(e)

        elif pilihan == "4":
            break

        else:
            print("Pilihan tidak valid!")


# ================= MAIN =================
def main():

    daftar_barang = [
        Barang("Aoka  ", 2500, 20),
        Barang("Mikako", 1500, 25),
        Barang("Gabin ", 1500, 15),
        Barang("Nabati", 2000, 30)
    ]

    admin = Admin("Admin", "Kantor", "admin123")
    santri = Santri("Santri", "Asrama Ibnu Katsir", "santri123", 50000)


    while True:
        print("\n      === SISTEM TOKO MAKANAN PONDOK ===\n")
        print("1. Login Admin")
        print("2. Login Santri")
        print("3. Keluar")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            password = input("Masukkan password admin: ")
            if admin.cek_password(password):
                menu_admin(admin, daftar_barang)
            else:
                print("Password salah!")

        elif pilihan == "2":
            password = input("Masukkan password santri: ")
            if santri.cek_password(password):
                menu_santri(santri, daftar_barang)
            else:
                print("Password salah!")

        elif pilihan == "3":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
