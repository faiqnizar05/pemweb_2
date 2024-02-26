# union
set1 = {1,2,3}
set2 = {2,4,6}
set3 = set1.union(set2)
print(set3)

# udpdate
set1 = {1,2,3}
set2 = {2,4,6}
set1.update(set2)
print(set1)


# dictonary
data_diri = {
"nama":"Reza",
"matpel":"DDP"}
data_diri["semester"] = 1
print(data_diri["nama"])


# #  Mengakses dengan key, cth: 
# x = data_diri['nama'] # bisa juga data_diri.get('nama') 
# # ● Mengubah value
# data_diri['nama']="Dian"
# # ● Menambah entri
# data_diri['alamat'] = "Jakarta"
# # ● Menghapus key
# data_diri.pop('alamat')
# # ● Mengecek keberadaan key, pakai operator in
# if('nama' in data_diri):
#     print('nama ada di data_diri')


#1
print("no1")
hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

lulus_saja = []

for nama_mahasiswa in hasil_akhir:
    if nama_mahasiswa['nilai'] > 65:
        lulus_saja.append(nama_mahasiswa['nama'])
print(lulus_saja)


print("no2")
#2 membalik
daftar_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
print(daftar_buah[::-1])

print("no3")
#3 menduplikasi
hasil_duplikasi = []
for buah in daftar_buah:
    hasil_duplikasi += [buah, buah]
print(hasil_duplikasi)

print("no4")
#4 hanya konsonan
def huruf_konsonan(string):
    konsonan = ""
    for alfabet in string:
        if alfabet.isalpha() and alfabet.lower() not in 'aeiou':
            konsonan += alfabet
    return konsonan

string = "Nurul Fikri"
hasil = huruf_konsonan(string)
print(hasil)

