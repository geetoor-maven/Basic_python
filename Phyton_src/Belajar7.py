# Statement if 

print("\n -- Program Kasir E-warung -- \n")

print(" --1 Pesan Makanan ")
print(" --2 Pesan Minuman ")
print(" --3 Keluar Program \n")

nomor = input("-- Masukan Menu pilihan [1-3] : ")

if nomor == "1":
    print("\n -- Anda masuk ke menu pesan makanan --")
    print("\n -- Menu Makanan --")
    print(" --1 Bakso raksasa ")
    print(" --2 Bakso biasa ")
    print(" --3 Mie pangsit \n")

    menu_makan = str(input(" -- Masukkan menu makanan [1-3] : "))

    if menu_makan == "1":
        
        print("\n -- Menu makanan adalah Bakso raksasa Rp.15.000 --")
        bakso = 15000
        jumlah = int(input(" -- Masukkan jumlah Pesanan : "))
        bakso = bakso * jumlah
        print(" -- Pembayaran anda : ",bakso)

    elif menu_makan == "2":
        
        print("\n -- Menu makanan adalah Bakso biasa Rp.10.000 --")
        bakso = 10000
        jumlah = int(input(" -- Masukkan jumlah Pesanan : "))
        bakso = bakso * jumlah
        print(" -- Pembayaran anda : ",bakso)

    elif menu_makan == "3":

        print("\n -- Menu makanan adalah Mie pangsit Rp.13.000 --")
        bakso = 13000
        jumlah = int(input(" -- Masukkan jumlah Pesanan : "))
        bakso = bakso * jumlah
        print(" -- Pembayaran anda : ",bakso)

    else:
        print(" -- Menu tidak tersedia --")

elif nomor == "2":
    print("\n -- Anda masuk ke menu pesan minuman")

    print("\n -- Menu Minuman --")
    print(" --1 Jus Alpukado ")
    print(" --2 Jus Melonia ")
    print(" --3 Es teh \n")

    menu_minum = str(input(" -- Masukkan menu minuman [1-3] : "))

    if menu_minum == "1":

        print("\n -- Menu minuman Kamu adalah Jus Alpokado Rp.8.000 --")
        jus = 8000
        jumlah = int(input(" -- Masukan jumlah pesanan : "))
        jus = jus * jumlah
        print(" -- Pembayaran anda : ",jus) 

    elif menu_minum == "2":
        
        print("\n -- Menu minuman Kamu adalah Jus Melonia Rp.7.000 --")
        jus = 7000
        jumlah = int(input(" -- Masukan jumlah pesanan : "))
        jus = jus * jumlah
        print(" -- Pembayaran anda : ",jus)

    elif menu_minum == "3":

        print("\n -- Menu minuman Kamu adalah Es teh Rp.5.000 --")
        jus = 5000
        jumlah = int(input(" -- Masukan jumlah pesanan : "))
        jus = jus * jumlah
        print(" -- Pembayaran anda : ",jus)

    else:

         print(" -- Menu tidak tersedia --")

else:
    print("\n -- Anda Keluar dari program")





print('-----------------------------------------')
print('-----------------from--------------------')
print('----------- shegi-developer -------------')