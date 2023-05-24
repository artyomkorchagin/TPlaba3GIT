import pandas as pd
import matplotlib.pyplot as plt
def var2():
    df = pd.read_excel('art\currency.xlsx') # Получение информации из таблицы эксель
    print('Полная информация из таблицы')
    print(df)

    usd = df.loc[:,"USD/RUB"]               # разделение на столбики
    cny = df.loc[:,"CNY/RUB"]
    dat = df.loc[:,"Date"]

    fig1, ax1 = plt.subplots()              # создание двух фигур для графиков курса валют
    fig2, ax2 = plt.subplots()

    ax1.set_xlabel('Дата')                  # установка названий для Х и Y осей графиков
    ax1.set_ylabel('Курс USD/RUB')
    ax2.set_xlabel('Дата')
    ax2.set_ylabel('Курс CNY/RUB')

    ax1.plot(dat, usd)                      # построение графиков
    ax2.plot(dat, cny)
    plt.show()
