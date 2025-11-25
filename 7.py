def baca_nama():
    daftar = []
    for i in range(10):
        nama = input(f"Masukkan nama ke-{i+1}: ")
        daftar.append(nama)
    return daftar

def urutkan_nama(daftar):
    daftar.sort()
    return daftar

def tampilkan_nama(daftar):
    print("Nama urut nya")
    for n in daftar:
        print(n)

# Program utama
nama_list = baca_nama()
nama_list = urutkan_nama(nama_list)
tampilkan_nama(nama_list)
