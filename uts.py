print("no1")
# input nama kendaraan 
nama_kendaraan  = input("Nama Kendaraan ? contoh : Mobil dan Motor ? " )

jenis_bensin  = input("Jenis Bensin ? (Pertalite, Pertamax, Pertamax Turbo ?)")

kota_tujuan = input("Kota yang dituju? :")


# Menentukan Harga per liter dan jarak  Tempuh Perliter sesuai  jenis bensin

if jenis_bensin == "Pertalite" :
    harga_per_liter = 10000
    jarak_tempuh_per_liter = 12 
elif jenis_bensin == "Pertamax":
    harga_per_liter = 14000
    jarak_tempuh_per_liter = 13
elif jenis_bensin == "Pertamax Turbo":
    harga_per_liter =  17000 
    jarak_tempuh_per_liter = 13.5

# Nentuin Jarak 
if kota_tujuan == "Jakarta": 
    jarak_kota = 20
elif kota_tujuan == "Bekasi":
    jarak_kota = 35.7
elif kota_tujuan == "Depok":
   jarak_kota = 5
elif kota_tujuan == "Tanggeran":
    jarak_kota = 99 
elif kota_tujuan == "Bogor":
    jarak_kota = 120.6 

# Hitung
pemakaian_bensin = jarak_kota / jarak_tempuh_per_liter
total_harga_bensin = pemakaian_bensin * harga_per_liter

# Output 

print("Nama Kendaraan :" ,nama_kendaraan)
print("Jenis Bensin :" ,jenis_bensin)
print("Kota Tujuan :" ,kota_tujuan)
print("Pemakaian Bensin :" ,pemakaian_bensin,"liter")
print("Total Harga Bensin :" ,total_harga_bensin, "rupiah")

print("no2")


# Tampilkan Menu Makanan dan Minuman
menu_makanan = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Geprek": 18000
}

menu_minuman = {
    "Aneka Jus": 15000,
    "Soft Drink": 10000,
    "Sweet Ice Tea": 5000
}

# Input Nama Pembeli dan No Hp Pembeli
nama_pembeli = input("Masukkan Nama Pembeli: ")
no_hp_pembeli = input("Masukkan No Hp Pembeli: ")

# Pesan Menu Makanan atau Minuman
jenis_pesanan = input("Pesan Menu Apa? (makanan atau minuman): ")

# Tampilkan Menu Sesuai Jenis Pesanan
if jenis_pesanan.lower() == "makanan":
    print("Menu Makanan:")
    for menu, harga in menu_makanan.items():
        print(f"{menu} - Rp. {harga}")
    pesanan = input("Masukkan pesanan: ")
    harga_pesanan = menu_makanan.get(pesanan, 0)
elif jenis_pesanan.lower() == "minuman":
    print("Menu Minuman:")
    for menu, harga in menu_minuman.items():
        print(f"{menu} - Rp. {harga}")
    pesanan = input("Masukkan pesanan: ")
    harga_pesanan = menu_minuman.get(pesanan, 0)
else:
    print("Jenis pesanan tidak valid. Silakan pilih makanan atau minuman.")
    exit()

# Input Jumlah Pesanan
jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

# Hitung Harga Total
harga_total = harga_pesanan * jumlah_pesanan

# Output Informasi Pemesanan
print("\nInformasi Pemesanan:")
print(f"Nama Pembeli: {nama_pembeli}")
print(f"No Hp Pembeli: {no_hp_pembeli}")
print(f"Menu yang di Pesan: {pesanan}")
print(f"Jumlah Pesanan: {jumlah_pesanan}")
print(f"Harga yang harus di bayarkan: Rp. {harga_total}")




print("no3")
for i in range(1, 21):
    print(i)
    if i % 2 != 0:
        print("STT Nurul Fikri")