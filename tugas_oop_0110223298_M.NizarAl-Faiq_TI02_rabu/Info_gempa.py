# Isi dari file info_gempa.py
from Gempa import Gempa

# Membuat 5 objek Gempa sesuai permintaan
gempa_banten = Gempa("Banten", 1.2)
gempa_palu = Gempa("Palu", 6.1)
gempa_cianjur = Gempa("Cianjur", 5.6)
gempa_jayapura = Gempa("Jayapura", 3.3)
gempa_garut = Gempa("Garut", 4.0)

# Memanggil method dampak() untuk setiap objek Gempa
print("Dampak Gempa di Banten:")
gempa_banten.dampak()

print("\nDampak Gempa di Palu:")
gempa_palu.dampak()

print("\nDampak Gempa di Cianjur:")
gempa_cianjur.dampak()

print("\nDampak Gempa di Jayapura:")
gempa_jayapura.dampak()

print("\nDampak Gempa di Garut:")
gempa_garut.dampak()
