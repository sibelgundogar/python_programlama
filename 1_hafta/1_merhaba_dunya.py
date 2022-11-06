#merhaba dünya
print("Hello World!")



#syntax
print("Hello")
print("World! (alt alta yazar)")

print("World")

if 1<2:
    print("if bloğunun içi")
print("if bloğunun dışı")

if(1<2):
        print("burası if bloğunun içi")
        print("burası da if bloğunun içi")



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



#tip dönüşümleri
a = 10
print(type(a))
a = float(10)
print(type(a))
a = str(10)
print(type(a))
class a:
    b = 10

t = a
print(type(a))
print(type(t))
print(t.b)
print(type(t.b))

