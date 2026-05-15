"""Модуль для работы с JSON"""
import json
from datetime import datetime
from typing import List
from orders import Order


def load(path: str) -> List[Order]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    orders = []
    for item in data.get("orders", []):
        try:
            order: Order = {
                "id": int(item["id"]),
                "title": item["title"],
                "amount": float(item["amount"]),
                "email": item["email"],
                "status": item["status"],
                "tags": set(item.get("tags", [])),
                "created_at": datetime.fromisoformat(item["created_at"]) if item.get("created_at") else None,
                "due": datetime.fromisoformat(item["due"]) if item.get("due") else None,
                "closed_at": datetime.fromisoformat(item["closed_at"]) if item.get("closed_at") else None,
            }
            orders.append(order)
        except Exception as e:
            print(f"Пропущен заказ: {e}")
    return orders


def save(path: str, orders: List[Order]):
    data = {
        "orders": [
            {
                "id": order["id"],
                "title": order["title"],
                "amount": order["amount"],
                "email": order["email"],
                "status": order["status"],
                "tags": list(order["tags"]) if order["tags"] else [],
                "created_at": order["created_at"].isoformat() if order["created_at"] else None,
                "due": order["due"].isoformat() if order["due"] else None,
                "closed_at": order["closed_at"].isoformat() if order["closed_at"] else None,
            }
            for order in orders
        ]
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
