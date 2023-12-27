"while döngüsü --> belli koşula göre hareket edilir. döngüye girer."

sayi=1
while sayi<=15:
    print(sayi,"koşulu sağlıyor. OK.")
    sayi+=1

n=int(input())
top=0
i=0 ## değişken
while i<n:
    a=int(input())
    top= top+a
    i= i+1
print(top)

# basamak sayma örneği
a=int(input())
say=0
while a>0:
    a=a//10
    say=say+1
print(say)

# sayının rakamları toplama örneği
x=int(input())
toplam=0
while x>0:
    a=x%10
    toplam=toplam+a
    x=x//10
print(toplam)

# if elseli örneği
m=int(input())
topl=0
while m !=0:
    if m<0:
        break
    topl= topl+m
    m=int(input())
else:
    print(topl)

# yer değiştirme döngüsü
a=5
b=3
print(a,b)
t=a
a=b
b=t
print(a,b)

# n sayısına kadar olan sayıların karesini bulma örneği
n=int(input())
sy=1
while sy*sy<=n:
    print(sy*sy,end=" ")
    sy=sy+1

# sayının bütün bölenleri örneği
n=int(input())
d=2
while d*d <= n:
    if n % d==0:
        print(d)
        n=n//d
    else:
        d=d+1
if n>1:
    print(n)

# sporcu koşusu örneği
x=int(input())
y=int(input())
gun=1
while x<y:
    x=x+x*0.1
    gun= gun+1
print(gun)

#fibonacci sayısı örneği
n=int(input())
a=0
b=1
i=2
while i <=n:
    t=b
    b=a+b
    a=t
    i=i+1
if n==0:
    b=0
print(b)

# sayı tahmin oyunu
from random import randint
rastgele=randint(1,10)
print("0 ile programdan çıkabilirsiniz")
a=int(input())
sayı=1
while not (a==0 or a==rastgele):
    if a>rastgele:
        print("daha küçük sayı giriniz")
    else:
        print("daha büyük sayı giriniz")
    sayı=sayı+1
    a=int(input())
if a !=0:
    print(say,"defada buldunuz")