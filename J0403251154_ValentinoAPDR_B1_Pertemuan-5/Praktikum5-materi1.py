#=============================================
# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPL B/P1
#=============================================

#=============================================
# Materi Rekursif: Faktorial
# Recursive case: 3! = 3 x 2 x 1
# Base case: jika n == 0 maka berhenti
#=============================================

def faktorial(n):
    # Base case
    if n == 0:
        return 1
    
    # Recursive case
    return n * faktorial(n - 1)


print("===== Program Faktorial =====")

f = int(input("Masukkan angka: "))

if f < 0:
    print("Faktorial tidak bisa untuk angka negatif.")
else:
    print("Hasil faktorial:", faktorial(f))

print("Program selesai.")