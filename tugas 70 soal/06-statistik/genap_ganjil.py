print("=== PROGRAM GENAP GANJIL ===")
print("Pilih soal:")
print("Soal 44 - Jumlahkan angka genap")
print("Soal 45 - Jumlahkan angka ganjil")

pilihan = int(input("Masukkan pilihan (44/45): "))

if pilihan == 44 or pilihan == 45:
    n = int(input("Jumlah angka: "))
    total = 0
    for i in range(n):
        x = int(input("Angka ke-" + str(i + 1) + ": "))
        if pilihan == 44:
            if x % 2 == 0:
                total = total + x
        else:
            if x % 2 != 0:
                total = total + x
    print("Total:", total)
else:
    print("Pilihan tidak tersedia.")
