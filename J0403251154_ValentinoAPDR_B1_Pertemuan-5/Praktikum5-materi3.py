#=============================================
#Nama : Valentino Agripina Pranaja de Ropa
#NIM : J0403251154
#Kelas :TPL B/P1
#=============================================

#=============================================
#Materi Rekursif: Menjumlah elemen list
#=============================================

def jumlah_list(data, index=0):
    #base case
    if index == len(data):
        return 0
    
    #recursive case
    return data[index] + jumlah_list(data, index+1)

print("=====Program Jumlah Data======")
print(jumlah_list([2,4,5]))