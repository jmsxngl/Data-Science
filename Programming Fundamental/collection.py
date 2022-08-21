# ========== LIST ==========

# ========== indexing ==========
listContoh = ['hello', 1,  1, 3, True]

print(listContoh[0])
print(listContoh[2])
print(listContoh[4])

print(listContoh[-1])
print(listContoh[-2])
print(listContoh[-5])

print(listContoh[-4:-1])
print(listContoh[1:4])
print(listContoh[-5:2])
print(listContoh[0:-2])
print(listContoh[2:])

print(listContoh[::-1])



# ========== change code ========== 
listContoh = ['hello', 1, 1, 3, True]

listContoh[1] = 'test'
listContoh[-2] = 'coba'
print(listContoh)



# ========== add data ========== 
listContoh = ['hello', 1, 1, 3, True]

listContoh.append('coba') # menambah di bagian terakhir
listContoh.insert(1, 'boleh') # mengubah sesuai index
print(listContoh)



# ========== delete data ==========
listContoh = ['hello', 'coba', 'coba', 3, True]

listContoh.remove('coba') # remove only first found data
listContoh.pop() # remove last item
del listContoh[1] # remove item at index 1
print(listContoh)

listContoh.clear() # remove all items
print(listContoh)



# ========== loop trough a list ========== 
listContoh = ['hello', 1, 1, 3, True]

for item in listContoh :
    print(item)



# ==========  check if an item exists in a list ========== 
listContoh = ['hello', 1, 1, 3, True]

if 'hello' in listContoh :
    print('ada string hello di listContoh')
else :
    print('hmmmmm :( 404 not found')



# ========== lenght of list ========== 
listContoh = ['hello', 'coba', 'coba', 3, True]
print(len(listContoh))



# ========== copy list ========== 
listContoh = ['hello', 'coba', 'coba', 3, True]

newList1 = listContoh
newList1[1] = 'test'

newList2 = listContoh.copy()
newList2[2] = 'baru'

print(listContoh)
print(newList1)
print(newList2)



# ========== list concatenanting ========== 
listContoh = ['hello', 'coba', 'coba', 3, True]
listBaru = [5, 'test', False]
listCoba = ['tarik', 8]

listGabungan = listBaru + listContoh
print(listGabungan)

listGabungan.extend(listBaru)
print(listGabungan)



# ========== find index ========== 
listContoh = ['eddie', 'baron', 'andi', 'charlie', 'samson']
indexYgDicari1 = listContoh.index('andi')

print(indexYgDicari1)

indexYgDicari2 = listContoh.index('kuri')
print(indexYgDicari2)



# ========== sorting ==========
listContoh = ['eddie', 'baron', 'andi', 'charlie', 'samson']
listContoh.sort() # default ascending
print(listContoh)

listAngka = [4, 3, 1, 5, 2]
listAngka.sort(reverse = True) # descending
print(listAngka,type(listAngka))



# ========== reverse ==========
listContoh = ['eddie', 'baron', 'andi', 'charlie', 'samson']
listContoh.reverse()
print(listContoh)



# ========== two dimension list  ==========
things = [
    ['red pen', 'blue pen'],
    ['analog clock', 'digital clock'],
    ['futsal shoes', 'badminton shoes']
]

print(things)
print(things[1])
print(things[2])
print(things[1][1])
print(things[2][0])
print(things[0][1])

contoh = [
    [
        ['hello', 'apa', 'kabar']
        [1, 2, 3]
    ],
    [
        [True, False, [1, [2, 3]]]
    ]
]

print(contoh)
print(contoh[0][1][1])
print(contoh[1][0][2][1][1])





# ========== TUPLE  ==========

# ========== edit tuple ==========
tupleContoh = ('hello', 1, 1, 3, True)

listContoh = list(tupleContoh)
del listContoh[2]
listContoh.append('test')

tupleContoh = tuple(listContoh)
print(tupleContoh)



# ========== loop trough a tuple ==========
for item in tupleContoh :
    print(item)



# ========== loop trough a tuple ==========
tupleContoh = ('hello', 1, 1, 3, True)

if 'hello' in tupleContoh :
    print('ada string hello di tupleContoh')
else :
    print('tidak ada string hello di tupleContoh')



# ========== length of tuple ==========
tupleContoh = ('hello', 1, 1, 3, True)

print(len(tupleContoh))



# ========== tuple only one item ==========
tuple1 = ('hello',)
print(tuple1, type(tuple1))

