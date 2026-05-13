# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPLB1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Materi 2 - Implementasi Algoritma Prim
# ==========================================================
# Algoritma Prim membangun MST dengan cara:
# 1. Mulai dari satu node awal
# 2. Selalu pilih edge berbobot terkecil yang menghubungkan
#    node yang sudah dikunjungi ke node yang belum
# 3. Lanjutkan sampai semua node terhubung
# Prim menggunakan priority queue (min-heap) agar efisien

import heapq  # Modul heap untuk priority queue

# ----------------------------------------------------------
# Representasi graph sebagai adjacency dictionary
# Format: graph[node] = {tetangga: bobot, ...}
# ----------------------------------------------------------
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# ----------------------------------------------------------
# Fungsi prim: membangun MST menggunakan algoritma Prim
# Parameter:
#   graph - adjacency dict weighted graph
#   start - node awal untuk memulai pembangunan MST
# Return:
#   mst          - list edge yang terpilih (u, v, bobot)
#   total_weight - total bobot MST
# ----------------------------------------------------------
def prim(graph, start):
    visited = set([start])  # Set node yang sudah masuk MST
    edges = []              # Min-heap untuk kandidat edge

    # Masukkan semua edge dari node awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    # ----------------------------------------------------------
    # Proses utama: selalu ambil edge terkecil dari heap
    # Jika node tujuan belum dikunjungi → tambahkan ke MST
    # ----------------------------------------------------------
    while edges:
        weight, u, v = heapq.heappop(edges)  # Ambil edge terkecil

        if v not in visited:
            # Node v belum dikunjungi → edge ini aman, tidak membentuk cycle
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            print(f"  Pilih edge {u}-{v} (bobot={weight}) → node aktif: {sorted(visited)}")

            # Tambahkan semua edge dari node v ke heap (kandidat berikutnya)
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
        else:
            print(f"  Skip edge {u}-{v} (bobot={weight}) → {v} sudah dikunjungi")

    return mst, total_weight


# ----------------------------------------------------------
# Jalankan Prim mulai dari node 'A'
# ----------------------------------------------------------
print("=== Proses Algoritma Prim (mulai dari 'A') ===")
mst, total = prim(graph, 'A')

print("\n=== Minimum Spanning Tree (Prim) ===")
for edge in mst:
    print(f"  {edge[0]} - {edge[1]}, bobot = {edge[2]}")

print(f"\nTotal bobot MST = {total}")