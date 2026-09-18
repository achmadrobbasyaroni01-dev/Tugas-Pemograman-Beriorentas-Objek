for i in range(6):
    if i == 0 or i == 3:
        baris = "0" * 7
    elif i == 1 or i == 4:
        baris = "*" * 7
    else:
        baris = "=" * 7
    print(baris)
