"""
== --> Eşitse
!= --> Eşit Değilse
<  --> Küçükse
>  --> Büyükse
<= --> Küçük Eşitse
>= --> Büyük Eşitse
"""

sayi=input("Bir Sayı Giriniz: ")
sayi=int(sayi)

if sayi>60 :
    print("Başarılı Geçer.")
elif sayi<60 :
    print("Başarısız Kalır.")
elif sayi==60 :
    print("Koşullu Geçer.")
else :
    print("Yanlış Girilen Bir Değer.")