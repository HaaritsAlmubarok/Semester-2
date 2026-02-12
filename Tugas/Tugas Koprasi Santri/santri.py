from orang import Orang


class Santri(Orang):
    def __init__(self, nama: str, asrama: str, password: str, saldo: int):
        super().__init__(nama, asrama, password)
        self.__saldo = saldo # saldo bersifat private

    @property
    def saldo(self):
        return self.__saldo
    # orang luar bisa lihat saldo, tapi gak bisa ubah langsung
    
    def kurangi_saldo(self, jumlah: int):
        if jumlah <= self.__saldo: # maksudnya = Apakah uang cukup untuk bayar?
            self.__saldo -= jumlah
        else:
            raise ValueError("Saldo tidak cukup, sabar ya!")