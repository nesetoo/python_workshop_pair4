#Kullanıcının girdiği sayının asal olup olmadığını söyleyen bir program:

sayi = int(input("Sayı giriniz:"))
asalmi = 0  #eğer kalan 0 ise girilen sayı asal sayı değldir.

for i in range (2,sayi): 
    if sayi%i == 0:
      asalmi += 1
      break


if asalmi == 0:
      print(sayi, "sayısı asaldır.")
else: 
      print(sayi, "sayısı asal değildir.")