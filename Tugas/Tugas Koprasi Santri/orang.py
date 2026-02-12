class Orang:

    def __init__(self, nama : str,asrama : str, password : str):
        self.nama = nama
        self.asrama = asrama
        self.__password = password

    def cek_password(self, password_input):
        return self.__password == password_input