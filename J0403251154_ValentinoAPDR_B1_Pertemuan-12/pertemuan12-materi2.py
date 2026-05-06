#===============================================
#Nama : Valentino Agripina Pranaja de Ropa
#NIM : J0403251154
#Kelas : B / P1
#===============================================

#===============================================
#Implementasi Bellman-Ford
#===============================================


def bellman_ford(graph, start): 
 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 
 
    # Relaksasi berulang 
    for _ in range(len(graph) - 1): 
 
        for node in graph: 
 
            for neighbor, weight in graph[node].items(): 
 
                if distances[node] + weight < distances[neighbor]: 
 
                    distances[neighbor] = distances[node] + weight 
 
    return distances 

'''
Penjelasan:
1. Fungsi bellman_ford menerima graph dan node awal sebagai input.
2. Jarak semua node diinisialisasi dengan nilai tak hingga, kecuali node awal yang diinisialisasi dengan 0.
3. Relaksasi dilakukan sebanyak (jumlah node - 1) kali.
4. Pada setiap iterasi relaksasi, semua edge dalam graph diperiksa.
5. Jika ditemukan jarak yang lebih kecil, jarak tersebut diperbarui.
6. Hasil akhir adalah jarak terpendek dari node awal ke semua node lain dalam graph.
7. Bellman-Ford dapat menangani graph dengan bobot negatif, tetapi tidak boleh ada siklus negatif.'''