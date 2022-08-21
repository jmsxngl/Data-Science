# ========== soal 1 ==========

def ganjilGenap(angka) :
    if(angka % 2 == 0) :
        return 'Genap'
    return 'Ganjil'

def ubahJadiGanjilGenap(listAngka) :
    return list(map(ganjilGenap, listAngka))

list1 = [1,3,4,5]
list2 = [22,17,19,20,14]
list3 = [1,3,5]
list4 = [2,4,6]

list1 = ubahJadiGanjilGenap(list1)
list2 = ubahJadiGanjilGenap(list2)
list3 = ubahJadiGanjilGenap(list3)
list4 = ubahJadiGanjilGenap(list4)

print(list1)
print(list2)
print(list3)
print(list4)





# ========== soal 2 ==========

def filterGaji(listGaji) :
    return list(filter(lambda gaji : gaji * 95/100 > 9000000, listGaji))

list1 = [9100000,9800000,9500000,10300000,9300000]

list1 = filterGaji(list1)

print(list1)




# ========== market ==========

listBuah = [
    {
        'nama': 'Apel',
        'stock': 20,
        'harga': 10000
    },
    {
        'nama': 'Jeruk',
        'stock': 15,
        'harga': 15000
    },
    {
        'nama': 'Anggur',
        'stock': 25,
        'harga': 20000
    }
]

cart = []

def menampilkanDaftarBuah() :
    print('Daftar Buah\n')
    print('Index\t| Nama  \t| Stock\t| Harga')
    for i in range(len(listBuah)) :
        print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i]['nama'],listBuah[i]['stock'],listBuah[i]['harga']))

def menambahBuah() :
    namaBuah = input('Masukkan Nama Buah : ')
    stockBuah = int(input('Masukkan Stock Buah : '))
    hargaBuah = int(input('Masukkan Harga Buah : '))
    listBuah.append({
        'nama': namaBuah,
        'stock': stockBuah,
        'harga': hargaBuah
    })
    menampilkanDaftarBuah()

def menghapusBuah() :
    menampilkanDaftarBuah()
    indexBuah = int(input('Masukkan index buah yang ingin dihapus : '))
    del listBuah[indexBuah]
    menampilkanDaftarBuah()

def membeliBuah() :
    menampilkanDaftarBuah()
    while True :
        indexBuah = int(input('Masukkan index buah yang ingin dibeli : '))
        qtyBuah = int(input('Masukkan jumlah yang ingin dibeli : '))
        if(qtyBuah > listBuah[indexBuah]['stock']) :
            print('Stock tidak cukup, stock {} tinggal {}'.format(listBuah[indexBuah]['nama'],listBuah[indexBuah]['stock']))
        else :
            cart.append({
                'nama': listBuah[indexBuah]['nama'], 
                'qty': qtyBuah, 
                'harga': listBuah[indexBuah]['harga'], 
                'index': indexBuah
            })
        print('Isi Cart :')
        print('Nama\t| Qty\t| Harga')
        for item in cart :
            print('{}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga']))
        checker = input('Mau beli yang lain? (ya/tidak) = ')
        if(checker == 'tidak') :
            break

    print('Daftar Belanja :')
    print('Nama\t| Qty\t| Harga\t| Total Harga')
    totalHarga = 0
    for item in cart :
        print('{}\t| {}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga'], item['qty'] * item['harga']))
        totalHarga += item['qty'] * item['harga']    
    while True :
        print('Total Yang Harus Dibayar = {}'.format(totalHarga))
        jmlUang = int(input('Masukkan jumlah uang : '))
        if(jmlUang > totalHarga) :
            kembali = jmlUang - totalHarga
            print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
            for item in cart :
                listBuah[item['index']]['stock'] -= item['qty']
            cart.clear()
            break
        elif(jmlUang == totalHarga) :
            print('Terima kasih')
            for item in cart :
                listBuah[item['index']]['stock'] -= item['qty']
            cart.clear()
            break
        else :
            kekurangan = totalHarga - jmlUang
            print('Uang anda kurang sebesar {}'.format(kekurangan))

while True :
    pilihanMenu = input('''
        Selamat Datang di Pasar Buah

        List Menu :
        1. Menampilkan Daftar Buah
        2. Menambah Buah
        3. Menghapus Buah
        4. Membeli Buah
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        menampilkanDaftarBuah()
    elif(pilihanMenu == '2') :
        menambahBuah()
    elif(pilihanMenu == '3') :
        menghapusBuah()
    elif(pilihanMenu == '4') :
        membeliBuah()
    elif(pilihanMenu == '5') :
        break
