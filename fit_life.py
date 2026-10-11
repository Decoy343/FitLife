# узнаем имя
name = input()

# узнаем возраст
age = input()
age_int = int(age)

# узнаем вес
weight_str = input()
weight = float(weight_str)

# узнаем рост
height_str = input()
height = float(height_str)

# расчёт индекса массы тела
bmi = round(weight / (height ** 2), 1)

# расчёт нормы воды в день
water_l = (weight * 30) / 1000

# ---ВЫВОД
print(f'Отчет для пользователя:{name}, ({age_int} г.)')
print(f'Ваш Индекс Массы Тела:{bmi}')
print(f'Рекомендуемая норма воды:{water_l} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')
