#=============================================
# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPL B/P1
#=============================================

#=============================================
# Materi Rekursif: Call Stack
# Tracing bilangan (masuk - keluar)
#
# Contoh:
# Input 3
# Masuk  : 3 2 1
# Keluar : 1 2 3
#=============================================

def hitung(n):
    # Base case
    if n == 0:
        print("\nSelesai\n")
        return

    # Proses sebelum rekursi (Masuk ke stack)
    print("Masuk :", n)

    # Recursive call
    hitung(n - 1)

    # Proses setelah rekursi (Keluar dari stack)
    print("Keluar:", n)


print("===== Program Tracing Call Stack =====")
angka = int(input("Masukkan angka yang ingin ditracing: "))

if angka < 0:
    print("Masukkan angka positif!")
else:
    hitung(angka)

print("\nProgram selesai.")