# ========== soal 1 ==========
# bentuk 1

stars = ''
size = 5

for i in range(size) :
    for j in range(size - i) :
        stars += '* '
    stars += '\n'

for i in range(1, size) :
    for j in range(i + 1) :
        stars += '* '
    stars += '\n'

print(stars)

# * * * * * 
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
# * * * * *

# bentuk 2

stars = ''
size = 5

for i in range(size) :
    for j in range(size - i) :
        stars += '  '
    for k in range(i * 2 + 1) :
        stars += '* '
    stars += '\n'

for i in range(1, size) :
    for j in range(i + 1) :
        stars += '  '
    for k in range((size * 2) - (i * 2) - 1) :
        stars += '* '
    stars += '\n'

print(stars)

#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *





# ========== market ==========

hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

stockApel = 5
stockJeruk = 7
stockAnggur = 6

while(True) :
    jumlahApel = int(input('Masukkan Jumlah Apel : '))
    if(jumlahApel > stockApel) :
        print('Jumlah yang dimasukkan terlalu banyak \nStock Apel tinggal : ' + str(stockApel))
    else :
        break
while(True) :
    jumlahJeruk = int(input('Masukkan Jumlah Jeruk : '))
    if(jumlahJeruk > stockJeruk) :
        print('Jumlah yang dimasukkan terlalu banyak \nStock Jeruk tinggal : ' + str(stockJeruk))
    else :
        break
while(True) :
    jumlahAnggur = int(input('Masukkan Jumlah Anggur : '))
    if(jumlahAnggur > stockAnggur) :
        print('Jumlah yang dimasukkan terlalu banyak \nStock Anggur tinggal : ' + str(stockAnggur))
    else :
        break

totalHargaApel = jumlahApel * hargaApel
totalHargaJeruk = jumlahJeruk * hargaJeruk
totalHargaAnggur = jumlahAnggur * hargaAnggur
totalHarga = totalHargaAnggur+totalHargaApel+totalHargaJeruk

print('''
    Detail Belanja

    Apel : {jmlApel} x {hrgApel} = {totalHrgApel}
    Jeruk : {jmlJeruk} x {hrgJeruk} = {totalHrgJeruk}
    Anggur : {jmlAnggur} x {hrgAnggur} = {totalHrgAnggur}

    Total : {totalHarga}
    '''.format(jmlApel=jumlahApel, hrgApel=hargaApel, totalHrgApel=totalHargaApel, 
        jmlJeruk=jumlahJeruk, hrgJeruk=hargaJeruk, totalHrgJeruk=totalHargaJeruk,
        jmlAnggur=jumlahAnggur, hrgAnggur=hargaAnggur, totalHrgAnggur=totalHargaAnggur,
        totalHarga=totalHarga))

while(True) :
    jmlUang = int(input('Masukkan jumlah uang : '))

    if(jmlUang > totalHarga) :
        kembali = jmlUang - totalHarga
        print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
        break
    elif(jmlUang == totalHarga) :
        print('Terima kasih')
        break
    else :
        kekurangan = totalHarga - jmlUang
        print('Uang anda kurang sebesar {}'.format(kekurangan))
