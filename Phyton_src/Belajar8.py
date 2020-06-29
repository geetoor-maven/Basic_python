# Belajar List 

# menganalisasi data ccnt
ccnt = ["Agus kurniawan","Andri","Karmila","Sari Ufa","wahid","Sidik","Hartina"]

print(ccnt)

# Perintah untuk menambah data ccnt 
ccnt.append("Nur syahrani")

# Perintah untuk mengakses satu data ccnt
print(ccnt[0])

# Perintah untuk menghapus data 
ccnt.remove("Nur syahrani")

# Perintah untuk mengedit data 
ccnt[1] = "Andri berek \n "

print(ccnt)

# mengakses data ccnt dengan efisien menggunakan keword for

for nama in ccnt:
    print("-- Nama BPH coconut computer club : ",nama)


# Belajar Range di python

nomor = range(1,11)

for no in nomor:
    print(no)

print('-----------------------------------------')
print('-----------------from--------------------')
print('----------- shegi-developer -------------')