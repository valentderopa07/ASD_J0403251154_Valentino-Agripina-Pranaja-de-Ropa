########################################
# Latihan 5 : Membuat Node
########################################

# Class Node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan
    
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" -> ")
        

# Membuat tree
# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menjalankan traversal postorder
print("Hasil Traversal postorder: ")
postorder(root)
'''
Penjelasan :
Pada latihan kali ini, dibuat salah satu struktur data yaitu tree yang dimana memiliki cara pengurutan yang berbeda-beda 
dan disini dipakai cara pengurutan preorder, cara pengurutannya adalah left -> right -> root.

dimulai dari kiri bawah yaitu child level 2 dari B yaitu D dan E dilanjut dengan child level 1 kanan yaitu A baru terakhir root yaitu A

Berikut visualisasi nya:
D -> E -> B -> C -> A
'''