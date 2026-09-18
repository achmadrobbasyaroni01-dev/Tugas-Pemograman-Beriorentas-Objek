print("=== PROGRAM STRING ===")
print("Pilih soal:")
print("1. Soal 1 - Balik tulisan (Hallo -> ollaH)")
print("2. Soal 2 - Hitung huruf tertentu")
print("3. Soal 3 - Hitung jumlah karakter")

pilihan = int(input("Masukkan pilihan (1/2/3): "))

if pilihan == 1:
    s = input("Masukkan kalimat: ")
    balik = s[::-1]
    print("Hasil:", balik)
elif pilihan == 2:
    s = input("Masukkan kalimat: ")
    cari = input("Huruf yang dihitung: ")
    jumlah = 0
    for huruf in s:
        if huruf == cari:
            jumlah = jumlah + 1
    print("Jumlah huruf", cari, ":", jumlah)
elif pilihan == 3:
    s = input("Masukkan kalimat: ")
    jumlah = 0
    for huruf in s:
        jumlah = jumlah + 1
    print("Jumlah karakter:", jumlah)
else:
    print("Pilihan tidak tersedia.")
