# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPLB1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Materi 1 - Implementasi Algoritma Kruskal
# ==========================================================
# Algoritma Kruskal membangun MST dengan cara:
# 1. Mengurutkan semua edge dari bobot terkecil ke terbesar
# 2. Memilih edge satu per satu selama tidak membentuk cycle
# 3. Berhenti saat semua node sudah terhubung

# ----------------------------------------------------------
# Daftar edge graph: format (bobot, node1, node2)
# Graph ini merepresentasikan weighted undirected graph
# dengan 4 node: A, B, C, D
# ----------------------------------------------------------
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# ----------------------------------------------------------
# Langkah 1: Urutkan semua edge berdasarkan bobot terkecil
# Sorting ini adalah inti dari pendekatan greedy Kruskal
# ----------------------------------------------------------
edges.sort()

mst = []          # List untuk menyimpan edge yang masuk MST
total_weight = 0  # Akumulator total bobot MST

# connected = set node yang sudah terhubung dalam MST
# Ini adalah pendekatan deteksi cycle yang disederhanakan
connected = set()

# ----------------------------------------------------------
# Langkah 2: Iterasi setiap edge (sudah terurut)
# Pilih edge jika tidak menyebabkan cycle
# ----------------------------------------------------------
for weight, u, v in edges:
    # Kondisi: edge aman jika minimal salah satu node-nya
    # belum ada di MST (tidak akan membentuk cycle sederhana)
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)
        print(f"  Pilih edge {u}-{v} (bobot={weight}) → DITAMBAHKAN ke MST")
    else:
        print(f"  Skip edge {u}-{v} (bobot={weight}) → akan membentuk cycle")

# ----------------------------------------------------------
# Output hasil MST
# ----------------------------------------------------------
print("\n=== Minimum Spanning Tree (Kruskal) ===")
for edge in mst:
    print(f"  {edge[0]} - {edge[1]}, bobot = {edge[2]}")

print(f"\nTotal bobot MST = {total_weight}")
print(f"Jumlah edge MST = {len(mst)} (= jumlah node - 1 = {len(connected)} - 1)")