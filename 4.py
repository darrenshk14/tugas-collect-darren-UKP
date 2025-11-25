def pangkat(x, n):
    return x ** n


x = float(input("Masukkan nilai x: "))
n = int(input("Masukkan nilai n: "))

y = pangkat(x, n)
print(f"Hasil dari y = {x}^{n} adalah {y}")
