# Belajar type data dictonary(tuple)

data = {"Nama":"Agus kurniawan","Umur":"20","kerjaan":"Chairman of Coconut","Asal":"Sinjai"}

# ini untuk memasukkan data ke variabel nama dengan memanggil data["Nama"]
nama = data["Nama"]

tambah = int(input("\n Masukan berapa data yang ingin di tambah : "))
for a in range(0,tambah):
    key = str(input("Masukan key : "))
    value = str(input("Masukan value : "))
    data[key] = value

# Listing untuk mengubah data
data["Umur"] = "21"

print("\n--untuk memunculkan key dari data--")

# untuk memunculkan key dari data
for key in data:
    print(key)

print("\n--untuk memunculkan key dan value dari data--")

# untuk memunculkan key dan value dari data
for key in data:
    value = data[key]
    print(key," : ",value)

print("\n--menampilkan nilai key value dari data dengan method items--")
print(data.items())

# Untuk menghapus key value dari data
hapus = str(input("Masukan Key yang ingin di hapus : "))
del data[hapus]


print("\n--untuk memunculkan key dan value dari data dengan metode tupel--")
for key in data.items():
    print(key[0]," : ",key[1])


print('-----------------------------------------')
print('-----------------from--------------------')
print('----------- shegi-developer -------------')