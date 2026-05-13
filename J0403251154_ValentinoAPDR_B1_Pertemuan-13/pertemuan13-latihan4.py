# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPLB1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 4 - Studi Kasus: Jaringan Kabel Antar Gedung
# ==========================================================
# Kasus: Kampus ingin membangun jaringan internet antar gedung
# dengan total biaya pemasangan kabel yang minimum.
# Algoritma yang digunakan: Kruskal
# Alasan: edge-edge antar gedung jumlahnya tidak banyak (sparse),
# sehingga Kruskal cocok digunakan.

# ----------------------------------------------------------
# Representasi weighted graph sebagai adjacency dictionary
# Nama node = nama gedung kampus
# Bobot = biaya pemasangan kabel (satuan: juta rupiah / meter)
# ----------------------------------------------------------
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# ----------------------------------------------------------
# Membuat daftar edge dari adjacency dict untuk Kruskal
# Hindari duplikasi edge (A-B dan B-A adalah edge yang sama)
# ----------------------------------------------------------
edge_set = set()
edges = []

for u in graph:
    for v, weight in graph[u].items():
        # Simpan edge dengan urutan alphabetical agar tidak duplikat
        key = tuple(sorted([u, v]))
        if key not in edge_set:
            edge_set.add(key)
            edges.append((weight, u, v))

# ----------------------------------------------------------
# Implementasi Kruskal
# ----------------------------------------------------------
edges.sort()  # Urutkan berdasarkan biaya terkecil

mst = []
total_cost = 0
connected = set()

print("=== Proses Pemilihan Edge (Kruskal) ===")
for weight, u, v in edges:
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_cost += weight
        connected.add(u)
        connected.add(v)
        print(f"  ✓ Pilih: {u} - {v} (biaya={weight})")
    else:
        print(f"  ✗ Skip : {u} - {v} (biaya={weight}) → cycle")

# ----------------------------------------------------------
# Output hasil jaringan kabel minimum
# ----------------------------------------------------------
print("\n=== Jaringan Kabel Optimal (MST) ===")
for edge in mst:
    print(f"  {edge[0]}  ←→  {edge[1]}  |  Biaya = {edge[2]}")

print(f"\nTotal biaya minimum pemasangan kabel = {total_cost}")
print(f"Jumlah koneksi kabel = {len(mst)}")


# ==========================================================
# Jawaban Analisis:
#
# 1. Algoritma apa yang digunakan?
#    Algoritma Kruskal. Dipilih karena jumlah hubungan antar
#    gedung relatif sedikit (sparse graph), dan Kruskal efisien
#    untuk kasus seperti ini.
#
# 2. Edge mana saja yang dipilih?
#    - GedungC - GedungD (biaya = 1)
#    - GedungA - GedungC (biaya = 2)
#    - GedungB - GedungD (biaya = 3)
#
# 3. Berapa total biaya minimum?
#    Total = 1 + 2 + 3 = 6
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena MST menjamin semua gedung tetap terhubung (bisa
#    saling mengakses internet) tanpa kabel redundant. Tidak
#    perlu pasang kabel ekstra yang hanya menambah biaya tanpa
#    memberi koneksi baru. Hasilnya adalah jaringan paling hemat
#    yang tetap fungsional.
# ==========================================================