#=============================================
# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPL B/P1
#=============================================

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)


# ==========================================================
# Diskusi dan Penjelasan
# ==========================================================
# Menurut saya program ini menggunakan rekursi
# untuk menghasilkan semua kemungkinan PIN
# dengan panjang tertentu.
#
# Base case terjadi saat panjang string "hasil"
# sudah sama dengan panjang yang ditentukan.
# Jika sudah sama, maka PIN dicetak dan fungsi berhenti.
#
# Recursive call terjadi di dalam perulangan for,
# dimana setiap langkah kita menambahkan
# satu angka ("0", "1", atau "2") ke string hasil.
#
# Karena setiap posisi memiliki 3 pilihan angka,
# maka total kombinasi yang dihasilkan adalah:
# 3^n (tiga pangkat n).
#
# ===============================
# Cara Mencegah Angka yang Sama Berulang
# ===============================
# Saat ini angka bisa muncul berulang, misalnya:
# 000, 111, 121, dll.
#
# Jika ingin mencegah angka yang sama muncul berulang,
# maka kita perlu menambahkan kondisi (pruning),
# yaitu mengecek apakah angka yang akan ditambahkan
# sudah ada di dalam string "hasil".
#
# Contohnya dengan menambahkan pengecekan:
# if angka not in hasil:
#
# Dengan begitu, setiap angka hanya boleh muncul sekali
# dalam satu kombinasi PIN.
#
# Jadi intinya, untuk mencegah angka yang sama berulang,
# kita perlu menambahkan kondisi pembatas sebelum
# melakukan recursive call.