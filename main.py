from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=34, borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
Font_tuple = ("Comic Sans MS", 20, "bold")

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, int(str(current) + str(number)))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_equalto():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtract":
        e.insert(0, f_num - float(second_number))
    if math == "multiply":
        e.insert(0, f_num * float(second_number))
    if math == "divide":
        e.insert(0, f_num / float(second_number))
        


def subtract():
    first_number = e.get()
    global f_num 
    global math
    math = "subtract"
    f_num = float(first_number)
    e.delete(0, END)

def multiply():
    first_number = e.get()
    global f_num 
    global math
    math = "multiply"
    f_num = float(first_number)
    e.delete(0, END)

def divide():
    first_number = e.get()
    global f_num 
    global math
    math = "divide"
    f_num = float(first_number)
    e.delete(0, END)



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
button_sum = Button(root, text="+", padx=27, pady=20, fg="red", command=button_add)
button_subtract = Button(root, text="-", padx=30, fg="red", pady=20, command=subtract)
button_multiply = Button(root, text="x", padx=28, fg="red", pady=20, command=multiply)
button_divide = Button(root, text="/", padx=30, fg="red", pady=20, command=divide)



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