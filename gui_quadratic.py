import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import random
import time
import math
import cmath

matplotlib.use("TkAgg")


def sign(a):
    if a >= 0:
        return "+"
    else:
        return "-"


class QuadraticEquationGame:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x600")
        self.root.title("Quadratic Equations")

        self.label_equation = tk.Label(
            root, text="Solve for x:", font=("Helvetica", 16)
        )
        self.label_equation.pack()

        self.equation_var = tk.StringVar()
        self.equation_label = tk.Label(
            root, textvariable=self.equation_var, font=("Monaspace Neon Var", 20)
        )
        self.equation_label.pack()

        self.button_submit = tk.Button(
            root, text="Done", command=self.submit, font=("Helvetica", 18)
        )
        self.button_submit.pack()

        self.correct = tk.Button(
            root, text="Correct", command=self.display_result, font=("Helvetica", 18)
        )

        self.start_time = 0

        self.generate_equation()

    def show_eq(self, num, denom):
        tmptext = "$" + f"\\frac{num} {denom} " + "$"
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.label = tk.Label(self.frame)
        self.label.pack()
        self.fig = matplotlib.figure.Figure(figsize=(7, 4), dpi=100)
        self.wx = self.fig.add_subplot(111)

        self.wx.clear()
        self.wx.text(0.2, 0.6, tmptext, fontsize=20)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.label)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.draw()

        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)

        self.correct.pack()

    def format_numerator(self, num):
        term_1, rd = num
        radical, value = rd

        if value is not None:
            if radical:
                numerator_format = (
                    "{" + str(term_1) + "\pm" + "\sqrt{" + str(value) + "}" + "}"
                )
            else:
                numerator_format = "{" + str(term_1) + "\pm" + str(int(value)) + "}"
        elif value is None:
            numerator_format = "{" + str(term_1) + "}"
        return numerator_format

    def generate_equation(self):
        self.a = 0
        while self.a == 0:
            self.a = random.randint(-15, 15)
        self.b = random.randint(-15, 15)
        self.c = random.randint(-15, 15)

        # self.a, self.b, self.c = 1, -4, 4

        equation_str = (
            f"{self.a}x² {sign(self.b)} {abs(self.b)}x {sign(self.c)} {abs(self.c)} = 0"
        )
        self.equation_var.set(equation_str)

        self.correct_answer = self.solve_quadratic(self.a, self.b, self.c)
        self.start_time = time.time()

    def solve_quadratic(self, a, b, c):
        discriminant = b**2 - 4 * a * c

        if discriminant < 0:
            if math.sqrt(-discriminant).is_integer():
                rad_discriminant = False, complex(cmath.sqrt(discriminant))
            else:
                rad_discriminant = True, discriminant
        elif discriminant > 0:
            if math.sqrt(discriminant).is_integer():
                rad_discriminant = False, math.sqrt(discriminant)
            else:
                rad_discriminant = True, discriminant
        else:
            rad_discriminant = False, None

        # if math.gcd(2 * a, -b) > 1:
        #     print(-b)
        #     print(2 * a)
        #     b = b // math.gcd(2 * a, -b)
        #     a = (a // math.gcd(2 * a, -b)) // 2

        numerator = [-b, rad_discriminant]
        denominator = "{" + str(2 * a) + "}"

        return numerator, denominator

    def submit(self):
        num, den = self.solve_quadratic(self.a, self.b, self.c)
        self.elapsed_time = time.time() - self.start_time
        self.show_eq(self.format_numerator(num), den)

    def display_result(self):
        messagebox.showinfo(
            "Correct",
            f"Congratulations!\nElapsed Time: {self.elapsed_time:.2f} seconds.",
        )
        self.generate_equation()


if __name__ == "__main__":
    root = tk.Tk()
    game = QuadraticEquationGame(root)
    root.mainloop()
