from Animal import * 

# membuat 
katak = Animal(4, "Memilikki paru-paru', 'TIDAK BERBULU','amfibi")
kucing = Animal(4, "MEMILIKI PARU-PARU', 'TIDAK BERBULU YANG LEBAT','mamalia")
merpati = Animal(2, "'MEMILIKI PARU-PARU', 'TIDAK BERBULU','memiliki bulu untuk terbang','avest'")

print(Animal.BKSDA, 
      "\n==============")
katak.cetak()
kucing.cetak()
merpati.cetak()

      