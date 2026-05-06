#===============================================
#Nama : Valentino Agripina Pranaja de Ropa
#NIM : J0403251154
#Kelas : B / P1
#===============================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================
import heapq
from turtle import distance
# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
 'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
 'Perpustakaan': {'Lab': 3},
 'Kantin': {'Lab': 4, 'Aula': 7},
 'Lab': {'Aula': 1},
 'Aula': {}
}
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?

# JAWABAN
#1. Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh 2 menit.
#2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit melalui jalur Gerbang -> Kantin -> Lab -> Aula.
#3. Tidak, jalur langsung tidak selalu menghasilkan jarak paling kecil karena bobot pada setiap edge dapat berbeda. Dalam kasus ini, meskipun ada jalur langsung dari Gerbang ke Aula melalui Kantin, jalur tersebut memiliki bobot yang lebih besar dibandingkan dengan jalur yang melalui Perpustakaan dan Lab. Oleh karena itu, dalam menentukan jalur terpendek, kita harus mempertimbangkan total bobot dari jalur tersebut, bukan hanya jumlah edge.
#4. Dijkstra cocok digunakan pada kasus lokasi kampus ini karena algoritma ini dirancang untuk menemukan jalur terpendek dalam graph dengan bobot positif, seperti waktu tempuh antara lokasi. Dijkstra efisien dan mudah diimplementasikan, sehingga sangat sesuai untuk aplikasi seperti ini di mana kita ingin mengetahui waktu tempuh tercepat antara berbagai lokasi di kampus.    
