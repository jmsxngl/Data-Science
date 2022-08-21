# ========== conditional statement ==========
# true and false = false
# true or false = true

# ========== if statement ==========

print('selamat datang!')

umur = int(input('masukan umur : '))

if (umur >= 17) :
    print('anda sudah boleh bikin sim')
    nama = input('masukan nama : ')
    if (len(nama) > 1) :
        print('terimakasih {}'.format(nama))
    else :
        print('nama harus diatas 1 huruf')
else :
    print('anda belum boleh bikin sim :(')

print('sampai jumpa!')



# ========== if elif else ==========
print('pengecheckan nilai')
nilai = int(input('masukan nilai : '))
grade = ' '

if(nilai >= 90 and nilai <= 100) :
    grade = 'A'
elif(nilai >= 80 and nilai  <= 89) :
    grade = 'B'
elif(nilai >= 70 and nilai  <= 79) :
    grade = 'C'
elif(nilai >= 60 and nilai  <= 69) :
    grade = 'D'
elif(nilai >= 0 and nilai <= 59) :
    grade = 'F'
else :
    grade = '?'
    print('nilai harus 0 - 100 saja')

print('Grade : {}'.format(grade))
