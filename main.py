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

        button1 = Button(self, text="1", padx=60, pady=20, command=lambda: self.button_click(1))
        button2 = Button(self, text="2", padx=60, pady=20, command=lambda: self.button_click(2))
        button3 = Button(self, text="3", padx=60, pady=20, command=lambda: self.button_click(3))
        button4 = Button(self, text="4", padx=60, pady=20, command=lambda: self.button_click(4))
        button5 = Button(self, text="5", padx=60, pady=20, command=lambda: self.button_click(5))
        button6 = Button(self, text="6", padx=60, pady=20, command=lambda: self.button_click(6))
        button7 = Button(self, text="7", padx=60, pady=20, command=lambda: self.button_click(7))
        button8 = Button(self, text="8", padx=60, pady=20, command=lambda: self.button_click(8))
        button9 = Button(self, text="9", padx=60, pady=20, command=lambda: self.button_click(9))
        button0 = Button(self, text="0", padx=60, pady=20, command=lambda: self.button_click(0))

        button_add = Button(self, text="+", padx=58, pady=20, command=self.click_addition)
        button_subtract = Button(self, text="-", padx=61, pady=20, command=self.click_subtraction)
        button_multiply = Button(self, text="*", padx=61, pady=20, command=self.click_multiplication)
        button_divide = Button(self, text="/", padx=62, pady=20, command=self.click_division)
        button_exponentiation = Button(self, text="^", padx=58, pady=20, command=self.click_exponentiation)
        button_root = Button(self, text="√", padx=60, pady=20, command=self.click_root)
        button_clear = Button(self, text="Clear", padx=47, pady=20, command=self.click_clearing)
        button_equal = Button(self, text="=", padx=58, pady=20, command=self.calculation)

        button1.grid(row=3, column=0)
        button2.grid(row=3, column=1)
        button3.grid(row=3, column=2)
        button4.grid(row=2, column=0)
        button5.grid(row=2, column=1)
        button6.grid(row=2, column=2)
        button7.grid(row=1, column=0)
        button8.grid(row=1, column=1)
        button9.grid(row=1, column=2)
        button0.grid(row=4, column=0)

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

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()