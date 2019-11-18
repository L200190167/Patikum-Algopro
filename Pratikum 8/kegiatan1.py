Data = {"NIM":"L200190167", "Nama":"Hanyfah Rizqi Indra Nurfarida","Tempat/Tanggal lahir":"Magetan / 07 Agustus 1999", "jenis kelamin":"Perempuan", "Agama":"Islam", "Pekerjaan":"Mahasiswa", "Alamat":"Maospati,Magetan"}
def TampilNIM():
    print(Data["NIM"])
def TampilNama():
    print(Data["Nama"])
def TampilTTL():
    print(Data["Tempat/Tanggal lahir"])
def TampilJK():
    print(Data["jenis kelamin"])
def TampilAgama():
    print(Data["Agama"])
def TampilAlamat():
    print(Data["Alamat"])
def TampilPekerjaan():
    print(Data["Pekarjaan"])

print("Pilihan Yang Tersedia:")
print("a menampilakan bantuaan ini")
print("b menampilakan NIM")
print("c menampilakan Nama")
print("d menampilakan Tempat/Tanggal lahir")
print("e menampilakan jenis kelamin")
print("f menampilakan Agama")
print("g menampilakan Alamat")
print("h menampilakan Pekarjaan")
print("i untuk keluar")
print(" ")

a = """Pilihan Yang Tersededia:
a menampilakan bantuaan ini
b menampilakan NIM
c menampilakan Nama
d menampilakan Tempat/Tanggal lahir
e menampilakan jenis kelamin
f menampilakan Agama
g menampilakan Alamat
h menampilakan Pekarjaan
i untuk keluar"""

print(a)
i = "Terima Kasih"
x = input("Masukkan huruf:")
while x != "i":
    if x == "a":
        print(a)
        print(" ")
        x = input("Masukkan huruf:")
    elif x == "b":
        TampilNIM()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "c":
        TampilNama()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "d":
        TampilTTL()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "e":
        TampilJK()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "f":
        TampilAgama()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "g":
        TampilAlamat()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "h":
        TampilPekerjaan()
        print(" ")
        x = input("Masukkan huruf")
print(i)
