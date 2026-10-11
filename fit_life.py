print('Добро пожаловать')
# узнаем имя и возвраст
user_name = input('Как вас зовут?')
user_age = input('Какой ваш возвраст?')
age_int = int(user_age)
#узнаем вес и рост пользователя 
user_weight = float(input('Какой ваш вес (в кг)?'))
user_height = float(input('Какой ваш рост(в метрах)?'))
# расчёт индекса массы тела
bmi = round(user_weight / (user_height ** 2),2)

# расчёт нормы воды в день
water_ml = user_weight * 30
water_l = water_ml / 1000

print()
print(f'Отчет для пользователя:{user_name},({user_age} г.)')
print(f'Ваш Индекс Массы Тела:{bmi}')
print(f'Рекомендуемая норма воды:{water_l} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')