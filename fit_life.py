def generate_report(user_name, user_age, bmi, water_l):
    """Возвращает отформатированный отчёт с данными пользователя."""
    # Разбиваем длинную строку на части внутри скобок.
    report = (
        f"Report for user: {user_name}, ({user_age} y.o.)\n"
        f"Your BMI: {bmi}\n"
        f"Recommended water: {water_l} L per day\n"
        f"\nCalculation finished. Be healthy!"
    )
    return report


if __name__ == "__main__":
    user_name = input('Name: ').strip()

    age_raw = input('Age: ').strip()
    user_age = int(age_raw)

    weight_raw = input('Weight: ').strip()
    user_weight = float(weight_raw)

    height_raw = input('Height: ').strip()
    user_height = float(height_raw)

    if user_height <= 0:
        raise ValueError("Рост должен быть больше нуля!")

    bmi = round(user_weight / (user_height ** 2), 1)
    water_ml = user_weight * 30
    water_l = round(water_ml / 1000, 3)

    # Используем f-строку
    print(
        f"Report for user: {user_name}, ({user_age} y.o.)\n"
        f"Your BMI: {bmi}\n"
        f"Recommended water: {water_l} L per day\n"
        f"\nCalculation finished. Be healthy!",
        flush=True
    )
