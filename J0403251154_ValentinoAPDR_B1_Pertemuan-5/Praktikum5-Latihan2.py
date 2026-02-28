#=============================================
# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPL B/P1
#=============================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)


# ==========================================================
# Diskusi dan Penjelasan
# ==========================================================
# Menurut saya kenapa output "Keluar" muncul terbalik itu
# karena cara kerja rekursi menggunakan sistem stack (tumpukan).
#
# Saat countdown(3) dijalankan, program tidak langsung mencetak
# "Keluar", tetapi akan terus masuk ke pemanggilan fungsi berikutnya
# sampai mencapai base case yaitu n == 0.
#
# Urutan yang terjadi:
# Masuk: 3
# Masuk: 2
# Masuk: 1
# Selesai
#
# Setelah mencapai base case, program mulai kembali ke atas
# (proses ini disebut unwinding).
#
# Karena yang terakhir masuk adalah countdown(1),
# maka dia yang pertama keluar.
#
# Sehingga urutan "Keluar" menjadi:
# Keluar: 1
# Keluar: 2
# Keluar: 3
#
# Jadi kesimpulannya, output "Keluar" muncul terbalik
# karena rekursi bekerja dengan sistem LIFO (Last In First Out),
# yaitu yang terakhir masuk akan keluar lebih dulu.