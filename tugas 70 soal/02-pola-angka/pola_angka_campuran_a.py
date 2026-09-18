print("=== POLA ANGKA CAMPURAN A ===")
print("Pilih soal:")
print("Soal 8 - 112333123455555123456")
print("Soal 9 - 122123444412345666666")
print("Soal 10 - 654321555554321333211")
print("Soal 11 - 666666123454444123221")

pilihan = int(input("Masukkan pilihan (8-11): "))

if pilihan == 8:
    hasil = ""
    for i in range (1, 7):
        if i % 2 == 1:
            hasil = hasil + str(i) * i
        else:
            for j in range(1, i + 1):
                hasil = hasil + str(j)
    print(hasil)
elif pilihan == 9:
    hasil = ""
    for i in range (1, 7):
        if i % 2 == 0:
            hasil = hasil + str(i) * i
        else:
            for j in range(1, i + 1):
                hasil = hasil + str(j)
    print(hasil)

elif pilihan == 10:
    hasil = ""
    for i in range (6, 0, -1):
        if i % 2 == 1:
           hasil = hasil + str(i) * i
        else:
             for j in range(i, 0, -1):
                hasil = hasil + str(j)
    print(hasil)
elif pilihan == 11:
    hasil = ""
    for i in range (6, 0, -1):
        if i % 2 == 0:
            hasil = hasil + str(i) * i
        else:
            for j in range(1, i + 1):
                hasil = hasil + str(j)
    print(hasil)

else:
    print("Pilihan tidak tersedia.")
