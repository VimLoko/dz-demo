"""Модуль для работы с заказами

Структура заказа:
    •    id — уникальный идентификатор (int).
    •    title — название заказа (строка).
    •    amount — сумма заказа (число с плавающей точкой).
    •    email — email клиента (строка).
    •    status — статус заказа (new, in_progress, done, cancelled).
    •    tags — множество тегов (set строк).
    •    created_at — дата и время создания (ISO 8601, UTC).
    •    due — дедлайн (строка в ISO 8601 или None).
    •    closed_at — дата и время закрытия заказа (ISO 8601, UTC или None).
"""

from typing import TypedDict, Optional
from datetime import datetime


class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: str
    tags: Optional[set[str]]
    created_at: Optional[datetime]
    due: Optional[datetime]
    closed_at: Optional[datetime]


STATUSES = ("new", "in_progress", "done", "cancelled")
ORDERS_STORAGE: list[Order] = []


def create_order(id_: int, title: str, amount: float, email: str, status: str = "new", tags: Optional[set[str]] = None, created_at: Optional[datetime] = None, due: Optional[datetime] = None, closed_at: Optional[datetime] = None):
    if status not in STATUSES:
        raise ValueError(
            f"Неверный статус - {status}. Доступны следующие статусы: {STATUSES}")
    order: Order = {
        "id": id_,
        "title": title,
        "amount": amount,
        "email": email,
        "status": status,
        "tags": tags,
        "created_at": created_at,
        "due": due,
        "closed_at": closed_at
    }
    ORDERS_STORAGE.append(order)


def list_orders():
    for order in ORDERS_STORAGE:
        print(
            f"id: {order['id']} | Название: {order['title']} | Сумма: {order['amount']} ")
        print(
            f"Эл.почта: {order['email']} | Статус: {order['status']} | Тэги: {', '.join(order['tags'])}")
        print(
            f"Создано: {order['created_at'].strftime('%d.%m.%Y %H:%M')} | Дедлайн: {order['due'].strftime('%d.%m.%Y %H:%M')} | Закрыт: {order['closed_at'].strftime('%d.%m.%Y %H:%M')}")
        print("-" * 40)


def edit_order(id_: int, title: str, amount: float, email: str, status: str = "new", tags: Optional[set[str]] = None, created_at: Optional[datetime] = None, due: Optional[datetime] = None, closed_at: Optional[datetime] = None):
    result_order = None
    key_order = None
    for key, order in enumerate(ORDERS_STORAGE):
        if order["id"] == id_:
            result_order = order
            key_order = key
            break

    if result_order is None:
        raise ValueError(f"Заказ с id: {id_} отсутствует")

    ORDERS_STORAGE[key_order] = {
        "id": ORDERS_STORAGE[key_order]["id"],
        "title": title,
        "amount": amount,
        "email": email,
        "status": status,
        "tags": tags,
        "created_at": created_at,
        "due": due,
        "closed_at": closed_at
    }


def remove_order(id_: int):
    for key, order in enumerate(ORDERS_STORAGE):
        if order["id"] == id_:
            del ORDERS_STORAGE[key]
            break
