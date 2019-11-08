## Program Akun
## Dibuat oleh Hanyfah L200190167
import random
angka = random.randint(0,1000)

Nama = 'Hanyfah Rizqi Indra Nurfarida'
TanggalLahir = '7 Agustus 1999'
NamaSingkat = Nama[0] + '.' + Nama[8] + '.' + Nama[14] + '.' + Nama[20:30]
Username = Nama[0] + TanggalLahir[0] + TanggalLahir[11:15]
Password = Nama[0:7] + str(angka)

print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Username)
print(Password)
