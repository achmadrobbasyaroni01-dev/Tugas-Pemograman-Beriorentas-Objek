print("=== POLA ANGKA CAMPURAN B ===")
print("Pilih soal:")
print("Soal 12 - 122123123455555666666123456712345678999999999")
print("Soal 13 - 112333444412345123456777777788888888123456789")
print("Soal 14 - 888888887777777654321543214444333211")
print("Soal 15 - 876543217654321666666555554321321221")

pilihan = int(input("Masukkan pilihan (12-15): "))

if pilihan == 12:
    hasil = ""

    for i in range(1, 10):
        if i in [1, 2, 5, 6, 9]:
            hasil = hasil + str(i) * i
        else:
            for j in range(1, i + 1):
                hasil = hasil + str(j)
    print(hasil)

elif pilihan == 13:
    hasil = ""

    for i in range(1, 10):
        if i in [1, 3, 4, 7, 8]:
            hasil = hasil + str(i) * i
        else:
            for j in range(1, i + 1):
                hasil = hasil + str(j)
    print(hasil)

elif pilihan == 14:
    hasil = ""

    for i in range(8, 0, -1):
        if i in [8, 7, 4, 3]:
            hasil = hasil + str(i) * i
        else:
            for j in range(i, 0, -1):
                hasil = hasil + str(j)

    print(hasil)

elif pilihan == 15:
    hasil = ""
    for i in range(8, 0, -1):
        if i in [6, 5, 2, 1]:
            hasil = hasil + str(i) * i
        else:
            for j in range(i, 0, -1):
                hasil = hasil + str(j)
    print(hasil)

else:
    print("Pilihan tidak tersedia.")
