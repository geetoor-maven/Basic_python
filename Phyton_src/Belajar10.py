# Belajar Tuple 
# Tuple Konsepnya Hampir sama dengan List akan tetapi Data tuple sekali di deklarasikan maka data tidak boleh di rubah

# Contoh deklarasi pada tuple 

#print("\n")
coconut = ("Bp","Ang 1","Ang 2","Ang 3","Ang 4","Ang 5","Ang 6","Ang 7","Ang 8","Ang 9","Ang 10")

# di sini saya cuma menampilkan saja karena ingat Tuple itu data nya tidak bisa di ubah

for a in range(0,len(coconut)):
    print(coconut[a])


# Belajar set
# Beda dengan tuple dan list , type set merupakan data yang apabila terdapat data yang sama maka data yang satunya akan di hapus

# Data akan berpindah pindah jika program set di jalankan
datanama = {"Agus","Ikbal","Fathur","Wawan","Najwa"}

print(datanama)
# Untuk tipe set itu tidak mendukung mengambil data melalui index karena akan terjadi error kecuali melalui for loop
# disini saya akan membuat perintah untuk menambahkan data melalui looping
berapadata = int(input("Masukkan berapa data : "))
for b in range(0,berapadata):
    datanya = str(input("Masukkan nama : "))
    datanama.add(datanya)

for data in datanama:
    print(data)

hapus = str(input("Masukan nama yang ingin di hapus : "))
datanama.remove(hapus)

print('-----------------------------------------')
print('-----------------from--------------------')
print('----------- shegi-developer -------------')