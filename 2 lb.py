def task_if19():
    """
    Завдання 1 (If19): Дано чотири цілих числа, одне з яких відрізняється від трьох інших рівних між собою.
    Визначити порядковий номер числа, відмінного від інших.
    """
    try:
        nums = [int(input(f"Введіть число {i+1}: ")) for i in range(4)]
        if nums.count(nums[0]) == 3:
            print("Відрізняється число 4 (останнє)")
        elif nums.count(nums[1]) == 3:
            print("Відрізняється число 1 (перше)")
        elif nums.count(nums[2]) == 3:
            print("Відрізняється число 2 (друге)")
        else:
            print("Відрізняється число 3 (третє)")
    except ValueError:
        print("Помилка: Введіть ціле число!")




def is_in_yellow_area(x, y):
    
    return 0 <= x <= 1 and 0 <= y <= 1  # Задайте межі жовтої області

def task_geom_area(points):
   
    count_in_yellow_area = sum(1 for x, y in points if is_in_yellow_area(x, y))
    return count_in_yellow_area
try:
    n = int(input("Введіть кількість точок: "))  # Кількість точок
    points = []

    for i in range(n):
        x, y = map(float, input(f"Введіть координати точки {i+1} (x y): ").split())
        points.append((x, y))

    result = task_geom_area(points)
    print(f"Кількість точок, що потрапляють у жовту область: {result}")

except ValueError as e:
    print(f"Помилка: {e}")


import math

def factorial_series(epsilon=1e-5, g=1e5, max_iter=10000):
    n = 1
    total_sum = 0
    
    while n <= max_iter:
        # Обчислення чисельника (2n+1)!
        numerator = math.factorial(2 * n + 1)
        
        # Обчислення знаменника 1 * 4 * ... * (3n - 2)
        denominator = 1
        for i in range(1, n + 1):
            denominator *= (3 * i - 2)
        
        # Обчислюємо поточний член ряду
        term = numerator / denominator
        
        # Перевіряємо умови збіжності або розбіжності
        if abs(term) < epsilon:
            print(f'Ряд збігається на кроці {n}, терм: {term}')
            break
        if abs(term) > g:
            print(f'Ряд розбігається на кроці {n}, терм: {term}')
            break
            
        # Додаємо поточний член до суми
        total_sum += term
        n += 1
    
    return total_sum

# Приклад виклику функції
epsilon = 1e-10  # Можна змінити, наприклад, на 1e-20
g = 1e3         # Межа для розбіжності
result = factorial_series(epsilon, g)
print(f'Сума ряду: {result}')





from math import factorial

def calculate_series(epsilon, g, max_iter):
    n = 1
    total_sum = 0
    
    while True:
        # Обчислення терміна ряду
        numerator = factorial(2 * n + 1)
        denominator = 1
        for i in range(1, n + 1):
            denominator *= (3 * i - 2)
        term = numerator / denominator

        # Умова зупинки
        if abs(term) < epsilon:
            print(f"Ряд збігається. Сума: {total_sum}")
            break
        if abs(term) > g:
            print("Ряд розбігається.")
            break
        
        total_sum += term
        n += 1

        if n > max_iter:
            print("Достигнуто максимального числа ітерацій.")
            break

def menu():
    while True:
        print("\nМеню:")
        print("1. Обчислити суму ряду")
        print("2. Вихід")
        
        choice = input("Оберіть опцію (1-2): ")

        if choice == '1':
            epsilon = float(input("Введіть epsilon (10^-5 до 10^-20): "))
            g = float(input("Введіть g (10^2 до 10^5): "))
            max_iter = int(input("Введіть максимальну кількість ітерацій (1000 до 10000): "))
            calculate_series(epsilon, g, max_iter)
        elif choice == '2':
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір, будь ласка, спробуйте ще раз.")

# Викликаємо меню
menu()
 
