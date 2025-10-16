import os
import csv

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'data.csv')

data_2021 = {}
data_2022 = {}

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader) 

    for row in reader:
        country = row[1].strip() 
        try:
            value_2021 = row[2].strip()
            value_2022 = row[3].strip()
            # Проверяем, что данные не пустые или некорректные
            if value_2021 not in ['..']:  
                if country not in data_2021:
                    data_2021[country] = {}
                data_2021[country][row[0]] = value_2021  

            if value_2022 not in ['..']:  
                if country not in data_2022:
                    data_2022[country] = {}
                data_2022[country][row[0]] = value_2022  

        except ValueError:
            continue  # Пропускаем строки с ошибками в данных

# Выводим все данные за 2021 год
print("\nВсе данные за 2021 год:")
for country, indicators in data_2021.items():
    print(f"{country}: {indicators}")

# Выводим все данные за 2022 год
print("\nВсе данные за 2022 год:")
for country, indicators in data_2022.items():
    print(f"{country}: {indicators}")

# Нахождение максимума и минимума по иммунизации за 2021 год
max_bcg_2021_value = -1  
min_bcg_2021_value = float('inf')  
max_bcg_2021_country = ""
min_bcg_2021_country = ""

# Проходим по всем странам в data_2021
for country in data_2021:
    value = data_2021[country].get("Immunization, BCG (% of one-year-old children)", None)
    
    # Если значение есть и оно корректное
    if value:
        value = float(value)  

        # Проверка на максимальное значение
        if value > max_bcg_2021_value:
            max_bcg_2021_value = value
            max_bcg_2021_country = country

        # Проверка на минимальное значение
        if value < min_bcg_2021_value:
            min_bcg_2021_value = value
            min_bcg_2021_country = country

# Нахождение максимума и минимума по иммунизации за 2022 год
max_bcg_2022_value = -1  
min_bcg_2022_value = float('inf') 
max_bcg_2022_country = ""
min_bcg_2022_country = ""

for country in data_2022:
    value = data_2022[country].get("Immunization, BCG (% of one-year-old children)", None)

    if value:
        value = float(value)  

        # Проверка на максимальное значение
        if value > max_bcg_2022_value:
            max_bcg_2022_value = value
            max_bcg_2022_country = country

        # Проверка на минимальное значение
        if value < min_bcg_2022_value:
            min_bcg_2022_value = value
            min_bcg_2022_country = country

# Выводим результаты по иммунизации
print(f"\n=== ИММУНИЗАЦИЯ БЦЖ ===")
print(f"Максимум по иммунизации BCG за 2021 год: {max_bcg_2021_country} с значением {max_bcg_2021_value}")
print(f"Минимум по иммунизации BCG за 2021 год: {min_bcg_2021_country} с значением {min_bcg_2021_value}")
print(f"Максимум по иммунизации BCG за 2022 год: {max_bcg_2022_country} с значением {max_bcg_2022_value}")
print(f"Минимум по иммунизации BCG за 2022 год: {min_bcg_2022_country} с значением {min_bcg_2022_value}")

print(f"\n=== ЗАБОЛЕВАЕМОСТЬ ТУБЕРКУЛЕЗОМ ===")

# Для 2021 года
max_incidence_2021_value = -1
min_incidence_2021_value = float('inf')
max_incidence_2021_country = ""
min_incidence_2021_country = ""

for country in data_2021:
    value = data_2021[country].get("Incidence of tuberculosis (per 100,000 people)", None)
    if value:
        value = float(value)
        if value > max_incidence_2021_value:
            max_incidence_2021_value = value
            max_incidence_2021_country = country
        if value < min_incidence_2021_value:
            min_incidence_2021_value = value
            min_incidence_2021_country = country

print(f"Максимум заболеваемости за 2021 год: {max_incidence_2021_country} с значением {max_incidence_2021_value}")
print(f"Минимум заболеваемости за 2021 год: {min_incidence_2021_country} с значением {min_incidence_2021_value}")

# Для 2022 года
max_incidence_2022_value = -1
min_incidence_2022_value = float('inf')
max_incidence_2022_country = ""
min_incidence_2022_country = ""

for country in data_2022:
    value = data_2022[country].get("Incidence of tuberculosis (per 100,000 people)", None)
    if value:
        value = float(value)
        if value > max_incidence_2022_value:
            max_incidence_2022_value = value
            max_incidence_2022_country = country
        if value < min_incidence_2022_value:
            min_incidence_2022_value = value
            min_incidence_2022_country = country

