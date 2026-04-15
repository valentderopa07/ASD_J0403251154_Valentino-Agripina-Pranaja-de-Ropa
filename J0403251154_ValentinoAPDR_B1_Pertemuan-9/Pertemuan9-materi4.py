########################################
# Latihan 4 : Membuat Node
########################################

# Class Node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan
    
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" -> ")
        inorder(node.right)

# Membuat tree
# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menjalankan traversal inorder
print("Hasil Traversal inorder: ")
inorder(root)