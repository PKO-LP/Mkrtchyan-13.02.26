
cars = {
    "Жигули": 200000,
    "Дэу Нексия": 400000,
    "Лада Калина": 700000,
    "Киа Рио": 1000000,
    "БМВ Х3": 1600000,
    "Мерседес S класса": 8000000
}

people = {
    "Иван": 1400000,
    "Кирилл": 800000,
    "Виктор": 600000,
    "Роман": 7000000,
    "Даниил": 2300000,
    "Настя": 3000000
}

print("Какие автомобили может позволить себе каждый:")
for person, budget in people.items():
    affordable = [car for car, price in cars.items() if price <= budget]
    print(f"{person}: {', '.join(affordable) if affordable else 'ничего'}")

print("\nКакие автомобили можно купить вскладчину (всеми вместе):")
total_budget = sum(people.values())
affordable_together = [car for car, price in cars.items() if price <= total_budget]
print(f"Все вместе могут купить: {', '.join(affordable_together) if affordable_together else 'ничего'}")