# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPLB1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 1 - Memahami Konsep Spanning Tree
# ==========================================================
# Graph yang digunakan: 4 node (A, B, C, D)
# Edge: A-B, A-C, A-D, C-D, B-D
# Graph ini mengandung cycle sehingga bukan spanning tree

# ----------------------------------------------------------
# Daftar semua edge pada graph awal (unweighted)
# ----------------------------------------------------------
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# ----------------------------------------------------------
# Contoh spanning tree yang valid dari graph di atas
# Spanning tree dipilih manual: A-C, C-D, D-B
# → Semua node (A, B, C, D) terhubung, tidak ada cycle
# → Jumlah edge = 4 - 1 = 3 ✓
# ----------------------------------------------------------
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# ----------------------------------------------------------
# Menampilkan semua edge pada graph awal
# ----------------------------------------------------------
print("=== Edge pada Graph Awal ===")
for edge in edges:
    print(f"  {edge[0]} - {edge[1]}")

# ----------------------------------------------------------
# Menampilkan edge pada spanning tree yang dipilih
# ----------------------------------------------------------
print("\n=== Contoh Spanning Tree yang Valid ===")
for edge in spanning_tree:
    print(f"  {edge[0]} - {edge[1]}")

# ----------------------------------------------------------
# Perbandingan jumlah edge
# ----------------------------------------------------------
print(f"\nJumlah edge graph awal    = {len(edges)}")
print(f"Jumlah edge spanning tree = {len(spanning_tree)}")

# Menghitung dan menampilkan node yang terlibat
nodes = set()
for u, v in spanning_tree:
    nodes.add(u)
    nodes.add(v)
print(f"Jumlah node               = {len(nodes)}")
print(f"Rumus edge spanning tree  = jumlah node - 1 = {len(nodes)} - 1 = {len(nodes)-1} ✓")


# ==========================================================
# Jawaban Analisis:
#
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki 5 edge dan mengandung cycle
#    (misal: A-D-C-A atau A-B-D-C-A). Spanning tree hanya
#    memiliki 3 edge, menghubungkan seluruh 4 node tanpa
#    siklus apapun.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Cycle berarti ada jalur ganda antara dua node, artinya
#    ada edge yang redundant (tidak diperlukan). Dalam konteks
#    nyata seperti jaringan kabel, edge ekstra itu hanya
#    menambah biaya tanpa memberi manfaat konektivitas baru.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Untuk menghubungkan N node tanpa cycle, cukup dibutuhkan
#    tepat N-1 edge. Setiap edge tambahan pasti membentuk
#    cycle karena semua node sudah terhubung. Itulah mengapa
#    spanning tree selalu punya tepat (jumlah node - 1) edge.
# ==========================================================