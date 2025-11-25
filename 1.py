def terbilang(n):
    angka = ["", "satu", "dua", "tiga", "empat", "lima", 
             "enam", "tujuh", "delapan", "sembilan"]
    
    if n == 0:
        return "nol"
    elif n < 10:
        return angka[n]
    elif n < 20:
        if n == 10: return "sepuluh"
        if n == 11: return "sebelas"
        return angka[n - 10] + " belas"
    elif n < 100:
        return angka[n // 10] + " puluh " + terbilang(n % 10)
    elif n < 1000:
        if n < 200: return "seratus " + terbilang(n - 100)
        return angka[n // 100] + " ratus " + terbilang(n % 100)
    elif n < 1000000:
        if n < 2000: return "seribu " + terbilang(n - 1000)
        return terbilang(n // 1000) + " ribu " + terbilang(n % 1000)
    else:
        return "maksimal 6 digit saja"


angka = int(input("Masukkan angka: "))
print(f"{angka} ditulis sebagai: {terbilang(angka).strip().capitalize()}")
