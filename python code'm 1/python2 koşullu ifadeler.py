a=int(input())
b=int(input())
c=int(input())
if a>b and b>c:
    print("En Büyük Sayı:",a)
elif b>a and b>c:
    print("En Büyük Sayı:",b)
else :
    print("En Büyük Sayı:",c)

# iç içe koşullu ifadeler kullanarak da koşullu ifadeler oluşturulabilir.
# koordinat düzleminde bölge bulma örneği
x=int(input())
y=int(input())
if x>0:
    if y>0:
        print("I. Bölgedir.")
    else:
        print("IV. Bölgedir")
else:
    if y>0:
        print("II. Bölgedir.")
    else:
        print("II. Bölgedir.")


#TOPLAMLARI ÇİFT Mİ TEK Mİ? ÖRNEĞİ
n=int(input())
A=n//100
B=n//10%10
C=n%10
if (A+B+C)%2==0:
    print("ÇİFT")
else:
    print("TEK")

# SANTRAÇ TAHTASI ÖRNEĞİ
k=int(input())
l=int(input())
m=int(input())
n=int(input())


if (k+l)%2==(m+n)%2:
    print("AYNI")
else:
    print("FARKLI")

# ARTIK YIL ÖRNEĞİ
year=int(input())
if year%400==0 or(year%4==0 and year%100!=0):
    print("EVET")
else:
    print("HAYIR")

# ÜÇGEN Mİ? ÖRNEĞİ
X=int(input())
Y=int(input())
Z=int(input())
if X+Y>Z and X+Z>Y and Y+Z>X:
    print("evet")
else:
    print("hayır")

# ÇİKOLATA BÖLME ÖRNEĞİ
q=int(input())
w=int(input())
e=int(input())
if (e%q==0 or e%w==0) and (e<q*w):
    print("evet")
else:
    print("hayır")