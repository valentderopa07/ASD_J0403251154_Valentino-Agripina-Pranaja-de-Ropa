# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPLB1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================
# Latihan 3 - Implementasi Algoritma Prim
# ==========================================================

import heapq  # Priority queue (min-heap) untuk efisiensi Prim

# ----------------------------------------------------------
# Representasi graph sebagai adjacency dictionary
# graph[node] = {tetangga: bobot}
# ----------------------------------------------------------
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# ----------------------------------------------------------
# Fungsi prim: membangun MST dari node 'start'
# ----------------------------------------------------------
def prim(graph, start):
    visited = set([start])  # Mulai: hanya node awal yang dikunjungi
    edges = []              # Min-heap kandidat edge

    # Masukkan semua edge dari node awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        # Ambil edge dengan bobot terkecil dari heap
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            # Node v belum dikunjungi → edge ini valid untuk MST
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Tambahkan edge-edge dari node v sebagai kandidat baru
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


# ----------------------------------------------------------
# Jalankan Prim dari node 'A'
# ----------------------------------------------------------
mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)


# ==========================================================
# Jawaban Analisis:
#
# 1. Node awal apa yang digunakan?
#    Node 'A' digunakan sebagai titik awal pembangunan MST.
#
# 2. Edge mana yang dipilih pertama kali?
#    Edge A-C dengan bobot 2. Dari node A, edge terkecil yang
#    tersedia adalah A-C (bobot 2) dibanding A-B (4) atau A-D (5).
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim menggunakan min-heap. Setiap kali node baru ditambahkan
#    ke MST, semua edge dari node tersebut ke node yang belum
#    dikunjungi dimasukkan ke heap. Lalu heap selalu mengeluarkan
#    edge terkecil. Jika node tujuan sudah dikunjungi, edge di-skip.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobot = 2 + 1 + 3 = 6
#    Edge: A-C(2), C-D(1), D-B(3)
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    - Kruskal: melihat semua edge sekaligus, mengurutkan global,
#      lalu memilih dari seluruh graph. Cocok untuk sparse graph.
#    - Prim: tumbuh dari satu node, hanya melihat edge yang
#      bersentuhan dengan tree saat ini. Cocok untuk dense graph.
#    Keduanya menghasilkan MST yang sama (dengan total bobot sama),
#    tapi urutan edge yang dipilih bisa berbeda.
# ==========================================================