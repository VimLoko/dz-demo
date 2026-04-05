"""
Домашнее задание - Строки

Принять строку формата "<руб> руб <коп> коп" (пример: 100 руб 10 коп) и вывести нормализованную сумму в рублях с двумя знаками после запятой: 100.10 ₽.

Поддержать варианты без копеек ("159 руб" → "159.00 ₽").

- Программа читает одну строку из input()
- Регистр и лишние пробелы игнорируются
- Допустимые слова для единиц
- На выходе — сумма в виде X.YY ₽ (два знака после запятой)
- Если формат некорректный — вывести: Некорректный формат суммы
"""
user_summa: str = input("Введите сумму: ").strip().lower()

splitted_user_summa: list[str] = user_summa.split()
monetary_units: list[str] = splitted_user_summa[1::2]
rub: str
kop: str
if "руб" in monetary_units and "коп" in monetary_units:
    rub, kop = splitted_user_summa[::2]
    print(f"{rub}.{kop} ₽")
elif "руб" in monetary_units and "коп" not in monetary_units:
    rub = splitted_user_summa[0]
    print(f"{float(rub):.2f} ₽")
else:
    print("Некорректный формат суммы")
