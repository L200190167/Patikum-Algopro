Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Hanyfah Rizqi Indra Nurfarida'
>>> NIM = 167
>>> Tinggi = 1.55
>>> Berat = 59
>>> TahunLahir = 1999
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(aku)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(aku)
NameError: name 'aku' is not defined
>>> type(Aku)
<class 'tuple'>
>>> # Karena tipe data koleksi tuple tidak bisa di ganti
>>> Aku[0]
1999
>>> # Karena objek ke 1 adalah tahun lahir
>>> a = NIM % 4; Aku[a]
167
>>> # Karena objek aku ke 3 adalah NIM
>>> type(Aku[a])
<class 'int'>
>>> # Karena objek ke 3 adalah NIM dan NIM adalah integer
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # Karena tipe data Tuple tidak bisa di ubah
>>> type(Data)
<class 'list'>
>>> # Karena tipe data koleksi berupa list bisa bertambah , berkurang,berubah.
>>> type(Data[4])
<class 'str'>
>>> # Karena objek data ke 4 adalah Nama yang berupa string
>>> Data[4][5]
'a'
>>> # Krena indeks 4 dan indeks 5 dari data di peroses dan menghasilkan a
>>> Data[4][a:6]
'yfa'
>>> # Karena objek data ke 4 adalah Nama dan objek nama ke 6 adalah yfa
>>> Data[0] = 'ok'; Data
['ok', 59, 1.55, 167, 'Hanyfah Rizqi Indra Nurfarida']
>>> # Karena tipe data koleksi berupa list dapat berubah,bekurang,berambah
>>> Data[-a]
1.55
>>> # Karena data -3 adalah data ke 3 dari kanan yaitu  1.55
>>> range(a)
range(0, 3)
>>> # Karena a adalah 3 jadi range a menghasilkan data 0 sampai 3
