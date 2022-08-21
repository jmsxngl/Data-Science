# ========== FUNCTION ==========
# ========== regular function ==========

# ========== function without input and outpu ==========
def salam() :
    print('hello selamat datang di purwadhika')
    print('semoga hari anda menyenangkan')

salam()

salam()

test = salam() # tidak akan ada value apapun
print(test,type(test))



# ========== function with input but without output ==========
def salamBalik(nama,usia) :
    print('hello perkenalkan nama saya {}, usia saya {}'.format(nama,usia))
    print('senang bertemu dengan anda')

salamBalik('andi',25)

salamBalik(usia=27,nama ='budi')

salamBalik(30,'dedi') # argument terbalik tidak sesuai parameter 'nama','usia

# salamBalik('nyoman') # typeError missing argument : 'usia'
# salamBalik() # typeError missing argument : 'nama' and 'usia'



# ========== default parameter ==========
def salamBalik(nama = 'Unknown', usia = 0) :
    if(nama == 'Unknown' and usia > 0) :
        print('saya berusia {}'.format(usia))
    elif(nama != 'Unknown' and usia == 0) :
        print('hello nama saya {}'.format(nama))
    elif(nama != 'Unknown' and usia > 0) :
        print('hello perkenalkan nama saya {} dan usia saya {}'.format(nama,usia))
    print('senang bertemu dengan anda')

salamBalik(usia=25)
salamBalik('budi')
salamBalik(usia=30,nama='ciko')



# ========== function with input and output ==========

# contoh 1
def tambah(angka1,angka2) :
    return angka1 + angka2

hasil1 = tambah(5,4)
print(hasil1)

print(tambah(10,2))


# contoh 2
def coba(nama) :
    print('selamat datang {} di toko kue bahagia'.format(nama))
    print('kue nya dijamin bikin bahagia loh :p')

    while(True) :
        mau = input('mau coba kue ini ? : ')
        if(mau == 'yes') :
            print('thank you! silahkan ini kue nya :D')
            return 'kue cokelat'
        elif(mau == 'no') :
            break
        print('anda yakin?')

    print('semoga anda sudah bahagia dan sampai jumpa lagi -_-')

kue = coba('kuri')
print(kue,type(kue))



# ========== local variable vs global variable ==========

# local and global variable
# contoh 1
def coba() :
    print(x + 2)
    return x + 3

x = 5
print(coba(), x)


# contoh 2
def coba() :
    x = 8
    print(x + 2)
    return x + 3

x = 5
print(coba(), x)

# contoh 3
def coba() :
    x = 2
    x += 8
    print(x + 2)
    return x + 3

x = 5
print(coba(), x)

# contoh 4
def coba() :
    global x
    x += 8
    print(x + 2)
    return x + 3

x = 5
print(coba(), x)



# ========== callback function ==========
def tambah(num1,num2) :
    return num1 + num2

def kurang(num1,num2) :
    return num1 - num2

def hitung(fnOperator, angka1, angka2) :
    hasil = fnOperator (angka1,angka2)
    return hasil

print(hitung(tambah, 9, 5))
print(hitung(kurang, 9, 5))




# ========== calling other function ==========
def tampilkanJawaban(jawaban) :
    print('hasil = {}'.format(jawaban))

def pertambahan(angka1, angka2) :
    hasil = angka1 + angka2
    tampilkanJawaban(hasil)

def pengurangan(angka1, angka2) :
    hasil = angka1 - angka2
    tampilkanJawaban(hasil)

def perkalian(angka1, angka2) :
    hasil = angka1 * angka2
    tampilkanJawaban(hasil)

def pembagian(angka1, angka2) :
    hasil = angka1 / angka2
    tampilkanJawaban(hasil)

pertambahan(10, 5)
pengurangan(10, 5)
perkalian(10, 5)
pembagian(10, 5)




# ========== recursive function ==========
def countdown(counter) :
    print(counter)
    counter -= 1

    if(counter >= 0) :
        countdown(counter)
        print('counter = {}'.format(counter))

countdown(3)



# ========== lamda function ==========
# ==========  map function ==========
# contoh 1
list1 = [1, 2, 3, 4, 5]

def kali2(angka) :
    return angka * 2

hasilMap = map(kali2,list1)
print(hasilMap, type(hasilMap))

hasilMapList = list(hasilMap)
print(hasilMapList)

# contoh 2 (with lamba function)
list1 = [1, 2, 3, 4, 5]

hasilMapList1 = list(map(lambda angka : angka * 2, list1))
print(hasilMapList1)

# contoh 3
def mapDuplikat(fn,collection) :
    newCollection = []
    for item in collection :
        newCollection.append(fn(item))

    return newCollection

list1 = [1, 2, 3, 4, 5]

def ubah(angka) :
    return 'angka {}'.format(angka)

newList1 = mapDuplikat(ubah,list1)
print(newList1)

# contoh 4 (with lambda function (more simple))
print(mapDuplikat(lambda angka : 'angka {}'.format(angka),list1))



# ==========  filter function ==========
# contoh 1
list1 = [1, 2, 3, 4, 5]

def angkaGenap(angka) :
    return angka % 2 == 0

hasilFilter = filter(angkaGenap, list1)
print(hasilFilter, type(hasilFilter))

hasilFilterList = list(hasilFilter)
print(hasilFilterList)

# contoh 2 (with lambda function (more simple))
hasilFilterList = list(filter(lambda angka : angka % 2 == 0,list1))
print(hasilFilterList)

# contoh 3
def filterDuplikat(fn, collection) :
    newCollection = []
    for item in collection :
        if(fn(item)) :
            newCollection.append(item)

    return newCollection

list1 = [1, 2, 3, 4, 5]

def angkaGenap(angka) :
    return angka % 2 == 0

newList = filterDuplikat(angkaGenap,list1)
print(newList)

# contoh 4 (with lambda function (more simple))
print(filterDuplikat(lambda angka : angka % 2 == 0, list1))
