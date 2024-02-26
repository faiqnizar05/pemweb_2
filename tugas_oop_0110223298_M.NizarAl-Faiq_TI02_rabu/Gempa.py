class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("Dampak gempa tidak berasa")
        elif 2 <= self.skala < 4:
            print("Dampak gempa: bangunan retak-retak")
        elif 4 <= self.skala < 6:
            print("Dampak gempa: bangunan roboh")
        else:
            print("Dampak gempa: bangunan roboh dan berpotensi tsunami")

# Contoh penggunaan kelas Gempa
lokasi_gempa = "Wilayah X"
skala_gempa = 5.5

gempa_terjadi = Gempa(lokasi_gempa, skala_gempa)
gempa_terjadi.dampak()
