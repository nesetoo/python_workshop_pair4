#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
# pi sabiti için math modulü kullanarak hesaplamayı gerçekleştirdik.

import math

yaricap = float(input("Yarıçapı giriniz: "))

alan= (math.pi*yaricap*yaricap)
cevre= (2*math.pi*yaricap)

totalText = f"Dairenin alanı= {alan}"
print(totalText)

totalText2 = f"Dairenin cevresi= {cevre}"
print(totalText2)

