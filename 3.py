def hitung_kata(teks):
    return len(teks.split())

kalimat = input("Masukkan kalimat: ")
print("Jumlah kata-kata:", hitung_kata(kalimat))
