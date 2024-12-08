import tkinter as tk
from tkinter import messagebox

def TrianglePS(a):

    if a <= 0:
        raise ValueError("Сторона трикутника має бути додатною !!!!!!!!")
    perimeter = 3 * a
    area = (a ** 2 * (3 ** 0.5)) / 4
    return perimeter, area

class TriangleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор 5лб")

        # Елементи інтерфейсу
        self.label = tk.Label(root, text="Введіть сторону трикутника")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.calculate_button = tk.Button(root, text="Обчислити", command=self.calculate)
        self.calculate_button.pack(pady=5)

        self.result_label = tk.Label(root, text="Результати виходят тута :)")
        self.result_label.pack(pady=5)

    def calculate(self):
        try:
            a = float(self.entry.get())
            perimeter, area = TrianglePS(a)
            result_text = f"Периметр: {perimeter:.2f}\nПлоща: {area:.2f}"
            self.result_label.config(text=result_text)
        except ValueError as e:
            messagebox.showerror("Помилка", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = TriangleApp(root)
    root.mainloop()
