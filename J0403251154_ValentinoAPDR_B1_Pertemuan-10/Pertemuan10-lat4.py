#=======================================================================================
# Nama   : Valentino Agripina Pranaja de Ropa
# NIM    : J0403251154
# Kelas  : TPL B/P1
#=======================================================================================

# ==========================================================
# Latihan 4: Membuat BST yang Tidak Seimbang
# ==========================================================
# Diskusi:
# Ketika data dimasukkan secara berurutan naik (10, 20, 30),
# setiap nilai baru selalu lebih besar dari node sebelumnya,
# sehingga semua node masuk ke subtree KANAN terus-menerus.
# Hasilnya, tree menjadi condong ke kanan (right-skewed),
# menyerupai Linked List. Ini adalah kelemahan BST biasa:
# tidak ada mekanisme otomatis untuk menjaga keseimbangan.
# Semakin panjang tree seperti ini, pencarian menjadi O(n),
# bukan O(log n) seperti pada tree yang seimbang.

# Class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data      # nilai pada node
        self.left = None      # child kiri
        self.right = None     # child kanan

# Fungsi insert untuk BST
def insert(root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data)
    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

# Fungsi preorder untuk melihat bentuk tree
# Urutan kunjungan: Akar → Kiri → Kanan
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi sederhana untuk menampilkan struktur tree
# level menunjukkan kedalaman node, posisi menunjukkan arah (L/R/Root)
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("   " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# -----------------------------
# Program utama
# -----------------------------
root = None

# Data dimasukkan berurutan naik → menghasilkan tree condong kanan
# Struktur yang terbentuk:
# 10
#  \
#   20
#    \
#     30
data_list = [10, 20, 30]
for data in data_list:
    root = insert(root, data)

print("Preorder BST:")
preorder(root)

print("\n\nStruktur BST:")
tampil_struktur(root)

# Output yang diharapkan:
# Preorder BST:
# 10 20 30
#
# Struktur BST:
# Root: 10
#    R: 20
#       R: 30
#
# Kesimpulan diskusi:
# - Tree condong ke kanan karena data masuk berurutan naik
# - BST tidak selalu seimbang, tergantung urutan data yang dimasukkan
# - Pencarian pada tree seperti ini bisa lambat karena menelusuri
#   setiap node satu per satu, seperti Linked List (kompleksitas O(n))
# - Solusinya adalah menggunakan AVL Tree yang menjaga keseimbangan
#   secara otomatis dengan mekanisme rotasi