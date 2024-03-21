#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
# öncelikle hesaplama için gerekenler üzerinden yola çıkıldım

maas = float(input("Lütfen maaşınızı giriniz: "))
zamOrani = float(input("Lütfen zam oranınızın yüzde kaç olduğunu giriniz: "))
zamliMaas = (maas*(100 + zamOrani)/100)

totalText = f"Zamlı maaşınız= {zamliMaas}"
print(totalText)


#İkincil olarak kullanıcının, virgül ve harf gibi string değer girdiğinde
#programın hata vermesini engellemek üzere program düzenlendi:

while True:
    try:
        maas = float(input("Lütfen maaşınızı giriniz: "))
        break
    except(TypeError,ValueError):
        print("Sadece rakam ve nokta kullanarak giriş yapınız!")
    

while True:
    try:
        zamOrani = float(input("Lütfen zam oranınızın yüzde kaç olduğunu giriniz: "))
        break
    except(TypeError,ValueError):
        print("Sadece rakam ve nokta kullanarak giriş yapınız!")

zamliMaas = (maas*(100 + zamOrani)/100)

totalText = f"Zamlı maaşınız= {zamliMaas}"
print(totalText)
