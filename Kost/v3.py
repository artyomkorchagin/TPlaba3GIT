import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def var3():
    df = pd.read_csv('temperature_data.csv') # Чтение данных из файла в DataFrame

    print(df[['Max', 'Min', 'Average']]) # Вывод информации о максимальной, минимальной и средней температуре за каждый день

    diff = np.abs(df['Max'] - df['Min']) # Вычисление и вывод информации о наибольшем перепаде температур между днями
    max_diff_index = diff.idxmax()
    print(f'Наибольший перепад температур был между днями {max_diff_index} и {max_diff_index+1}, равный {diff[max_diff_index]:.2f} градусов')

    plt.plot(df['Day'], df['Max'], 'r', label='Максимальная температура') # Построение графика температур за каждый день
    plt.plot(df['Day'], df['Min'], 'b', label='Минимальная температура')
    plt.plot(df['Day'], df['Average'], 'g', label='Средняя температура')
    plt.legend(loc='best')
    plt.title('Температуры за месяц')
    plt.xlabel('Дни')
    plt.ylabel('Температура')
    plt.show()
    