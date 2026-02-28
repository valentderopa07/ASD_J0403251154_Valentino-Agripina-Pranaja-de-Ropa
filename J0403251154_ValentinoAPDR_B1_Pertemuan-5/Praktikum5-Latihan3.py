#=============================================
# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPL B/P1
#=============================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================
def cari_maks(data, index=0):
    # Base case
    if index == len(data) - 1:
        return data[index]

    # Recursive case
    maks_sisa = cari_maks(data, index + 1)
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))


# ==========================================================
# Diskusi dan Penjelasan
# ==========================================================
# Menurut saya cara kerja program ini adalah mencari nilai terbesar
# dalam sebuah list menggunakan konsep rekursi.
#
# Awalnya fungsi dipanggil dengan index = 0, artinya mulai dari
# elemen pertama pada list.
#
# Base case terjadi saat index sudah berada di elemen terakhir
# (index == len(data) - 1). Pada kondisi ini fungsi langsung
# mengembalikan nilai elemen terakhir karena tidak ada lagi
# yang bisa dibandingkan.
#
# Recursive call terjadi pada bagian:
# maks_sisa = cari_maks(data, index + 1)
# Artinya fungsi memanggil dirinya sendiri untuk mengecek
# nilai maksimum dari sisa elemen setelah index sekarang.
#
# Setelah sampai ke elemen terakhir (base case),
# program akan kembali ke atas (proses unwinding).
# Setiap kembali, program membandingkan:
# data[index] dengan maks_sisa.
#
# Jika data[index] lebih besar, maka nilai itu dikembalikan.
# Jika tidak, maka maks_sisa yang dikembalikan.
#
# Proses ini terus berlangsung sampai kembali ke pemanggilan pertama.
#
# Jadi kesimpulannya, program ini bekerja dengan membandingkan
# setiap elemen dengan hasil maksimum dari sisa elemen,
# sampai akhirnya ditemukan nilai terbesar dalam list.