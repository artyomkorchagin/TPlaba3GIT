import pandas as pd
import matplotlib.pyplot as plt

# Получение информации из таблицы эксель
df = pd.read_excel('currency.xlsx')
print('Полная информация из таблицы')
print(df)

# разделение на столбики
usd = df.loc[:,"USD/RUB"]
cny = df.loc[:,"CNY/RUB"]
dat = df.loc[:,"Date"]

# создание двух фигур для графиков курса валют
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

# установка названий для Х и Y осей графиков
ax1.set_xlabel('Дата')
ax1.set_ylabel('Курс USD/RUB')

ax2.set_xlabel('Дата')
ax2.set_ylabel('Курс CNY/RUB')

# построение графиков
ax1.plot(dat, usd)
ax2.plot(dat, cny)

plt.show()