# Tugas 
# buatlah sebuah program python yang mengahasilkan nilai dari perbandingan :
# buat program python menggunakan if, elif dan else untuk konversi suhu :
# buat program python untuk menampilkan status mahasiswa berdasarkan keaktifannya
# buat program kalkulator sederhana :
# untuk hasilnya dikumpulkan ke email : ridhobigboy@gmail.com
# maximal pengumpulan malam ini jam 01:00

# jawab

print("No. 1")

x = input ("Masukan nilai x")
y = input ("Masukan nilai y ")

if x > y:
    print("x lebih besar dari y") 
elif x < y:
    print("x kecil dari y")  
else : 
    print("x sama dengan y")




print("No.2")
#buat program python menggunakan if, elif dan else untuk konversi suhu
F = float(input("masukan nilai fahrenheit :"))
C = 5/9 * F - 32
if C<0:
  print("Suhu Rendah")
elif C>0:
  print("Suhu Tinggi")
else:
  print("Suhu Sangat Tinggi atau Suhu Sangat Rendah")




print( "No 3")
# Meminta pengguna memasukkan jumlah kehadiran mahasiswa
jumlah_kehadiran = int(input("Masukkan jumlah kehadiran mahasiswa: "))

# Menentukan status mahasiswa berdasarkan jumlah kehadiran
if jumlah_kehadiran >= 75:
    print("Status mahasiswa: Aktif")
else:
    print("Status mahasiswa: Tidak Aktif")




print("No 4")

# Fungsi untuk penambahan
def tambah(x, y):
    return x + y

# Fungsi untuk pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk perkalian
def kali(x, y):
    return x * y

# Fungsi untuk pembagian
def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Pembagian oleh nol tidak diperbolehkan"

# Menampilkan menu operasi kalkulator
print("Pilih operasi:")
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta input dari pengguna
pilihan = input("Masukkan nomor operasi (1/2/3/4): ")

# Meminta input angka dari pengguna
x = float(input("Masukkan angka pertama: "))
y = float(input("Masukkan angka kedua: "))

# Memproses operasi sesuai dengan pilihan pengguna
if pilihan == '1':
    print("Hasil: ", tambah(x, y))
elif pilihan == '2':
    print("Hasil: ", kurang(x, y))
elif pilihan == '3':
    print("Hasil: ", kali(x, y))
elif pilihan == '4':
    print("Hasil: ", bagi(x, y))
else:
    print("Pilihan tidak valid")





