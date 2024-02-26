# a = [1,2,3,4,5]
# nama = ["reza" , "miya" ,"miya","jaka"]
# profil = ["01234","reza" ,19,60.7,172]
# nama = ["zilong", "miya", "layla"]

# # menambahkan
# profil.insert(2,"pria")

# # menambahkan bagian belakang
# nama.append("baxia")
# # menghapus
# profil.remove (60,7)

# # menghapus sesuai nomor
# nama.pop(3)

# jumlahlist = a + nama

# print(profil)
# print(nama)

# print(jumlahlist)

# match 

# cuaca = input ("input cuaca pada hari ini ?")

# match cuaca :
#     case "panas":
#         print ("ke kampus memakai mobil")
#     case "hujan" :
#         print ("ke kampus memakai jas hujan")
#     case "badai" :
#         print ("tidak berangkat ke kampus")
#     case _:
#         print ("tetap berangkat kekampus")     


#pakai int
# a = int (input ("Masukan bilangan 1")) #4
# b = int(input ("Masukan bilangan 2")) #5

# c = a + b  #45
# print(c)



# a = int (input ("Masukan Jari-jari ?")) #4
# b = int(input ("Masukan bilangan 2 ?")) #5

# luasL = 3, 14 * a * a
# print(luasL)



# Tugas
# 1. Buatlah variabel list dengan value : [namaKendaraan,JenisKendaraan,ccKendaraan,warna kendaraan, rodakendaraan]
# tambahkan dari list tersebut dibelakang dengan value : [harga kendaraan, tipe kendaraan ]
# tambahkan setelah jenis kendaraan dengan value : [ merk kendaraan]

2. # latihan 2 : Buat program python dengan match case untuk menghitung luas bangun datar : 
# jika pilih 1 maka menghitung luas persegi. 
# jika pilih 2 maka menghitung luas lingkaran. 
# jika pilih 3 maka menghitung luas segitiga
# selain pilih di atas, maka keterangan:salah pilih angka 






# jawab :

# 1.
# Membuat variabel list dengan nilai awal
Transportasi = ["namaKendaraan", "JenisKendaraan", "ccKendaraan", "warnaKendaraan", "rodaKendaraan"]

# Menambahkan nilai ke dalam list (dibelakang)
Transportasi.extend(["hargaKendaraan", "tipeKendaraan"])

# Menambahkan nilai setelah JenisKendaraan
indeks_jenis_transportasi = Transportasi.index("JenisKendaraan")
Transportasi.insert(indeks_jenis_transportasi + 1, "merkKendaraan")

# Menampilkan list kendaraan setelah ditambahkan nilai
print(Transportasi)

#2
# pilihan = input 

# match pilihan :
#     case "1" :
#         print("kamu memilih 1 untuk menghitung luas persegi")
#         sisi = int(input("masukan sisi ?"))
#         luasP = sisi * sisi
#         print ("Luas persegi yang sisinya",sisi,"adalah",luasP)
#     case "2" :
#          print("kamu memilih 2 untuk menghitung luas lingkaran")
#          jari2 = float(input("masukan jari2"))
#          luasL = 3.14 * jari2 * jari2
#          print = "luas lingkaran yang jari2nya",jari2,"adalah"int(luasL)
#     case "3"
#         print ("kami memilih 3 untuk menghitung luas segitiga")
#         alas = int(input("masukan alas ?"))
#         tinggi = int(input("masukan tinggi ?"))
#         luasS = 0.5 * alas * tinggi 
#         print ("luas segitiga yang alasnya ", alas,"dan tingginya", tinggi,"adalah")
#     case _:
#         print("salah memilih pilihan ?")

#luas persegi
ket = """masukkan pilihan:
1. untuk menghitung luas persegi
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga
"""
pilihan = input (ket)

match pilihan:
    case "1":
        print ("memilih 1 untuk menghitung luas persegi")
        sisi = int (input("masukan sisi?"))
        luasp = sisi * sisi
        print ("luas persegi yang sisinya",sisi,"adalah",luasp)

    case "2":
        print ("memilih 2 untuk menghitung luas lingkaran")
        jari2 = float (input("masukkan jari2?"))
        luasL = 3.14*jari2*jari2
        print("luas lingkaran yang jari2nya",jari2,"adalah",int(luasL))

    case "3":
        print ("memilih 3 untuk menghitung luas segitiga")
        alas = float (input("masukkan panjang alas segitiga:"))
        tinggi = float (input("masukkan tinggi segitiga"))
        luasS = 0.5*alas*tinggi
        print("luas segitiga yang alasnya",alas,"dan tingginya",tinggi,"adalah",luasS)
    case _:
        print("salah memilih pilihan")









