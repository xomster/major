def power_a3(a):
    """Повертає третій ступінь числа a."""
    return a ** 3

def power_of_5(in_list):
    """Повертає список із п'яти чисел, зведених у третій ступінь."""
    return [power_a3(a) for a in in_list]

def task1():
    """Запитує у користувача п'ять чисел, виводить їх третій ступінь."""
    in_data = []
    for i in range(5):
        number = float(input("Введіть число: "))
        in_data.append(number)
    out_data = power_of_5(in_data)  
    print("Числа, зведені на третій ступінь:", out_data)


if __name__ == "__main__":
    task1()



import numpy as np

def calculate_matrix(matrix):
    # Обчислюємо суму елементів по рядках
    row_sums = np.sum(matrix, axis=1)
    # Обчислюємо добуток елементів по рядках
    row_products = np.prod(matrix, axis=1)
    
    print("Суми елементів рядків:", row_sums)
    print("Добутки елементів рядків:", row_products)
    
    # Створюємо випадкову матрицю того ж розміру
    random_matrix = np.random.randint(1, 10, size=matrix.shape)
    
    # Обчислюємо різницю між початковою і випадковою матрицями
    result_matrix = matrix - random_matrix
    print("Різниця початкової і випадкової матриць:\n", result_matrix)
    
    return row_sums, row_products, result_matrix

def process_matrix():
    choice = input("Оберіть метод введення матриці (1 - з файлу, 2 - вручну): ")
    
    if choice == "1":
        filename = input("Введіть шлях до файлу з матрицею: ")
        try:
            # Завантажуємо матрицю з файлу
            matrix = np.loadtxt(filename, dtype=int)
        except Exception as e:
            print(f"Помилка при завантаженні файлу: {e}")
            return
    elif choice == "2":
        try:
            rows = int(input("Введіть кількість рядків матриці: "))
            cols = int(input("Введіть кількість стовпців матриці: "))
            matrix = []
            print("Введіть елементи матриці:")
            for i in range(rows):
                row = list(map(int, input(f"Рядок {i + 1}: ").split()))
                if len(row) != cols:
                    print("Кількість елементів у рядку не відповідає вказаній кількості стовпців.")
                    return
                matrix.append(row)
            matrix = np.array(matrix)
        except ValueError:
            print("Помилка: введіть коректні цілі числа.")
            return
    else:
        print("Некоректний вибір. Спробуйте ще раз.")
        return

    # Викликаємо функцію обчислення параметрів
    calculate_matrix(matrix)

# Виконуємо основну функцію
if __name__ == "__main__":
    process_matrix()
