# liste tanımlama
#liste elemanlarını yazdırma [5]
#iç içe listelerde erişim
listem=[159,21.5,"python",[13,154,258],True]
print(listem)
print(listem[0])
print(listem[1])
print(listem[2])
print(listem[3])
print(listem[3][1])
print(listem[4])

for i in listem:
    print(i,":",type(i))