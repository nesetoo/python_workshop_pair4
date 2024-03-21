#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

#Alternatif 1

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))
sayi3 = float(input("Üçüncü sayıyı giriniz: "))

en_büyük_sayi = max(sayi1, sayi2, sayi3)

print("En Büyük Sayi:", en_büyük_sayi)


#Alternatif 2

sayi1 = float(input("Birinci sayı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))
sayi3 = float(input("Üçüncü sayıyı giriniz: "))

if (sayi1>sayi2) and (sayi1>= sayi3):
    buyukSayi = sayi1
elif (sayi2>=sayi1) and (sayi2>=sayi3):
    buyukSayi=sayi2
else:
    buyukSayi=sayi3

totalText = f"Girdiğiniz sayılardan en büyüğü= {buyukSayi}"
print(totalText)


