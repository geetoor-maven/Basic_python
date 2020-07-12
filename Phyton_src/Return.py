# disini kita akan belajar tentang method function yang mengembalikan nilai (return)

def Nilai_kembali(angka1,angka2):
    hasil = angka1 * angka2
    return hasil

angka1 = int(input("Masukan angka1 :"))
angka2 = int(input("Masukan angka2 :"))

# di sini kita deklarasikan kembali variabel hasil dan memproses method function Nilai_kembali agar masuk di variabel hasil
hasil = Nilai_kembali(angka1,angka2)

#lalu print hasil
print("Total Perkalian : ",hasil)

print("\n --- Menjumlahkan lalu return list dan total ---- \n")

def Menjumlahkan(*listt):
    total = 0
    for angka in listt:
        total = total + angka
    return (listt,total)

listt,total = Menjumlahkan(10,10,10)

print("Angka :",listt," Total : ",total)