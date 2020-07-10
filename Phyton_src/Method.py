
# Di sini kita akan belajar tentang bagaimana cara membuat method

# Method/Function adalah sebuah kode di dalam blok yang bisa di panggil berulang kali kapanpun kita mau


nama = []

# Cara membuat method
def PrintNama() :
    for data in nama:
        print(data)

inputdata  = int(input("Masukan berapa data : "))

for a in range(0,inputdata):
    inp = str(input("Masukan Nama : "))
    nama.append(inp)
    
# dan cara memanggil method yang sudah di buat
PrintNama()    

print('-----------------------------------------')
print('-----------------from--------------------')
print('----------- shegi-developer -------------')