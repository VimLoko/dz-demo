# main.py
import argparse
from datetime import datetime
from orders import (
    create_order, list_orders, print_orders_table, edit_order,
    remove_order, manage_tags, set_status, ORDERS_STORAGE
)
import storage


def main():
    parser = argparse.ArgumentParser(description="Управление заказами")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list
    list_parser = subparsers.add_parser("list", help="Показать заказы")
    list_parser.add_argument(
        "--overdue", action="store_true", help="Только просроченные")
    list_parser.add_argument("--tag", type=str, help="Фильтр по тегу")
    list_parser.add_argument("--limit", type=int, help="Максимум записей")

    # add
    add_parser = subparsers.add_parser("add", help="Добавить заказ")
    add_parser.add_argument("--title", required=True)
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--email", required=True)
    add_parser.add_argument(
        "--due", type=str, help="ISO дата, например 2025-12-31T23:59")
    add_parser.add_argument(
        "--tags", type=str, help="Теги через запятую, например a,b,c")

    # remove
    remove_parser = subparsers.add_parser("remove", help="Удалить заказ")
    remove_parser.add_argument("--id", type=int, required=True)

    # edit
    edit_parser = subparsers.add_parser(
        "edit", help="Редактировать заказ (частично)")
    edit_parser.add_argument("--id", type=int, required=True)
    edit_parser.add_argument("--title")
    edit_parser.add_argument("--amount", type=float)
    edit_parser.add_argument("--email")
    edit_parser.add_argument("--due", type=str)

    # tags
    tags_parser = subparsers.add_parser("tags", help="Управление тегами")
    tags_parser.add_argument("--id", type=int, required=True)
    tags_parser.add_argument(
        "--add", type=str, help="Добавить теги через запятую")
    tags_parser.add_argument("--remove", type=str,
                             help="Удалить теги через запятую")

    # status
    status_parser = subparsers.add_parser("status", help="Изменить статус")
    status_parser.add_argument("--id", type=int, required=True)
    status_parser.add_argument(
        "status", choices=["new", "in_progress", "done", "cancelled"])

    args = parser.parse_args()

    # загрузка данных при старте
    ORDERS_STORAGE[:] = storage.load("orders.json")

    try:
        if args.command == "list":
            orders = list_orders(overdue=args.overdue,
                                 tag=args.tag, limit=args.limit)
            print_orders_table(orders)
        elif args.command == "add":
            due = datetime.fromisoformat(args.due) if args.due else None
            tags = set(args.tags.split(",")) if args.tags else None
            # генерируем id (максимальный +1)
            new_id = max((o["id"] for o in ORDERS_STORAGE), default=0) + 1
            create_order(new_id, args.title, args.amount, args.email,
                         due=due, tags=tags, created_at=datetime.now())
            print(f"Заказ {new_id} добавлен")
        elif args.command == "remove":
            remove_order(args.id)
            print(f"Заказ {args.id} удалён")
        elif args.command == "edit":
            updates = {}
            if args.title is not None:
                updates["title"] = args.title
            if args.amount is not None:
                updates["amount"] = args.amount
            if args.email is not None:
                updates["email"] = args.email
            if args.due is not None:
                updates["due"] = datetime.fromisoformat(args.due)
            if updates:
                edit_order(args.id, **updates)
                print(f"Заказ {args.id} обновлён")
            else:
                print("Ничего не передано для изменения")
        elif args.command == "tags":
            add_tags = args.add.split(",") if args.add else None
            remove_tags = args.remove.split(",") if args.remove else None
            manage_tags(args.id, add=add_tags, remove=remove_tags)
            print(f"Теги заказа {args.id} обновлены")
        elif args.command == "status":
            set_status(args.id, args.status)
            print(f"Статус заказа {args.id} изменён на {args.status}")
    except Exception as e:
        print(f"Ошибка: {e}")

    # сохранение после изменений
    storage.save("orders.json", ORDERS_STORAGE)


if __name__ == "__main__":
    main()
