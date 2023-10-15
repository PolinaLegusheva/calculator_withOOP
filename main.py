from tkinter import *

def button_click(number):
    current_number = display.get()
    display.delete(0, END)
    display.insert(0, str(current_number)+str(number))

def click_addition():
    global first_number
    global operation
    first_number = float(display.get())
    operation = "+"
    display.delete(0, END)

def click_subtraction():
    global first_number
    global operation
    first_number = float(display.get())
    operation = "-"
    display.delete(0, END)

def click_multiplication():
    global first_number
    global operation
    first_number = float(display.get())
    operation = "*"
    display.delete(0, END)

def click_division():
    global first_number
    global operation
    first_number = float(display.get())
    operation = "/"
    display.delete(0, END)

def click_exponentiation():
    global first_number
    global operation
    first_number = float(display.get())
    operation = "^"
    display.delete(0, END)

def click_root():
    global first_number
    global operation
    first_number = float(display.get())
    operation = "√"
    display.delete(0, END)

def click_clearing():
    display.delete(0, END)
    global first_number
    global operation
    global second_number
    global result
    first_number = None
    operation = None
    second_number = None
    result = None

def calculation():
    global first_number
    global operation
    global second_number
    global result
    if operation == "+":
        second_number = float(display.get())
        result = first_number + second_number
    elif operation == "-":
        second_number = float(display.get())
        result = first_number - second_number
    elif operation == "*":
        second_number = float(display.get())
        result = first_number * second_number
    elif operation == "/":
        second_number = float(display.get())
        if second_number == 0:
            display.insert(0, 'Error')
        else:
            result = first_number / second_number
    elif operation == "^":
        second_number = float(display.get())
        result = first_number ** second_number
    elif operation == "√":
        second_number = float(display.get())
        result = first_number ** (1/second_number)

    if result is not None:
        display.delete(0, END)
        display.insert(0, str(result))
        first_number = None
        second_number = None
        operation = None
        result = None

root = Tk()
root.title("Calculator")
root.geometry('445x450+700+300')
root.resizable(False, False)

display = Entry(root, width = 50, borderwidth = 10)
display.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

button1 = Button(root, text="1", padx=60, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=60, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=60, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=60, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=60, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=60, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=60, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=60, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=60, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=60, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=58, pady=20, command= click_addition)
button_subtract = Button(root, text="-", padx=61, pady=20, command=click_subtraction)
button_multiply = Button(root, text="*", padx=61, pady=20, command=click_multiplication)
button_divide = Button(root, text="/", padx=62, pady=20, command=click_division)
button_exponentiation = Button(root, text="^", padx=58, pady=20, command=click_exponentiation)
button_root = Button(root, text="√", padx=60, pady=20, command=click_root)
button_clear = Button(root, text="Clear", padx=46, pady=20, command=click_clearing)
button_equal = Button(root, text="=", padx=58, pady=20, command=calculation)

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

first_number = None
second_number = None
operation = None
result = None

root.mainloop()