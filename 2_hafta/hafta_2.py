#main
a = 5
b = 4
c = -5
if __name__ == "__main__":
    print(a)
print("------------------------------------")


#if
if a > b:
    print("a b den büyüktür")
if a < b:
    print("a b den küçüktür")
print("------------------------------------")


#elif
if a > 5:
    print("a 5 ten büyüktür")
elif a == 5:
    print("a 5 e eşittir")
elif a < 5:
    print("a 5 ten küçüktür")
print("------------------------------------")


#short if
a, d = 5, 5
print("a ile d farklı") if a != d else print("a ile d aynı")
print("a d den büyüktür") if a > d else print(" a d ye eşittir") if a == d else print("a d den küçüktür")
print("------------------------------------")


#and or
a, b, c = 5, 10, -4
if a < 10 or b < 10:
    print("a veya b 10 dan küçüktür")
if a == 5 and b == 10:
    print("a 5 e ve b 10 a eşit")
print("------------------------------------")


#is
a = 5
if a is 4:
    print("a 4 e eşit")
if a is not 4:
    print("a 4 e eşit değil")
print("------------------------------------")



#iç içe koşullu ifadeler
a, b = 1, 10
if a < 5:
    if b == 10:
        print("a 5 ten küçük ve b 10 a eşit")
print("------------------------------------")


#pass
a = 5
if a > 5:
    pass
print("pass")
print("------------------------------------")


#while
a = 5
while a < 15:
    a += 1
    if a == 10:
        continue
    if a == 12:
        break
    print(a)
else:
    print("a artık daha büyük")
print("------------------------------------")


#for
for i in range(0, 10):
    print(i)
print("---------")
for i in range(0, 10, 2):
    print(i)
print("---------")
for i in range(10, 0, -2):
        print(i)
print("------------------------------------")


liste = ["as", True, 1.9, 5, ["asdsa", "sdf", "asssert"]]
for i in liste:
    print(i)
for i in liste[4]:
    print(i)
print("------------------------------------")

for i in range(0, 3):
    print(i)
else:
    print("for bitti")
print("------------------------------------")


#enumerate
for i, eleman, in enumerate(liste):
    print(i+1 , ". eleman: ", eleman, sep="")
print("------------------------------------")



#fonksiyonlar
def yazdir():
    print("yazıom")
yazdir()

def topla(a,b):
    return a + b
print(topla(10, 21))


#2 değer geri döndürme
def topla_carp(a, b):
    return a + b, a * b
print(topla_carp(3, 5))

toplam, carpim = topla_carp(3, 7)
print(topla_carp(3, 7))
print(toplam)
print(carpim)


#birden çok parametre
def topla_git(*a):
    toplam=0
    for deger in a:
        toplam += deger
    return toplam
print(topla_git(1, 5, 3, 9, 5, 6))


#parametre olarak parametre gönderme
def topla(*toplanacak, fazladan = 0):
    toplam = 0
    for deger in toplanacak:
        toplam += deger + fazladan
    return toplam

print(topla(3, 5, 9, 15.2, 36, fazladan=2))


#key value oluşturma
def birim_islem(**birim):
    print("Birim tipi :", type(birim))
    print("Birim adı : " + birim["ad"])
    print("Birim tip : " + birim["tip"])
    print("Birim yıl : " + birim["yıl"])

birim_islem(ad = "balkes", tip = "67", yıl = "689")
print("------------------------------------")


#lambda
lambda_fonk = lambda a : a + 10
print(lambda_fonk(5))

#
lambdatopla = lambda a, b: a + b
def toplama(a, b): return a + b

print(lambdatopla(3, 5))
print(toplama(3, 5))
print(type(lambdatopla))
print(type(toplama))


#fav
def benim_fonksiyonum(n):
  return lambda a: a * n

katini_al = benim_fonksiyonum(2)
print(katini_al(5)) #a 5 olcak

katini_al = benim_fonksiyonum(5)
print(katini_al(5))


print("okeyy")