import time

print("=== ANIMASI ANGKA 0 ===")
print("Pilih soal:")
print("Soal 34 - Jalan kiri ke kanan, kembali ke kiri (atas)")
print("Soal 35 - Pingpong kiri-kanan (atas)")
print("Soal 36 - Jalan kiri ke kanan, kembali ke kiri (bawah)")
print("Soal 37 - Pingpong kiri-kanan (bawah)")

pilihan = int(input("Masukkan pilihan (34-37): "))

if pilihan == 34 or pilihan == 35 or pilihan == 36 or pilihan == 37:

    lebar = 30

    pos = 0

    arah = 1

    pingpong = pilihan == 35 or pilihan == 37

    print("\033[2J", end="")
    print("\033[H", end="")

    try:
        while True:

            baris_atas = [" "] * lebar
            baris_tengah = [" "] * lebar
            baris_bawah = [" "] * lebar

            if pilihan == 34 or pilihan == 35:
                baris_atas[pos] = "0"

            else:
                baris_bawah[pos] = "0"

            teks_atas = "".join(baris_atas)
            teks_tengah = "".join(baris_tengah)
            teks_bawah = "".join(baris_bawah)

            print("\033[H", end="")

            print("+" + "-" * lebar + "+")
            print("|" + teks_atas + "|")
            print("|" + teks_tengah + "|")
            print("|" + teks_bawah + "|")
            print("+" + "-" * lebar + "+")

            time.sleep(0.1)

            pos = pos + arah

            if pos >= lebar:

                if pingpong:
                    arah = -1
                    pos = lebar - 1

                else:
                    pos = 0

            if pos < 0:

                arah = 1
                pos = 0

    except KeyboardInterrupt:

        print("\nAnimasi berhenti.")

else:
    print("Pilihan tidak tersedia.")
