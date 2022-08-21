# ========== soal 1 ==========

angka = int(input('Masukkan angka : '))

if(angka % 2 == 0) :
    print('Angka {} tergolong bilangan GENAP!'.format(angka))
else :
    print('Angka {} tergolong bilangan GANJIL!'.format(angka))





# ========== soal 2 ==========
massa = int(input("Masukkan Massa(kg) : "))
tinggi = int(input("Masukkan Tinggi(cm) : "))

IMT = massa / ((tinggi/100)**2)

text = ""

if(IMT < 18.5) :
    text = "BERAT BADAN KURANG!"
elif(IMT >= 18.5 and IMT <= 24.9) :
    text = "BERAT BADAN IDEAL!"
elif(IMT >= 25.0 and IMT <= 29.9) :
    text = "BERAT BADAN BERLEBIH!"
elif(IMT >= 30.0 and IMT <= 39.9) :
    text = "BERAT BADAN SANGAT BERLEBIH!"
else :
    text = "OBESITAS!"

print("Massa " + str(massa) + " kg & tinggi " + str(tinggi/100) + " m")
print("IMT = " + str(IMT) + ", " + text)





# ========== market ==========
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

jumlahApel = int(input('Masukkan Jumlah Apel : '))
jumlahJeruk = int(input('Masukkan Jumlah Jeruk : '))
jumlahAnggur = int(input('Masukkan Jumlah Anggur : '))

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

jmlUang = int(input('Masukkan jumlah uang : '))

if(jmlUang > totalHarga) :
    kembali = jmlUang - totalHarga
    print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
elif(jmlUang == totalHarga) :
    print('Terima kasih')
else :
    kekurangan = totalHarga - jmlUang
    print('Transaksi anda dibatalkan \nuangnya kurang sebesar {}'.format(kekurangan))
