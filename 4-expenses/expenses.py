"""
Домашнее задание - Списки, кортежи

Создать список из трат за неделю (7 чисел)

Посчитать сумму, среднее, минимум и максимум.

Сохранить в кортеже (минимум, максимум, сумма) и вывести его.

"""
expenses: list[float] = [100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0]

expenses_sum: float = sum(expenses)
expenses_len: int = len(expenses)
expenses_avg: float = round(expenses_sum / expenses_len, 2)
expenses_min: float = min(expenses)
expenses_max: float = max(expenses)
result: tuple[float, ...] = (expenses_min, expenses_max, expenses_sum)

print(result)
