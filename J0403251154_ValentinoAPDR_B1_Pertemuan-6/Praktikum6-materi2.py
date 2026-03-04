#==============================================================
# Nama : Valentino Agripina Pranaja de Ropa
# NIM  : J0403251154
# Kelas: TPL B1
#==============================================================

#==============================================================
#Insertion Sort dengan tracing
#==============================================================

def insertion_sort(data):
    
    #melihat data awal
    print("Data awal: ", data)
    print("="*50)
    
    #Loop mulai dari data ke 2 (index array ke 1
    for i in range(1, len(data)):
        
        key = data[i] #simpan nilai yang disisipkan
        j = i-1 #index elemen terakhir di bagian kiri

        print("Iterasi ke-",i)
        print("Nilai key: ", key)
        print("Bagian kiri (terurut): ",data[:i])
        print("Bagian kanan (belum terurut): ",data[i:])

        #Geser 
        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disisipkan: ", data)
        print("-"*50)

    return data

angka = [7,8,5,2,4,6]
print('Hasil Sorting: ', insertion_sort(angka))