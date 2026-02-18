#=======================================================================
#Nama : Valentino Agripina Pranaja de Ropa
#NIM  : J0403251154
#=======================================================================

#=======================================================================
#Implementasu Dasar : Node pada Linked List
#=======================================================================


#membuat class Node (merupakan unit dasar dari LinkedList)
class Node:
    def __init__(self,data): #Konstruktor
        self.data = data #menyimpan nilai/data
        self.next = None #pointer ke note berikutnya (awal=none)

# 1) membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menetukan node Pertama (head)
head = nodeA

# 4) Traversal : menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data)    # menampilkan data pada note saat ini
    current = current.next # pindah ke node berikutnya

#====================================================
#Implementasi Dasar : Linked List + Insert Awal
#====================================================

class LinkedList: #class implementasi stack
    def __init__(self):
        self.head = None # awalnya Kosong

    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peek dalam stack
        # menggeser heas ke node berikutnya
        self.head = self.head.next
        print("Node yang dihapus adalah :", data_terhapus)

    def insert_awal(self,data): #push dalam stack
        # 1) buat node baru
        nodeBaru = Node(data) #panggil class node

        # 2) node baru menunjuk ke head lama
        nodeBaru.next = self.head

        # 3) head pindah ke node baru
        self.head = nodeBaru

    def tampilkan(self): #implementasi traversal
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print("=====List Baru=====")
ll = LinkedList() #instantiasi objek ke class Linked List
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()


