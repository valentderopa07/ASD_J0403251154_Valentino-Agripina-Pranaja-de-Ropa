# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPLB1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 2 - Implementasi Algoritma Kruskal
# ==========================================================

# ----------------------------------------------------------
# Daftar edge: (bobot, node1, node2)
# Ini adalah weighted graph dengan 4 node: A, B, C, D
# ----------------------------------------------------------
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# ----------------------------------------------------------
# Langkah Kruskal 1: Urutkan edge berdasarkan bobot terkecil
# Ini memastikan greedy selection selalu ambil yang terkecil
# ----------------------------------------------------------
edges.sort()

mst = []
total_weight = 0

# connected = set node yang sudah masuk ke MST
# Digunakan untuk deteksi cycle secara sederhana:
# jika kedua node sudah ada di connected → akan terbentuk cycle
connected = set()

# ----------------------------------------------------------
# Langkah Kruskal 2-6: Iterasi, periksa cycle, tambahkan/skip
# ----------------------------------------------------------
for weight, u, v in edges:
    # Edge aman jika setidaknya satu node belum terhubung
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

# ----------------------------------------------------------
# Tampilkan hasil MST
# ----------------------------------------------------------
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)


# ==========================================================
# Jawaban Analisis:
#
# 1. Edge mana yang dipilih pertama kali?
#    Edge C-D dengan bobot 1. Karena setelah diurutkan,
#    edge ini memiliki bobot paling kecil di antara semua edge.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Kruskal adalah algoritma greedy — selalu memilih pilihan
#    terbaik (terkecil) saat itu. Dengan memulai dari bobot
#    terkecil, total akumulasi bobot MST dijamin minimum.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot = 1 + 2 + 3 = 6
#    Edge yang dipilih: C-D(1), A-C(2), B-D(3)
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Edge A-B (bobot 4) dan A-D (bobot 5) tidak dipilih karena
#    saat gilirannya, semua node (A, B, C, D) sudah terhubung
#    melalui MST. Menambahkan edge tersebut hanya akan membentuk
#    cycle yang tidak diperlukan.
# ==========================================================