#==========================================================================
#Latihan 1 : Membuat node tree
#==========================================================================

#class node digumakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat root
root = Node("A")

#menampilkan isi node
print("Data pada root", root.data)
print("Data child kiri root", root.left)
print("Data child kanan root", root.right)

"""
Kode tersebut secara sederhana membuat struktur node untuk pohon biner. 
Class `Node` berfungsi sebagai cetakan, di mana 
setiap node memiliki tiga atribut: `data` untuk menyimpan nilai, `left` untuk anak kiri, dan `right` untuk anak kanan. 
Saat objek `root` dibuat dengan nilai `"A"`, node tersebut menjadi akar pohon. Karena anak kiri dan kanan belum diisi, keduanya bernilai `None`. 
Hasil cetakan menunjukkan isi root adalah `"A"`, sedangkan child kiri dan kanan masih kosong. 
"""