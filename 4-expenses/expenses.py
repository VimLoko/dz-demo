"""
Домашнее задание - Функции

Сделать функции:

add_expense(expenses, value) — добавляет расход
delete_expense(expenses, index) — удалить расход
get_total(expenses) — возвращает сумму
get_average(expenses) — возвращает средний расход
print_report(expenses) — печатает красивый отчёт

Вызывать все функции в меню. Расходы хранить в list

"""


MENU: str = """1. Добавить расход.
2. Показать все расходы.
3. Показать сумму и средний расход.
4. Удалить расход по номеру.
0. Выход."""

EXPENSES: list[float] = []


def add_expenses(expenses: list[float], value: float) -> None:
    """Добавляет расход"""
    expenses.append(value)


def delete_expenses(expenses: list[float], index: int) -> None:
    """Удаляет расход по индексу"""
    del expenses[index]


def get_total(expenses: list[float]) -> float:
    """Возвращает общую сумму расходов"""
    return sum(expenses)


def get_average(expenses: list[float]) -> float:
    """Возвращает среднее значение расходов"""
    return get_total(expenses) / len(expenses)


def print_expenses(expenses: list[float]) -> None:
    """Выводит все расходы"""
    for k, v in enumerate(expenses):
        print(f"{k} -> {v}")


def print_report(expenses: list[float]) -> None:
    """Печатает отчет по расходам"""
    print("Общая сумма расходов:", get_total(expenses))
    print("Среднее значение расхода:", get_average(expenses))


while True:
    print(MENU)
    menu_num: int = int(input("Введите номер пункта меню: "))
    match menu_num:
        case 0:
            print("Программа будет закрыта.")
            exit()
        case 1:
            user_value: float = float(input("Введите сумму расхода: "))
            add_expenses(EXPENSES, user_value)
        case 2:
            print("Ваши расходы:")
            print_expenses(EXPENSES)
        case 3:
            print("Отчет по расходам")
            print_report(EXPENSES)
        case 4:
            print_expenses(EXPENSES)
            user_index: int = int(
                input("Введите index расхода для удаления: "))
            if user_index >= len(EXPENSES) or user_index < 0:
                print("Вы ввели не существующий индекс расхода")
            else:
                delete_expenses(EXPENSES, user_index)
        case _:
            print("Вы ввели не существующий номер пункта меню.", end="\n\n")
