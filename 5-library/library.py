"""
Создай словарь books, где ключ — название книги, значение — автор.

- Добавь несколько записей. При этом может быть у одного автора несколько книг
- Вывести: список всех книг, список всех уникальных авторов.
"""


def print_books(books: dict[str: str]) -> None:
    """Выводит список всех книг"""
    for book, author in books.items():
        print(f"- {book}, {author}")


def print_unique_authors(books: dict[str: str]) -> None:
    """Выводит список всех уникальных авторов"""
    authors = set(books.values())
    for author in authors:
        print(f"- {author}")


books: dict[str: str] = {
    "Преступление и наказание": "Достоевский Ф.М.",
    "Мастер и Маргарита": "Булгаков М.А.",
    "Идиот": "Достоевский Ф.М.",
    "Евгений Онегин": "Пушкин А.С.",
}

print("Список всех книг:")
print_books(books)

print("Список всех уникальных авторов:")
print_unique_authors(books)
