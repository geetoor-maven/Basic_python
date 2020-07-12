# Kali ini saya akan membuat parameter dalam python

# parameter adalah sebuah variabel yang di sisipkan ke dalam method contoh :

def Hello(nama):
    print("Nama kamu",nama)

Hello("Agus kurniawan")

# Dan ada juga cara untuk membolak balikkan parameter
# misalnya 

def Say(nama_kamu = "",nama_pacar = ""):
    print("Nama kamu",nama_kamu,"- Nama pacar kamu ",nama_pacar)

# disini meski kita tidak berikan nilai ke dalam parameternya itu tidak aka terjadi error karena di defenisi methodnya sudah kita deklarasikan nilainya
Say()

# sebaliknya di sini saya akan memberikan nilai kepada parameter Say meski suda di defenisikan di method nya 
Say("Agus kurniawan","Wiwi")

# nah untuk anda yang indin membolak balikkan nilai parameternya dapat langsung mengaksses variabel parameter yang telah didefenisikan di method nya
Say(nama_pacar="Widya",nama_kamu="AL bandru")

print("\n Contoh parameter pertambahan \n")

def Tambah(nilai1,nilai2):
    total = nilai1 + nilai2
    print("Total pertambahan di atas adalah :",total)


a = int(input("Masukkan nilai pertama :"))
b = int(input("Masukkan nilai kedua :"))

Tambah(a,b)

print("\n")

# Belajar argument parameter = list *

def Perkalian(*kali):
    hasil = 0
    for angka in kali:
        hasil = hasil + angka
    print("Angka ke :",kali," :",hasil)

Perkalian(30,20)


print('-----------------------------------------')
print('-----------------from--------------------')
print('----------- shegi-developer -------------')