class Animal:
    jumlah_kaki = 0
    memiliki_paruparu = ""
    jenis_kulit = ""
    jenis = ""
    BKSDA = "Berikut ini adalah kategori hewan dilindungi"

    def __init__(self, jumlah_kaki, memiliki_paruparu, jenis_kulit, jenis):
        self.jumlah_kaki = jumlah_kaki
        self.memiliki_paruparu = memiliki_paruparu 
        self.jenis_kulit = jenis_kulit
        self.jenis = jenis

    def tambah_jenis(self, golongan):
        self.jenis += golongan

    def cetak(self):
        print(Animal.BKSDA,
              "\n Hewan berkaki dua:", self.jumlah_kaki,
              "\n Alat pernapasan:", self.memiliki_paruparu,
              "\n Jenis kulit:", self.jenis_kulit
              )

# Example usage:
hewan = Animal(2, "Paru-paru", "Bulu", "Mamalia")
hewan.tambah_jenis(" Herbivora")
hewan.cetak()
