class Barang:

    def __init__(self, nama: str, harga: float, stok: int):
        self.nama = nama
        self.harga = harga
        self.__stok = stok  # private attribute

    @property
    def stok(self):
        return self.__stok
    # orang luar bisa lihat stok, tapi gak bisa ubah langsung

    def tambah_stok(self, jumlah: int):
        self.__stok += jumlah

    def kurangi_stok(self, jumlah: int):
        if jumlah <= self.__stok:
            self.__stok -= jumlah
        else:
            raise ValueError("Stok habis, maaf!")
