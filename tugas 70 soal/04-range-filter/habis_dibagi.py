print("=== PROGRAM HABIS DIBAGI ===")
print("Pilih soal:")
print("Soal 29 - Habis dibagi 3")
print("Soal 30 - Habis dibagi 4")
print("Soal 31 - Habis dibagi 5")
print("Soal 32 - Habis dibagi 6")
print("Soal 33 - Habis dibagi 7")

pilihan = int(input("Masukkan pilihan (29-33): "))

pembagi = 0
if pilihan == 29:
    pembagi = 3
elif pilihan == 30:
    pembagi = 4
elif pilihan == 31:
    pembagi = 5
elif pilihan == 32:
    pembagi = 6
elif pilihan == 33:
    pembagi = 7
else:
    print("Pilihan tidak tersedia.")

if pembagi != 0:
    awal = int(input("Angka awal: "))
    akhir = int(input("Angka akhir: "))
    for i in range(awal, akhir + 1):
        if i % pembagi == 0:
            print(i," ", end="")
