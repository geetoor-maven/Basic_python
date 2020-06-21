# Komparasi dan logika pada python

inputuser = float(input('Masukan angka yang bernilai \n -- Kurang Dari tiga \n -- Lebih dari sepuluh ='))

# pengecekan apakah angka kurang dari tiga dengan keyword < ?
cekkurangdari = (inputuser < 3)
print('Angka Kurang dari tiga =',cekkurangdari)

# pengecekan apakah angka lebih dari 10 dengan keyword >?
ceklebihdari = (inputuser > 10)
print('Angka Lebih dari sepuluh =',ceklebihdari)

# pengecekan angka sekaligus 2 variabel agar di satukan (OR)
cekangka = cekkurangdari or ceklebihdari
print('Angka yang di masukan adalah =',cekangka)

print('====================')

inputuser = float(input('Masukan angka yang bernilai \n -- Lebih Dari tiga \n -- kurang dari sepuluh ='))

# pengecekan apakah angka lebih dari 3 dengan keyword >
lebihtiga = inputuser > 3
print('Angka lebih dari tiga =',lebihtiga)

# pengecekan apakah angka kurang dari 10 dengan keyword <
kurangsepuluh = inputuser < 10
print('Angka Kurang dari sepuluh =',kurangsepuluh)

# Pengecekan angka sekaligus 2 variabel agar di satukan (AND)
cekangka = lebihtiga and kurangsepuluh
print('Angka yang and masukan = ',cekangka)


print('-----------------------------------------')
print('-----------------from--------------------')
print('----------- shegi-developer -------------')

