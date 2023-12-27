# range(1,12,2) sayı dizisi list(range(10))
# sort küçükten büyüğe sıralama
# reverse listeyi tersine çevirme(sortun tersi) 
# listeyi kopyalamal copy()
# append ("dönem") listeye eleman eklemek
# insert(1,"sınav")listenin istediğiniz konumuna eleman eklemek için
# remove("dönem") istediğiniz elemanı çıkarmak için ||| iki tane aynı eleman silinirse ilk gördüğünü siler|||
# pop(1) elelman konumu verecek silmek çıkartmak 
# count() eleman sayısını bulma 
# index() ilie konum sırasını bulma 
# clear ile liste içini temizlemek
# extend listeye liste eklemek

# range(1,12,2) sayı dizisi list(range(10))
yeni=list(range(10))
print(yeni)
yeni=list(range(1,10,2))
print(yeni)

# sort küçükten büyüğe sıralama
yeni2=[123,21,34,1999,1297,1997]
print(yeni2)
yeni2=[123,21,34,1999,1297,1997]
yeni2.sort()
print(yeni2)

# reverse listeyi tersine çevirme(sortun tersi)
yeni=list(range(1,10,2))
yeni.reverse()
print(yeni)
yeni2=[123,21,34,1999,1297,1997]
yeni2.sort()
yeni2.reverse()
print(yeni2)

# listeyi kopyalamal copy()
yeni2=[123,21,34,1999,1297,1997]
kopya=yeni2.copy()
print(kopya)

# append("dönem") listeye eleman eklemek
yeni2=[123,21,34,1999,1297,1997]
yeni2.append("python")
yeni2.append(571)
print(yeni2)

# insert(1,"sınav")listenin istediğiniz konumuna eleman eklemek için
yeni2=[123,21,34,1999,1297,1997]
yeni2.insert(2,"seyithan")
print(yeni2)
yeni=list(range(1,10,2))
yeni.insert(3,"seyda")
print(yeni)

# remove("dönem") istediğiniz elemanı çıkarmak için ||| iki tane aynı eleman silinirse ilk gördüğünü siler|||
yeni=list(range(1,10,2))
yeni.remove(5)
print(yeni)
yeni2=[123,21,123,34,1999,123,1297,1997]
yeni2.remove(123)
print(yeni2)

# pop(1) elelman konumu verecek silmek çıkartmak 
yeni2=[123,21,123,34,1999,123,1297,1997]
yeni2.pop(2)
print(yeni2)

# count() eleman sayısını bulma 
yeni2=[123,21,123,34,1999,123,1297,1997]
print(yeni2.count(123))

# index() ilie konum sırasını bulma 
yeni2=[123,21,123,34,1999,123,1297,1997]
print(yeni2.index(1999))

# clear ile liste içini temizlemek
yeni2=[123,21,123,34,1999,123,1297,1997]
yeni2.clear()
print(yeni2)

# extend listeye liste eklemek
yeni2=[123,21,123,34,1999,123,1297,1997]
yeni=list(range(1,10,2))
yeni2.extend(yeni)
print(yeni2)