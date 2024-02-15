import math
import random

import np
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from itertools import product, combinations
from mpl_toolkits.mplot3d import Axes3D

kol_co_in_room = 0
sensors_kol = 0
aa = 4
bb = 4
cc = 4
sensor_S = 0
# Ввод данных о комнате
print('Введите длину, ширину и высоту комнаты (в метрах): ')
a = input()
b = input()
c = input()
a = float(a)
b = float(b)
c = float(c)
while a < 2 or a > 20:
    print("Неверно введена длина. Введите длину снова:")
    a = input()
    a = float(a)
while b < 2 or b > 20:
    print('Неверно введена ширина. Введите ширину снова:')
    b = input()
    b = float(b)
while c < 2 or c > 20:
    print('Неверно введена высота. Введите высоту снова:')
    c = input()
    c = float(c)

# Ввод данных о датчиках
print('Введите количество датчиков в комнате: ')
sensor_kol = input()
sensors = [0]
sensors.clear()
i = 0
print('Введите координаты датчиков в таком порядке: по длине, ширине, высоте!, количество обнаруженного CO2 (в ppm)')
while i < int(sensor_kol):
    print("Введите данные для", i + 1, "датчика:")
    sensor_a = input()
    sensor_b = input()
    sensor_c = input()
    sensor_co = input()
    sensors.append([float(sensor_a), float(sensor_b), float(sensor_c), float(sensor_co)])
    i = i + 1

# Проверка правильности введённых данных о датчиках
for j in sensors:
    while j[0] < 0 or j[0] > a:
        print("Неверно введена длина у датчика с данными", j, ". Введите длину снова:")
        j[0] = input()
        j[0] = float(j[0])
    while j[1] < 0 or j[1] > b:
        print("Неверно введена ширина у датчика с данными", j, ". Введите ширину снова:")
        j[1] = input()
        j[1] = float(j[1])
    while j[2] < 0 or j[2] > c:
        print("Неверно введена высота у датчика с данными", j, ". Введите высоту снова:")
        j[2] = input()
        j[2] = float(j[2])
for i in sensors:
    for j in sensors:
        if i != j and sensors.index(i) + 1 < sensors.index(j) + 1:
            print("Расстояние между", sensors.index(i) + 1, "и", sensors.index(j) + 1, "датчиками:",
                  math.sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 + (i[2] - j[2]) ** 2))

# Расчёт C02 (a, b, c, sensor_kol, sensors)
S = 2 * (float(a) * float(b) + float(b) * float(c) + float(a) * float(c))  # Площадь CO2
for j in sensors:
    aa = 4
    bb = 4
    cc = 4

    if j[0] - 2 < 0:
        aa = aa - np.abs(j[0] - 2)
    if j[0] + 2 > a:
        aa = aa - (j[0] + 2 - a)

    if j[1] - 2 < 0:
        bb = bb - np.abs(j[1] - 2)
    if j[1] + 2 > b:
        bb = bb - (j[1] + 2 - b)

    if j[2] - 2 < 0:
        cc = cc - np.abs(j[2] - 2)
    if j[2] + 2 > c:
        cc = cc - (j[2] + 2 - c)
    sensor_S = sensor_S + 2 * (aa*bb + bb*cc + aa*cc)
    print(aa)
for j in sensors:
    sensor_CO2 = sensor_S + j[3]
CO2 = S * sensor_CO2 / sensor_S

print("Количество C02 в помещении: ", CO2)

# Построение комнаты с датчиками и визуализация CO2
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

for j in sensors:
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = 2 * np.outer(np.cos(u), np.sin(v)) + j[0]
    y = 2 * np.outer(np.sin(u), np.sin(v)) + +j[1]
    z = 2 * np.outer(np.ones(np.size(u)), np.cos(v)) + j[2]

    ax.plot_wireframe(x, y, z, color="green")
ax.set_title("Визуализация комнаты")

r1 = [0, a]
r2 = [0, b]
r3 = [0, c]
ax.scatter(a, b, c, s=0)
for s, e in combinations(np.array(list(product(r1, r2, r3))), 2):
    if np.sum(np.abs(s - e)) == r1[1] - r1[0] or np.sum(np.abs(s - e)) == r2[1] - r2[0] or np.sum(np.abs(s - e)) == r3[
        1] - r3[0]:
        ax.plot3D(*zip(s, e), color="red")

for i in range(0, int(CO2) // 5):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 0.01 * np.outer(np.cos(u), np.sin(v)) + random.uniform(0, a)
    y = 0.01 * np.outer(np.sin(u), np.sin(v)) + random.uniform(0, b)
    z = 0.01 * np.outer(np.ones(np.size(u)), np.cos(v)) + random.uniform(0, c)

    ax.plot_wireframe(x, y, z, color="black")
plt.show()
