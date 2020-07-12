# disni kelas aplikasi dan saya akan memanggil method dari kelas Objek.py

# cara memenggilnya dengan menggunakan keyword import
import Objek

# bagaimana kalau di kelas objek.py memiliki ratusan method? pastinya anda tidak memanggil semuanya
# di sini ada cara untuk memanggil method tertentu yng ingin di pakai dari kelas objek.py
from Objek import Muncul_nama

# method muncul nama ini berasal dari kelas objek.py
Objek.Muncul_nama("Agus Kurniawan")
# tanpa memanggil objek
Muncul_nama("Shegi - dev")

angka1 = int(input("Masukan angka pertama : "))
angka2 = int(input("Masukan angka kedua : "))

Objek.Penambahan(angka1,angka2)
print("Total dari semua penambahan : ",Objek.Penambahan(angka1,angka2))