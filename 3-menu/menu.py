category: str = input("Выберите категорию (напиток, суп, десерт): ").lower()

if category == "напиток":
    juice: str = input("Выберите напиток (чай, кофе, сок): ").lower()
    match juice:
        case "чай":
            print("Стоимость: 100")
        case "кофе":
            print("Стоимость: 200")
        case "сок":
            print("Стоимость: 300")
        case _:
            print("Введенный Вами напиток отсутствует")
elif category == "суп":
    soup: str = input("Выберите суп (борщ, щи, суп-пюре): ").lower()
    match soup:
        case "борщ":
            print("Стоимость: 400")
        case "щи":
            print("Стоимость: 500")
        case "суп-пюре":
            print("Стоимость: 600")
        case _:
            print("Введенный Вами суп отсутствует")
elif category == "десерт":
    dessert: str = input("Выберите десерт (торт, мороженое, фрукты): ").lower()
    match dessert:
        case "торт":
            print("Стоимость: 700")
        case "мороженое":
            print("Стоимость: 800")
        case "фрукты":
            print("Стоимость: 900")
        case _:
            print("Введенный Вами десерт отсутствует")
else:
    print("Вы выбрали несуществующую категорию меню")

