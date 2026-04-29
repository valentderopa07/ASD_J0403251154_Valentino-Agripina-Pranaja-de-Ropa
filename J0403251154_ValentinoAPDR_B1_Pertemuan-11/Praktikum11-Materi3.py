# =============================================
# Nama : Valentino Agripina Pranaja de Ropa
# NIM : J0403251154
# Kelas : B / P1
# =============================================
# Implementasi DFS (Depth First Search) pada Graph
# =============================================
graph = {
 'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'D': [],
 'E': [],
 'F': []
}

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited = set()
print("DFS dari A:")
dfs(graph, 'A', visited)

# Penjelasan:
# Fungsi dfs di atas menggunakan rekursi untuk melakukan penelusuran pada graph.
# Fungsi ini menerima tiga parameter: graph (struktur graph), node (node saat ini yang sedang diproses), dan visited (set untuk menyimpan node yang sudah dikunjungi).
# Proses DFS dimulai dengan menandai node saat ini sebagai sudah dikunjungi dan
# mencetak node tersebut. Kemudian, untuk setiap tetangga dari node saat ini, jika tetangga tersebut belum dikunjungi, fungsi dfs dipanggil secara rekursif untuk menelusuri tetangga tersebut. Output dari kode di atas akan menampilkan urutan node yang dikunjungi selama proses DFS, dimulai dari node 'A'.