print(f"Максимум заболеваемости за 2022 год: {max_incidence_2022_country} с значением {max_incidence_2022_value}")
print(f"Минимум заболеваемости за 2022 год: {min_incidence_2022_country} с значением {min_incidence_2022_value}")

print(f"\n=== СМЕРТНОСТЬ ОТ ТУБЕРКУЛЕЗА ===")

# Для 2021 года
max_death_2021_value = -1
min_death_2021_value = float('inf')
max_death_2021_country = ""
min_death_2021_country = ""

for country in data_2021:
    value = data_2021[country].get("Tuberculosis death rate (per 100,000 people)", None)
    if value:
        value = float(value)
        if value > max_death_2021_value:
            max_death_2021_value = value
            max_death_2021_country = country
        if value < min_death_2021_value:
            min_death_2021_value = value
            min_death_2021_country = country

print(f"Максимум смертности за 2021 год: {max_death_2021_country} с значением {max_death_2021_value}")
print(f"Минимум смертности за 2021 год: {min_death_2021_country} с значением {min_death_2021_value}")

# Для 2022 года
max_death_2022_value = -1
min_death_2022_value = float('inf')
max_death_2022_country = ""
min_death_2022_country = ""

for country in data_2022:
    value = data_2022[country].get("Tuberculosis death rate (per 100,000 people)", None)
    if value:
        value = float(value)
        if value > max_death_2022_value:
            max_death_2022_value = value
            max_death_2022_country = country
        if value < min_death_2022_value:
            min_death_2022_value = value
            min_death_2022_country = country

print(f"Максимум смертности за 2022 год: {max_death_2022_country} с значением {max_death_2022_value}")
print(f"Минимум смертности за 2022 год: {min_death_2022_country} с значением {min_death_2022_value}")

#  Сортируем данные по заболеваемости туберкулезом за 2021 и 2022 годы
data_2021_incidence = [(country, float(data_2021[country].get("Incidence of tuberculosis (per 100,000 people)", 0)))
                       for country in data_2021]

data_2022_incidence = [(country, float(data_2022[country].get("Incidence of tuberculosis (per 100,000 people)", 0)))
                       for country in data_2022]

for i in range(len(data_2021_incidence)):
    for j in range(i + 1, len(data_2021_incidence)):
        if data_2021_incidence[i][1] < data_2021_incidence[j][1]:
            data_2021_incidence[i], data_2021_incidence[j] = data_2021_incidence[j], data_2021_incidence[i]

for i in range(len(data_2022_incidence)):
    for j in range(i + 1, len(data_2022_incidence)):
        if data_2022_incidence[i][1] < data_2022_incidence[j][1]:
            data_2022_incidence[i], data_2022_incidence[j] = data_2022_incidence[j], data_2022_incidence[i]

# Выводим рейтинг по заболеваемости за 2021 год
print("\n=== РЕЙТИНГ ПО ЗАБОЛЕВАЕМОСТИ ТУБЕРКУЛЕЗОМ ===")
print("\nРейтинг по заболеваемости туберкулеза за 2021 год:")
rank = 1
for country, incidence_rate in data_2021_incidence:
    print(f"{rank}. {country}: {incidence_rate} случаев на 100,000 людей")
    rank += 1

# Выводим рейтинг по заболеваемости за 2022 год
print("\nРейтинг по заболеваемости туберкулеза за 2022 год:")
rank = 1
for country, incidence_rate in data_2022_incidence:
    print(f"{rank}. {country}: {incidence_rate} случаев на 100,000 людей")
    rank += 1


# Сортируем данные по смертности от туберкулеза за 2021 и 2022 годы
data_2021_death_rate = [(country, float(data_2021[country].get("Tuberculosis death rate (per 100,000 people)", 0)))
                        for country in data_2021]

data_2022_death_rate = [(country, float(data_2022[country].get("Tuberculosis death rate (per 100,000 people)", 0)))
                        for country in data_2022]

for i in range(len(data_2021_death_rate)):
    for j in range(i + 1, len(data_2021_death_rate)):
        if data_2021_death_rate[i][1] < data_2021_death_rate[j][1]:
            data_2021_death_rate[i], data_2021_death_rate[j] = data_2021_death_rate[j], data_2021_death_rate[i]

for i in range(len(data_2022_death_rate)):
    for j in range(i + 1, len(data_2022_death_rate)):
        if data_2022_death_rate[i][1] < data_2022_death_rate[j][1]:
            data_2022_death_rate[i], data_2022_death_rate[j] = data_2022_death_rate[j], data_2022_death_rate[i]

