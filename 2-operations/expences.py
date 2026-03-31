food = float(input("Введите Ваши траты за еду: "))
transport = float(input("Введите Ваши траты на транспорт: "))
entertainment = float(input("Введите Ваши траты на развлечения: "))

total_amount = food + transport + entertainment
avg_value = total_amount / 3

print(f"Общая сумма Ваших трат: {total_amount}")
print(f"Средняя сумма Ваших трат: {avg_value}")
