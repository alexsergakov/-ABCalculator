# А/В калькулятор

import tkinter as tk

# Функция закрытия программы
def du_close():
    root.destroy()

# Создание главного окна
root = tk.Tk()
root.geometry("280x300")
root.title("A/B калькулятор")

# Добавление метки заголовка
lblTitle = tk.Label(text = "A/B калькулятор", font = ('Helvetika', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=55, y=20)

# Добавление кнопки "Расчитать"
btnProcess = tk.Button(root, text="Расчитать", font = ('Helvetika', 10, 'bold'))
btnProcess.place(x=25, y=250, width=90, height=30)

# Добавление кнопки закрытия программы
btnClose = tk.Button(root, text="Закрыть", font = ('Helvetica', 10, 'bold'),command=du_close)
btnClose.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()
