n = 5

print("1. Segitiga siku kiri bawah")
for i in range(1, n + 1):
    print("*" * i)

print("")
print("2. Segitiga siku kanan bawah")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

print("")
print("3. Segitiga siku kiri atas")
for i in range(n, 0, -1):
    print("*" * i)

print("")
print("4. Segitiga siku kanan atas")
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)

print("")
print("5. Piramida tengah")
for i in range(n):
    print(" " * (n - 1 - i) + "*" * (2 * i + 1))
