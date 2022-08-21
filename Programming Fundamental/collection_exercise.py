# ========== LIST ==========
# ========== soal 1 ==========
numbers = [41, 5, 1, 3, 89, 32]
minVal = numbers[0]
maxVal = numbers[0]

for num in numbers : 
    if(num < minVal) :
        minVal = num
    if(num > maxVal) :
        maxVal = num

print("Numbers = {}".format(numbers))
print("Minimum value = {}".format(minVal))
print("Maximum value = {}".format(maxVal))





# ========== soal 2 ==========
numbers = [41, 5, 1, 3, 89, 32]

print('List Sebelum Di Sort = {}'.format(numbers))

for i in range(len(numbers) - 1) :
    for j in range(i+1,len(numbers)) :
        if(numbers[i] > numbers[j]) :
            numbers[i],numbers[j] = numbers[j],numbers[i]
        
print('List Setelah Di Sort = {}'.format(numbers))





# ========== market ==========
listBuah = [
    ['Apel', 20, 10000],
    ['Jeruk', 15, 15000],
    ['Anggur', 25, 20000]
]

cart = []

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

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))

    elif(pilihanMenu == '2') :

        namaBuah = input('Masukkan Nama Buah : ')
        stockBuah = int(input('Masukkan Stock Buah : '))
        hargaBuah = int(input('Masukkan Harga Buah : '))
        listBuah.append([namaBuah,stockBuah,hargaBuah])
        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))

    elif(pilihanMenu == '3') :

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))
        indexBuah = int(input('Masukkan index buah yang ingin dihapus : '))
        del listBuah[indexBuah]
        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))

    elif(pilihanMenu == '4') :

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))
        while True :
            indexBuah = int(input('Masukkan index buah yang ingin dibeli : '))
            qtyBuah = int(input('Masukkan jumlah yang ingin dibeli : '))
            if(qtyBuah > listBuah[indexBuah][1]) :
                print('Stock tidak cukup, stock {} tinggal {}'.format(listBuah[indexBuah][0],listBuah[indexBuah][1]))
            else :
                cart.append([listBuah[indexBuah][0], qtyBuah, listBuah[indexBuah][2], indexBuah])
            print('Isi Cart :')
            print('Nama\t| Qty\t| Harga')
            for item in cart :
                print('{}\t| {}\t| {}'.format(item[0], item[1], item[2]))
            checker = input('Mau beli yang lain? (ya/tidak) = ')
            if(checker == 'tidak') :
                break
        print('Daftar Belanja :')
        print('Nama\t| Qty\t| Harga\t| Total Harga')
        totalHarga = 0
        for item in cart :
            print('{}\t| {}\t| {}\t| {}'.format(item[0], item[1], item[2], item[1] * item[2]))
            totalHarga += item[1] * item[2]    
        while True :
            print('Total Yang Harus Dibayar = {}'.format(totalHarga))
            jmlUang = int(input('Masukkan jumlah uang : '))
            if(jmlUang > totalHarga) :
                kembali = jmlUang - totalHarga
                print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
                for item in cart :
                    listBuah[item[3]][1] -= item[1]
                cart.clear()
                break
            elif(jmlUang == totalHarga) :
                print('Terima kasih')
                for item in cart :
                    listBuah[item[3]][1] -= item[1]
                cart.clear()
                break
            else :
                kekurangan = totalHarga - jmlUang
                print('Uang anda kurang sebesar {}'.format(kekurangan))
                
    elif(pilihanMenu == '5') :
        break




# ========== SET ==========
# ========== soal 1 ==========
setMovieKesukaanKu = set(input('Masukkan 5 Film Kesukaan anda dipisahkan dengan koma : ').split(','))
setMovieKesukaanTemanKu = set(input('Masukkan 5 Film Kesukaan teman anda dipisahkan dengan koma : ').split(','))

setMovieYangSama = setMovieKesukaanKu.intersection(setMovieKesukaanTemanKu)
print("Kesukaan Film kalian yang sama sebesar {}%".format((len(setMovieYangSama)/len(setMovieKesukaanKu)) * 100))





# ========== DICTIONARY ==========
# ========== soal 1 ==========
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

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i]['nama'],listBuah[i]['stock'],listBuah[i]['harga']))

    elif(pilihanMenu == '2') :

        namaBuah = input('Masukkan Nama Buah : ')
        stockBuah = int(input('Masukkan Stock Buah : '))
        hargaBuah = int(input('Masukkan Harga Buah : '))
        listBuah.append({
            'nama': namaBuah,
            'stock': stockBuah,
            'harga': hargaBuah
        })
        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i]['nama'],listBuah[i]['stock'],listBuah[i]['harga']))

    elif(pilihanMenu == '3') :

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i]['nama'],listBuah[i]['stock'],listBuah[i]['harga']))
        indexBuah = int(input('Masukkan index buah yang ingin dihapus : '))
        del listBuah[indexBuah]
        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i]['nama'],listBuah[i]['stock'],listBuah[i]['harga']))

    elif(pilihanMenu == '4') :

        print('Daftar Buah\n')
        print('Index\t| Nama  \t| Stock\t| Harga')
        for i in range(len(listBuah)) :
            print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i]['nama'],listBuah[i]['stock'],listBuah[i]['harga']))
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
                
    elif(pilihanMenu == '5') :
        break
