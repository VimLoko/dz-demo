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
# orders.py
from typing import Optional, TypedDict
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


def create_order(id_: int, title: str, amount: float, email: str, status: str = "new",
                 tags: Optional[set[str]] = None, created_at: Optional[datetime] = None,
                 due: Optional[datetime] = None, closed_at: Optional[datetime] = None):
    if status not in STATUSES:
        raise ValueError(f"Неверный статус - {status}. Доступны: {STATUSES}")
    order: Order = {
        "id": id_,
        "title": title,
        "amount": amount,
        "email": email,
        "status": status,
        "tags": tags if tags is not None else set(),
        "created_at": created_at,
        "due": due,
        "closed_at": closed_at
    }
    ORDERS_STORAGE.append(order)


def find_order_by_id(order_id: int) -> Optional[Order]:
    for order in ORDERS_STORAGE:
        if order["id"] == order_id:
            return order
    return None


def list_orders(overdue: bool = False, tag: Optional[str] = None, limit: Optional[int] = None):
    """Возвращает отфильтрованный список заказов"""
    result = []
    for order in ORDERS_STORAGE:
        # фильтр overdue: дедлайн < текущего времени и статус не done/cancelled
        if overdue:
            if order["due"] and order["status"] not in ("done", "cancelled"):
                if order["due"] < datetime.now():
                    pass
                else:
                    continue
            else:
                continue
        # фильтр по тегу
        if tag:
            if not order["tags"] or tag not in order["tags"]:
                continue
        result.append(order)
    if limit:
        result = result[:limit]
    return result


def print_orders_table(orders: list[Order]):
    """Красивый вывод таблицы заказов"""
    if not orders:
        print("Нет заказов, удовлетворяющих условиям")
        return
    headers = ["ID", "Название", "Сумма", "Статус", "Дедлайн"]
    # форматирование значений

    def fmt(order, field):
        val = order.get(field)
        if val is None:
            return ""
        if field == "due" and isinstance(val, datetime):
            return val.strftime("%Y-%m-%d")
        if field == "amount":
            return f"{val:.2f}"
        return str(val)
    # ширина столбцов
    col_widths = [len(h) for h in headers]
    for order in orders:
        col_widths[0] = max(col_widths[0], len(str(order["id"])))
        col_widths[1] = max(col_widths[1], len(order["title"]))
        col_widths[2] = max(col_widths[2], len(f"{order['amount']:.2f}"))
        col_widths[3] = max(col_widths[3], len(order["status"]))
        due_str = fmt(order, "due")
        col_widths[4] = max(col_widths[4], len(due_str))
    # печать
    sep = "+" + "+".join("-" * (w+2) for w in col_widths) + "+"
    print(sep)
    row = "| " + " | ".join(headers[i].ljust(col_widths[i])
                            for i in range(5)) + " |"
    print(row)
    print(sep.replace("-", "="))
    for order in orders:
        row = f"| {order['id']:<{col_widths[0]}} | {order['title']:<{col_widths[1]}} | {fmt(order, 'amount'):>{col_widths[2]}} | {order['status']:<{col_widths[3]}} | {fmt(order, 'due'):<{col_widths[4]}} |"
        print(row)
        print(sep)


def edit_order(order_id: int, **kwargs):
    """Обновляет только переданные поля (частичное редактирование)"""
    order = find_order_by_id(order_id)
    if not order:
        raise ValueError(f"Заказ с id {order_id} не найден")
    # обновляем только те поля, которые переданы
    for key, value in kwargs.items():
        if key in order:
            if key == "tags" and value is not None:
                order[key] = set(value) if isinstance(value, list) else value
            else:
                order[key] = value
    # валидация статуса
    if "status" in kwargs and kwargs["status"] not in STATUSES:
        raise ValueError(f"Неверный статус: {kwargs['status']}")


def remove_order(order_id: int):
    for i, order in enumerate(ORDERS_STORAGE):
        if order["id"] == order_id:
            del ORDERS_STORAGE[i]
            return
    raise ValueError(f"Заказ с id {order_id} не найден")


def manage_tags(order_id: int, add: Optional[list[str]] = None, remove: Optional[list[str]] = None):
    order = find_order_by_id(order_id)
    if not order:
        raise ValueError(f"Заказ {order_id} не найден")
    if order["tags"] is None:
        order["tags"] = set()
    if add:
        order["tags"].update(add)
    if remove:
        order["tags"].difference_update(remove)


def set_status(order_id: int, new_status: str):
    if new_status not in STATUSES:
        raise ValueError(f"Неверный статус: {new_status}")
    order = find_order_by_id(order_id)
    if not order:
        raise ValueError(f"Заказ {order_id} не найден")
    order["status"] = new_status
    if new_status == "done" and order["closed_at"] is None:
        order["closed_at"] = datetime.now()
