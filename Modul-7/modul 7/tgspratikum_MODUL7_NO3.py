
# Program Pengelolaan Peserta Webinar

# Membuat tiga set kosong
undangan = set()
webinar_A = set()
webinar_B = set()

# Mengisi daftar undangan
print("===== DAFTAR UNDANGAN =====")
data = input("Masukkan nama undangan (pisahkan dengan koma): ")
undangan = set(data.split(","))

# Mengisi peserta Webinar A
print("\n===== PESERTA WEBINAR A =====")
data = input("Masukkan nama peserta (pisahkan dengan koma): ")
webinar_A = set(data.split(","))

# Mengisi peserta Webinar B
print("\n===== PESERTA WEBINAR B =====")
data = input("Masukkan nama peserta (pisahkan dengan koma): ")
webinar_B = set(data.split(","))

# Menampilkan semua peserta kedua webinar
semua_peserta = webinar_A.union(webinar_B)

print("===== HASIL PENGOLAHAN DATA =====")

print("1. Semua peserta dari kedua webinar:")
print(semua_peserta)

# Peserta yang hadir di kedua webinar
kedua_webinar = webinar_A.intersection(webinar_B)

print("2. Peserta yang hadir di kedua webinar:")
print(kedua_webinar)

# Peserta yang hanya hadir di salah satu webinar
satu_webinar = webinar_A.symmetric_difference(webinar_B)

print("3. Peserta yang hanya hadir di salah satu webinar:")
print(satu_webinar)

# Undangan yang tidak hadir di webinar mana pun
tidak_hadir = undangan.difference(semua_peserta)

print("4. Undangan yang tidak hadir di webinar mana pun:")
print(tidak_hadir)
