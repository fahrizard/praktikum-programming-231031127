vd = {'key1' : 'Nilai 1', 
      'key2' : 'Nilai 2',
      'key3' : 'Nilai 3'
      }
      
Vl = ['Nilai1',
      'Nilai2',
      'Nilai3']

print(Vl[1])
print(vd['key2'])

print('\n')

data = {'nama' : 'MUHAMMAD FAHRIZARD', 
        'nim'  : '231031127',
        'lulus': False
        }
print(data)
# mengakses data
print(data['nama'])
print(data.get('Nama'))

#Mengupdate data
data.update({'lulus':True})
data['lulus'] = True # mengupdate
# data['Lulus'] = True # Tambah data

del data['nama'] # menghapus data

print(data)
print('\n')
biodata = { 'nama'  : 'MUHAMMAD FAHRIZARD',
'nim'   : '231031127',
'kelas' : 'S123D',
'agama' : 'islam',
'alamat': 'jln.buru no.115',
'kewarganegaraan' : 'WNI',
'email' : 'fahrizard61@gmail.com'
}

print(biodata['nama'],biodata['nim'],biodata['email'])
print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:4])
print(selected_biodata)




