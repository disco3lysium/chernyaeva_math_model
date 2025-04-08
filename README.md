📌 README.md — Задача 3: Оптимизация маршрута доставки (задача коммивояжёра)

# 🚚 Задача коммивояжёра — Оптимизация маршрута доставки

Этот проект представляет собой реализацию математической модели задачи коммивояжёра (TSP — Traveling Salesman Problem) на языке Python с использованием библиотек NumPy, SciPy и Matplotlib.

Цель — найти кратчайший маршрут, проходящий через заданные города один раз и возвращающийся в начальную точку.

## 📊 Постановка задачи

- Моделируется маршрут доставки.
- Необходимо минимизировать суммарное расстояние между точками маршрута.
- Подходит для логистики, планирования перевозок и оптимизации выездных служб.

## 📐 Математическая модель

- Используется симметричная матрица расстояний между городами.
- Целевая функция: минимизация суммы расстояний между посещаемыми городами.
- Ограничения:
  - Каждый город посещается один раз.
  - Нет повторных посещений и подмаршрутов.

## ⚙️ Технологии и стек

- Язык: Python 3.x
- Среда: Jupyter Notebook
- Библиотеки:
  - NumPy (обработка массивов)
  - SciPy (оптимизация, расстояния)
  - Matplotlib (визуализация маршрута)

## 📁 Структура проекта

.
├── tsp_model.ipynb         # Основной ноутбук с реализацией модели
├── screenshots/            # Скриншоты графиков маршрутов
└── README.md               # Описание проекта

## ▶️ Как запустить

1. Клонируйте репозиторий:

   git clone https://github.com/yourusername/tsp-optimizer.git

2. Установите зависимости:

   pip install numpy scipy matplotlib

3. Запустите ноутбук:

   jupyter notebook tsp_model.ipynb

4. Измените количество городов или координаты по желанию, запустите все ячейки.

## 📈 Результаты

- Визуализируется оптимальный маршрут по сгенерированным городам.
- Отображается суммарная длина маршрута.
- Скриншоты графиков сохранены в папке screenshots/.

📸 Пример графика маршрута:

(здесь можно вставить скриншот или ссылку на изображение)

## 📌 Примечание

Метод, использованный в проекте — алгоритм линейного распределения (Hungarian algorithm), даёт приближённое решение TSP и работает хорошо при небольшом числе точек.

Для точного решения задачи при большом количестве городов рекомендованы методы ветвей и границ или библиотека OR-Tools от Google.

—

Готово! Ты можешь вставить это в файл README.md, предварительно заменив ссылку на свой репозиторий и добавив скриншоты, если хочешь. Хочешь, я ещё и markdown-файл подготовлю и скину как текст для вставки?
