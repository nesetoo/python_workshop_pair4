#Kullanıcının girdiği sayının EBOB ve EKOK'unu bulan bir program:


#versiyon1, math kütüphanesinden gcd(greatest common divisor) metodu ile:

import math 
sayi1=int(input("Birinci Sayıyı Giriniz: "))
sayi2=int(input("İkinci Sayıyı Giriniz: "))

ebob=math.gcd(sayi1, sayi2)
ekok=(sayi1*sayi2)//ebob

print("EBOB:", ebob)
print("EKOK:", ekok)



#versiyon2, for döngüsü kullanarak:

def ebob_ekok(sayi1,sayi2):
    if sayi1 > sayi2:
        kucuksayi = sayi2
    else:
        kucuksayi = sayi1
    for i in range(1, kucuksayi+1):
        if(sayi1 % i ==0) and (sayi2 % i ==0):
            ebob=i

    ekok =(sayi1 * sayi2) // ebob
    return ebob, ekok

sayi1 = int(input("Birinci Sayıyı Giriniz: "))
sayi2 = int(input("İkinci Sayıyı Giriniz: "))
 
ebob, ekok = ebob_ekok(sayi1, sayi2)
print("EBOB:", ebob)
print("EKOK:", ekok)


