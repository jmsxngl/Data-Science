print("========== while loop ==========")

i = 0
while (i < 5) :
    print('angka {}'.format(i))
    i += 1 # tanpa code ini akan terjadi infinite loop



print("========== range loop ==========")

print('contoh 1:')
data1 = range(5)
print(data1, type(data1))
listdata1 = list(data1)
print(listdata1, type(listdata1), '\n')

print('contoh 2:')
data2 = range(5,9)
print(data2, type(data2))
listdata2 = list(data2)
print(listdata2, type(listdata2), '\n')

print('contoh 3:')
data3 = range(7,3)
print(data3, type(data3))
listdata3 = list(data3)
print(listdata3, type(listdata3), '\n')

print('contoh 4:')
data4 = range(7,3,-1)
print(data4, type(data4))
listdata4 = list(data4)
print(listdata4, type(listdata4), '\n')

print('contoh 5:')
data5 = range(2,14,3)
print(data5, type(data5))
listdata5 = list(data5)
print(listdata5, type(listdata5),'\n')



print("\n ========== for loop ========== \n")

print('contoh 1')
for angka in range(5) :
    print(angka)

# print('contoh 2')
for angka in range(10,1,-3) :
    print(angka)

# print('contoh 3')
for char in 'Hello Guys!' :
    print(char)



print ("========== break / continue loop ==========")

# break 1
jmlPutaran = 0
while(True) :
    jmlPutaran += 1
    print('Putaran {}'.format(jmlPutaran))
    inputan = input('masukan yes untuk keluar : ')
    if (inputan == 'yes') :
        break


# break 2
text = 'halo apa kabar?'
hurufYangDicari = input('masukan huruf yang ingin dicari ({}) : '.format(text))
index = 0

for c in text :
    if(c == hurufYangDicari) :
        break

    index += 1

if(index == len(text)) :
    print('huruf {} tidak ditemukan'.format(hurufYangDicari))
else :
    print('huruf {} pertama ditemukan pada index ke {}'.format(hurufYangDicari, index))


# continue
text = 'halo apa kabar?'
hurufYgInginDilewati = input('masukan huruf yang ingin dilewati ({}) : '.format(text))

for c in text :
    if(c == hurufYgInginDilewati) :
        continue
    print(c)

# alternative 
for c in text :
  if(c != hurufYgInginDilewati) :
      print(c)



# print ("========== loop drawing ==========")

# horizontal
stars = ''
for i in range(5) :
    stars += '* '
print(stars)

# vertical
stars = ''
for i  in range(5) :
    stars += '*\n'
print(stars)

# persegi
stars = ''
size = 5
for i in range(size) :
    for j in range(size) :
        stars += '* '
    stars += '\n'
print(stars)

# segitiga siku-siku
stars = ''
size = 5
for i in range(size) :
    for j in range(1 + i) :
        stars += '* '
    stars += '\n'
print(stars)
