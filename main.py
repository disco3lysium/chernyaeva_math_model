import numpy as np
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt

# Сгенерируем случайные координаты городов
np.random.seed(0)
cities = np.random.rand(10, 2) * 100  # 10 городов в 2D пространстве

# Вычислим матрицу расстояний между городами
dist_matrix = distance_matrix(cities, cities)

# Используем алгоритм для нахождения оптимального пути
# В данном случае используем метод линейного распределения (или алгоритм Венгерского метода)
row_ind, col_ind = linear_sum_assignment(dist_matrix)

# Расстояния для оптимального маршрута
optimal_route = col_ind
route_length = dist_matrix[row_ind, col_ind].sum()

print(f"Оптимальный маршрут: {optimal_route}")
print(f"Длина маршрута: {route_length}")

# Построение графика маршрута
plt.figure(figsize=(8, 6))
plt.scatter(cities[:, 0], cities[:, 1], color='red')
for i, city in enumerate(cities):
    plt.text(city[0], city[1], str(i + 1), fontsize=12)

# Нарисуем оптимальный маршрут
for i in range(len(optimal_route) - 1):
    plt.plot([cities[optimal_route[i]][0], cities[optimal_route[i + 1]][0]],
             [cities[optimal_route[i]][1], cities[optimal_route[i + 1]][1]], 'b-')

# Соединение последнего города с первым
plt.plot([cities[optimal_route[-1]][0], cities[optimal_route[0]][0]],
         [cities[optimal_route[-1]][1], cities[optimal_route[0]][1]], 'b-')

plt.title(f"Оптимальный маршрут с длиной {route_length:.2f}")
plt.show()
