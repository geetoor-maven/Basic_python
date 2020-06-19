# Belajar tabel kebenaran 
# operasi logika atau boolean pada python
# not , or , and, xor

print('=== NOT ===')
a = True
c = not a
print('Data a =',a)
print('------------NOT')
print('Data c = ',c)

# OR APABILA SALAH SATUNYA TRUE MAKA HASILNYA TRUE

print('=== OR ===')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

a = False
b = True
c = a or b
print(a,'OR',b,'=',c)

a = True
b = False
c = a or b
print(a,'OR',b,'=',c)

a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

# AND APABILA SALAH SATUNYA FALSE MAKA HASILNYA AKAN FALSE

print('=== AND ===')

a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

a = False
b = True
c = a and b
print(a,'AND',b,'=',c)

a = True
b = False
c = a and b
print(a,'AND',b,'=',c)

a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

# XOR AKAN TRUE JIKA SALAH SATUNYA TRUE SISANYA FALSE
print('=== XOR ===')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

print('-----------------------------------------')
print('-----------------from--------------------')
print('----------- shegi-developer -------------')