tuple2 = ('hello')
print(tuple2, type(tuple2))



# ========== tuple concatenating ==========
tuple1 = (1, 2, 3)
tuple2 = ('kiri', 'kanan', 'atas')

tupleGabungan = tuple1 + tuple2
print(tupleGabungan)



# ========== find index tuple ==========
tupleContoh = ['eddie', 'baron', 'andi', 'charlie', 'samson']
indexYgDicari1 = tupleContoh.index('andi')

print(indexYgDicari1)

indexYgDicari2 = tupleContoh.index('kuri')
print(indexYgDicari2)



# ========== tuple inside tuple ==========
things = (
    ('red pen', 'blue pen'),
    ('analog clock', 'digital clock'),
    ['futsal shoes', 'badminton shoes']
)

print(things)
print(things[1])
print(things[2])
print(things[1][1])
print(things[2][0])

things[2][0] = 'basketball shoes'

print(things)
print(things[2])
print(things[2][0])





# ========== DICTIONARY ==========

# cara 1
dictionaryContoh1 = {
    'nama' : 'budi', 
    'usia' : 25, 
    'pekerjaan' : 'developer'
}

print(dictionaryContoh1, type(dictionaryContoh1))

# cara 2
dictionaryContoh2 = dict(nama='andi', usia=27, pekerjaan='data scientist')
print(dictionaryContoh2, type(dictionaryContoh2))



# ========== access data ==========
dictionaryContoh = {
    'nama' : 'budi',
    'usia' : 25,
    'pekerjaan' : 'developer',
    'menikah' : False
}

print(dictionaryContoh['nama'])
print(dictionaryContoh['usia'])
print(dictionaryContoh.get('pekerjaan'))
print(dictionaryContoh.get('menikah'))



# ========== change data ==========
dictionaryContoh = {
    'nama' : 'budi',
    'usia' : 25,
    'pekerjaan' : 'developer',
    'menikah' : False
}

dictionaryContoh['usia'] = 27
print(dictionaryContoh)



# ========== add data ==========
dictionaryContoh = {
    'nama' : 'budi',
    'usia' : 25,
    'pekerjaan' : 'developer',
    'menikah' : False
}

dictionaryContoh['kelamin'] = 'pria'
print(dictionaryContoh)



# ========== delete data ==========
dictionaryContoh = {
    'nama' : 'budi',
    'usia' : 25,
    'pekerjaan' : 'developer',
    'menikah' : False,
    'kelamin' : 'pria'
}

del dictionaryContoh['kelamin'] # removes key-value pair for kelamin key
dictionaryContoh.pop('usia') # removes key-value pair for usia key
dictionaryContoh.popitem() # remove last inserted item

print(dictionaryContoh)

dictionaryContoh.clear() # empties the dictionary
print(dictionaryContoh)



# ========== loop trough a dictionary ==========

dictionaryContoh = {
    'nama' : 'budi',
    'usia' : 25,
    'pekerjaan' : 'developer',
    'menikah' : False
}

for key in dictionaryContoh :
    print("{} = {}".format(key, dictionaryContoh[key]))

hasil = dictionaryContoh.keys()
print(hasil, type(hasil))

for key in dictionaryContoh.keys() :
    print("{} = {}".format(key, dictionaryContoh[key]))

hasil = dictionaryContoh.values()
print(hasil, type(hasil))


for val in dictionaryContoh.values() :
    print(val)

hasil = dictionaryContoh.items()
print(hasil, type(hasil))

for key,val in dictionaryContoh.items() :
    print('{} = {}'.format(key,val))



# ========== check if a key exists in a dictionary ==========
dictionaryContoh = {
    'nama' : 'budi',
    'usia' : 25,
    'pekerjaan' : 'developer',
    'menikah' : False
}

check = 'kelamin' in dictionaryContoh
print(check)

if 'usia' in dictionaryContoh :
    print('ada key usia pada dictionaryContoh')
else :
    print('tidak ada key usia dalam dictionaryContoh')



# ========== length of dictionary ==========
print(len(dictionaryContoh))


# ========== copy a dictionary ==========
dictionaryContoh = {
    'nama' : 'budi',
    'usia' : 25,
    'pekerjaan' : 'developer',
    'menikah' : False
}

newDictionary1 = dictionaryContoh
newDictionary1['nama'] = 'andi'

newDictionary2 = dictionaryContoh.copy()
newDictionary2['pekerjaan'] = 'mekanik'

