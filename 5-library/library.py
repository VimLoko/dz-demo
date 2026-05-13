"""
Нужно обработать все возможные ошибки в помощью ошибок:

- Не передан текст фильтра
- Передана кривая команда
- Передан кривой параметр сортировки

Сделать базовый класс ошибки и расширить нужными ошибками. Обработать их всех и вывести в консоль ошибки.
"""
import sys


class LibraryAppException(Exception):
    """Базовый класс исключений для приложения"""
    pass


class InvalidCountOfParameters(LibraryAppException):
    """Исключений о недопустимом количестве параметров"""
    pass


class InvalidAction(LibraryAppException):
    """Исключений о недопустимом action"""
    pass


class InvalidKeySort(LibraryAppException):
    """Исключений о недопустимом ключе сортировки"""
    pass


class InvalidFilterValue(LibraryAppException):
    """Исключений о пустом значении фильтра"""
    pass


def print_books(books: dict[str: str]) -> None:
    """Выводит список всех книг"""
    result: list[str] = list(map(lambda v: f"{v[0]} — {v[1]}", books.items()))
    print("\n".join(result))


books: dict[str: str] = {
    "Преступление и наказание": "Достоевский Ф.М.",
    "Мастер и Маргарита": "Булгаков М.А.",
    "Идиот": "Достоевский Ф.М.",
    "Евгений Онегин": "Пушкин А.С.",
}

TYPE_ACTIONS: tuple[str] = ("sort", "filter")
ACTIONS_SORT: tuple[str] = ("book", "author")

try:
    if len(sys.argv) < 3:
        raise InvalidCountOfParameters("Недопустимое количество параметров.")

    action: str = sys.argv[1].lower()
    value: str = sys.argv[2].lower()

    if action not in TYPE_ACTIONS:
        raise InvalidAction(f"Введен не существующий action: {action}")

    if action == "sort" and value not in ACTIONS_SORT:
        raise InvalidKeySort(
            f"Введен не существующий ключ сортировки: {value}")

    if action == "sort":
        sorted_books: dict[str: str] = dict(
            sorted(books.items(), key=lambda v: v[1] if value == "author" else v[0]))
        print_books(sorted_books)

    if action == "filter":
        if not value:
            raise InvalidFilterValue("Не передан текст фильтра")
        filtered_books: dict[str: str] = dict(
            filter(lambda v: v[0].lower().count(value) + v[1].lower().count(value), books.items()))
        print_books(filtered_books)
except (InvalidCountOfParameters, InvalidAction, InvalidKeySort, InvalidFilterValue) as e:
    print("Ошибка приложения:", e)
except Exception as e:
    print("Ошибка:", e)
