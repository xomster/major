import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt

# Глобальні змінні для даних
data_x = []
data_y = []

# Функція для обчислення мінімуму та максимуму
def calculate_min_max():
    try:
        if not data_x or not data_y:  # Перевірка на порожні масиви
            raise ValueError("Масиви даних порожні.")
        min_x, max_x = min(data_x), max(data_x)
        min_y, max_y = min(data_y), max(data_y)
        messagebox.showinfo("Результати", f"Мінімум X: {min_x}\nМаксимум X: {max_x}\nМінімум Y: {min_y}\nМаксимум Y: {max_y}")
    except Exception as e:
        messagebox.showerror("Помилка", f"Помилка: {e}")

# Функція для запису даних у файл
def save_to_file():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not file_path:
            return
        
        # Визначення роздільника залежно від варіанту
        delimiter = ';' if variant % 2 == 0 else '#'
        
        with open(file_path, "w") as f:
            for x, y in zip(data_x, data_y):
                f.write(f"{x}{delimiter} {y}\n")
        
        messagebox.showinfo("Успіх", "Дані успішно записано у файл.")
    except Exception as e:
        messagebox.showerror("Помилка", f"Помилка: {e}")

# Функція для зчитування даних з файлу
def load_from_file():
    global data_x, data_y  # Замінили nonlocal на global
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return
        
        with open(file_path, "r") as f:
            lines = f.readlines()

        delimiter = ";" if ";" in lines[0] else "#"
        data_x, data_y = [], []
        for line in lines:
            x, y = map(float, line.strip().split(delimiter))
            data_x.append(x)
            data_y.append(y)
        
        # Логування для перевірки зчитаних даних
        print("Зчитано дані:")
        print(f"data_x: {data_x}")
        print(f"data_y: {data_y}")
        
        messagebox.showinfo("Успіх", "Дані успішно зчитано.")
    except Exception as e:
        messagebox.showerror("Помилка", f"Помилка: {e}")

# Функція для побудови графіка
def plot_graph():
    try:
        if not data_x or not data_y:
            raise ValueError("Дані для графіка порожні.")
        
        plt.figure()
        plt.plot(data_x, data_y, label="Функція y(t)")
        plt.title("Графік функції")
        plt.xlabel("Час (t)")
        plt.ylabel("Значення (y)")
        plt.grid(True)
        plt.legend()
        plt.show()
    except Exception as e:
        messagebox.showerror("Помилка", f"Помилка: {e}")

# Основна функція для побудови GUI
def main():
    global variant  # Оголошуємо global для варіанту
    variant = 2  # Призначте значення варіанту

    root = tk.Tk()
    root.title("lab5_2-310CT-v02-Vozvyshaev-Alex")

    tk.Label(root, text="T (період):").grid(row=0, column=0, padx=5, pady=5)
    entry_T = tk.Entry(root)
    entry_T.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="K (коефіцієнт):").grid(row=1, column=0, padx=5, pady=5)
    entry_K = tk.Entry(root)
    entry_K.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="ξ (демпфування):").grid(row=2, column=0, padx=5, pady=5)
    entry_xi = tk.Entry(root)
    entry_xi.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text="U[0] (початкове значення):").grid(row=3, column=0, padx=5, pady=5)
    entry_U0 = tk.Entry(root)
    entry_U0.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(root, text="Зберегти у файл", command=save_to_file).grid(row=4, column=0, columnspan=2, pady=5)
    tk.Button(root, text="Зчитати з файлу", command=load_from_file).grid(row=5, column=0, columnspan=2, pady=5)
    tk.Button(root, text="Обчислити min/max", command=calculate_min_max).grid(row=6, column=0, columnspan=2, pady=5)
    tk.Button(root, text="Побудувати графік", command=plot_graph).grid(row=7, column=0, columnspan=2, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
