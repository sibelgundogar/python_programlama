#klavyeden girilen 5 tane sayının karesinin 20 eksiğini alarak küçükten büyüğe sıralayan ve listeye atan kodlar
"""""
a=0
liste = []
while a<5:
    sayı = int(input("bir sayı giriniz."))
    a+=1
    liste.append(sayı)

def siralama(sayı):
    return sayı*sayı-20

liste.sort(key=siralama)
print(liste)


if __name__ == "__main__": #program burdan başlar
"""

a=5
b=8
c=4
d=-5

if a> c :
    print("a c den küçüktür")
if d<0: print("d 0 dan küçüktür")
if d>0: print("böyle yan yana da yazabilirsin");print("ama o zaman noktalı virgül kullan"); d=5

if a > 5:
    print ("a 5 ten büyük")
elif a == 5:
    print("a 5e eşittir")
else :
    print("else")

a = 5
b = 4
print("a ile b farklı") if a != b else print("a ile b aynı")

















