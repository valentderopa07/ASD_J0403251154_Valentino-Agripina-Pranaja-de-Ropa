#===============================================
# Nama : Valentino Agripina Pranaja de Ropa
# NIM : J0403251154
# Kelas : B / P1
#===============================================
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print()
print("BFS dari Rumah:")
bfs(graph, 'Rumah')

'''Pertanyaan Analisis
1. Node mana yang dikunjungi pertama?
2. Mengapa BFS cocok untuk mencari jalur terdekat?
3. Apa perbedaan urutan BFS jika struktur graph diubah?'''

#1. Node yang dikunjungi pertama adalah 'Rumah', karena BFS memulai penelusuran dari node awal yang diberikan, yaitu 'Rumah'.
#2. BFS cocok untuk mencari jalur terdekat karena BFS mengeksplorasi semua node pada level yang sama sebelum melanjutkan ke level berikutnya. Dengan cara ini, BFS akan menemukan jalur terpendek (dalam hal jumlah edge) dari node awal ke node tujuan jika ada.
#3. Jika struktur graph diubah, urutan BFS akan berubah sesuai dengan hubungan antar node yang baru. Misalnya, jika kita menambahkan node baru yang terhubung langsung ke 'Rumah', maka node tersebut akan dikunjungi lebih awal dalam urutan BFS dibandingkan dengan node-node yang sebelumnya terhubung ke 'Rumah'. Urutan BFS sangat bergantung pada struktur graph dan hubungan antar node.