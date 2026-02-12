class Keranjang:

    def __init__(self):
        self.__items = []

    def tambah_barang(self, barang: object, jumlah: int):
        if jumlah <= 0:
            raise ValueError("niat beli kaga?  kalo beli jumlahnya yang bener")

        if jumlah > barang.stok:
            raise ValueError("Stok tidak mencukupi, maaf!")

        self.__items.append((barang, jumlah)) # menyimpan barang dan jumlahnya kedalam keranjang

    def hitung_total(self):
        total = 0 # Awalnya 0 karena belum dijumlahkan.
        for barang, jumlah in self.__items: # Ambil satu per satu isi keranjang, lalu pisahkan jadi: barang & jumlah
            total += barang.harga * jumlah
        return total # Mengembalikan hasil total belanja ke luar method.

    def checkout(self):
        for barang, jumlah in self.__items: # sama kaya di atas
            barang.kurangi_stok(jumlah) # Suruh object (Barang) mengurangi stoknya sebanyak (jumlah)

    def tampilkan_keranjang(self):
        for barang, jumlah in self.__items: # sama kaya di atas juga
            print(f"{barang.nama} x{jumlah} = {barang.harga * jumlah}")
