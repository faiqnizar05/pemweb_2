
# class Orang:
#     # PROPERTI 
#     nama="midun"
#     umur="18"

#     # method
#     def __init__(self, name, age): #fungsi init
#         self.nama = name
#         self.umur = age
        
       

 

#     # method
#     def berjalan(self):
#         print("saya bisa berjalan")

# # objek
# mahasiswa = Orang("acong" ,"19 tahun") #fungsi
# print(mahasiswa.nama)
# print(mahasiswa.umur)
# mahasiswa.berjalan()

# # objek 2
# dosen = Orang("Dr. Alfonso", "30 tahun")
# dosen.nama = "Dr. Alfonso"
# print(dosen.nama)



class Bank:
#member1 variabel
    norek = ''
    nama ='' 
    saldo = 0
    jmlNasabah = 0 # variabel static
    BANK = 'Bank Syariah Nurul Fikri' # variabel konstanta
#member2 konstruktor
    def __init__(self,no,nasabah,saldo):
            self.norek = no
            self.nama = nasabah
            self.saldo = saldo
            Bank.jmlNasabah += 1 


    #member3 method
    def nabung(self,uang):
#self.saldo = self.saldo + uang
        self.saldo += uang
    def tarik(self,uang):
#self.saldo = self.saldo - uang
         self.saldo -= uang
    def cetak(self):
        print(Bank.BANK,
                '\n==========================',
                '\nNo. Rekening\t:',self.norek,
                '\nNama Nasabah\t:',self.nama,
                '\nSaldo\t\t: Rp. ',format(self.saldo, ','),
                '\n--------------------------'
)

