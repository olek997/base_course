import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Circle

# ===== НАСТРОЙКИ =====
# Параметры симуляции (берем простые числа для наглядности)
M = 3.0        # Масса звезды
G = 1.0        # Гравитационная постоянная
c = 1.0        # Скорость света

# Параметры луча
# Прицельный параметр - насколько далеко от центра проходит луч
b_values = [2.5, 3.5, 4.5, 6.0]  # Несколько разных лучей
colors = ['red', 'orange', 'green', 'blue']

# Границы графика
x_min, x_max = -12, 12
y_min, y_max = -4, 8

# ===== СОЗДАЕМ РИСУНОК =====
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

# Настраиваем внешний вид
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_xlabel('X координата')
ax.set_ylabel('Y координата')
ax.set_title('Искривление света вблизи массивной звезды')

# Рисуем звезду в центре
star = Circle((0, 0), 1.8, color='orange', alpha=0.8, label='Звезда')
ax.add_patch(star)

# Добавим свечение вокруг звезды
glow = Circle((0, 0), 2.5, color='yellow', alpha=0.2)
ax.add_patch(glow)

# ===== ФУНКЦИЯ ДЛЯ РАСЧЕТА ТРАЕКТОРИИ =====
def calculate_ray(b):
    """
    Рассчитывает траекторию луча с заданным прицельным параметром b
    """
    # Создаем точки по оси X
    x = np.linspace(x_min, x_max, 300)
    
    # Угол отклонения (формула Эйнштейна)
    theta = 4 * G * M / (c**2 * b)
    
    # Рассчитываем Y координаты
    y = np.zeros_like(x)
    
    for i, xi in enumerate(x):
        if xi < 0:
            # Луч приближается к звезде
            y[i] = b
        else:
            # Луч удаляется от звезды - искривляется
            # Чем дальше от звезды, тем меньше искривление
            distance_effect = np.exp(-xi/4)  # Убывает с расстоянием
            y[i] = b - theta * xi * distance_effect
    
    return x, y

# ===== ПОДГОТАВЛИВАЕМ ЛУЧИ =====
rays = []
ray_data = []

for i, (b, color) in enumerate(zip(b_values, colors)):
    # Рассчитываем траекторию
    x, y = calculate_ray(b)
    ray_data.append((x, y))
    
    # Создаем линию (пока пустую)
    ray, = ax.plot([], [], color=color, linewidth=2, label=f'b = {b}')
    rays.append(ray)

# Добавляем легенду
ax.legend(loc='upper right')

# Добавляем текстовую информацию
info_text = ax.text(0.02, 0.98, '', transform=ax.transAxes,
                    verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# ===== ФУНКЦИИ АНИМАЦИИ =====
def init():
    """Начальное состояние"""
    for ray in rays:
        ray.set_data([], [])
    info_text.set_text('')
    return rays + [info_text]

def animate(frame):
    """
    Обновление для каждого кадра
    frame - номер кадра (0 до 50)
    """
    # Прогресс анимации (от 0 до 1)
    progress = frame / 50
    
    # До какой координаты X показываем лучи
    max_x = x_min + (x_max - x_min) * progress
    
    # Обновляем каждый луч
    for i, (ray, (x, y)) in enumerate(zip(rays, ray_data)):
        # Берем только точки до текущего max_x
        mask = x <= max_x
        ray.set_data(x[mask], y[mask])
    
    # Обновляем информационный текст
    info = f"Кадр: {frame}/50\n"
    info += f"Прогресс: {progress*100:.0f}%\n\n"
    
    for i, b in enumerate(b_values):
        theta = 4 * G * M / (c**2 * b)
        info += f"b={b:.1f}: {np.degrees(theta):.1f}°\n"
    
    info_text.set_text(info)
    
    return rays + [info_text]

# ===== ЗАПУСК =====
print("Создаю анимацию...")

# Создаем анимацию
anim = FuncAnimation(fig, animate, init_func=init, 
                     frames=51, interval=100, blit=True)

# Сохраняем в GIF
writer = PillowWriter(fps=10)
anim.save('light_bending.gif', writer=writer)
print("Анимация сохранена как 'light_bending.gif'")

# Показываем
plt.show()

# ===== ВЫВОДИМ ИНФОРМАЦИЮ =====
print("\n" + "="*40)
print("ИНФОРМАЦИЯ О СИМУЛЯЦИИ")
print("="*40)
print("Что показывает анимация:")
print("1. Лучи света искривляются при прохождении мимо звезды")
print("2. Чем ближе луч к звезде (меньше b), тем сильнее искривление")
print("3. Формула отклонения: θ = 4GM/(c²b)")
print("\nРассчитанные углы:")
for b in b_values:
    theta = 4 * G * M / (c**2 * b)
    print(f"b = {b:.1f}: θ = {np.degrees(theta):.2f} градусов")
print("="*40)