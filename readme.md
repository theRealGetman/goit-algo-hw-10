# Обчислення визначеного інтеграла

## Опис завдання

Задача полягає в обчисленні визначеного інтеграла функції f(x) = x^2 на інтервалі [0, 2] методом Монте-Карло та порівняння отриманого результату з аналітичним розрахунком інтеграла за допомогою функції `quad` з бібліотеки SciPy.

## Метод Монте-Карло

Метод Монте-Карло використовує випадкове вибіркове значення з інтервалу інтеграції та обчислює середнє значення функції, помножене на довжину інтервалу.

### Реалізація методу Монте-Карло:

```python
import numpy as np

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Реалізація методу Монте-Карло для обчислення інтегралу
def monte_carlo_integral(func, a, b, num_samples=10000):
    x_samples = np.random.uniform(a, b, num_samples)
    y_samples = func(x_samples)
    integral = (b - a) * np.mean(y_samples)
    return integral

# Обчислення інтегралу методом Монте-Карло
mc_integral = monte_carlo_integral(f, a, b)
print(f"Інтеграл методом Монте-Карло: {mc_integral}")
```

### Результат:
Інтеграл методом Монте-Карло: 2.682597

## Аналітичне обчислення за допомогою SciPy

Функція quad з бібліотеки SciPy обчислює визначений інтеграл за допомогою чисельного інтегрування.

```python
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Обчислення інтегралу за допомогою SciPy
result, error = spi.quad(f, a, b)
print("Інтеграл аналітично (SciPy quad):", result)
print("Абсолютна помилка:", error)

```

### Результат:
Інтеграл аналітично (SciPy quad): 2.666666666666667

Абсолютна помилка: 2.960594732333751e-14

## Висновки

Метод Монте-Карло дав результат 2.682597, що дуже близько до аналітичного значення 2.666666666666667, обчисленого за допомогою функції quad. Різниця між цими значеннями є невеликою, що підтверджує ефективність методу Монте-Карло для даної задачі. Однак, аналітичний метод є більш точним і швидким для цього конкретного випадку.

Загалом, метод Монте-Карло є корисним для випадків, коли аналітичне обчислення є складним або неможливим, але потребує великої кількості вибірок для досягнення високої точності.