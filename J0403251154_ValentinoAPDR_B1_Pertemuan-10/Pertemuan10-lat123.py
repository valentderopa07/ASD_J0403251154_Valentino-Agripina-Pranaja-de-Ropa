#=======================================================================================
# Nama   : Valentino Agripina Pranaja de Ropa
# NIM    : J0403251154
# Kelas  : TPL B/P1
#=======================================================================================

#=======================================================================================
# Latihan 1 : BST
#=======================================================================================

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left,data)
    elif data > root.data:
        root.right = insert(root.right,data)

    return root

#Mengisi data pada BST 
root = None
data_list = [50,30,70,20,40,60,80]

for data in data_list:
    root = insert(root,data)

print("BST berhasil dibuat")


#========================================
#Latihan 2 : tranversal inorder
#========================================

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print ("Hasil Inorder: ")
inorder(root)

#========================================
#Latihan 3 : Search di BST
#========================================

def search(root,key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    if key < root.data:
        return search (root.left,key)
    else:
        return search (root.right,key)
    
# Uji pencarian
key = 40
if search (root,key):
    print("Data ditemukan")
else:
    print("Data ditemukan")