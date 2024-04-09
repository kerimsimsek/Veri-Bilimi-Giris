import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_excel("Sınıf.xlsx")
print(df["Adlar"])
print(df["Yaşlar"])
plt.bar(df["Adlar"],df["Yaşlar"])
plt.show()