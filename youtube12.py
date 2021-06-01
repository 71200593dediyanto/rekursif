# Dedi Yanto
# 71200593
# Universitas Kristen Duta Wacana
# Prodi Teknik Informatika
# Fungsi Rekursif

'''
joko ingin sekali membuat program untuk mengkonversi bilangan desimal 
menjadi bilangan binner, namun karena joko tidak pandai untuk membuat program
bantulah joko untuk membuat program yang dapat mengkonversi bilangan desimal 
menjadi bilangan binner, dengan membuat fungsi rekursif

'''

'''
Input:
bilangan desimal = 6

Proses:

6%2 > 0
6/2 > 3
3%2 > 1
3/2 > 1
1%2 > 1
1/2 > 0

011

110
Output:

110


'''

#source code

def binaryconvert(value,a=[]):
    if value == 0:
        a.reverse()
        return ''.join(a)
    biner = value%2
    a.append(str(biner))
    return binaryconvert(value//2)


desimal = int(input('Masukkan angka : '))

print('hasil konversi',desimal,'ke binary adalah',binaryconvert(desimal))