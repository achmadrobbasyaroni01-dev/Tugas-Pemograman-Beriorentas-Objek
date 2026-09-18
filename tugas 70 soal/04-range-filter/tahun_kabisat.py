print("=== TAHUN KABISAT ===")
print("Pilih soal:")
print("Soal 24 - Kabisat yang digit akhir 0")
print("Soal 25 - Kabisat yang digit akhir 2")
print("Soal 26 - Kabisat yang digit akhir 4")
print("Soal 27 - Kabisat yang digit akhir 6")
print("Soal 28 - Kabisat yang digit akhir 8")

pilihan = int(input("Masukkan pilihan (24-28): "))

akhir = 0
if pilihan == 24:
    akhir = 0
elif pilihan == 25:
    akhir = 2
elif pilihan == 26:
    akhir = 4
elif pilihan == 27:
    akhir = 6
elif pilihan == 28:
    akhir = 8
else:
    print("Pilihan tidak tersedia.")

if pilihan >= 24 and pilihan <= 28:
    awal = int(input("Tahun awal: "))
    akhir_tahun = int(input("Tahun akhir: "))
    for tahun in range(awal, akhir_tahun + 1):
        kabisat = False
        if tahun % 400 == 0:
            kabisat = True
        elif tahun % 100 == 0:
            kabisat = False
        elif tahun % 4 == 0:
            kabisat = True
        if kabisat and tahun % 10 == akhir:
            print(tahun)