# Выводим рейтинг по смертности за 2021 год
print("\n=== РЕЙТИНГ ПО СМЕРТНОСТИ ОТ ТУБЕРКУЛЕЗА ===")
print("\nРейтинг по смертности от туберкулеза за 2021 год:")
rank = 1
for country, death_rate in data_2021_death_rate:
    print(f"{rank}. {country}: {death_rate} случаев на 100,000 людей")
    rank += 1

# Выводим рейтинг по смертности за 2022 год
print("\nРейтинг по смертности от туберкулеза за 2022 год:")
rank = 1
for country, death_rate in data_2022_death_rate:
    print(f"{rank}. {country}: {death_rate} случаев на 100,000 людей")
    rank += 1

print("\n=== ИЗМЕНЕНИЯ ПОКАЗАТЕЛЕЙ (2021 → 2022) ===")

# Расчет средних значений по обнаружению случаев туберкулеза
print("\n" + "=" * 60)
print("СРЕДНИЕ ЗНАЧЕНИЯ ПО УРОВНЮ ОБНАРУЖЕНИЯ СЛУЧАЕВ ТУБЕРКУЛЕЗА")
print("=" * 60)

# Собираем данные по обнаружению случаев туберкулеза за 2021 год
detection_2021_values = []
for country in data_2021:
    value = data_2021[country].get("Tuberculosis case detection rate (%, all forms)", None)
    if value:
        try:
            detection_2021_values.append(float(value))
        except ValueError:
            continue

# Собираем данные по обнаружению случаев туберкулеза за 2022 год
detection_2022_values = []
for country in data_2022:
    value = data_2022[country].get("Tuberculosis case detection rate (%, all forms)", None)
    if value:
        try:
            detection_2022_values.append(float(value))
        except ValueError:
            continue

# Вычисляем и выводим средние значения
if detection_2021_values:
    avg_2021 = sum(detection_2021_values) / len(detection_2021_values)
    print(f"Среднее значение за 2021 год: {avg_2021:.1f}%")
else:
    print("Нет данных по обнаружению случаев туберкулеза за 2021 год")

if detection_2022_values:
    avg_2022 = sum(detection_2022_values) / len(detection_2022_values)
    print(f"Среднее значение за 2022 год: {avg_2022:.1f}%")
else:
    print("Нет данных по обнаружению случаев туберкулеза за 2022 год")

# Анализ изменений по заболеваемости
print("\nИзменения заболеваемости туберкулезом:")
for country in data_2021:
    if country in data_2022:
        incidence_2021 = data_2021[country].get("Incidence of tuberculosis (per 100,000 people)")
        incidence_2022 = data_2022[country].get("Incidence of tuberculosis (per 100,000 people)")
        if incidence_2021 and incidence_2022:
            change = float(incidence_2022) - float(incidence_2021)
            trend = "↑ увеличение" if change > 0 else "↓ снижение" if change < 0 else "→ без изменений"
            print(f"{country}: {incidence_2021} → {incidence_2022} ({trend}, изменение: {change:+.1f})")

# Анализ изменений по смертности
print("\nИзменения смертности от туберкулеза:")
for country in data_2021:
    if country in data_2022:
        death_2021 = data_2021[country].get("Tuberculosis death rate (per 100,000 people)")
        death_2022 = data_2022[country].get("Tuberculosis death rate (per 100,000 people)")
        if death_2021 and death_2022:
            change = float(death_2022) - float(death_2021)
            trend = "↑ увеличение" if change > 0 else "↓ снижение" if change < 0 else "→ без изменений"
            print(f"{country}: {death_2021} → {death_2022} ({trend}, изменение: {change:+.2f})")

# Анализ изменений по успешности лечения
print("\n" + "=" * 60)
print("ИЗМЕНЕНИЯ ПО ПОКАЗАТЕЛЮ УСПЕШНОСТИ ЛЕЧЕНИЯ (2021 → 2022)")
print("=" * 60)

# Собираем и сравниваем данные по успешности лечения
for country in data_2021:
    if country in data_2022:
        value_2021 = data_2021[country].get("Tuberculosis treatment success rate (% of new cases)", None)
        value_2022 = data_2022[country].get("Tuberculosis treatment success rate (% of new cases)", None)

        if value_2021 and value_2022:
            try:
                val_2021_float = float(value_2021)
                val_2022_float = float(value_2022)
                change = val_2022_float - val_2021_float
                trend = "↑ рост" if change > 0 else "↓ снижение" if change < 0 else "→ без изменений"
                print(f"{country}: {val_2021_float}% → {val_2022_float}% ({change:+.1f}%) {trend}")
            except ValueError:
                continue
