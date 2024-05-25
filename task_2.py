import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

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

# Обчислення інтегралу аналітично за допомогою SciPy
analytical_integral, error = spi.quad(f, a, b)
print(f"Інтеграл аналітично (SciPy quad): {analytical_integral}")
print(f"Абсолютна помилка: {error}")

# Побудова графіка для візуалізації
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
