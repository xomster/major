def task_integer11():
    """Given a three-digit number, find the sum and product of its digits."""
    try:
        num = int(input("Enter a three-digit number: "))
        print(f"You entered: {num}")  # Додаємо перевірку на введене число
        
        if num < 100 or num > 999:
            raise ValueError("The number must be three digits!")
    except ValueError as e:
        print(e)
        return  # Зупиняємо виконання, якщо є помилка
    else:
        # Витягуємо цифри
        hundreds = num // 100
        tens = (num // 10) % 10
        ones = num % 10

        # Сума та добуток цифр        
        digit_sum = hundreds + tens + ones
        digit_product = hundreds * tens * ones

        # Обчислюємо чисельник
        print(f"Sum of digits: {digit_sum}")
        print(f"Product of digits: {digit_product}")



import math

def calculate_y(x):
    try:
        # Обчислюємо чисельник
        numerator = (2 * x**2 - abs(math.sin(x)) * abs(math.tan(x)) * 2.5**math.cos(x))**(1/5)
        
        # Обчислюємо знаменник
        denominator = 0.625 + 2 * math.log2(x + 7.5)
        
        # Повний вираз
        y = numerator / denominator
        
        return y
    except ValueError:
        return " Помилка: неприпустимі значення для логарифму чи інших математичних операцій."

# Приклад використання
x = float(input("Введіть значення x: "))
result = calculate_y(x)
print(f"y = {resudef check_positive():
    try:
        # Ввод трёх целых чисел A, B, C
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))
        C = int(input("Введите число C: "))
    except ValueError:
        print("Усі значення мають бути цілими числами!")       
        return
    
        # Перевірка умови: хоча б одне із чисел позитивне    
        res = A > 0 or B > 0 or C > 0
    
        # Висновок результату
        print( res)

lt}")




