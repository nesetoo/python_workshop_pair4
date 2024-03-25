#Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program:

def mukemmel_mi(sayi):
    
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
   
    if toplam == sayi:
        return True
    else:
        return False


sayi = int(input("Bir sayi girin: "))


if mukemmel_mi(sayi):
    print(f"{sayi} mükemmel bir sayidir.")
else:
    print(f"{sayi} mükemmel bir sayi değildir.")