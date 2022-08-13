# А/В калькулятор

import tkinter as tk

# Функция закрытия программы
def du_close():
    root.destroy()

def popup_window():
    window=tk.Toplevel()
    window.geometry("280x300")
    window.title("A/B результат")
    
    # Добавление кнопки закрытия окна
    btnClosePopup = tk.Button(window, text="Закрыть", font = ('Helvetica', 10, 'bold'),command=window.destroy)
    btnClosePopup.place(x=160, y=250, width=90, height=30)

# Создание главного окна
root = tk.Tk()
root.geometry("280x300")
root.title("A/B калькулятор")

# Добавление метки заголовка
lblTitle = tk.Label(text = "A/B калькулятор", font = ('Helvetika', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=55, y=20)

# Добавление метки заголовка контрольной группы
lblTitle = tk.Label(text = "Контрольная группа", font = ('Helvetika', 12, 'bold'), fg = '#0066ff')
lblTitle.place(x=25, y=55)

# Добавление полей ввода контрольной группы
lblVisitors1 = tk.Label(text = "Посетители:", font = ('Helvetika', 10, 'bold'))
lblVisitors1.place(x=25, y=85)

entVisitors1 = tk.Entry(font = ('Helvetika', 10, 'bold'))
entVisitors1.place(x=115, y=85, width=90, height=20)

lblVisitors1 = tk.Label(text = "Конверсии:", font = ('Helvetika', 10, 'bold'))
lblVisitors1.place(x=25, y=115)

entVisitors1 = tk.Entry(font = ('Helvetika', 10, 'bold'))
entVisitors1.place(x=115, y=115, width=90, height=20)

# Добавление метки заголовка тестовой группы
lblTitle = tk.Label(text = "Тестовая группа", font = ('Helvetika', 12, 'bold'), fg = '#008800')
lblTitle.place(x=25, y=145)

# Добавление полей ввода тестовой группы
lblVisitors1 = tk.Label(text = "Посетители:", font = ('Helvetika', 10, 'bold'))
lblVisitors1.place(x=25, y=175)

entVisitors1 = tk.Entry(font = ('Helvetika', 10, 'bold'))
entVisitors1.place(x=115, y=175, width=90, height=20)

lblVisitors1 = tk.Label(text = "Конверсии:", font = ('Helvetika', 10, 'bold'))
lblVisitors1.place(x=25, y=205)

entVisitors1 = tk.Entry(font = ('Helvetika', 10, 'bold'))
entVisitors1.place(x=115, y=205, width=90, height=20)

# Добавление кнопки "Расчитать"
btnProcess = tk.Button(root, text="Расчитать", font = ('Helvetika', 10, 'bold'), command=popup_window)
btnProcess.place(x=25, y=250, width=90, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text="Закрыть", font = ('Helvetica', 10, 'bold'),command=du_close)
btnClose.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()
