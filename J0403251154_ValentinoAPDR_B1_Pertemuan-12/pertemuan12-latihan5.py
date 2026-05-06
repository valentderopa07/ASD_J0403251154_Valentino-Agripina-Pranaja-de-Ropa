#===============================================
#Nama : Valentino Agripina Pranaja de Ropa
#NIM : J0403251154
#Kelas : B / P1
#===============================================

#===============================================
# STUDI KASUS
#===============================================

import heapq

# Representasi weighted graph antar kota menggunakan dictionary bersarang
# Bobot menunjukkan jarak (atau waktu tempuh) antar kota
graph = {
    'Bogor'   : {'Jakarta': 5, 'Depok': 2},
    'Depok'   : {'Jakarta': 2, 'Bandung': 6},
    'Jakarta' : {'Bandung': 7},
    'Bandung' : {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga (belum diketahui)
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    # Node dengan jarak terkecil akan diproses lebih dulu
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari yang sudah tercatat,
        # berarti sudah ada jalur lebih pendek sebelumnya, lewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Tentukan node awal: Bogor
node_awal = 'Bogor'
hasil = dijkstra(graph, node_awal)

# Tampilkan hasil jarak terpendek dari Bogor ke semua kota
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")


# Jawaban Analisis: 
# 1. Node awal yang digunakan apa? 
# 2. Node mana yang memiliki jarak paling kecil dari node awal? 
# 3. Node mana yang memiliki jarak paling besar dari node awal? 
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat. 

# JAWABAN
# 1. Node awal yang digunakan adalah Bogor.
# 2. Node yang memiliki jarak paling kecil dari Bogor adalah Depok dengan jarak 2.
# 3. Node yang memiliki jarak paling besar dari Bogor adalah Bandung dengan jarak 8.
# 4. Dijkstra bekerja dengan memilih node berbobot terkecil secara bertahap. Dimulai dari Bogor (jarak 0),
#    algoritma memperbarui jarak ke Depok (2) dan Jakarta (5). Kemudian memproses Depok karena jaraknya
#    terkecil, lalu memperbarui Jakarta menjadi 4 (Bogor->Depok->Jakarta = 2+2) dan Bandung menjadi 8
#    (Bogor->Depok->Bandung = 2+6). Selanjutnya memproses Jakarta (jarak 4), mencoba memperbarui Bandung
#    menjadi 4+7=11, namun 11 lebih besar dari 8 sehingga tidak diperbarui. Terakhir memproses Bandung
#    yang tidak memiliki tetangga. Hasil akhir: Bogor=0, Depok=2, Jakarta=4, Bandung=8.