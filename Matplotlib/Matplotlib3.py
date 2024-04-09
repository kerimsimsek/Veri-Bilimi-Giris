import matplotlib.pyplot as plt

# Veri oluştur
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Figure ve Axes oluştur
fig, ax = plt.subplots()

# Çizgi grafiği çiz
ax.plot(x, y)

# Eksen etiketlerini ayarla
ax.set_xlabel('X Ekseni')
ax.set_ylabel('Y Ekseni')

# Grafiği göster
plt.show()