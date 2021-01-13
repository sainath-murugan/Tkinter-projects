from tkinter import *

root = Tk()
root.title("CALCULATOR")    # naming the title bar
enter_value = Entry(root, width=65, borderwidth=10)    # size of the display screen
enter_value.grid(row=0, column=0, columnspan=5, ipadx=20, ipady=10)


def common_button(number):    # getting value from the number 0 - 9
    value_2 = number
    enter_value.insert(2000, value_2)


def add():                    # addition operation
    global operation
    operation = "addition"
    global value_1
    value_1 = enter_value.get()
    enter_value.delete(0, END)


def sub():                    # subtraction operation
    global operation
    operation = "subtraction"
    global value_1
    value_1 = enter_value.get()
    enter_value.delete(0, END)


def mul():                     # multiplication operation
    global operation
    operation = "multiplication"
    global value_1
    value_1 = enter_value.get()
    enter_value.delete(0, END)


def div():                   # division operation
    global operation
    operation = "division"
    global value_1
    value_1 = enter_value.get()
    enter_value.delete(0, END)


def clear():                     # used to clear the screen
    enter_value.delete(0, END)


def equal_to():
    if operation == "addition":               # addition of two numbers
        second_value = enter_value.get()
        enter_value.delete(0, END)
        enter_value.insert(0, int(value_1)+int(second_value))

    elif operation == "subtraction":             # subtraction of two numbers
        second_value = enter_value.get()
        enter_value.delete(0, END)
        enter_value.insert(0, int(value_1) - int(second_value))

    elif operation == "multiplication":         # multiplication of two numbers
        second_value = enter_value.get()
        enter_value.delete(0, END)
        enter_value.insert(0, int(value_1) * int(second_value))

    elif operation == "division":              # division of two numbers
        second_value = enter_value.get()
        enter_value.delete(0, END)
        enter_value.insert(0, int(value_1) / int(second_value))

# alignment of the buttons


button_1 = Button(root, text=1, activebackground="red", padx=40, pady=20, command=lambda: common_button(1))
button_2 = Button(root, text=2, activebackground="red", padx=40, pady=20, command=lambda: common_button(2))
button_3 = Button(root, text=3, activebackground="red", padx=40, pady=20, command=lambda: common_button(3))
button_4 = Button(root, text=4, activebackground="red", padx=40, pady=20, command=lambda: common_button(4))
button_5 = Button(root, text=5, activebackground="red", padx=40, pady=20, command=lambda: common_button(5))
button_6 = Button(root, text=6, activebackground="red", padx=40, pady=20, command=lambda: common_button(6))
button_7 = Button(root, text=7, activebackground="red", padx=40, pady=20, command=lambda: common_button(7))
button_8 = Button(root, text=8, activebackground="red", padx=40, pady=20, command=lambda: common_button(8))
button_9 = Button(root, text=9, activebackground="red", padx=40, pady=20, command=lambda: common_button(9))
button_0 = Button(root, text=0, activebackground="red", padx=138, pady=20, command=lambda: common_button(0))
button_add = Button(root, text="+", activebackground="red", padx=40, pady=20, command=add)
button_sub = Button(root, text="-", activebackground="red", padx=40, pady=20, command=sub)
button_mul = Button(root, text="*", activebackground="red", padx=40, pady=20, command=mul)
button_div = Button(root, text="/", activebackground="red", padx=40, pady=20, command=div)
button_equal_to = Button(root, text="=", activebackground="red", padx=20, pady=50, command=equal_to)
button_clear = Button(root, text="C", activebackground="red", padx=20, pady=50, command=clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0, columnspan=3)
button_add.grid(row=1, column=3)
button_sub.grid(row=4, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=2, column=3)
button_equal_to.grid(row=3, rowspan=2, column=4)
button_clear.grid(row=1, rowspan=2, column=4)

root.mainloop()
