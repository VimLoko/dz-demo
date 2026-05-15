"""Модуль для работы с JSON"""
import json
from orders import Order


def load(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print("[WARN] Поврежденный JSON")
        return []
    orders: list[Order] = []
    for item in raw.get("orders", []):
        try:
            order: Order = {
                "id": int(item["id"]),
                "title": item["title"],
                "amount": float(item["amount"]),
                "email": item["email"],
                "status": item["status"],
                "tags": set(item.get("tags", [])),
                "created_at": item["created_at"].strftime('%d.%m.%Y %H:%M'),
                "due": item["due"].strftime('%d.%m.%Y %H:%M'),
                "closed_at": item["closed_at"].strftime('%d.%m.%Y %H:%M')
            }
            orders.append(order)
        except Exception as e:
            print("Пропущен заказ: {e}")
    return orders


def save(path: str, orders: list[Order]):
    data = {
        "orders": [
            {
                "id": int(item["id"]),
                "title": item["title"],
                "amount": float(item["amount"]),
                "email": item["email"],
                "status": item["status"],
                "tags": set(item.get("tags", [])),
                "created_at": item["created_at"].strftime('%d.%m.%Y %H:%M'),
                "due": item["due"].strftime('%d.%m.%Y %H:%M'),
                "closed_at": item["closed_at"].strftime('%d.%m.%Y %H:%M')
            }
            for item in orders
        ]
    }
    with open(path, encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
