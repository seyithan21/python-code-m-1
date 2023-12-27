isim="Seyithan"
for i in isim:
    print(i)
    print("merhaba")
    print("dünya")

for x in range(1,101,2):
    print(x)
    print("hoş geldin")

for x in range(1,6):
    print(x)

for x in range(10,1,-2):
    print(x)

n=int(input())
toplam=0
for i in range(1,n+1):
    toplam= toplam+i
print(toplam)

for i in "yeşil","kırmızı","sarı",0,"siyah","turuncu","mavi","mor":
    print(i)

for i in "yeşil","kırmızı","sarı",0,"siyah","turuncu","mavi","mor":
    if i =="siyah":
        break
    print(i)

for i in "yeşil","kırmızı","sarı",0,"siyah","turuncu","mavi","mor":
    if i =="siyah":
        continue
    print(i)

for i in "yeşil",1,"kırmızı",9,"sarı",0,"siyah",5,"turuncu","mavi","mor":
    if i in range(0,9):
        continue
    print(i)

isim="Seyithan"
for i in isim:
    print(i,end='*')

# FAKTÖRİYEL HESAPLAMA ÖRNEĞİ
f=int(input())
çarpma=1
for i in range(1,f+1):
    çarpma= çarpma*i
print(çarpma)

# ASAL SAYI OLMASI ÖRNEĞİ
A=int(input())
say=0
for i in range(2,A):
    if A % i==0:
        say =say+1
        break
if say== 0:
    print("evet")
else:
    print("hayır")

# MAX MİN SAYI BULMA ÖRNEĞİ
a=int(input())
mx=int(input())
mn=mx
for i in range(a-1):
    x=int(input())
    if x>mx:
        mx=x
    if x<mn:
        mn=x
print(mx,mn)

# SAYININ BÖLENLERİNİ BULMA ÖRNEĞİ
b=int(input())
for i in range(1,b+1):
    if b%i==0:
        print(i,end=" ")