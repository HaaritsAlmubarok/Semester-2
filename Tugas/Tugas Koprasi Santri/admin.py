from orang import Orang
from barang import Barang


class Admin(Orang):
    def __init__(self, nama: str, asrama: str, password: str):
        super().__init__(nama, asrama, password)
        # super() = panggil metode dari kelas parent

    def tambah_barang_baru(self, daftar_barang: list, barang_baru: Barang):
        daftar_barang.append(barang_baru)
        # Tambahkan object barang_baru ke dalam list daftar_barang
        # append = Menambahkan item ke bagian paling akhir list (baris baru)

    def tambah_stok_barang(self, barang: Barang, jumlah: int):
        barang.tambah_stok(jumlah)
        # Memanggil method tambah_stok dari object barang sebanyak (jumlah) yang diinginkan
