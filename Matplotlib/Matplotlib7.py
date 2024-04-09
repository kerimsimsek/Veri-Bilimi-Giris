import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel("Sınıf.xlsx")
kategoriler=["üstyas","altyas"]
yaslar = []
üstyas = 0
altyas = 0

"""Yaşların içinde kaç tane eleman var"""
print(len(df["Yaşlar"]))
for i in range(len(df["Yaşlar"])):
    if df["Yaşlar"][i]>=25:
        üstyas += (df["Yaşlar"][i])
    if df["Yaşlar"][i]<=25:
        altyas += (df["Yaşlar"][i])
print(f"25'den büyük yaşların toplamı : {üstyas}\n25'den küçük yaşların toplamı : {altyas}")

yaslar.append(üstyas)
yaslar.append(altyas)
plt.bar(kategoriler,yaslar)
plt.show()