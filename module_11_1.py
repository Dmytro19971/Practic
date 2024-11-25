import pandas as pd
import matplotlib.pyplot as plt

data = {'Продукт': ['Колбаса', 'Напитки', 'Яйца', 'Мясо', 'Хлеб'],
        'Продажи (шт.)': [15, 10, 4, 7, 20]
        }
df = pd.DataFrame(data)


total_sales = df['Продажи (шт.)'].sum()
print('Общий объем продаж:', total_sales)
mean_sales = df['Продажи (шт.)'].mean()

plt.bar(x=df['Продукт'], height=df['Продажи (шт.)'])
plt.title('Продажи по продуктам')
plt.xlabel('Продукт')
plt.xlabel('Продажи')
plt.show()
