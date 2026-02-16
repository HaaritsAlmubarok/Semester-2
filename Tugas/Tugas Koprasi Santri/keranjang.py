class Keranjang:

    def __init__(self):
        self.__items = [] # [] = list kosong, untuk menyimpan (barang, jumlah) dalam bentuk tuple.
        # items 👆 = atribut

    def tambah_barang(self, barang: object, jumlah: int):
        if jumlah <= 0:
            raise ValueError("niat beli kaga?  kalo beli jumlahnya yang bener")

        if jumlah > barang.stok:
            raise ValueError("Stok tidak mencukupi, maaf!")

        self.__items.append((barang, jumlah)) # menyimpan barang dan jumlahnya kedalam keranjang

    def hitung_total(self):
        total = 0 # 0 = karena belum dijumlahkan.
        for barang, jumlah in self.__items: # Ambil satu per satu isi keranjang, lalu pisahkan jadi: barang & jumlah
            total += barang.harga * jumlah
        return total # Mengembalikan hasil total belanja ke luar method (dikirim kembali ke kode yang menjalankan (memanggil) method itu)

    def checkout(self):
        for barang, jumlah in self.__items: # sama kaya di atas
            barang.kurangi_stok(jumlah) # Suruh object (Barang) mengurangi stoknya sebanyak (jumlah)
