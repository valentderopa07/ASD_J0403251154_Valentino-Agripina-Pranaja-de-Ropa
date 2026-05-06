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