print("=== POLA ANGKA DASAR ===")
print("Pilih soal:")
print("Soal 4 - Pola 122333444455555666666")
print("Soal 5 - Pola 666666555554444333221")
print("Soal 6 - Pola 112123123412345123456")
print("Soal 7 - Pola 654321543214321321211")

pilihan = int(input("Masukkan pilihan (4-7): "))

if pilihan == 4:
    hasil = ""
    for i in range(1, 7):
        hasil = hasil + str(i) * i
    print(hasil)

elif pilihan == 5:
    hasil = ""
    for i in range(6, 0, -1):
        hasil = hasil + str(i) * i
    print(hasil)

elif pilihan == 6:
    hasil = ""
    for i in range(1, 7):
        for j in range(1, i + 1):
            hasil = hasil + str(j)
    print(hasil)

elif pilihan == 7:
    hasil = ""
    for i in range(6, 0, -1):
        for j in range(i, 0, -1):
            hasil = hasil + str(j)
    print(hasil)

else:
    print("Pilihan tidak tersedia.")
