print("=== PROGRAM DERET ===")
print("Pilih soal:")
print("Soal 16 - deret langkah +4, -2 (1 5 3 7 5 9 7 11 9 13 11 15)")
print("Soal 17 - deret langkah +10, -5 (2 12 7 17 12 22 17 27 22 32 )")
print("Soal 18 - deret langkah -3, +5 (5 2 7 4 9 6 11 8 13 10 15 12 )")
print("Soal 19 - deret langkah *3, -5 (3 9 4 12 7 21 16 48 43 129 )")
print("Soal 20 - deret langkah +1, +2, +3 berulang (1 2 4 7 8 10 13 14 16 19 20 22 25 )")
print("Soal 21 - deret pangkat 2 (2 pangkat n) (1 2 4 8 16 32 64 128 256 512 )")

pilihan = int(input("Masukkan pilihan (16-21): "))

if pilihan == 16:
    awal = 1
    banyak = 12
    nilai = awal
    langkah = [4, -2]
    for i in range(banyak):
        print(nilai, end=" ")
        nilai = nilai + langkah[i % 2]

elif pilihan == 17:
    awal = 2
    banyak = 10
    nilai = awal
    langkah = [10, -5]
    for i in range(banyak):
        print(nilai, end=" ")
        nilai = nilai + langkah[i % 2]

elif pilihan == 18:
    awal = 5
    banyak = 12
    nilai = awal
    langkah = [-3, 5]
    for i in range(banyak):
        print(nilai, end=" ")
        nilai = nilai + langkah[i % 2]

elif pilihan == 19:
    awal = 3
    banyak = 10
    nilai = awal
    langkah = [3, -5]
    for i in range(banyak):
        print(nilai, end=" ")
        if i % 2 == 0:
            nilai = nilai * langkah[i % 2]
        else:
            nilai = nilai + langkah[i % 2]

elif pilihan == 20:
    awal = 1
    banyak = 13
    nilai = awal
    langkah = [1, 2, 3]
    for i in range(banyak):
        print(nilai, end=" ")
        nilai = nilai + langkah[i % 3]

elif pilihan == 21:
    banyak = 10
    for i in range(banyak):
        print(2 ** i, end=" ")

else:
    print("Pilihan tidak tersedia.")
