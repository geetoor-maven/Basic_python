# Belajar while loop

# contoh kecilnya

#inisialisasi variabel str nama
nama = ""

# mengecek apakah nama tidak sama dengan shegi ? 
while nama != "shegi":
    print(" -- Akan berulang apabila namanya bukan shegi -- ")
    nama = input(" -- Masukan nama : ")


# Belajar continue

# melakukan looping berapa data yang ingin di tampilkan 

for i in range(1,101):
    # Nah di sini saya akan menampilkan angka yang genap saja 
    # membandingkan variabel i 
    if i % 2 == 1:
        continue
    print(i)

# Belajar kata kunci break 
# melakukan looping berapa data yang ingin di tampilkan 

for i in range(1,100):
    # di sini saya akan menghentikan program apabila variabel i sudah mencapai 20
    if i % 20 == 0:
        break
    # dan apabila belum tercapai dia akan langsung menuju kesini
    print(i)

# ini juga sama katakunci break 

while True:
    data = input("\n -- Masukkan nama : ")
    if data == "Agus":
        break
    print(data)


print('-----------------------------------------')
print('-----------------from--------------------')
print('----------- shegi-developer -------------')