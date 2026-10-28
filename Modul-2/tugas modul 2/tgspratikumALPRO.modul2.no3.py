
# Program Pemantauan Reaktor Krasny
# Input suhu dan tekanan
suhu = float(input("Masukkan suhu reaktor (C): "))
tekanan = float(input("Masukkan tekanan gas (Bar): "))

# Menampilkan data input
print("Suhu reaktor :", suhu, "C")
print("Tekanan gas  :", tekanan, "Bar")

# Menentukan status bahaya menggunakan kondisi bersarang
if suhu > 1000:
    if tekanan > 50:
        print("Status Bahaya : MELTDOWN! SEGERA EVAKUASI!")
    else:
        print("Status Bahaya : Bahaya Suhu: Segera Turunkan Daya!")

elif suhu > 500:
    if tekanan > 30:
        print("Status Bahaya : Tekanan Tidak Stabil")
    else:
        print("Status Bahaya : Operasi Reaktor Normal")

else:
    print("Status Bahaya : Reaktor Belum Cukup Panas")

# Menentukan status pompa dengan ternary operator
status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("Status Pompa :", status_pompa)
