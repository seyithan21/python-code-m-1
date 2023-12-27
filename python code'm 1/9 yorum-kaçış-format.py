# Yorum Satırları
# \n kaçışlar (alt satır için kullanılır.)
# format metodu

"# (yorum satırı)"
sayi=int(input("birinci sayıyı giriniz: "))  #buraya ne yazılırsa yazılsın çalışına görünmez.
print(sayi)

"\n kaçışlar"
print("birinci satır\nikinci satır\nüçüncü satır")

"Format metodu"
isim=input("isminizi giriniz: ")
soyad=input("soyadınızı giriniz: ")
print("hoş geldiniz {1} {0}".format(soyad,isim))
yas=input("yaşınızı giriniz: ")
print("merhaba hoş geldiniz {2} {0} {1}".format(soyad,yas,isim))
print("merhaba hoş geldiniz isminiz: {isim} soyadınız: {soyad} yaşınız: {yas}".format(soyad=input("soyadınızı giriniz: "),yas=input("yaşınızı giriniz: "),isim=input("isminizi giriniz: ")))

print("merhaba sayfama |{}| hoş geldiniz".format("mr.hemsire"))
print("merhaba sayfama |{:<21}| hoş geldiniz".format("mr.hemsire"))
print("merhaba sayfama |{:>21}| hoş geldiniz".format("mr.hemsire"))
print("merhaba sayfama |{:21}| hoş geldiniz".format("mr.hemsire"))