#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

# öncelikle hesaplama için gerekenler üzerinden yola çıkıldı:

agirlik = float(input("Lütfen kilonuzu kg cinsinden giriniz: "))
boy = float(input("Lütfen boyunuzu metre cinsinden giriniz: "))
vki = agirlik/(boy*boy)

totalText = f"Vücut kitle indeksiniz= {vki}'dir."
print(totalText)


#İkincil olarak kullanıcının, virgül ve harf gibi string değer girdiğinde
#programın hata vermesini engellemek ve yanlış formatta girdi olması durumunda, kullanıcıyı hedefine ulaştırmak üzere programı düzenlendi:


while True:
    try:
        agirlik = float(input("Lütfen kilonuzu kg cinsinden giriniz: "))
        break
    except(TypeError,ValueError):
        print("Sadece rakam ve nokta kullanarak giriş yapınız!")
    

while True:
    try:
        boy = float(input("Lütfen boyunuzu metre cinsinden giriniz: "))
        break
    except(TypeError,ValueError):
        print("Sadece rakam ve nokta kullanarak giriş yapınız!")

vki = agirlik/(boy*boy)

totalText = f"Vücut kitle indeksiniz= {vki}'dir."
print(totalText)