def generate_report(user_name, user_age, bmi, water_l):
    report = f"""Отчет для пользователя: {user_name}, ({user_age} г.)
Ваш Индекс Массы Тела: {bmi}
Рекомендуемая норма воды: {water_l} л. в день

Расчет окончен. Будьте здоровы!"""
    return report


if __name__ == "__main__":
    # Сбор данных
    print('Здравствуте, добро пожаловать в FitLifeBot.')
    user_name = input('Введите имя:')
    user_age = int(input('Введите возраст:'))
    user_weight = float(input('Введите вес:'))
    user_height = float(input('Введите рост:'))

    # расчёты
    bmi = round(user_weight / (user_height ** 2), 1)
    water_ml = user_weight * 30
    water_l = round(water_ml / 1000, 3)

    # ---ВЫВОД
    final_report = generate_report(user_name, user_age, bmi, water_l)


    print(f"{final_report}")
    