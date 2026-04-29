# =============================================
# Nama : Valentino Agripina Pranaja de Ropa
# NIM : J0403251154
# Kelas : B / P1
# =============================================
# Implementasi BFS (Breadth First Search) pada Graph
# =============================================

from collections import deque

# Representasi Graph
graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D'],
    'C' : ['A', 'D'],
    'D' : ['B', 'C']
}

def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran/pencarian pada graph dengan BFS (Breadth First Search)
    # Graph : Dictionary yang menyimpan struktur dari graph
    # Start : Node awal penelusuran
    
    # Queue digunakan untuk menyimpan node yang akan diproses atau dibaca  
    queue = deque()
    
    # Variabel yang digunakan untuk menyimpan node yang sudah diproses/sudah dikunjungi
    visited = set()
    
    # Masukkan node awal ke queue
    queue.append(start)
    
    # Tandai node awal yang sudah masuk queue tadi sebagai node yang sudah dikunjungi
    visited.add(start)
    
    while queue:
        # Mengambil node paling depan dari queue 
        node = queue.popleft()
        print(node)
        
        # Periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            # Jika tetangga belum dikunjungi
            if neighbor not in visited:
                # Tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                # Masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)
                
                
# Menjalankan BFS dari node A
bfs(graph, 'A')

# penjelasan:
# Fungsi bfs di atas menggunakan struktur data queue untuk menyimpan node yang akan diproses
# dan set untuk menyimpan node yang sudah dikunjungi. Proses BFS dimulai dengan memasukkan node awal ke dalam queue, kemudian secara iteratif mengambil node dari queue, memprosesnya, dan menambahkan tetangganya yang belum dikunjungi ke dalam queue hingga semua node yang terhubung telah diproses. Output dari
# kode di atas akan menampilkan urutan node yang dikunjungi selama proses BFS, dimulai dari node 'A'.
