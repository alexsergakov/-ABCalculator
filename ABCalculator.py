# А/В калькулятор

import tkinter as tk
from tkinter import messagebox as md
import os
import math

# Функция закрытия программы
def du_close():
    root.destroy()

# Функция формотирования процентов
def num_percent(num):
    return "{:.2f}".format(num*100).rjust(10) + '%'

def du_processing():
    # Счиывание данных из полей ввода
    n1 = int(entVisitors1.get())
    c1 = int(entConversions1.get())
    n2 = int(entVisitors2.get())
    c2 = int(entConversions2.get())

    # Проверка данных из полей ввода
    if n1<=0 or n2<=0:
        md.showerror(title="Ошибка", message="Неверное количество посетителей")
        return
    
    popup_window(n1, c1, n2, c2)

# Функция вызова окна результата
def popup_window(n1, c1, n2, c2):
    window=tk.Toplevel()
    window.geometry("500x500")
    window.title("A/B результат")
    
    # Добавление окна вызова текста
    txtOutput = tk.Text(window, font = ('Courier New', 10, 'bold'))
    txtOutput.place(x=15, y=115, width=470, height=300)
    
    # Добавление заголовка
    txtOutput.insert(tk.END, '                           Контрольная    Тестовая' + os.linesep)
    txtOutput.insert(tk.END, '                           группа         группа' + os.linesep)
    txtOutput.insert(tk.END, '------------------------------------------------------' + os.linesep)
    
    # Добавление вывода конверсии и стандартного отклонения
    p1 = c1/n1
    p2 = c2/n2
    txtOutput.insert(tk.END, 'Конверсия              ' + num_percent(p1)
         + '    ' + num_percent(p2) + os.linesep)
    
    sigma1 = math.sqrt(p1*(1-p1)/n1)
    sigma2 = math.sqrt(p2*(1-p2)/n2)
    txtOutput.insert(tk.END, 'Стандартное отклонение ' + num_percent(sigma1)
         + '    ' + num_percent(sigma2) + os.linesep)
    txtOutput.insert(tk.END, '------------------------------------------------------' + os.linesep)
    
    # Добавление кнопки закрытия окна
    btnClosePopup = tk.Button(window, text="Закрыть", font = ('Helvetica', 10, 'bold'),command=window.destroy)
    btnClosePopup.place(x=190, y=450, width=90, height=30)

    # Перевод фокуса на созданное окно
    window.focus_force() 

# Создание главного окна
root = tk.Tk()
root.geometry("280x300")
root.title("A/B калькулятор")

# Добавление метки заголовка
lblTitle = tk.Label(text = "A", font = ('Helvetika', 16, 'bold'), fg = '#0066ff')
lblTitle.place(x=25, y=5)

lblTitle = tk.Label(text = "/", font = ('Helvetika', 25, 'bold'))
lblTitle.place(x=43, y=10)

lblTitle = tk.Label(text = "B", font = ('Helvetika', 16, 'bold'), fg = '#008800')
lblTitle.place(x=55, y=20)

lblTitle = tk.Label(text = "Калькулятор", font = ('Helvetika', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=90, y=15)

# Добавление метки заголовка контрольной группы
lblTitle = tk.Label(text = "Контрольная группа", font = ('Helvetika', 12, 'bold'))
lblTitle.place(x=60, y=50)

# Добавление полей ввода контрольной группы
lblVisitors1 = tk.Label(text = "Посетители:", font = ('Helvetika', 10, 'bold'), fg = '#0066ff')
lblVisitors1.place(x=25, y=80)

entVisitors1 = tk.Entry(font = ('Helvetika', 10, 'bold'), justify='center')
entVisitors1.place(x=160, y=80, width=90, height=20)
entVisitors1.insert(tk.END, '255')

lblConversions1 = tk.Label(text = "Конверсии:", font = ('Helvetika', 10, 'bold'), fg = '#0066ff')
lblConversions1.place(x=25, y=110)

entConversions1 = tk.Entry(font = ('Helvetika', 10, 'bold'), justify='center')
entConversions1.place(x=160, y=110, width=90, height=20)
entConversions1.insert(tk.END, '26')

# Добавление метки заголовка тестовой группы
lblTitle = tk.Label(text = "Тестовая группа", font = ('Helvetika', 12, 'bold'))
lblTitle.place(x=75, y=150)

# Добавление полей ввода тестовой группы
lblVisitors2 = tk.Label(text = "Посетители:", font = ('Helvetika', 10, 'bold'), fg = '#008800')
lblVisitors2.place(x=25, y=180)

entVisitors2 = tk.Entry(font = ('Helvetika', 10, 'bold'), justify='center')
entVisitors2.place(x=160, y=180, width=90, height=20)
entVisitors2.insert(tk.END, '235')

lblConversions2 = tk.Label(text = "Конверсии:", font = ('Helvetika', 10, 'bold'), fg = '#008800')
lblConversions2.place(x=25, y=210)

entConversions2 = tk.Entry(font = ('Helvetika', 10, 'bold'), justify='center')
entConversions2.place(x=160, y=210, width=90, height=20)
entConversions2.insert(tk.END, '18')

# Добавление кнопки "Расчитать"
btnProcess = tk.Button(root, text="Расчитать", font = ('Helvetika', 10, 'bold'), command=du_processing)
btnProcess.place(x=25, y=250, width=90, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text="Закрыть", font = ('Helvetica', 10, 'bold'),command=du_close)
btnClose.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()
