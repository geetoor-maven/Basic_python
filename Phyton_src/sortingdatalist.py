# PROGRAM MENAMBAH, MENAMPILKAN, MENGEDIT, MENGHAPUS, MENCARI data menggunakan foor loop

print("\n -- Program Data Struchture -- \n")

# menginilialisasi variabel list di python
nama = ["Agus kurniawan","Andri","Karmila","Sari ulfa","Wahid","Subhan sidiq","Hartina"]

print(" --1 Menampilkan Data -- ")
print(" --2 Menambah Data -- ")
print(" --3 Mengedit Data -- ")
print(" --4 Menghapus Data -- ")
print(" --5 Mencari Data -- \n")

program = str(input(" -- Masukan nomor : "))

if program == "1":
    print("\n -- Menampilkan Data -- ")
    
    # Program ini me looping data sehingga tampilannya agak kelihatan rapi dan tidak berformat JSON
    for a in range(0,len(nama)):
        print("Nama : ",nama[a])

elif program == "2":
    print("\n -- Menambah Data -- ")

    berapa_data = int(input(" -- Berapa banyak data yang ingin di tambah : "))

    # Program akan looping sesuai berapa banyak data yang ingin di tambah
    for b in range(0,berapa_data):
        input_data = str(input(" -- Masukan nama : "))
        nama.append(input_data)

    # lalu memunculkannya kembali
    for a in range(0,len(nama)):
        print(" -- Nama : ",nama[a])

elif program == "3":
    print("\n -- Mengedit Data -- ")
    print(" -- ",nama," -- ")

    index = int(input("\n -- Index ke berapa yang ingin di edit : "))
    edit = str(input(" -- Masukkan nama baru : "))

    nama[index] = edit

    # lalu memunculkannya kembali
    for a in range(0,len(nama)):
        print(" -- Nama : ",nama[a])

elif program == "4":
    print("\n -- Menghapus Data -- ")
    print(" -- ",nama," -- \n")
    index = str(input(" -- Masukan nama yang ingin di hapus : "))
    nama.remove(index)
    
    # lalu memunculkannya kembali
    for a in range(0,len(nama)):
        print(a," -- Nama : ",nama[a])

elif program == "5":
    print("\n -- Mencari Data -- ")
    print(" -- ",nama," -- \n")

    cari = int(input(" -- Masukan index untuk mencari data : "))

    if nama[cari]:
        print(" -- Nama nya adalah : ",nama[cari])
    else:
        print(" -- Index tidak di dapat")

else:
    print(" -- Program Keluar -- ")