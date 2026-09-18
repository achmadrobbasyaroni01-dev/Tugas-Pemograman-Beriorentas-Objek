import time
import os

print("=== ANIMASI VERTIKAL ===")
print("Pilih soal:")
print("Soal 38 - Jalan atas-bawah (kolom kiri)")
print("Soal 39 - Pingpong (kolom kiri)")
print("Soal 40 - Jalan atas-bawah (kolom kanan)")
print("Soal 41 - Pingpong (kolom kanan)")

pilihan = int(input("Masukkan pilihan (38-41): "))

if pilihan >= 38 and pilihan <= 41:

    lebar = 30

    tinggi = 5

    pos = 0

    arah = 1

    pingpong = (pilihan == 39 or pilihan == 41)

    kanan = (pilihan == 40 or pilihan == 41)

    print("Tekan CTRL+C untuk berhenti.")

    try:
        while True:

            os.system("cls")

            print("+" + "-" * lebar + "+")

            for i in range(tinggi):

                baris = [" "] * lebar

                if i == pos:

                    if kanan:
                        baris[lebar - 1] = "0"
                    else:
                        baris[0] = "0"

                teks = ""

                for b in baris:
                    teks = teks + b

                print("|" + teks + "|")

            print("+" + "-" * lebar + "+")

            time.sleep(0.15)

            pos = pos + arah

            if pos >= tinggi:

                if pingpong:
                    arah = -1

                    pos = tinggi - 2

                else:
                    pos = 0

            if pos < 0:

                arah = 1

                pos = 1

    except KeyboardInterrupt:
        print()
        print("Animasi berhenti.")

else:
    print("Pilihan tidak tersedia.")
