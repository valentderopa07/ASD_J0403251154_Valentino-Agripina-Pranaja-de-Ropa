#===============================================
# Nama : Valentino Agripina Pranaja de Ropa
# NIM : J0403251154
# Kelas : B / P1
#===============================================
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

'''Pertanyaan Analisis
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
2. Apa yang terjadi jika urutan neighbor diubah?
3. Bandingkan hasil DFS dengan BFS pada graph yang sama.'''

#1. DFS masuk ke node terdalam terlebih dahulu karena algoritma ini menggunakan pendekatan rekursif atau stack untuk menyimpan node yang akan diproses. Ketika DFS menemukan sebuah node, ia akan langsung melanjutkan ke salah satu tetangganya yang belum dikunjungi, dan terus melanjutkan hingga mencapai node yang tidak memiliki tetangga yang belum dikunjungi. Setelah itu, DFS akan kembali ke node sebelumnya dan mencoba tetangga lainnya.
#2. Jika urutan neighbor diubah, hasil DFS juga akan berubah karena DFS akan mengikuti urutan tetangga yang diberikan. Misalnya, jika kita mengubah urutan neighbor dari node 'A' menjadi ['C', 'B'], maka DFS akan mengunjungi node 'C' terlebih dahulu sebelum node 'B', sehingga urutan kunjungan akan berbeda.
#3. Jika kita bandingkan hasil DFS dengan BFS pada graph yang sama, kita akan melihat bahwa DFS akan mengunjungi node-node yang lebih dalam terlebih dahulu, sedangkan BFS akan mengunjungi semua node pada level yang sama sebelum melanjutkan ke level berikutnya. Misalnya, untuk graph di atas, DFS dari 'A' akan menghasilkan urutan kunjungan seperti A -> B -> D -> E -> C -> F, sedangkan BFS dari 'A' akan menghasilkan urutan kunjungan seperti A -> B -> C -> D -> E -> F.