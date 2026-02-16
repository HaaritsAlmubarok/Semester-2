from admin import Admin
from santri import Santri
from barang import Barang
from keranjang import Keranjang



# ================= VALIDASI INPUT ANGKA =================

def input_angka(pesan):
    while True: # di ulang terus sampai inputnya bener
        try:
            angka = int(input(pesan)) # kalo ketik huruf bakal error
            if angka < 0:
                print("\n Pilih 1 - 3 aja...")
            else:
                return angka
        except ValueError:
            print("\n Masukin angka woi!") # jika error program akan menampilkan pesan ini (tidak crash)



# ================= TAMPILKAN BARANG =================

def tampilkan_barang(daftar_barang):
    print("\n=== DAFTAR MAKANAN ===")
    for i, barang in enumerate(daftar_barang): # enumerate = menampilkan index barang (nomer urut) beserta isinya
        print(f"{i+1}. {barang.nama} | Harga: {barang.harga} | Stok: {barang.stok}")

    # Menampilkan semua barang yang tersedia di toko beserta harga dan stoknya.



# ================= MENU ADMIN =================

def menu_admin(admin, daftar_barang):
    while True: # program ngulang terus sampai admin pilih logout
        print("\n   === MENU ADMIN ===\n")
        print("1. Tambah Makanan Baru")
        print("2. Tambah Stok")
        print("3. Lihat Daftar Makanan")
        print("4. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama makanan: ")
            harga = input_angka("Harga: ")
            stok = input_angka("Stok: ")

            makanan_baru = Barang(nama, harga, stok) # bikin object baru dari class Barang
            admin.tambah_barang_baru(daftar_barang, makanan_baru)

            print("Makanan berhasil ditambahkan!")

        elif pilihan == "2":
            if not daftar_barang:
                print("Belum ada makanan!")
                continue # continue = Melewati sisa kode di iterasi sekarang (lalu langsung lanjut ke iterasi berikutnya)

            tampilkan_barang(daftar_barang)
            index = input_angka("Pilih nomor makanan: ") - 1 # -1 karena index di list mulai dari 0

            if 0 <= index < len(daftar_barang):
                jumlah = input_angka("Jumlah stok tambahan: ")
                admin.tambah_stok_barang(daftar_barang[index], jumlah)
                print("Stok berhasil ditambahkan!")
            else:
                print("\n Isi yang bener...!")

        elif pilihan == "3":
            tampilkan_barang(daftar_barang)

        elif pilihan == "4":
            break # menghentikan while True dan keluar dari menu admin

        else:
            print("\n Pilih yang ada di layar woi...!")



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

        # ===== Lihat Daftar Makanan =====
        if pilihan == "1":
            tampilkan_barang(daftar_barang)

        # ===== Tambah ke Keranjang =====
        elif pilihan == "2":
            if not daftar_barang:
                print("\n Belum ada makanan!")
                continue

            tampilkan_barang(daftar_barang)
            index = input_angka("Pilih nomor makanan: ") - 1 # -1 = index di list mulai dari 0

            if 0 <= index < len(daftar_barang):
                jumlah = input_angka("Jumlah beli: ")
                try:
                    keranjang.tambah_barang(daftar_barang[index], jumlah)
                    print("Berhasil ditambahkan ke keranjang!")
                except ValueError as e: # e = variabel untuk menyimpan error
                    print(e)
            else:
                print("\n Belajar ngtik dulu...!")

        # ===== Checkout =====
        elif pilihan == "3":
            total = keranjang.hitung_total()

            if total == 0:
                print("\n Keranjang masih kosong!")
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

        # ===== Logout =====
        elif pilihan == "4":
            break

        else:
            print("\n Pilih yang bener...!")



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


    while True: # program terus berjalan sampai user pilih keluar
        print("\n\n      === SISTEM TOKO MAKANAN PONDOK ===\n")
        print("1. Login Admin")
        print("2. Login Santri")
        print("3. Keluar")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            # verifikasi admin
            password = input("Masukkan password admin: ")
            if admin.cek_password(password):
                menu_admin(admin, daftar_barang)
            else:
                print("\n Password salah!")

        elif pilihan == "2":
            # verifikasi santri
            password = input("Masukkan password santri: ")
            if santri.cek_password(password):
                menu_santri(santri, daftar_barang)
            else:
                print("\n Password salah!")

        elif pilihan == "3":
            print("\n               === Program selesai ===")
            print("   ================ Terima Kasih! ================\n")
            break

        else:
            print("\n Isi yang bener...!")


# Jalankan fingsi main hanya jika file ini dijalankan langsung bukan diimpor sebagai modul
if __name__ == "__main__":
    main()
