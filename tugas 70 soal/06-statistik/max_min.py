print("=== PROGRAM TERBESAR DAN TERKECIL ===")
print("Pilih soal:")
print("Soal 42 - Cari nilai terbesar (min 10 angka)")
print("Soal 43 - Cari nilai terkecil (min 10 angka)")

pilihan = int(input("Masukkan pilihan (42/43): "))

if pilihan == 42:
    n = int(input("Jumlah angka (min 10): "))
    besar = None
    for i in range(n):
        x = int(input("Angka ke-" + str(i + 1) + ": "))
        if besar is None or x > besar:
            besar = x
    print("Terbesar:", besar)

elif pilihan == 43:
    n = int(input("Jumlah angka (min 10): "))
    kecil = None
    for i in range(n):
        x = int(input("Angka ke-" + str(i + 1) + ": "))
        if kecil is None or x < kecil:
            kecil = x
    print("Terkecil:", kecil)

else:
    print("Pilihan tidak tersedia.")
