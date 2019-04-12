from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Первая нормальная програа на питоне Калькулятор")


# Функции
def cal(key):
    global memory
    if key == "=":
        # что можно вести в строк
        mogno_vesty = "-+0123456789.*/"
        if calc_windows.get()[0] not in mogno_vesty:
            calc_windows.insert(END, "Первый символ не число")
            messagebox.showerror("Ошибка!", "Вы вели не коректный символ!")
            print("В консоле работает")
            eval(calc_windows.get())
            # арифметика
            try:
                result = eval(calc_windows.get())
                calc_windows.insert(END, "=" + str(result))
                print(eval(calc_windows.get()))

            except:
                calc_windows.insert(END, "Ошибка!")
                messagebox.showerror("Ошибка", "Проверти веденые данные на ошибки")

    # Очистка поля
    elif key == "C":
        calc_windows.delete(0, END)

    # сднлать положительно отрицателным и наоборот
    elif key == "+/-":
        if "=" in calc_windows.get():
            calc_windows.delete(0, END)
            try:
                if calc_windows.get()[0] == "-":
                    calc_windows.delete(0)
                else:
                    calc_windows.insert(0, "-")
            except IndexError:
                pass
    else:
        if "=" in calc_windows.get():
            calc_windows.delete(0, END)
        calc_windows.insert(END, key)


btth_list = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "+/-", "=",
    "0", ".", "C"

]

one = 1
zero = 0

for i in btth_list:
    rel = ""
    cmd = lambda x=i: cal(x)
    ttk.Button(root, text=i, command=cmd).grid(row=one, column=zero)
    zero += 1
    if zero > 4:
        zero = 0
        one += 1

# Окно результатов
calc_windows = Entry(root, width=40)
calc_windows.grid(row=0, column=0, columnspan=5)




root.mainloop()
