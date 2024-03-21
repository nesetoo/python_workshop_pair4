#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir programı:
#palindromlar tersten de okunduğunda aynı olan kelimeler ve sayılar için kullanılan bir terimdir.
#palindromlar ondalıklı sayılar için de kullanılan bir terim.
#bir sonraki aşamada planladığım çözüm arayışı: harf ve rakamın
#kullanici tarafindan sorguya girilmesi durumunda, tersi de aynı olduğunda programın palindrom çıktısı vermesi problemi.

#ALTERNATIF 1:

sayi = str(input("Bir sayı giriniz: "))
sayiTers =sayi[::-1]


if sayiTers==sayi:
    totalText = f"{sayi} palindromdur."
    print(totalText)

else:
    totalText2 = f"{sayi} palindrom değildir."
    print(totalText2)


#ALTERNATIF 2

def palindromMu(sayi):
    sayi_str = str(sayi)
    tersi = sayi_str[::-1]
    
    if sayi_str == tersi:
        return True
    else:
        return False

sayi = (input("Bir sayi girin: "))

if palindromMu(sayi):
    print("Bu bir palindromdur.")
else:
    print("Bu bir palindrom değildir.")
