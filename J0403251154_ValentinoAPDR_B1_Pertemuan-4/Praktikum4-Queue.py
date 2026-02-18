#=======================================================================
#Nama : Valentino Agripina Pranaja de Ropa
#NIM  : J0403251154
#=======================================================================

#=======================================================================
#Implementasu Dasar : Queue pada Linked List
#=======================================================================


#membuat class Node (merupakan unit dasar dari LinkedList)
class Node:
    def __init__(self,data): #Konstruktor
        self.data = data #menyimpan nilai/data
        self.next = None #pointer ke note berikutnya (awal=none)

#Queue dengan 2 Pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang
    
    def is_empty(self):
        return self.front is None
        
    def enqueue(self,data):
        #menambah data di belakang (rear)
        nodeBaru = Node(data)

        #jika queue kosong, front da rear menunjuk ke node  yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #jika queue tidak kosong:
        #Rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        #rear pindah ke node baru
        self.rear = nodeBaru

    def dequeueu(self):
        #menghapus data dari depan
        # 1) ambil data yang paling depan
        data_terhapus = self.front.data

        # 2) geser front ke node berikutnya
        self.front =self.front.next

        # 3) jika setelah geser front menjadi none maka queue kosong
        # rear juga harus jadi none
        if self.front is None:
            self.rear = None
        return data_terhapus

    def tampilkan(self):
        #menampilkan isi queue dari front ke rear
        current = self.front
        print("Front", end=" -> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Rear")

#Instantiasi objek class QueueLL
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.tampilkan()

q.dequeueu()
q.tampilkan()