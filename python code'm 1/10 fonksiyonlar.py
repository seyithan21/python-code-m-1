def topla():
    sonuc=5+9
    print(sonuc)
topla()


def topla(birincisayı,ikincisayı):
    sonuc=birincisayı+ikincisayı
    print(sonuc)
x=int(input("birincis sayıyı giriniz: "))
y=int(input("ikinci sayıyı giriniz: "))
topla(x,y)


def topla(birincisayı,ikincisayı):
    sonuc=birincisayı+ikincisayı
    return sonuc
x=int(input("birincis sayıyı giriniz: "))
y=int(input("ikinci sayıyı giriniz: "))
topla(x,y)


def ucgenmi(x,y,hipotenüs):
    if x**2+y**2==hipotenüs**2:
        return "bu bir dik üçgendir!!!"
    else :
        return "bu bir dik üçgen değildir!!!"
    
print(ucgenmi(3,4,5))
print(ucgenmi(5,12,13))
print(ucgenmi(5,8,10))