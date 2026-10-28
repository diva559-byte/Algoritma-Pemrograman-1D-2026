
while True:
    n = int(input("Masukkan bilangan bulat positif: "))

    if n > 0:
        break
    else:
        print("Masukkan bilangan lebih dari 0!")

for i in range(1, n + 1):

    # Membuat piramida angka pertama
    for j in range(1, i + 1):
        print(j, end="")

    # Membuat jarak antar-piramida
    for k in range(1, 2 * (n - i) + 2):
        print("*", end="")

    # Membuat piramida angka kedua
    for j in range(i, 0, -1):
        print(j, end="")

    print()
