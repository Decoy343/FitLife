import subprocess
import sys

# Данные, которые подсовывает тест
input_data = "Анна\n25\n75.5\n1.8\n"

print("--- ЗАПУСК ТВОЕГО main.py ---")
print(f"Входные данные: {input_data.strip()}")
print("-" * 30)

# Запускаем твой main.py, передавая ему данные через stdin
# universal_newlines=True нужен, чтобы видеть текст, а не байты
process = subprocess.run(
    [sys.executable, "C:/Users/Пользователь/Desktop/интепрекатор/FitLife/fit_life.py"],
    input=input_data,
    text=True,
    capture_output=True
)

# Твой вывод (то, что напечатал print)
my_output = process.stdout

# Ошибки, если программа упала (красный текст)
my_errors = process.stderr

print("\n--- ВЫВОД ТВОЕЙ ПРОГРАММЫ (stdout) ---")
if my_output:
    print(my_output)
else:
    print("[ПУСТО] Программа ничего не напечатала!")

print("\n--- ОШИБКИ (stderr) ---")
if my_errors:
    print(my_errors)
else:
    print("[Нет ошибок]")

print("-" * 30)

# --- ЭТАЛОН (то, что ждёт тест) ---
# Мы считаем его сами по той же формуле, что и тест
weight = 75.5
height = 1.8
age = 25
name = "Анна"

expected_bmi = round(weight / (height ** 2), 1)
expected_water = (weight * 30) / 1000

print("\n--- ОЖИДАЕМЫЙ ВЫВОД (эталон) ---")
print()
print(f"Отчет для пользователя:{name}, ({age} г.)")
print(f"Ваш Индекс Массы Тела:{expected_bmi}")
print(f"Рекомендуемая норма воды:{expected_water} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
print("-" * 30)

# Сравнение
if my_output.strip() == f"""
Отчет для пользователя:{name}, ({age} г.)
Ваш Индекс Массы Тела:{expected_bmi}
Рекомендуемая норма воды:{expected_water} л. в день

Расчет окончен. Будьте здоровы!
""".strip():
    print("✅ ВЫВОД ПОЛНОСТЬЮ СОВПАДАЕТ!")
else:
    print("❌ ВЫВОД НЕ СОВПАДАЕТ. Сравни построчно выше!")