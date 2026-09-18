def is_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("=== PROGRAM PRIMA ===")
print("Pilih soal:")
print("Soal 49 - Tampilkan bilangan prima")
print("Soal 50 - Hitung total bilangan prima")

pilihan = int(input("Masukkan pilihan (49/50): "))

if pilihan == 49:
    awal = int(input("Angka awal: "))
    akhir = int(input("Angka akhir: "))
    for i in range(awal, akhir + 1):
        if is_prima(i):
            print(i)

elif pilihan == 50:
    awal = int(input("Angka awal: "))
    akhir = int(input("Angka akhir: "))
    total = 0
    for i in range(awal, akhir + 1):
        if is_prima(i):
            total = total + i
    print("Total:", total)

else:
    print("Pilihan tidak tersedia.")
