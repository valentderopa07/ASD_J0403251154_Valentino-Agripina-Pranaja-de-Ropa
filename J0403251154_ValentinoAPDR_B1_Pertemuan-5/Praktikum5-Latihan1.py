#=============================================
# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPL B/P1
#=============================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    # Base case
    if n == 0:
        return 1

    # Recursive case
    return a * pangkat(a, n - 1)

print(pangkat(2, 4))  # Output: 16