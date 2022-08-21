# ========== tipe data ==========

a = 'Hello Purwadhika'
b = 23
c = 23.5
d = ['jeruk', 'apel', 'mangga']
e = ('jeruk', 'apel', 'mangga')
f = range(7)
g = {'nama' : 'james', 'umur' : '29'}
h = {'jeruk', 'apel', 'mangga'}
i = True
j = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))



# ========== aritmatika ==========

a = 5; b = 10

# penjumlahan
hasil = a + b
print('hasil penjumlahan : ', hasil)

#pengurangan
hasil = b - a
print('hasil pengurangan : ', hasil)

# perkalian
hasil = a * b
print('hasil perkalian : ', hasil)

# pembagian
hasil = b / a
print('hasil pembagian : ', hasil)

#  modulus
hasil = b % a
print('hasil modulus : ', hasil)

# pemangkatan
hasil = b ** a
print('hasil pemangkatan : ', hasil)

# pembagian kebawah
a = 11; b = 3
hasil = a // b
print('hasil pembagian kebawah : ', hasil)



# ========== assigment operator ==========

x = 5

x += 2
print(x)

x -= 2 
print(x)

x *= 2
print(x)

x /= 2
print(x)

x %= 2
print(x)

x //= 2 
print(x)

x **= 2
print(x)



# ========== math module ==========

import math

print('ceil method') # pembulatan ke atas
x = 4.2
x = math.ceil(x)
print(x)
print(math.ceil(7.1))

print('floor method') # pembulatan ke bawah
x = 4.8
x = math.floor(x)
print(x)
print(math.floor(7.9))

print('fabs method') # angka absolut
x = -4.5
x = math.fabs(x)
print(x)
print(math.fabs(-7))

print('power method') # pangkat
x = 4
y = 3
hasil = math.pow(x,y)
print(hasil)
print(math.pow(2,3))

print('sqrt method') # akar kuadrat
x = 25
x = math.sqrt(x)
print(x)
print(math.sqrt(9))

print('pi constant') # pi 3.14
radius = 3
luas = math.pi * math.pow(radius,2)
print(luas)


# ========== casting ==========

x = 10

# integer to float, str
x = (float(x))
print(x, type(x))

x = (str(x))
print(x, type(x))

# x = (str(x))  # str tidak bisa int
# print(x, type(x))



# ========== STRING ========== 

# ========== len function & methods ==========
text = 'hallo apa kabar?'

panjangString = len(text)
print(panjangString)

indexApa = text.index('apa')
print(indexApa)

indexAPertama = text.index('a')
print(indexAPertama)

hasilSplit1 = text.split(' ')
print(hasilSplit1)

hasilSplit2 = text.split('a')
print(hasilSplit2)

versiHurufKecil = text.lower()
print(versiHurufKecil)

versiHurufBesar = text.upper()
print(versiHurufBesar)

hurufPertamaCapital = text.capitalize()
print(hurufPertamaCapital)



# ========== string slicing ==========
text = "i'm dimitri, nice to meet you"

print(text[1])
print(text[2:])
print(text[:4])
print(text[2:5])
print(text[:])
print(text[-1])
print(text[::-1]) # reverse text



# ========== string concatenation ==========
a = 'apel'
b = 'jeruk'

c = a + b
print(c)

d = a + ' ' + b + 'mangga'
print(d)

e = a + ' ' + str(5) #casting str to int
print(e)



# ========== string format ==========
umur = 23
nama = 'dimitri'
txt = 'nama saya {}, usia saya {}'.format(nama,umur)

print(txt)

apel = 3
jeruk = 5
pembelian = 'saya mau beli {xApel} apel  dan {xJeruk} jeruk'

print(pembelian.format(xApel = apel, xJeruk = jeruk))



# ========== string format ==========
txt = 'nama saya kuri'
a = 'aya' in txt
b = 'maya' in txt

print(a,type(a))
print(b, type(b))



# ========== user input ==========
inputanUser = input('masukan angka : ')
print(inputanUser,type(inputanUser))
