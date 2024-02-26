# no1 

# print("No.1")

# print("Variabel Yang Benar")

# alat_tulis = 'buku'
# alat_tulis = 10



# a = float(input("Masukan panjang sisi a  (sisi alas) :"))
# b = float(input("Masukan panjang sisi b  (sisi tumpuan) :"))
# t = float(input("Masukan tinggi trapesium :"))

# luas = 0.5 * (a+b) * t

# keliling = a + b + 2 * ((a**2 + b**2)**0.5)

# print("Luas Trapesium : ",luas)
# print("Keliling Trapesium : ",keliling)



angka1 = float(input("Masukan angka 1 : "))

angka2 = float(input("Masukan angka 2 :"))

operator = input("Pilih operator (+, -, /, **) :")

print("Angka pertama : ", angka1)
print("Angka kedua :", angka2)

if operator == "+" :
    hasil = angka1 + angka2
elif operator == "-" :
    hasil = angka1 - angka2 
elif operator == "*" :
    hasil = angka1 * angka2
elif operator == "/" : 
    if angka2 != 0 :
        hasil = angka1 / angka2
    else: 
        print("Error! pembagian dengan 0 tidak diizinkan.")
        exit()
    
print("Hasil operator: ", angka1, operator, angka2, "=", hasil)





