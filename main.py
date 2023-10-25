from tkinter import Tk, Entry, END, Button


class Calculator:

    def __int__(self, master):
        self.master = master
        master.title = 'Calculator'
        self.display = Entry(master, width=50, borderwidth=10)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        button1 = Button(master, text="1", padx=60, pady=20, command=lambda: self.button_click(1))
        button2 = Button(master, text="2", padx=60, pady=20, command=lambda: self.button_click(2))
        button3 = Button(master, text="3", padx=60, pady=20, command=lambda: self.button_click(3))
        button4 = Button(master, text="4", padx=60, pady=20, command=lambda: self.button_click(4))
        button5 = Button(master, text="5", padx=60, pady=20, command=lambda: self.button_click(5))
        button6 = Button(master, text="6", padx=60, pady=20, command=lambda: self.button_click(6))
        button7 = Button(master, text="7", padx=60, pady=20, command=lambda: self.button_click(7))
        button8 = Button(master, text="8", padx=60, pady=20, command=lambda: self.button_click(8))
        button9 = Button(master, text="9", padx=60, pady=20, command=lambda: self.button_click(9))
        button0 = Button(master, text="0", padx=60, pady=20, command=lambda: self.button_click(0))

        button_add = Button(master, text="+", padx=58, pady=20, command=self.click_addition)
        button_subtract = Button(master, text="-", padx=61, pady=20, command=self.click_subtraction)
        button_multiply = Button(master, text="*", padx=61, pady=20, command=self.click_multiplication)
        button_divide = Button(master, text="/", padx=62, pady=20, command=self.click_division)
        button_exponentiation = Button(master, text="^", padx=58, pady=20, command=self.click_exponentiation)
        button_root = Button(master, text="√", padx=60, pady=20, command=self.click_root)
        button_clear = Button(master, text="Clear", padx=46, pady=20, command=self.click_clearing)
        button_equal = Button(master, text="=", padx=58, pady=20, command=self.calculation)

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


root = Tk()
calculator = Calculator(root)
root.geometry('445x450+700+300')
root.resizable(False, False)
root.mainloop()