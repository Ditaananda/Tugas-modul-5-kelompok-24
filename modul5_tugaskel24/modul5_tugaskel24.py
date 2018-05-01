print ('-----------------------------------------------')
print ('  Program  Menghitung Pembelian       ')
print ('      ')
print ('      ')
print ('      Kelompok 24                    ')
print ('  1. Dita Ananda  / 21120117140009   ')
print ('  2. Gisza        / 21120117140012   ')
print ('-----------------------------------------------')
print ('\n')

from inputan import inputan
from fungsi import fungsi

pembeli = inputan()
pembeli.inputnama()
pembeli.hargabarang()
pembeli.jumlah()
pembeli.uang()


Fungsipembeli = fungsi()
Fungsipembeli.totalharga()
Fungsipembeli.kemb()

print('')
print('===========================================')
print('             CAKE STORE ')
print('===========================================')
print('Nama Barang              : ',pembeli.nama[0] )  
print('')
print('Harga Barang             : ','Rp.',pembeli.harga[0])
print('')
print('Jumlah Barang            : ', pembeli.jumlahbarang[0])
print('')
print('Total Harga              : ','Rp.',Fungsipembeli.total[0])
print('')
print('Uang Anda                : ','Rp.',Fungsipembeli.uangku[0])
print('')
print('Kembalian                : ','Rp.',Fungsipembeli.kembalian[0])
print('')

