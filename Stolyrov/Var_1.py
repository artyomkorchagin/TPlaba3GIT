import csv
import matplotlib.pyplot as plt
from datetime import datetime

weekend_distance_sum = 0.0
dates = []
durations = []
distances = []
max_speeds = []
min_speeds = []
avg_speeds = []
avg_pulses = []

with open("data.csv.txt", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader) # пропускаем заголовок
    for row in reader:
        date = datetime.strptime(row[0], '%d.%m.%Y')
        duration = int(row[1])
        distance = float(row[2])
        max_speed = float(row[3])
        min_speed = float(row[4])
        avg_speed = float(row[5])
        avg_pulse = int(row[6])
        dates.append(date)
        durations.append(duration)
        distances.append(distance)
        max_speeds.append(max_speed)
        min_speeds.append(min_speed)
        avg_speeds.append(avg_speed)
        avg_pulses.append(avg_pulse)
        weekday = date.weekday()
        if weekday == 5 or weekday == 6: # проверяем, является ли день выходным
            weekend_distance_sum += distance

# Сортировка данных по дате
sorted_data = sorted(zip(dates, durations, distances, max_speeds, min_speeds, avg_speeds, avg_pulses), key=lambda x: x[0])
dates, durations, distances, max_speeds, min_speeds, avg_speeds, avg_pulses = zip(*sorted_data)

# Вывод информации о пробежках на экран
for i in range(len(dates)):
    print(f"{dates[i].strftime('%d.%m.%Y')}: Длительность: {durations[i]} мин, Расстояние: {distances[i]} км, Макс. скорость: {max_speeds[i]} км/ч, Мин. скорость: {min_speeds[i]} км/ч, Средняя скорость: {avg_speeds[i]} км/ч, Средний пульс: {avg_pulses[i]}")

# Построение графика зависимости длительности пробежки от даты
plt.plot(dates, durations)
plt.xlabel('Дата')
plt.ylabel('Длительность, мин')
plt.title('Зависимость длительности пробежки от даты')
plt.show()

# Сортировка данных по длительности
sorted_data = sorted(zip(durations, avg_speeds), key=lambda x: x[0])
durations, avg_speeds = zip(*sorted_data)

# Построение графика зависимости средней скорости пробежки от длительности
plt.plot(durations, avg_speeds)
plt.xlabel('Длительность, мин')
plt.ylabel('Средняя скорость, км/ч')
plt.title('Зависимость средней скорости пробежки от длительности')
plt.show()

# Вывод суммы пройденных км за выходные
print(f"Сумма пройденных км за все выходные дни: {weekend_distance_sum} км")