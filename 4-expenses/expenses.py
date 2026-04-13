"""
Домашнее задание - Строки

Принять строку формата "<руб> руб <коп> коп" (пример: 100 руб 10 коп) и вывести
нормализованную сумму в рублях с двумя знаками после запятой: 100.10 ₽.

Поддержать варианты без копеек ("159 руб" → "159.00 ₽").

- Программа читает одну строку из input()
- Регистр и лишние пробелы игнорируются
- Допустимые слова для единиц
- На выходе — сумма в виде X.YY ₽ (два знака после запятой)
- Если формат некорректный — вывести: Некорректный формат суммы

user_summa: str = input("Введите сумму: ").strip().lower()

splitted_user_summa: list[str] = user_summa.split()
monetary_units: list[str] = splitted_user_summa[1::2]
rub: str
kop: str
result: str = "Некорректный формат суммы"
if "руб" in monetary_units and "коп" in monetary_units:
    rub, kop = splitted_user_summa[::2]
    if rub.isdigit() and kop.isdigit():
        result = f"{rub}.{kop.zfill(2)} ₽"

if "руб" in monetary_units and "коп" not in monetary_units:
    rub = splitted_user_summa[0]
    if rub.isdigit():
        result = f"{float(rub):.2f} ₽"

print(result)

Сделать интерактивное меню управления расходами с помощью циклов.

- Добавить расход
- Показать все расходы
- Показать сумму и средний расход
- Удалить расход по номеру
- Выход

Пока сделать только выход
"""
MENU: str = """1. Добавить расход.
2. Показать все расходы.
3. Показать сумму и средний расход.
4. Удалить расход по номеру.
0. Выход."""

while True:
    print(MENU)
    menu_num: int = int(input("Введите номер пункта меню: "))
    if 0 <= menu_num <= 4:
        if menu_num == 0:
            print("Программа будет закрыта.")
            exit()
    else:
        print("Вы ввели не существующий номер пункта меню.", end="\n\n")
