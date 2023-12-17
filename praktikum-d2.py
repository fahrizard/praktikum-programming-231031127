print('praktikum-2\n\n')
('==print========Ini and==========')

a = True
b = False
print('\n==========Ini and==========')
hasil = a and a
print('Nilai',a,'and',a,'adalah',hasil)
hasil = a and b
print('Nilai',a,'and',b,'adalah',hasil)
hasil = b and b
print('Nilai',b,'and',a,'adalah',hasil)
hasil = b and a
print('Nilai',b,'and',b,'adalah',hasil)

print('\n==========Ini or==========')
hasil = a or a
print('Nilai',a,'or',a,'adalah',hasil)
hasil = a or b
print('Nilai',a,'or',b,'adalah',hasil)
hasil = b or a
print('Nilai',b,'or',a,'adalah',hasil)
hasil = b or b
print('Nilai',b,'or',b,'adalah',hasil)

print('\n==========Ini not==========')
hasil = not a
print('Hasil not',a,'adalah',hasil)
hasil = not b
print('hasil not',b,'adalah',hasil)

print('\n==========Ini xor==========')
hasil = a^a
print('Nilai',a,'xor',a,'adalah',hasil)
hasil = a^b
print('Nilai',a,'xor',b,'adalah',hasil)
hasil = b^a
print('Nilai',b,'xor',a,'adalah',hasil)
hasil = b^b
print('Nilai',b,'xor',b,'adalah',hasil)

print('\n==========Ini nand==========')
hasil = not (a and a)
print('Nilai',a,'nand',a,'adalah',hasil)
hasil = not (a and b)
print('Nilai',a,'nand',b,'adalah',hasil)
hasil = not (b and b)
print('Nilai',b,'nand',a,'adalah',hasil)
hasil = not (b and a)
print('Nilai',b,'nand',b,'adalah',hasil)

print('\n==========Ini nor==========')
hasil = not (a or a)
print('Nilai',a,'nor',a,'adalah',hasil)
hasil = not (a or b)
print('Nilai',a,'nor',b,'adalah',hasil)
hasil = not (b or a)
print('Nilai',b,'nor',a,'adalah',hasil)
hasil = not (b or b)
print('Nilai',b,'nor',b,'adalah',hasil)

print('\n==========Ini nxor==========')
hasil = a^a
print('Nilai',a,'nxor',a,'adalah',not hasil)
hasil = a^b
print('Nilai',a,'nxor',b,'adalah',not hasil)
hasil = b^a
print('Nilai',b,'nxor',a,'adalah',not hasil)
hasil = b^b
print('Nilai',b,'nxor',b,'adalah',not hasil)

print('========== IS')
a = 5
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)
a = 6
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)

print('\n========== IS')
a = 5
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)
a = 6
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)

print('\n========== In')
nama = 'Bacharuddin Jusuf Habibie'
test = 'rud'
cek  =  test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'bach'
cek  =  test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'ib'
cek  =  test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek  =  test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek  =  test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek  =  test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek  =  test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek  =  test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

print('\n========== not In')
#tugas nama not in
nama = 'Muhammad Fahrizard'
test = 'mad'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'muha'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'iz'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek  =  test not in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

print('\n========== In')
data = ['Institut',
        'Teknologi',
        'Bacharuddin',
        'Jususf',
        'Habibie']
print('Data adalah',data)
test1 = 'Habibie'
test2 = 'Parepare'
test3 = 'Kampus'
test4 = 'Institut'

cek = test1 in data
print(test1,'terdapat di data adalah '+str(cek))
cek = test2 in data
print(test2,'terdapat di data adalah '+str(cek))
cek = test3 in data
print(test3,'terdapat di data adalah '+str(cek))
cek = test4 in data
print(test4,'terdapat di data adalah '+str(cek))

print('\n========== not In')
#Tugas dengan cara yang sama buat operator untuk not in
data=['Institut',
      'Teknologi',
      'Bacharuddin',
      'Jusuf',
      'Habibie']
