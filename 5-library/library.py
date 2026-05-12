"""
Сделай программу, которая работает с каталогом книг из словаря books и
выполняет действие в зависимости от параметра запуска action. Используй
модуль sys и получай action из sys.argv[1] (import sys)

Если action == "filter" - С помощью filter выбери книги переданные в
sys.argv[2]. С помощью map выведи список строк "Книга — Автор".

Если action == "sort" - С помощью map подготовь список строк "Книга — Автор".
Отсортируй список по алфавиту в зависимости от author или book.
"""
import sys


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

if len(sys.argv) < 3:
    print("Недопустимое количество параметров.")
    exit()

TYPE_ACTIONS: tuple[str] = ("sort", "filter")
ACTIONS_SORT: tuple[str] = ("book", "author")

action: str = sys.argv[1].lower()
value: str = sys.argv[2].lower()

if action not in TYPE_ACTIONS:
    print(f"Введен не существующий action: {action}")
    print(f"Допустимы следующие значения: {TYPE_ACTIONS}")
    exit()

if action == "sort" and value not in ACTIONS_SORT:
    print(f"Введен не существующий ключ сортировки: {value}")
    print(f"Допустимы следующие значения: {ACTIONS_SORT}")
    exit()


if action == "sort":
    sorted_books: dict[str: str] = dict(
        sorted(books.items(), key=lambda v: v[1] if value == "author" else v[0]))
    print_books(sorted_books)

if action == "filter":
    filtered_books: dict[str: str] = dict(
        filter(lambda v: v[0].lower().count(value) + v[1].lower().count(value), books.items()))
    print_books(filtered_books)
