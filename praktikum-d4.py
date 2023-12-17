a = [2,3,1,0,3,1,1,2,7]
# akses item
print(a)
print(f'item indeks:0 {a[0]}')
print(f'item indeks:3 {a[3]}')
print(f'item indeks:terakhir {a[len(a)-1]}')
# akses item indeks negatif
print(f'item indeks:terakhir (-1) {a[-1]}')
print(f'item indeks:pertama  (-9) {a[-len(a)]}')
print(f'item indeks:1 (-8) {a[-8]}')
print(f'item indeks:5 (-4) {a[-4]}')
# akses indeks batas
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:1,2,... {a[1:]}')
print(f'item indeks:3,4,... {a[3:]}')
print(f'item indeks:0,1,2 {a[:3]}')
print(f'item indeks:0,1,2,3,4 {a[:5]}')
print(f'item indeks:semua {a[:]}')
# pengirisan indeks
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:2,3,4 {a[2:5]}')
print(f'item indeks:[1:8] {a[1:-1]}')

kelas = [('pemrograman',3),
         ('agama',3),
         ('sains',2)
         ]
print(f'data kelas {kelas}')
kelas.append(('cinta',3))
print(f'data kelas {kelas}')
kelas.append(('bahasa indonesia',3))
print(f'data kelas {kelas}')

#tugas
# nama mata kuliah 1: matkul1 dengan jumlah sks:3
# nama mata kuliah 2: matkul2 dengan jumlah sks:2
# nama mata kuliah 3: matkul3 dengan jumlah sks:2
# nama mata kuliah 4: matkul4 dengan jumlah sks:3
# nama mata kuliah 5: matkul5 dengan jumlah sks:3

#Nama Mata Kuliah 1: pemrograman dengan jumlah sks:3
print('Nama Mata Kuliah 1:',kelas [0][0],'dengan jumlah sks :',kelas [0][1])
#Nama Mata Kuliah 2: agama dengan jumlah sks:2
print('Nama Mata Kuliah 2:',kelas [1][0],'dengan jumlah sks :',kelas [1][1])
#Nama Mata Kuliah 3: sains dengan jumlah sks:2
print('Nama Mata Kuliah 3:',kelas [2][0],'dengan jumlah sks :',kelas [2][1])
#Nama Mata Kuliah 4: cinta dengan jumlah sks:3
print('Nama Mata Kuliah 4:',kelas [3][0],'dengan jumlah sks :',kelas [3][1])
#nama mata kuliah 5: bahasa indonesia dengan jumlah sks:3
print('Nama Mata Kuliah 5:',kelas [4][0],'dengan jumlah sks :',kelas [4][1])

data = [('Muhammad Fahrizard',2023,'Aktif'),
        (90,89,93,97,99),
        (20,22),
        ('S1-Reguler','Sistem Informasi D','Ganjil')]

#Nama Mahasiswa: Muhammad Fahrizard
print('Nama Mahasiswa :',data [0][0])
#Nim Mahasiswa: 231031127
print('NIM Mahasiswa :',a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8])
#Program pendidikan Muhammad Fahrizard: Sistem Informasi D S1-Reguler
print('Program Pendidikan',data [0][0],'adalah :',data [3][1],data[3][0])
#Angkatan : 2023-Ganjil
print('Angkatan :',data [0][1],'-',data[3][2])
#Jumlah nilai Muhammad Fahrizard adalah: 5
print('Jumlah nilai',data [0][0],'adalah :',len(data[1]))
#Data terkecil Muhammad Fahrizard adalah: 89
print('Data terkecil',data [0][0],'adalah :',min(data[1]))
#Data terbesar Muhammad Fahrizard adalah: 99
print('Data terbesar',data [0][0],'adalah :',max(data[1]))
#Rata-rata nilai Muhammad Fahrizard adalah: 92.25
rata = sum(data[1])/len(data[1])
print('Rata-rata nilai',data [0][0],'adalah :',rata)