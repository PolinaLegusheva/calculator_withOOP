import tkinter as tk
from tkinter import ttk, END, Button

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('445x450+700+300')
        self.resizable(False, False)
        self.display = ttk.Entry(self, width=50)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        for i in range(0, 10):
            button = Button(self, text=str(i), padx=60, pady=20, command=lambda x=i: self.button_click(x))
            button.grid(row=i//3+1, column=i%3)

        button_add = Button(self, text="+", padx=58, pady=20, command=self.click_addition)
        button_subtract = Button(self, text="-", padx=61, pady=20, command=self.click_subtraction)
        button_multiply = Button(self, text="*", padx=61, pady=20, command=self.click_multiplication)
        button_divide = Button(self, text="/", padx=62, pady=20, command=self.click_division)
        button_exponentiation = Button(self, text="^", padx=58, pady=20, command=self.click_exponentiation)
        button_root = Button(self, text="√", padx=60, pady=20, command=self.click_root)
        button_clear = Button(self, text="Clear", padx=47, pady=20, command=self.click_clearing)
        button_equal = Button(self, text="=", padx=58, pady=20, command=self.calculation)

        button_add.grid(row=5, column=0)
        button_subtract.grid(row=6, column=0)
        button_multiply.grid(row=6, column=1)
        button_divide.grid(row=4, column=1)
        button_root.grid(row=5, column=1)
        button_exponentiation.grid(row=5, column=2)
        button_clear.grid(row=6, column=2)
        button_equal.grid(row=4, column=2)

        self.first_number = None
        self.second_number = None
        self.operation = None
        self.result = None

    def button_click(self, number):
        current_number = self.display.get()
        self.display.delete(0, END)
        self.display.insert(0, str(current_number)+str(number))

    def click_addition(self):
        self.first_number = float(self.display.get())
        self.operation = "+"
        self.display.delete(0, END)

    def click_subtraction(self):
        self.first_number = float(self.display.get())
        self.operation = "-"
        self.display.delete(0, END)

    def click_multiplication(self):
        self.first_number = float(self.display.get())
        self.operation = "*"
        self.display.delete(0, END)

    def click_division(self):
        self.first_number = float(self.display.get())
        self.operation = "/"
        self.display.delete(0, END)

    def click_exponentiation(self):
        self.first_number = float(self.display.get())
        self.operation = "^"
        self.display.delete(0, END)

    def click_root(self):
        self.first_number = float(self.display.get())
        self.operation = "√"
        self.display.delete(0, END)

    def click_clearing(self):
        self.display.delete(0, END)
        self.first_number = None
        self.operation = None
        self.second_number = None
        self.result = None

    def calculation(self):
        if self.operation == "+":
            self.second_number = float(self.display.get())
            self.result = self.first_number + self.second_number
        elif self.operation == "-":
            self.second_number = float(self.display.get())
            self.result = self.first_number - self.second_number
        elif self.operation == "*":
            self.second_number = float(self.display.get())
            self.result = self.first_number * self.second_number
        elif self.operation == "/":
            self.second_number = float(self.display.get())
            if self.second_number == 0:
                self.display.insert(0, 'Error')
            else:
                self.result = self.first_number / self.second_number
        elif self.operation == "^":
            self.second_number = float(self.display.get())
            self.result = self.first_number ** self.second_number
        elif self.operation == "√":
            self.second_number = float(self.display.get())
            self.result = self.first_number ** (1/self.second_number)

        if self.result is not None:
            self.display.delete(0, END)
            self.display.insert(0, str(self.result))
            self.first_number = None
            self.second_number = None
            self.operation = None
            self.result = None
