nilai = int(input("Masukkan nilai: "))

if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)