print()
print('Data adalah',data)
test1='Habibie'
test2='Parepare'
test3='Kampus'
test4='Institut'
print()
cek=test1 not in data
print(test1,'Terdapat di data adalah',cek)
cek=test2 not in data
print(test2,'Terdapat di data adalah',cek)
cek=test3 not in data
print(test3,'Terdapat di data adalah',cek)
cek=test4 not in data
print(test4,'Terdapat di data adalah',cek)

#INI OPERATOR BITWISE
print('\n========== not In')
a = 1  #isi dengan tanggal lahir
b = 5  #isi dengan bulan lahir
b+= 80
print('\n========== and')
print('Nilai',a,'dalam biner       = ',format(a,'08b'))
print('Nilai',b,'dalam biner      = ',format(b,'08b'))
print('-----------------------------------------AND')
c = a & b
print('Nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))
a = 1  #isi dengan tanggal lahir
b = 5  #isi dengan bulan lahir
b-= 80
print('\n========== and')
print('Nilai',a,'dalam biner       = ',format(a,'08b'))
print('Nilai',b,'dalam biner      = ',format(b,'08b'))
print('-----------------------------------------AND')
c = a & b
print('Nilai',a,'&',b,'dalam biner adalah',format(c,'08b'))

# Tugas Untuk Operator XOR c= a^n
print('=========================XOR')
print('Nilai',a,'Dalam biner           =',format(a,'08b'))
print('Nilai',b,'Dalam biner           =',format(b,'08b'))
print('-----------------------------------------------------XOR')
c= a ^ b
print('Nilai',a,'&',b,'Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator NOT c= ~a
print('=========================NOT a')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('-----------------------------------------------------NOT a')
c= ~a
print('Nilai','~','\b',a,'Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator NOT c= ~b
print('=========================NOT a')
print('Nilai',b,'Dalam biner         =',format(b,'08b'))
print('-----------------------------------------------------NOT a')
c= ~b
print('Nilai','~','\b',b,'Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator Geser Kanan, c= a>>2
print('=========================>>')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('----------------------------------------------------->>')
c= a>>2
print('Nilai',a,'>>','Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator Geser kiri , c= a<<2
print('=========================<<')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('-----------------------------------------------------<<')
c= a<<2
print('Nilai',a,'>>','Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator NOT and, c= ~(a&b)
print('=========================not and')
print('Nilai',a,'Dalam biner                 =',format(a,'08b'))
print('Nilai',b,'Dalam biner                 =',format(b,'08b'))
print('-----------------------------------------------------not and')
c=~(a&b)
print('Nilai','~(',a,'&',b,')','Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator NOT or, c= ~(a|b)
print('=========================not OR')
print('Nilai',a,'Dalam biner                 =',format(a,'08b'))
print('Nilai',b,'Dalam biner                 =',format(b,'08b'))
print('-----------------------------------------------------OR')
c= ~(a|b)
print('Nilai','~(',a,'|',b,')','Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator not xor, c = ~(a^b)
print('=========================not XOR')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('Nilai',b,'Dalam biner                =',format(b,'08b'))
print('-----------------------------------------------------not XOR')
c= ~(a ^ b)
print('Nilai ~(',a,'^',b,')Dalam Biner Adalah',format(c,'08b'))

# Tugas untuk Operasi not geser kanan, c = ~(a >> 2)
print('=========================not Geser kanan')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('-----------------------------------------------------not geser kanan')
c= ~(a >> 2)
print('Nilai ~(',a,'>> 2)','Dalam Biner Adalah',format(c,'08b'))

# Tugas untuk Operasi not geser Kiri, c = ~(a << 2)
print('=========================not Geser kanan')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('-----------------------------------------------------not geser kiri')
c= ~(a << 2)
print('Nilai ~(',a,'<< 2)','Dalam Biner Adalah',format(c,'08b'))

































