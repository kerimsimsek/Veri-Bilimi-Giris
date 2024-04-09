import matplotlib.pyplot as plt

categories = ['Araba','Ev','Silah','Yiyecek']
values =[30,50,10,100]

#Pasta grafiği çiz.
plt.pie(values, labels=categories, autopct='%1.f%%')

plt.show()