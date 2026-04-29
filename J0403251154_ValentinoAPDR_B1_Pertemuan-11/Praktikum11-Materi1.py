#===============================================
# Nama : Valentino Agripina Pranaja de Ropa
# NIM : J0403251154
# Kelas : B / P1
#===============================================
#Implemantasi Dasar Graph
#===============================================

graph = {
    'A': ['B','C'],
    'B': ['A','D'],
    'C': ['A','D'],
    'D': ['B','C']
}

for node in graph:
    print(node, "->", graph[node])


# Penjelasan:
# Graph di atas direpresentasikan menggunakan dictionary, dimana setiap key adalah node dan value-nya adalah list dari node-node yang terhubung dengan key tersebut. Misalnya, node 'A' terhubung dengan node 'B' dan 'C', sehingga value untuk key 'A' adalah ['B', 'C'].
# Output dari kode di atas akan menampilkan setiap node beserta node-node yang terhubung dengannya, seperti berikut:
# A -> ['B', 'C']
# B -> ['A', 'D']
# C -> ['A', 'D']
# D -> ['B', 'C']
