def baca_ukuran(nama):
    print(f"Masukkan ukuran matriks {nama}:")
    baris = int(input("Jumlah baris: "))
    kolom = int(input("Jumlah kolom: "))
    return baris, kolom

def baca_matrix(baris, kolom, nama):
    print(f"Masukkan matriks nya {nama}:")
    matrix = []
    for i in range(baris):
        row = list(map(float, input(f"Baris ke-{i+1}: ").split()))
        while len(row) != kolom:
            print("jumlah eleemen salah")
            row = list(map(float, input(f"Baris ke-{i+1}: ").split()))
        matrix.append(row)
    return matrix

def validasi_ukuran(kolom_A, baris_B):
    return kolom_A == baris_B

def kali_matrix(A, B):
    baris_A, kolom_A = len(A), len(A[0])
    kolom_B = len(B[0])
    hasil = [[0 for _ in range(kolom_B)] for _ in range(baris_A)]

    for i in range(baris_A):
        for j in range(kolom_B):
            for k in range(kolom_A):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil

def tampil_matrix(M):
    for baris in M:
        print(" ".join(f"{x:.2f}" for x in baris))

print("=== PERKALIAN DUA MATRIKS FLOATING POINT ===")

baris_A, kolom_A = baca_ukuran("A")
baris_B, kolom_B = baca_ukuran("B")


if not validasi_ukuran(kolom_A, baris_B):
    print("\nUkuran matriks tidak valid untuk perkalian! (Kolom A harus = Baris B)")
else:
    # Baca isi matriks
    A = baca_matrix(baris_A, kolom_A, "A")
    B = baca_matrix(baris_B, kolom_B, "B")

    # Hitung hasil perkalian
    C = kali_matrix(A, B)

    # Tampilkan hasil
    print("\nHasil perkalian A x B adalah:")
    tampil_matrix(C)
