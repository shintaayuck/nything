N-YTHING
========

N-ything problem merupakan modifikasi N-queen problem. Perbedaannya, buah catur yang menjadi pertimbangan bukan hanya ratu (*queen*), namun juga meliputi kuda (*knight*), gajah (*bishop*), dan benteng (*rook*). 
Seperti N-queen problem, permasalahan dari N-ything problem adalah mencari susunan buah-buah catur pada papan catur berukuran 8x8 dengan jumlah buah catur yang menyerang buah catur lain minimum.

Program berguna untuk membentuk susunan buah catur paling optimal sehingga jumlah pasangan terurut (​p​, ​q)​ di mana ​p menyerang ​q,​ minimum bila ​p dan ​q​ berwarna sama, maksimum bila ​p​ dan ​q​ berbeda warna.  Adapun sifat penyerangan ini mengikuti sifat penyerangan pada permainan catur pada umumnya. Misalnya, sebuah benteng dapat menyerang buah catur lain yang berada pada jalur vertikal/horizontal apabila buah catur tersebut tidak terhalang oleh buah catur lainnya, dan seterusnya.

Program diimplementasikan dalam 3 algoritma, yaitu :
1. Hill climbing
2. Simulated annealing
3. Genetic algorithm


# Input :
```
 <warna> <jenis buah catur> <jumlah> 
```
Keterangan : Jumlah setiap buah catur (​knight​, ​bishop​, ​rook​, ​queen)​ berupa bilangan bulat tak negatif. Jumlah seluruh buah catur pasti kurang dari 64.

# Output :
Susunan buah-buah catur, pada baris terakhir, tertulis 2 buah angka ​a dan ​b​, di mana ​a adalah jumlah bidak catur yang menyerang bidak sewarna, dan ​b adalah jumlah bidak catur yang menyerang bidak berbeda warna. Bidak warna berwarna hitam direpresentasikan dengan huruf kecil, sedangkan warna putih direpresentasikan dalam huruf kapital.
