def baca_ukuran():
    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))
    return baris, kolom

def baca_matrix(baris, kolom, nama):
    print(f"masukin matriks nya {nama}:")
    matrix = []
    for i in range(baris):
        row = list(map(float, input(f"Baris ke-{i+1}: ").split()))
        while len(row) != kolom:
            print("salah elemen")
            row = list(map(float, input(f"Baris ke-{i+1}: ").split()))
        matrix.append(row)
    return matrix

def kali_matrix(A, B):
    baris_A = len(A)
    kolom_A = len(A[0])
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

print("Matriks A:")
baris_A, kolom_A = baca_ukuran()
print("Matriks B:")
baris_B, kolom_B = baca_ukuran()

if kolom_A != baris_B:
    print("ukuran matriks tidak pas")
else:
    A = baca_matrix(baris_A, kolom_A, "A")
    B = baca_matrix(baris_B, kolom_B, "B")

    print("Hasil perkalian A x B:")
    C = kali_matrix(A, B)
    tampil_matrix(C)
