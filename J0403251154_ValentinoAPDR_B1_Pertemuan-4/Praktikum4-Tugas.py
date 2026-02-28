#=============================================
# Nama  : Valentino Agripina Pranaja de Ropa
# NIM   : J0403251154
# Kelas : TPL B/P1
#=============================================

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# Konsep: Implementasi Queue menggunakan Linked List (FIFO)
# Queue  : Front -> A -> B -> C -> Rear
# Enqueue: Menambahkan data di belakang (rear)
# Dequeue: Menghapus data dari depan (front)
# ==========================================================


# 1. Mendefinisikan Node (unit dasar Linked List)
class Node:
    def __init__(self, no_antrian, nama, servis):
        self.no_antrian = no_antrian   # Menyimpan nomor antrian
        self.nama = nama               # Menyimpan nama pelanggan
        self.servis = servis           # Menyimpan jenis servis
        self.next = None               # Pointer ke node berikutnya


# 2. Mendefinisikan Queue (memiliki front dan rear)
class QueueBengkel:
    def __init__(self):
        self.front = None   # Menunjuk pelanggan paling depan
        self.rear = None    # Menunjuk pelanggan paling belakang

    def is_empty(self):
        # Queue kosong jika front bernilai None
        return self.front is None

    # Menambahkan pelanggan ke bagian belakang (rear)
    def enqueue(self, no_antrian, nama, servis):
        nodeBaru = Node(no_antrian, nama, servis)

        # Jika antrian kosong
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
        else:
            self.rear.next = nodeBaru
            self.rear = nodeBaru

    # Menghapus pelanggan paling depan (dilayani)
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong. Tidak ada pelanggan yang dilayani.")
            return None

        # Simpan data yang akan dilayani
        node_dilayani = self.front

        # Geser pointer front ke node berikutnya
        self.front = self.front.next

        # Jika setelah digeser menjadi None,
        # berarti antrian sudah kosong
        if self.front is None:
            self.rear = None

        return node_dilayani

    # Menampilkan seluruh antrian
    def tampilkan(self):
        if self.is_empty():
            print("Antrian kosong.")
            return

        print("\nDaftar Antrian Bengkel (Front -> Rear):")
        current = self.front
        no = 1

        while current is not None:
            print(f"{no}. No Antrian: {current.no_antrian} | "
                  f"Nama: {current.nama} | "
                  f"Servis: {current.servis}")
            current = current.next
            no += 1


# ==========================================================
# Program Utama
# ==========================================================
def main():

    # Inisialisasi Queue
    q = QueueBengkel()

    while True:
        print("\n===== Sistem Antrian Bengkel Motor =====")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilihan Menu (1-4): ").strip()

        if pilihan == "1":
            no_antrian = input("Masukkan Nomor Antrian : ").strip()
            nama = input("Masukkan Nama Pelanggan : ").strip()
            servis = input("Masukkan Jenis Servis : ").strip()

            q.enqueue(no_antrian, nama, servis)
            print("Pelanggan berhasil ditambahkan ke antrian.")

        elif pilihan == "2":
            dilayani = q.dequeue()
            if dilayani is not None:
                print(f"Pelanggan dilayani: {dilayani.no_antrian} - "
                      f"{dilayani.nama} ({dilayani.servis})")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi (1-4).")


if __name__ == "__main__":
    main()