# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPL-B1
# ==========================================================


# ----------------------------------------------------------
# Konstanta
# Menyimpan nama file yang digunakan untuk data stok barang
# ----------------------------------------------------------
nama_file = "stok_barang.txt"


# ----------------------------------------------------------
# Fungsi: baca_stok_barang
# Tujuan:
# - Membaca data stok barang dari file .txt
# - Menyimpan data ke dalam dictionary
# Format file:
#   kode_barang,nama_barang,stok
# ----------------------------------------------------------
def baca_stok_barang(nama_file):
    data_dict = {}  # Dictionary untuk menyimpan seluruh data barang

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()              # Menghapus spasi dan newline
            kode, nama, stok = baris.split(",")  # Memisahkan data berdasarkan koma

            # Menyimpan data ke dictionary dengan kode sebagai key
            data_dict[kode] = {
                "nama": nama,
                "stok": int(stok)
            }

    return data_dict


# ----------------------------------------------------------
# Fungsi: tampilkan_data
# Tujuan:
# - Menampilkan seluruh data barang dalam bentuk tabel
# - Data ditampilkan secara terurut berdasarkan kode barang
# ----------------------------------------------------------
def tampilkan_data(data_dict):
    if len(data_dict) == 0:
        print("Data kosong")
        return

    print("\n========= Daftar Barang =========")
    print(f"{'KODE':<10} | {'NAMA':<12} | {'STOK':>5}")
    print("-" * 32)

    # Menampilkan data satu per satu
    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]["nama"]
        stok = data_dict[kode]["stok"]
        print(f"{kode:<10} | {nama:<12} | {stok:>5}")


# ----------------------------------------------------------
# Fungsi: cari_data
# Tujuan:
# - Mencari data barang berdasarkan kode barang
# - Menampilkan detail barang jika ditemukan
# ----------------------------------------------------------
def cari_data(data_dict):
    barang_cari = input("Masukkan KODE barang yang ingin dicari: ").strip()

    if barang_cari in data_dict:
        nama = data_dict[barang_cari]["nama"]
        stok = data_dict[barang_cari]["stok"]

        print("\n======= Data Barang Ditemukan =======")
        print(f"Kode Barang : {barang_cari}")
        print(f"Nama Barang : {nama}")
        print(f"Stok        : {stok}")
    else:
        print("Data tidak ditemukan")


# ----------------------------------------------------------
# Fungsi: tambah_barang
# Tujuan:
# - Menambahkan barang baru ke dalam dictionary
# - Data belum langsung disimpan ke file
# ----------------------------------------------------------
def tambah_barang(data_dict):
    kode = input("Masukkan kode barang: ").strip()

    # Cek apakah kode sudah ada
    if kode in data_dict:
        print("Kode barang sudah ada.")
        return

    nama = input("Masukkan nama barang: ").strip()

    # Validasi input stok
    try:
        stok = int(input("Masukkan jumlah stok: "))
        if stok < 0:
            print("Stok tidak boleh negatif.")
            return
    except ValueError:
        print("Stok harus berupa angka.")
        return

    # Menambahkan data ke dictionary
    data_dict[kode] = {
        "nama": nama,
        "stok": stok
    }

    print("Barang berhasil ditambahkan (belum disimpan ke file)")


# ----------------------------------------------------------
# Fungsi: update_stok_barang
# Tujuan:
# - Mengubah jumlah stok barang yang sudah ada
# ----------------------------------------------------------
def update_stok_barang(data_dict):
    kode = input("Masukkan KODE barang yang akan diupdate stoknya: ").strip()

    # Cek apakah kode ada di data
    if kode not in data_dict:
        print("Kode barang tidak ditemukan")
        return

    try:
        stok_baru = int(input("Masukkan stok baru: ").strip())
    except ValueError:
        print("Stok harus berupa angka. Update dibatalkan")
        return

    if stok_baru < 0:
        print("Stok tidak boleh negatif. Update dibatalkan")
        return

    # Menyimpan stok lama sebelum diupdate
    stok_lama = data_dict[kode]["stok"]
    data_dict[kode]["stok"] = stok_baru

    print(f"Update berhasil. Stok {kode} berubah dari {stok_lama} menjadi {stok_baru}")


# ----------------------------------------------------------
# Fungsi: simpan_data
# Tujuan:
# - Menyimpan seluruh data dari dictionary ke file
# - File lama akan ditimpa (overwrite)
# ----------------------------------------------------------
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]["nama"]
            stok = data_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")


# ----------------------------------------------------------
# Fungsi Utama (Main Program)
# Tujuan:
# - Mengatur alur program
# - Menampilkan menu dan memanggil fungsi sesuai pilihan user
# ----------------------------------------------------------
def main():

    # Membaca data dari file ke dictionary
    data_barang = baca_stok_barang(nama_file)

    while True:
        print("\n=== MENU STOK BARANG KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang")
        print("4. Update stok barang")
        print("5. Simpan data ke file")
        print("0. Keluar")

        pilihan = input("Pilihan menu: ").strip()

        if pilihan == "1":
            tampilkan_data(data_barang)

        elif pilihan == "2":
            cari_data(data_barang)

        elif pilihan == "3":
            tambah_barang(data_barang)

        elif pilihan == "4":
            update_stok_barang(data_barang)

        elif pilihan == "5":
            simpan_data(nama_file, data_barang)
            print("Data berhasil disimpan")

        elif pilihan == "0":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid")


# Menjalankan program utama
if __name__ == "__main__":
    main()
