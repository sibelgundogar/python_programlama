a=5
while a<15:
    print(a)
    a+=1
    if a == 10:
        continue
    if a == 12:
         break
else:
    print("a artık daha büyük")

##
for i in range(0, 10):
    print(i)
for i in range(0, 10, 2):
    print(i)
    for i in range(10, 0, -2):
        print(i)

##
liste = ["as", True, 1.9, 5, ["asdsa", "sdf","asssert"]]
for i in liste:
    print(i)
for i in liste[4]:
    print(i)
for i in range(0, 3):
    print(i)
else:
    print("for bitti")

##
for i, eleman, in enumerate(liste):
    print(i+1 , ". eleman: ", eleman, sep="")

##
def yazdir():
    print("yazıom")

yazdir()

##

def topla(a,b):
    return a+b
print (topla(10,21))

##

## 2 değer geri döndürme
def topla_carp(a,b):
    return a+b , a*b
print(topla_carp(3,5))

toplam, carpim = topla_carp(3,7)
print(topla_carp(3,7))
print(toplam,carpim)


##
def topla_git(*a):
    toplam=0
    for deger in a:
        toplam += deger
    return toplam
print (topla_git(1,5,3,9,5,6))

##key value oluşturma
def birim_islem(**birim):
    print("Birim tipi :", type(birim))
    print("Birim adı : " + birim["ad"])
    print("Birim tip : " + birim["tip"])
    print("Birim yıl : " + birim["yıl"])

birim_islem(ad="balkes", tip="67",yıl="689")


##
lambda_fonk = lambda a:a+10
print(lambda_fonk(5))

##
topla =lambda a,b:a+b
print (topla(5,9))

def toplama (a,b):
    return a+b
print (topla(3,5))
print (toplama(3,7))
print (type(topla))
print (type(toplama))

##

def benim_fonksiyonum(n):
  return lambda a: a * n


katini_al = benim_fonksiyonum(2)
print(katini_al(5)) #a 5 olcak

katini_al = benim_fonksiyonum(5)
print(katini_al(5))




