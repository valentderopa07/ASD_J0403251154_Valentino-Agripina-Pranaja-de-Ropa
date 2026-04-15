#=======================================================================================
# Membuat Traversal preorder
#=======================================================================================
# Class Node adalah unit dasar pada  tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

# Fungsi preorder root => left => right

def preorder(node):
    if node is not None:
        print(node.data, end="")
        preorder(node.left)
        preorder(node.right)

# Membuat tree
# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menjalankan traversal preorder
print("Hasil Traversal Preorder: ")
preorder(root)

'''
Penjelasan :
Pada latihan kali ini, dibuat salah satu struktur data yaitu tree yang dimana memiliki cara pengurutan yang berbeda-beda 
dan disini dipakai cara pengurutan preorder, cara pengurutannya adalah root -> left -> right.

A sebagai root, lalu dibawah sebelah kiri ada B sebagai child level 1 yang memiliki child level 2 D dan E dan 
Lalu ada C sebagai child level 1 di bawah root sebelah kanan
Berikut visualisasi nya:
ABDEC
'''