## Kita uji coba dulu wkwkwkwk :)

input_user = float(input('\n  Masukan angka yang lebih besar > dari 0 \n dan < kurang dari 5 \n atau lebih dari > 8 \n dan kurang dari < 11 = '))

if1 = (input_user > 0 and input_user < 5)
if2 = (input_user > 8 and input_user < 11)

cek = if1 or if2

print('Angka yang anda masukan = ',cek)

print('==================================')

input_user = float(input(' Masukan angka yang\nkurang besar < dari 0 atau\nlebih dari > 5 dan \nkurang dari < 8 atau lebih > dari 11 = '))

if3 = (input_user < 0 or input_user > 5)
if4 = (input_user < 8 or input_user > 11)

cek1 = if3 and if4

print('Angka yang anda masukan = ',cek1)