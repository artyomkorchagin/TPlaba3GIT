import csv
import matplotlib.pyplot as plt
import datetime

filename = "data.csv"

# Считываем данные из файла и сохраняем их в список
data = []
with open(filename, "r") as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        data.append(row)
# Выводим данные на экран
for row in data:
    print("Дата:", row[0])
    print("Длительность (мин):", row[1])
    print("Расстояние (км):", row[2])
    print("Макс. скорость (км/ч):", row[3])
    print("Мин. скорость (км/ч):", row[4])
    print("Средняя скорость (км/ч):", row[5])
    print("Средний пульс:", row[6])
    print("\n")
# Создаем список дат
dates = [datetime.datetime.strptime(row[0], "%d.%m.%Y").date() for row in data]
# Создаем первый график для длительности
fig, ax1 = plt.subplots()
ax1.set_xlabel('Дата')
ax1.set_ylabel('Длительность (мин)')

# Строим график длительности по датам
duration = [int(row[1]) for row in data]
ax1.plot(dates, duration, label="Длительность (мин)")

# Устанавливаем положения меток на оси x и изменяем подписи дат на оси x
ax1.set_xticks(dates)
ax1.set_xticklabels([date.strftime("%d.%m.%Y") for date in dates])

# Добавляем легенду и выводим первый график на экран
ax1.legend()
plt.show()

# Создаем второй график для расстояния
fig, ax2 = plt.subplots()
ax2.set_xlabel('Дата')
ax2.set_ylabel('Расстояние (км)')

# Строим график расстояния по датам
distance = [float(row[2]) for row in data]
ax2.plot(dates, distance, label="Расстояние (км)")

# Устанавливаем положения меток на оси x и изменяем подписи дат на оси x
ax2.set_xticks(dates)
ax2.set_xticklabels([date.strftime("%d.%m.%Y") for date in dates])

# Добавляем легенду и выводим второй график на экран
ax2.legend()
plt.show()
# Вычисляем сумму пройденных км за все выходные дни
weekend_distance = 0
for row in data:
    date = row[0]
    day_of_week = datetime.datetime.strptime(date, "%d.%m.%Y").weekday()
    if day_of_week >= 5:  # 5 и 6 - суббота и воскресенье
        weekend_distance += float(row[2])

print("Сумма пройденных км за все выходные дни:", weekend_distance)