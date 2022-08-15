# А/В калькулятор

import tkinter as tk

# Функция закрытия программы
def du_close():
    root.destroy()

def du_processing():
    # Счиывание данных из полей ввода
    n1 = int(entVisitors1.get())
    c1 = int(entConversions1.get())
    n2 = int(entVisitors2.get())
    c2 = int(entConversions2.get())

    popup_window(n1, c1, n2, c2)

def popup_window(n1, c1, n2, c2):
    window=tk.Toplevel()
    window.geometry("280x300")
    window.title("A/B результат")
    
    # Добавление кнопки закрытия окна
    btnClosePopup = tk.Button(window, text="Закрыть", font = ('Helvetica', 10, 'bold'),command=window.destroy)
    btnClosePopup.place(x=160, y=250, width=90, height=30)

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
entVisitors1.insert(tk.END, '0')

lblConversions1 = tk.Label(text = "Конверсии:", font = ('Helvetika', 10, 'bold'), fg = '#0066ff')
lblConversions1.place(x=25, y=110)

entConversions1 = tk.Entry(font = ('Helvetika', 10, 'bold'), justify='center')
entConversions1.place(x=160, y=110, width=90, height=20)
entConversions1.insert(tk.END, '0')

# Добавление метки заголовка тестовой группы
lblTitle = tk.Label(text = "Тестовая группа", font = ('Helvetika', 12, 'bold'))
lblTitle.place(x=75, y=150)

# Добавление полей ввода тестовой группы
lblVisitors2 = tk.Label(text = "Посетители:", font = ('Helvetika', 10, 'bold'), fg = '#008800')
lblVisitors2.place(x=25, y=180)

entVisitors2 = tk.Entry(font = ('Helvetika', 10, 'bold'), justify='center')
entVisitors2.place(x=160, y=180, width=90, height=20)
entVisitors2.insert(tk.END, '0')

lblConversions2 = tk.Label(text = "Конверсии:", font = ('Helvetika', 10, 'bold'), fg = '#008800')
lblConversions2.place(x=25, y=210)

entConversions2 = tk.Entry(font = ('Helvetika', 10, 'bold'), justify='center')
entConversions2.place(x=160, y=210, width=90, height=20)
entConversions2.insert(tk.END, '0')

# Добавление кнопки "Расчитать"
btnProcess = tk.Button(root, text="Расчитать", font = ('Helvetika', 10, 'bold'), command=du_processing)
btnProcess.place(x=25, y=250, width=90, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text="Закрыть", font = ('Helvetica', 10, 'bold'),command=du_close)
btnClose.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()
