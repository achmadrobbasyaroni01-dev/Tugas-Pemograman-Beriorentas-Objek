print("=== FAKTORIAL DAN FIBONACCI ===")
print("Pilih soal:")
print("Soal 22 - Faktorial (3! = 3 x 2 x 1 = 6)")
print("Soal 23 - Fibonacci")

pilihan = int(input("Masukkan pilihan (22/23): "))

if pilihan == 22:
    n = int(input("Masukkan n: "))
    hasil = 1
    rincian = ""
    for i in range(n, 0, -1):
        hasil = hasil * i
        rincian = rincian + str(i)
        if i != 1:
            rincian = rincian + " x "
    print(n, "! =", rincian, "=", hasil)

elif pilihan == 23:
    banyak = int(input("Mau tampil berapa suku: "))
    a = 0
    b = 1
    for i in range(banyak):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

else:
    print("Pilihan tidak tersedia.")
