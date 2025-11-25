def caesar_cipher(teks, geser):
    hasil = ""
    for char in teks:
        if char.isalpha():
            kode_awal = 65 if char.isupper() else 97
            hasil += chr((ord(char) - kode_awal + geser) % 26 + kode_awal)
        else:
            hasil += char  
    return hasil

kalimat = input("Masukkan kalimat: ")
hasil = caesar_cipher(kalimat, 3)
print("Hasil pengkodean:", hasil)
