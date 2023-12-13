print('praktikum-d1')
print()
print('Nama Lengkap : MUHAMMAD FAHRIZARD')
print('NIM          : 231031127')
print('Prodi        : Sistem Informasi')

angkatan = 2023
print('angkatan adalah',angkatan)

print()
a = 20
print('data adalah =',a)
print('tipenya adalah =',type(a))

print()
b = 20.0
print('data adalah =',b)
print('tipenya adalah =',type(b))

print()
kampus = 'Institut Teknologi BJ Habibie'
print('data adalah =',kampus)
print('tipenya adalah =',type(kampus))

print()
log = True
print('data adalah =',log)
print('tipenya adalah =',type(log))

print()
c = complex(5,8)
print('data adalah =',c)
print('tipenya adalah =',type(c))

print()
p = 20
q = 5
hasil = p + q
print('hasi',p,'+',q,'adalah',hasil)

print()
p = 20
q = 5
hasil = p - q
print('hasi',p,'-',q,'adalah',hasil)

print()
p = 20
q = 5
hasil = p * q
print('hasi',p,'x',q,'adalah',hasil)

print()
p = 20
q = 5
hasil = p / q
print('hasi',p,'/',q,'adalah',hasil)

print()
p = 3
q = 2
hasil = p ** q
print('hasi',p,'^',q,'adalah',hasil)

print()
p = 37
q = 31
hasil = p % q
print('hasi',p,'%',q,'adalah',hasil)

print()
p = 37
q = 31
hasil = p // q
print('hasi',p,'//',q,'adalah',hasil)

print()
p = 30
q = 31
hasil = p // q
print('hasi',p,'//',q,'adalah',hasil)

print()
p = 20
q = 3
hasil = p / q
print('hasi',p,'/',q,'adalah',hasil)

print()
a = 20
print('nilai a adalah', a)
a = a + 1
print('nilai a menjadi', a)

print()
a = 20
print('nilai a adalah', a)
a = a + 1 #ini perintah a = a + 1
print('nilai a+=1 menjadi', a)

print()
a = 25
print('nilai a adalah', a)
a -= 2 #ini perintah a = a + 1
print('nilai a-=2 menjadi', a)

print()
a = 20
print('nilai a adalah', a)
a *= 2 #ini perintah a = a * 2
print('nilai a*=2 menjadi', a)

print()
a = 20
print('nilai a adalah', a)
a /= 5 #ini perintah a = a / 5
print('nilai a/=5 menjadi', a)

print()
a = 20
print('nilai a adalah', a)
a **= 2 #ini perintah a = a ** 2
print('nilai a**=2 menjadi', a)

print()
a = 20
print('nilai a adalah', a)
a %= 7 #ini perintah a = a % 7
print('nilai a%=7 menjadi', a)

print()
a = 20
print('nilai a adalah', a)
a //= 7 #ini perintah a = a // 7
print('nilai a%=7 menjadi', a)

print() #ini operasi or
log = True 
print('nilai log adalah',log)
log |= False #ini perintah log= False log
print('nilai log|=False menjadi',log)

print() #ini operasi AND
log = True 
print('nilai log adalah',log)
log &= False #ini perintah log= log & False 
print('nilai log|=False menjadi',log)

print() #ini operasi AND
log = True 
print('nilai log adalah',log)
log &= True #ini perintah log= log & False 
print('nilai log|=True menjadi',log)

print() #ini operasi XOR
log = True 
print('nilai log adalah',log)
log ^= False #ini perintah log= log ^ False 
print('nilai log^=False menjadi',log)

print() #ini operasi XOR
log = True 
print('nilai log adalah',log)
log ^= True #ini perintah log= log ^ False 
print('nilai log^=True menjadi',log)

print() # ini operasi shifting
bi = 0b0100
print('nilai bi =',format(bi,'04b'))
bi >>=1 #menggeser dikit ke kanan 1 kali
print('nilai bi >>=1 menjadi',format(bi,'04b'))

print() # ini operasi shifting
bi = 0b0100
print('nilai bi =',format(bi,'04b'))
bi <<=1 #menggeser dikit ke kanan 1 kali
print('nilai bi <<=1 menjadi',format(bi,'04b'))

print()
a = 20
hasil = a>15
print('hasil',a,'>15 adalah', hasil)

print()
a = 20
hasil = a==15
print('hasil',a,'==15 adalah', hasil)

print()
print('contoh koooperator komperasi')
a=3
b=4
c=2
d=6
print('Diketahui Bilangan\n a =',a,'\n b =',b,'\n c =',c,'\n d =',d)
print()

hasil=a<b
print('Perbadingan antara a<b adalah',hasil)

hasil=a>b
print('Perbadingan antara a>b adalah',hasil)

hasil=a<b>c
print('Perbadingan antara a<b>c adalah',hasil)

hasil=a>b<c
print('Perbadingan antara a<b>c adalah',hasil)

hasil=a>b<c
print('Perbadingan antara a<b>c adalah',hasil)

hasil=a>b<c
print('Perbadingan antara a<b>c adalah',hasil)

print()
a='apakah'
b='dia'
c='punya'
d='saya'
hasil=a is 'dia'

print('a adalah "aku"',hasil)

print('a tidak "aku"', a is not "aku" )

print(a,b,c,d,'ternyata', a is c)