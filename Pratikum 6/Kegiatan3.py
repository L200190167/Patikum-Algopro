Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Hanyfah Rizqi Indra Nurfarida'
>>> NIM = 'L200190167'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Karena data "X" berubah menjadi type integer
>>> type(b)
<class 'int'>
>>> # Karena data "Nama" memiliki intruksi len
>>> a / b
40.241379310344826
>>> # Karena hasil dari 1167 dibagi 29 adalah 40.241379310344826
>>> a // b
40
>>> # Karena arti dari "//" adalah hasil bagi dibulatkan
>>> 10 * (a - 999)
1680
>>> # Karena nilai "a" dikurangi 999 adalah 168, kemudian dikalikan dengan 10 menghasilkan 1680
>>> b ** 2
841
>>> # Karena arti dari '**' adalah di pangkat 2
>>> a % b
7
>>> # Karena arti dari '%' adalah hasil sisa bagi
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # Karena '12.5' adalah bilangan desimal
>>> a / c
93.36
>>> # Karena hasil dari 1167 dibagi 12.5 adalah 93.36
>>> a // c
93.0
>>> # Karena arti dari '//' adalah hasil bagi di bulatkan
>>> a % c
4.5
>>> # Karena arti dari '%' adalah hasil sisa bagi
>>> c > b
False
>>> # Karena nilai c lebih besar dari b adalah salah
>>> type(c > b)
<class 'bool'>
>>> # Karena boolen mempunyai dua kemungkinan yaitu true dan false
>>> a > b and b > c
True
>>> # Karena nilai a lebih besar dari b adalah benar dan b lebih besar dari c adalah benar
>>> a > 1100 or b < 10
True
>>> # Karena nilai a lebih besar dari 1100 adalah benar dan b lebih kecil dari 10 adalah benar
