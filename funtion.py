 
# # funtion
# # def hello():
# #   print("hello saya adalah Nizare")
# #   print("hello saya adalah jon")
# # hello()
# # hello()


# # def say(nama, prodi):
# #   print("nama saya adalah ", nama)
# #   print("program studi saya adalah", prodi)

# # say("ahmad","TI")
# # say("juki","SI")


# def jumlah(a,b):
#     jumlah = a+b 
#     print(jumlah)

# # memanggil funtion
# jumlah(3,50)

# # def say(nama, prodi):
# #   print("nama saya adalah ", nama)
# #   print("program studi saya adalah", prodi)

# # say("ahmad","TI")
# # say("juki","SI")

# def pengali(x):
#     return X*2
# def hitung(sisi):
#     luas = sisi*sisi
#     return luas
# print(hitung(5))


# no #1
def say(nama, prodi, alamat, gender, umur, hoby ):
  print("nama saya adalah " ,nama)
  print("program studi saya adalah" ,prodi)
  print("tempat tinggal saya ada di" ,alamat )
  print("jenis kelamin saya" ,gender )
  print("umur saya" ,umur )
  print("hoby saya" ,hoby )

say("Nizar","TI", "Depok", "Laki-laki", "19tahun", "Futsal,Ngoding")
# no2
def cek_kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif nilai >= 61 and nilai <= 70:
        return "Baik"
    elif nilai >= 71 and nilai <= 80:
        return "Sangat Baik"
    elif nilai >= 81 and nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"
nilai = 100
status = cek_kelulusan(nilai)
print(f"Nilai {nilai} mendapat status: {status}")



# no3
def ganjil(batas):
    print(f"Bilangan ganjil dari 1 sampai {batas}:")
    for i in range(1, batas+1, 2):
        print(i)

# Contoh penggunaan fungsi:
nilai = 100
ganjil(nilai)










  