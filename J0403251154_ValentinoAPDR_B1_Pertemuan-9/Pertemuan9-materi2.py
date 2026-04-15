#==========================================================================
#Latihan 2 : Membuat Binary search
#==========================================================================

#class node digumakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menampilkan isi node
print("Data pada root", root.data)
print("Data child kiri root", root.left.data)
print("Data child kanan root", root.right.data)
print("child kiri dari b", root.left.left.data)
print("child kanan dari b", root.left.right.data)

'''
Kode tersebut membuat struktur **binary tree** sederhana dengan beberapa level. 
Pertama, class `Node` didefinisikan untuk menyimpan data dan dua pointer (`left` dan `right`) 
yang menunjuk ke anak kiri dan kanan. Root dibuat dengan data `"A"`, lalu ditambahkan child level 1 yaitu `"B"` di kiri dan `"C"` di kanan. 
Selanjutnya, pada node `"B"` ditambahkan child level 2 yaitu `"D"` di kiri dan `"E"` di kanan. Bagian `print` digunakan untuk menampilkan isi 
dari setiap node: data root, anak kiri dan kanan root, serta anak-anak dari node `"B"`. Dengan cara ini, kode menunjukkan bagaimana pohon biner 
dibangun dan bagaimana data tiap node bisa diakses melalui atribut `left` dan `right`.
'''