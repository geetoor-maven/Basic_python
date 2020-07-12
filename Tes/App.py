import Objek

data_member = []
data_member.append({
    "nama" : "Shegi-developer",
    "alamat" : "Jln.Yusufbauty",
    "jurusan" : "Computer-Engineering"
})

while True:
    print("_______________________________________________________")
    print("\n---- PROGRAM LIST MEMBER 11 COCONUT COMPUTER CLUB ----")
    print("-------------------------------------------------------")
    print("------ 1. DAFTAR MEMBER                ----------------")
    print("------ 2. TAMBAH NEW MEMBER            ----------------")
    print("------ 3. HAPUS MEMBER                 ----------------")
    print("------ 4. CARI MEMBER                  ----------------")
    print("------ 0. ISTIRAHAT DAN KELUAR PROGRAM ----------------")
    print("_______________________________________________________")

    menu = input("------ PILIH MENU PROGRAM : ")
    if menu == "0":
        break
    elif menu == "1":
        print("\n--- LIST DAFTAR MEMBER 11 ---")
        Objek.Lihat_data(data_member)
    elif menu == "2":
        print("\n--- TAMBAH DAFTAR MEMBER 11 ---")


print("_____________________________________________________________")
print("--- PROGRAM LIST MEMBER 11 COCONUT COMPUTER CLUB TERHENTI ---")
print("_____________________________________________________________")

