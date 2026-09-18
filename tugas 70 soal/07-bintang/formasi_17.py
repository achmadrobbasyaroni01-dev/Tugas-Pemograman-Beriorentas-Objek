for i in range(6):
    baris = ""
    for j in range(7):
        if j == 6 - i:
            baris = baris + "*"
        else:
            baris = baris + "0"
    print(baris)
