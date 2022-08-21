# # ========== soal 1 ==========
x = 4
y = 3
z = 2

w = ((x+y*z)/(x*y)) ** z
print(w)





# ========== soal 2 ==========
a = int(input("Silahkan masukkan angka berapapun : "))

# print("Kuadrat dari " + a + " = " + str((int(a) ** 2)))
print('Kuadrat dari {} = {}'.format(a, a ** 2))





# ========== soal 3 ==========
import math

jmlHari = 485
sisaHari = jmlHari

# 485 / 360 = 1.34722 => dibulatkan kebawah jadi 1
# variable tahun isinya jadi int 1
tahun = math.floor(sisaHari/360)

# 485 % 360 = 125
# variable sisaHari isinya jadi int 125
sisaHari %= 360

# 125 / 30 = 4.1667 => dibulatkan kebawah jadi 4
# variable bulan isinya jadi int 4
bulan = math.floor(sisaHari/30)

# 125 % 30 = 5
# variable sisaHari isinya jadi int 5
sisaHari %= 30

# 5 / 7 = 0.7143 => dibulatkan kebawah jadi 0
# variable minggu isinya jadi int 0
minggu = math.floor(sisaHari/7)

# 5 % 7 = 5
# variable sisaHari isinya jadi tetap int 5
sisaHari %= 7

# ditampilkan ke terminal
print(str(jmlHari) + ' Hari adalah')
print('{} Tahun'.format(tahun))
print('{} Bulan'.format(bulan))
print('{} Minggu'.format(minggu))
print('{} Hari'.format(sisaHari))





# ========== soal 4 ==========
# usiaAndi + usiaBudi = 49
# rasio usiaAndi dan usiaBudi = 0.4 = 4 / 10 => 4 : 10 => 2 : 5
# rasio usiaAndi = 2 , rasio usiaBudi = 5
# total rasio = 2 + 5 = 7
# usiaAndi = total umur * (rasio usiaAndi / total rasio)
# usiaBudi = total umur * (rasio usiaBudi / total rasio)

totalUmur = 49
ratioAndi = 2
ratioBudi = 5
ratioTotal = 7

usiaAndi = totalUmur * (ratioAndi/ratioTotal)
usiaBudi = totalUmur * (ratioBudi/ratioTotal)

print('Usia Andi sekarang = {}'.format(usiaAndi))
print('Usia Budi sekarang = {}'.format(int(usiaBudi)))

print('Usia Andi 2 tahun lagi = ' + str(usiaAndi + 2))
print('Usia Budi 2 tahun lagi = ' + str(int(usiaBudi) + 2))




# ========== soal 5 ==========
# Dua mobil a dan b melaju berlawanan arah dan akan bertabrakan.
# Kita dapat hitung waktunya dengan menjumlahkan kecepatan dari kedua kendaraan tersebut.
# Lalu kemudian cari tahu dengan total kecepatan yang dimiliki,
# berapa waktu yang dibutuhkan untuk menempuh jarak tertentu

# 60 km/h + 40 km/h = 100 km/h
# Dengan kecepatan 100 km/h. Berapa waktu yang dibutuhkan untuk menempuh jarak 120 km?
# 120 / 100 = 1.2 jam
# 1.2 * 60 = 72 menit => 60 menit + 12 menit
# 9:00 => 10:12
# waktu bertemu jam 10 menit ke 12

import math 

jamAwal = 9
jarakKM = 120
kecepatanTotalKMperJam = 100
kecepatanTotalKMperDetik = kecepatanTotalKMperJam/3600

DetikTotal = jarakKM / kecepatanTotalKMperDetik
lamaJam = math.floor(DetikTotal / 3600)
lamaMenit = math.floor((DetikTotal%3600)/60)
lamaDetik = math.floor((DetikTotal%3600)%60)

print('Lama waktu ' +  str(lamaJam) + ' jam, ' + str(lamaMenit) + ' menit, ' + str(lamaDetik) + ' detik')
print('Tabraknya pukul {}:{}:{}'.format(jamAwal + lamaJam,lamaMenit,lamaDetik))




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

print('''
Detail Belanja

Apel : {jmlApel} x {hrgApel} = {totalHrgApel}
Jeruk : {jmlJeruk} x {hrgJeruk} = {totalHrgJeruk}
Anggur : {jmlAnggur} x {hrgAnggur} = {totalHrgAnggur}

Total : {totalHarga}
'''.format(jmlApel=jumlahApel, hrgApel=hargaApel, totalHrgApel=totalHargaApel, 
    jmlJeruk=jumlahJeruk, hrgJeruk=hargaJeruk, totalHrgJeruk=totalHargaJeruk,
    jmlAnggur=jumlahAnggur, hrgAnggur=hargaAnggur, totalHrgAnggur=totalHargaAnggur,
    totalHarga=(totalHargaAnggur+totalHargaApel+totalHargaJeruk)))

    # END
