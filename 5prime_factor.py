#Kullanıcının girdiği sayının asal çarpanlarını bulan bir program:

def asal_carpanlari_bul(sayi): 
    carpanlar = [] 
    i = 2 
    while i <= sayi: 
        if sayi % i == 0: 
            carpanlar.append(i)
            sayi //= i
        else:
            i += 1

    return carpanlar 

sayi = int(input("Bir sayi girin: "))

print(f"{sayi}'nin asal çarpanları:", asal_carpanlari_bul(sayi))

