#kendisine gönderilen sayılardan sadece palindrom olanları toplayan
#diğerlerini de bu toplamdan çıkaran ve geri döndüren python fonksiyon
def polindram(*dram):
    toplam = 0
    for sayi in dram:
        if str(sayi) == str(sayi)[::-1]:
            toplam += sayi
        else:
            toplam -= sayi
    return toplam

print(polindram(10, 101, 55, 40, 9009))
print("------------------------------------")



#class
class sinif:
    pass
nesne = sinif()
print(type(nesne))

class sinif_2:
    a = 8
    b = "qwer"
    c = [1, 2, 3]
nesne_2 = sinif_2()
print(nesne_2.a)
nesne_2.b = "asdf"
print(nesne_2.b)
print("------------------------------------")



#class içinde fonksiyon
class sinif_3:
    a = 8
    b = "qwer"
    c = [1, 2, 3]
    def yazdir(self):
        d = 10
        print(d, self.a)
    def yazdir_2(self, t):
        self.yazdir()
        print(t)

nesne_3 = sinif_3()
nesne_3.yazdir()
nesne_3.yazdir_2("qwerty")


#init del
class sinif_4:
    metin = ""
    def __init__(self, a):
        self.metin = a
    def __del__(self):
        print("silinecek")

nesne_4 = sinif_4("Metin")
print(nesne_4.metin)
del nesne_4


#str
class sinif_5:
    metin = ""
    def __init__(self, a):
        self.metin = a

    def __str__(self):
        return "yazdırılan : " + self.metin

nesne_5 = sinif_5("str")
print(nesne_5)
print("------------------------------------")



#import
"""import bizim_modul
from bizim_modul import topla
import bizim_modul as bm

print(bizim_modul.topla(5, 10))
print(bizim_modul.e)
print(topla(2, 3))
print(bm.q)"""
print("------------------------------------")



#try except
a = "qwert"
try:
    y = 5 + a
except:
    print("int bir ifadeyle string toplanamaz")
print("------------------------------------")


#import
from termcolor2 import c
print(c("Hellooo").red.on_white.blink.underline.dark)
print("------------------------------------")



#metin.txt dosyasını okuma
dosya = open("metin.txt", 'r')
for satir in dosya:
    print(satir[:-1])


#metin2.txt dosyasına yazdırma
dosya = open("metin2.txt" , 'w')
print("dosyaya yazdirma", file=dosya)
dosya.close()


#kendisi kod.txt dosyasını oluşturur ve içine yazar
dosya = open("kod.txt", 'w')
print("print('efsane python')", file=dosya)
dosya.close()

dosya = open("kod.txt", 'r')
satir = dosya.readline()
eval(satir)


print("okeyy")
