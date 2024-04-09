import matplotlib.pyplot as plt
import numpy as np

# Veri oluştur
x = np.array(['A','B','C','D'])
y = np.array([2, 90, 50, 10])
plt.title('Deneme')

# Kırmızı renkte çizgi grafiği çiz
plt.bar(x, y, color='red')

# Grafiği göster
plt.show()