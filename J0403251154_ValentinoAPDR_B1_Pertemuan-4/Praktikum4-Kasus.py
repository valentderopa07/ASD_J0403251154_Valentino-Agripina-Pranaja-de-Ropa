#=============================================
#Nama : Valentino Agripina Pranaja de Ropa
#NIM : J0403251154
#Kelas :TPL B/P1
#=============================================

#=============================================
#Studi kasus : Sistem antrian layanan akademik
#Implementasi Queue =>
#Stack => Front -> C -> B -> A -> none
#Enqueue => Memindahkan pointer rear (Nambah data baru)
#Dequeue => memindakan pointer front (menghapus data dari depan)
#Queue => Front -> A -> B -> C ->Rear
#=============================================

#1. Mendefinisikan Node (unit dasar linked list)
class Node:
    def __init__(self,nim,nama):
        self.nim    = nim   #Menyimpan nim mahasiswa
        self.nama   = nama  #menyimpan nama mahasiswa
        self.next   = None  #pointer ke node berikutnya

#2. Mendifinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        
        self.front = None
        self.rear = None

    def is_empty(self):
        #KEtika queue kosong maka front = rear
        return self.front is None
    
    #Menanmbahkan data baru ke bagian belakang (rear) => menambahkan antrian mahasiswa yang akan mengajukan layanan akademik
    def enqueue(self,nim,nama):
        nodeBaru = Node(nim,nama)
        #Jika data baru masuk dari queue yang kosong maka data = front = rear
        if self. is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #Jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    #Menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong :(, tidak ada mahasiswa yang dilayani ")
            return None
        #lihat data bagian front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilaayni = self.front

        #geser pointer front ke next front
        self.front = self.front.next

        #Jika front menjadi none (data terakhir antrian yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None

        return node_dilaayni
    
    def tampilkan(self):

        print("Daftar antrian mahasiswa (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1


            

#Program utama
def main():

    #instalasi queue
    q = queueAkademik()
    print("")
    while True:
        print("=====Sistem Antrian Akademik=====")
        print("1. Tambah Layanan")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilihan Menu (1-4): ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()

            q.enqueue(nim,nama)
            print("Mahasiswa Berhasil Ditambahkan")


        elif pilihan == "2":
            dilaayni = q.dequeue()
            print(f"Mahasiswa dilayani : {dilaayni.nim} - {dilaayni.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program Selesai. Terimakasih")
            break
        else :
            print("Pilihan tidak valid. Silahkan coba lagi (1-4)")

if __name__ == "__main__":
    main()





