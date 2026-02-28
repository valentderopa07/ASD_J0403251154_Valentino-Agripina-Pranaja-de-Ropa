#=============================================
# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPL B/P1
#=============================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================
def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)


# ==========================================================
# Diskusi dan Penjelasan
# ==========================================================
# Menurut saya program ini menggunakan konsep rekursi
# untuk menghasilkan semua kemungkinan kombinasi huruf
# dari "A" dan "B" sepanjang n karakter.
#
# Base case terjadi saat panjang string "hasil"
# sudah sama dengan n. Jika sudah sama,
# maka kombinasi tersebut dicetak dan fungsi berhenti.
#
# Recursive call terjadi pada dua baris ini:
# kombinasi(n, hasil + "A")
# kombinasi(n, hasil + "B")
#
# Artinya setiap langkah, program memiliki 2 pilihan:
# menambahkan huruf "A" atau huruf "B".
#
# Karena setiap posisi memiliki 2 kemungkinan,
# maka jumlah kombinasi yang dihasilkan adalah:
# 2^n (dua pangkat n).
#
# Pada contoh kombinasi(2),
# berarti jumlah kombinasi adalah 2^2 = 4.
#
# Hasil yang muncul:
# AA
# AB
# BA
# BB
#
# Jadi kesimpulannya, jumlah kombinasi yang dihasilkan
# bergantung pada nilai n dan mengikuti rumus 2^n,
# karena setiap posisi memiliki dua pilihan huruf.