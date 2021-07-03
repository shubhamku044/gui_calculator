from tkinter import *

root = Tk()
root.title("Simple Calculator")

Font_tuple = ("Comic Sans MS", 20, "bold")

equation = StringVar()
digits = ""

e = Entry(root, width=34, borderwidth=3, textvariable=equation)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    global digits

    digits = digits + str(number)

    equation.set(digits)


def button_clear():
    global digits
    digits = ""
    equation.set("")


def button_equalto():
    try:
        global digits
        total = str(eval(digits))

        equation.set(total)

        digits = total
    except:
        equation.set("error")
        digits = ""




button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_equal = Button(root, text="=", padx=40, pady=20, fg="red", command=button_equalto)
button_clear = Button(root, text="C", padx=40, pady=20, fg="red", command=button_clear)
button_sum = Button(root, text="+", padx=27, pady=20, fg="red", command=lambda: button_click("+"))
button_subtract = Button(root, text="-", padx=30, fg="red", pady=20, command=lambda: button_click("-"))
button_multiply = Button(root, text="x", padx=28, fg="red", pady=20, command=lambda: button_click("*"))
button_divide = Button(root, text="/", padx=30, fg="red", pady=20, command=lambda: button_click("/"))



button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=1)

button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=0)

button_sum.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)


root.mainloop()