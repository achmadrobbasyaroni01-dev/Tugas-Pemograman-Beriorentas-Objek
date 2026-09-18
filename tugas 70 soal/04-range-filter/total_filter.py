print("=== PROGRAM TOTAL FILTER ===")
print("Pilih soal:")
print("Soal 46 - Total angka positif")
print("Soal 47 - Total angka genap")
print("Soal 48 - Total angka ganjil")

pilihan = int(input("Masukkan pilihan (46-48): "))

if pilihan >= 46 and pilihan <= 48:
    awal = int(input("Angka awal: "))
    akhir = int(input("Angka akhir: "))
    total = 0
    for i in range(awal, akhir + 1):
        if pilihan == 46:
            if i > 0:
                total = total + i
        elif pilihan == 47:
            if i % 2 == 0:
                total = total + i
        elif pilihan == 48:
            if i % 2 != 0:
                total = total + i
    print("Total:", total)
else:
    print("Pilihan tidak tersedia.")
