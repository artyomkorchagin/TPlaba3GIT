import pandas as pd
import matplotlib.pyplot as plt
import numpy
def var2():
    df = pd.read_excel('art\currency.xlsx') # Получение информации из таблицы эксель
    print('Полная информация из таблицы')
    print(df)
    profit_loss = [[-100,0], [100,0], [-100,0], [100,0]]
    usd = df.loc[:,"USD/RUB"]               # разделение на столбики
    cny = df.loc[:,"CNY/RUB"]
    dat = df.loc[:,"Date"]
    for x in range(1, len(usd)):
        if usd[x-1] - usd[x] < 0:
            if usd[x-1] - usd[x] < profit_loss[1][0]:
                profit_loss[1][0] = usd[x-1] - usd[x]
                profit_loss[1][1] = x+1
        else:
            if usd[x-1] - usd[x] > profit_loss[0][0]:
                profit_loss[0][0] = usd[x-1] - usd[x]
                profit_loss[0][1] = x+1
        if cny[x - 1] - cny[x] < 0:
            if cny[x - 1] - cny[x] < profit_loss[3][0]:
                profit_loss[3][0] = cny[x - 1] - cny[x]
                profit_loss[3][1] = x+1
        else:
            if cny[x-1] - cny[x] > profit_loss[2][0]:
                profit_loss[2][0] = cny[x-1] - cny[x]
                profit_loss[2][1] = x+1

    print("Наибольшее падение/рост USD + день")
    print("%.2f" % -profit_loss[0][0], profit_loss[0][1],"%.2f" % abs(profit_loss[1][0]),profit_loss[1][1])
    print("Наибольшее падение/рост CNY + день")
    print("%.2f" % -profit_loss[2][0],profit_loss[2][1],"%.2f" % abs(profit_loss[3][0]),profit_loss[3][1])
    fig1, ax1 = plt.subplots()              # создание двух фигур для графиков курса валют
    fig2, ax2 = plt.subplots()

    ax1.set_xlabel('Дата')                  # установка названий для Х и Y осей графиков
    ax1.set_ylabel('Курс USD/RUB')
    ax2.set_xlabel('Дата')
    ax2.set_ylabel('Курс CNY/RUB')

    ax1.plot(dat, usd)                      # построение графиков
    ax2.plot(dat, cny)
    plt.show()
