#merhaba dünya
print("Hello World!")
print("----------------------------------------")


#syntax
print("Hello")
print("World! (alt alta yazar)")

print("World")

if 1 < 2:
    print("if bloğunun içi")
print("if bloğunun dışı")

if(1 < 2):
        print("burası if bloğunun içi")
        print("burası da if bloğunun içi")
print("----------------------------------------")


#degiskenler
a = 3
b = "string"
c = 3.5
d = -5
e = None
f = True
print(a, b, c, d, e, f)
print(a, b, c, d, e, f, sep=", ")
print(a, b, end="")
print("aynı satırda", "yazar")
print(a); print(b); print("farklı satırlarda yazar ; varsa o satırı bitirir")
a, c = 1, 3.7
print(a, c)
g = "çift tırnak"
h = 'tek tırnak'
i = 'i'
print(g, h, i)
print("----------------------------------------")


#degisken tipleri
print("a :", type(a))
print("b :", type(b))
print("c :", type(c))
print("d :", type(d))
print("e :", type(e))
print("f :", type(f))
print("i :", type(i))

j = [1, 2]
k = {a:"wer", d:"df"}
l = (1, 2, 3)

print("j :", type(j))
print("k :", type(k))
print("l :", type(l))
print("----------------------------------------")


#açıklama satırları
#tek satırlık açıklama

"""
satırlarca
açıklama
satırı
"""

'''
tek tırnak 
da olur
'''

m = '''açıklama
satırı bile
olsa yazar
'''
print(m)
print("----------------------------------------")


#tip dönüşümleri
a = 10
print(type(a))
a = float(10)
print(type(a))
a = str(10)
print(type(a))
class a:
    b = 10

c = a
print(type(a))
print(type(c))
print(c.b)
print(type(c.b))
print("----------------------------------------")


#küçük büyük harf farkı
a = 5
A = 10
print(a, "ve", A, "farklı")
print("----------------------------------------")


#evrensel değişkenler - global (fonksiyonun dışından da o değeri korur)
a = 5
def b():
    a = 10
    print(a)
b()
print(a)
def c():
    global a
    a = 10
    print(a)
c()
print(a)
print("----------------------------------------")


#büyük sayılar
a = 94614895614856154896548958795478956451485614789561456146
b = 98789656212314586489652486248548956489564625461458621456
c = a*b
print(c)
print("----------------------------------------")


#rastgele sayılar
from random import randrange
rnd = randrange(1, 20)
print(rnd)
print("----------------------------------------")


#metinler
a = "metin"
b = """açıklama
satırı
arasındaki metin
olduğu gibi yazılır"""
print(a, b)
print(a[0])
print(a[1])
print(b[4])
print(b[5])

print("a nın uzuluğu :", len(a))
print("b nin uzuluğu :", len(b))
print("----------------------------------------")


#metin karşılaştırma
a = "BaliKESir"

if a == "BaliKESir":
    print("a BaliKESir e eşit")

if "kes" in a:
    print("a da kes var")

if "KES" in a:
    print("a da KES var")

if "eks" in a:
    print("a da eks var")
print("----------------------------------------")



#metni biçimli yazdırma
a = 5
b = 10
c = 15
print("a = {} - b = {} - c = {}".format(a, b, c))

print("Tamamını Küçük Harflerle yazar".capitalize())
print("Tamamını büyük harflerle yazar".upper())
print("----------------------------------------")


#escape char
a = 'Tek tırnak içinde metin yazar\'ken kesme işareti kullanmak gerekirse'
print(a)
a = 'Tek tırnak içinde metin yazarken \\ slaş kullanmak gerekirse'
print(a)
print("----------------------------------------")


#boolean
print(1 > 2)
a = 1 < 2
print(a)
print("----------------------------------------")


#operatörler
print(3 + 5)
print(3 - 5)
print(3 * 5)
print(3 / 5)
print(9 % 2)
print(9 // 2)
print(2 ** 4)
print("----------------------------------------")


#listeler
a = [1, 2, 3]
b = [True, 0.5, 8423, None, [1, "liste elemanı", 3.5]]
print(a)
print(b)
print(b[0])
print(b[4][1])
c = "birinci elemanından dördüncü elemana kadar olan kısmını alacak"
print(c[1:4])
b[4][2] = [6, 99, 6.5, "liste içinde liste"]
print(b[4][2])
print(b[4][2][3])
print(b)
print("----------------------------------------")



#listeye append:eleman ekleme, pop:en sondakini çıkarma, remove: o sayıyı çıkarma, insert:girilen indexe o sayıyı ekleme, clear:boşaltma
d = [1, 3]
d.append(5)
print(d)

d.pop()
print(d)

d.append(9)
d.remove(1)
print(d)

d.insert(1, 100)
print(d)

print(d.pop())
print(d)

d.clear()
print(d)
print("----------------------------------------")


#listeyi sıralama, tersten yazdırma
liste = ["Elma", "Armut", "Ayva"]

liste.sort()
print(liste)

liste.reverse()
print(liste)

def fonksiyon(n):
  return abs(n - 50)

sayi_listesi = [100, 50, 65, 82, 23]
sayi_listesi.sort(key=fonksiyon)
print(sayi_listesi)
print("----------------------------------------")




sayi_list = [3, 5, 10, -8, 9, 15]
a = sayi_list
print(a)

sayi_list.sort()
print(a)

sayi_list = [3, 5, 10, -8, 9, 15]
a = sayi_list.copy()
print(a)

sayi_list.sort()
print(a)
print("----------------------------------------")


#tuples
degisitirilemez = ("armut", "hurma", "cilek")
print(degisitirilemez)
print(degisitirilemez[0])
print("----------------------------------------")



#dictionary
sozluk = {
  "marka": "Ford",
  "model": "Mustang",
  "yil": 1964
}

print(sozluk)
print(sozluk["marka"])
print(sozluk["model"])
print(sozluk["yil"])

sozluk["renk"] = "siyah"
print(sozluk)
print(sozluk["renk"])
sozluk["renk"] = "beyaz"
print(sozluk)

print(sozluk.keys())
print(sozluk.values())

for i in sozluk.keys():
    print(i, ":", sozluk[i])
print("----------------------------------------")
print("okey")
