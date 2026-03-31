price = float(input("Введите стоимость товара: "))
discount_percent = float(input("Введите процент скидки: "))

discount_value = price * (discount_percent / 100)
price_with_discount = price - discount_value

print(f"Цена со скидкой: {price_with_discount}")