print(dictionaryContoh)
print(newDictionary1)
print(newDictionary2)



# ========== dictionary inside dictionary ==========

# contoh 1
things = {
    'food1' : {
        'name' : 'ramen',
        'price' : 25000
    },
    'food2' : {
        'name' : 'pizza',
        'price' : 20000
    },
    'food3' : {
        'name' : 'spaghetti',
        'price' : 20000
    }
}

print(things['food1'])
print(things['food2']['name'])


# contoh 2
contoh = {
    'anggota' : [
        {
            'nama' : 'andi',
            'usia' : 21,
            'hobby' : ('main air', 'berenang', 'main air')
        },
        {
            'nama' : 'budi',
            'usia' : 22,
            'hobby' : ('makan', 'minum', 'sebat')
        }
    ],
    'ketua' : {
        'nama' : 'sultan',
        'usia' : 27,
        'hobby' : ('mancing', 'berlayar')
    }
}

print(contoh['ketua']['nama'])
print(contoh['anggota'][1])
print(contoh['anggota'][0]['hobby'])
print(contoh['anggota'][1]['hobby'][2])





# ========== SET ==========

setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Iron Man 3', 20, False}
print(setContoh,type(setContoh))


# ========== create set from list, tuple and dictionary ==========
list1 = ['budi', 2, 2, 'ceci']
tuple1 = (False, 1, 'andi', False)
dictionary1 = {
    'nama' : 'coder',
    'usia' : 25,
    'pekerjaan' : 'coder',
    'menikah' : False
}

setList = set(list1)
setTuple = set(tuple1)
setDictionary = set(dictionary1)
setDictionaryValues = set(dictionary1.values())

print(setList)
print(setTuple)
print(setDictionary)
print(setDictionaryValues)


# ========== access data ==========
setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron'}

for item in setContoh :
    print(item)


# ========== check if an item exists in a set ==========
setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron'}

if 'iron man 3' in setContoh :
    print('ada film iron man 3 pada setContoh')
else :
    print('tidak ada film iron man 3 pada setContoh')


# ========== add data ==========
setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron'}

setContoh.add('Iron Man') # only add one data
print(setContoh)

setContoh.update('Iron Man 3', 'Hulk') # can add more than one data



# ========== set ==========
setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk', 'Wonder Woman'}

setContoh.remove('The Avengers') # menghapus (jika tidak ada datanya maka akan error)

setContoh.discard('Hulk') # menghapus (jika tidak ada datanya tidak akan error)
print(setContoh)

setContoh.pop() # menghapus satu random data
print(setContoh)

setContoh.clear()
print(setContoh)



# ========== join set ==========
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk', 'Wonder Woman'}
setMovie2 = {'Titanic', 'The Avengers'}

setGabungan = setMovie1.union(setMovie2)
print(setGabungan)



# ========== get difference between 2 sets ==========
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}
setMovie2 = {'Titanic', 'The Avengers', 'Hulk'}

setMovie3 = setMovie1.difference(setMovie2) # hanya mencari unique data pada setMovie1
print(setMovie3)

setMovie1.difference_update(setMovie2) # sama dengan difference tapi merubah data pada variable setMovie1
print(setMovie1)



# ========== get symmetric difference between sets ==========
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}
setMovie2 = {'Titanic', 'The Avengers', 'Hulk'}

setMovie3 = setMovie1.symmetric_difference(setMovie2) # mencari perbedaan data tanpa merubah setMovie1
print(setMovie3)

setMovie1.symmetric_difference_update(setMovie2) # mencari perbedaan data dan merubah setMovie1
print(setMovie1)



# ========== get intersection between 2 sets ==========
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}
setMovie2 = {'Titanic', 'The Avengers', 'Hulk'}

setMovie3 = setMovie1.intersection(setMovie2) # mengambil data yang sama tanpa merubah setMovie1
print(setMovie3)

setMovie1.intersection_update(setMovie2) # mengambil data yang dan merubah setMovie1
print(setMovie1)



# ========== check disjoint, subset and superset ==========
setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}
setMovie2 = {'The Avengers', 'Hulk'}

checkDisjoint = setMovie1.isdisjoint(setMovie2)
checkSubset = setMovie2.issubset(setMovie1)
checkSuperset = setMovie1.issuperset(setMovie2)

print(checkDisjoint)
print(checkSubset)
print(checkSuperset)
