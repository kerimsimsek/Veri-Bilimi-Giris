import matplotlib.pyplot as plt
import numpy as np

öğrenci_notu = []
notlar_kategorisi=["10","20","30","40","50","60","70","80","90","100"]
while True:
    notlar = int(input("Öğrenci notlarını giriniz : "))
    
    if notlar<0 or notlar>100:
        print(öğrenci_notu)
        break

    öğrenci_notu.append(notlar)

notsayısı = [öğrenci_notu.count(10),öğrenci_notu.count(20),öğrenci_notu.count(30),öğrenci_notu.count(40),öğrenci_notu.count(50),öğrenci_notu.count(60),öğrenci_notu.count(70),öğrenci_notu.count(80),öğrenci_notu.count(90),öğrenci_notu.count(100)]

plt.title("Notların Dağılımı")
plt.bar(notlar_kategorisi,notsayısı,color="red")
plt.show()