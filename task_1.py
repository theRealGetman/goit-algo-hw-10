import pulp

# Створення задачі лінійного програмування
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні, які представляють кількість вироблених одиниць Лимонаду і Фруктового соку
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Об'єктивна функція: максимізація загальної кількості вироблених продуктів
model += lemonade + fruit_juice, "Total_Production"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
model += 1 * lemonade <= 50, "Sugar_Constraint"
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Розв'язання задачі
model.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade produced: {lemonade.varValue}")
print(f"Fruit Juice produced: {fruit_juice.varValue}")
