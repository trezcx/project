import sqlite3 as sq
import tkinter as tk
import random
import datetime
import os
import calendar
from tkinter import *
from tkinter import messagebox as mb



con = sq.connect('AVANZ BANK.db')
cursor = con.cursor()

class Registration:
    def __init__(self, title='AVANZ BANK'):
        self.root = tk.Tk()
        self.root.title(title)
        self.root['bg'] = 'gray'
        self.root.geometry('400x400')
        self.root.resizable(False, False)
        self.now = datetime.datetime.now()
        
    
    def save_all(self):
        surname = self.surname.get()
        name = self.name.get()
        otc = self.otc.get()
        num = self.num.get()
        card = random.randint(1111111111111111, 9999999999999999)
        pin = random.randint(1111, 9999)
        balance = 1000
        cursor.execute("INSERT INTO users (Фамилия, Имя, Отчество, Тел, Карта, Пин, Баланс) VALUES (?, ?, ?, ?, ?, ?, ?)", (surname, name, otc, num, card, pin, balance))
        con.commit()
        os.mkdir(f'H:\\project\\{surname}')
        os.mkdir(f'H:\\project\\{name}')
        os.mkdir(f'H:\\project\\{otc}')
        os.mkdir(f'H:\\project\\{num}')
        os.mkdir(f'H:\\project\\{card}')
        os.mkdir(f'H:\\project\\{pin}')
        mb.showinfo('Вы успешно зарегистрировались!')
        
    
    def sign_up(self):
        self.root_1 = tk.Tk()
        self.root_1.title('Регистрация')
        self.root_1['bg'] = 'gray'
        self.root_1.geometry('400x400')
        self.root_1.resizable(False, False)
        self.surname = Entry(self.root_1, width=15)
        self.name = Entry(self.root_1,width=15)
        self.otc = Entry(self.root_1, width=15)
        self.num = Entry(self.root_1, width=15)
        self.now = datetime.datetime.now()
        
        Label(self.root_1, text="AVANZ BANK", font=("Arial", 30), bg='gray').place(x=65, y=100)
        label = tk.Label(self.root_1, text=self.now.strftime("%H:%M:%S"))
        label.place(x=0, y=0)
        Label(self.root_1, text="Регистрация", font=("Arial", 30), bg='gray').place(x=70, y=100)
        Label(self.root_1, text='Имя:', bg='gray').place(x=40, y=180)
        self.name.place(x=70, y=180)
        Label(self.root_1, text='Фамилия:', bg='gray').place(x=10, y=210)
        self.surname.place(x=70, y= 210)
        Label(self.root_1, text='Отчество:', bg='gray').place(x=10, y= 240)
        self.otc.place(x=70, y=240)
        Label(self.root_1, text='Тел:', bg='gray').place(x=40, y= 270)
        self.num.place(x=70, y=270)
        Button(self.root_1, text='Зарегистрироваться', command=self.save_all, width=15).place(x=220, y=200)
        Button(self.root_1, text='Выйти', width=15, command=self.exit).place(x=220, y=250)


    def widgets_button(self):
        Label(self.root, text="AVANZ BANK", font=("Arial", 30), bg='gray').place(x=65, y=100)
        Button(self.root, text= 'Зарегистрироваться', width=15, command =self.sign_up).place(x=70, y=200)
        Button(self.root, text= 'Войти', width=15, command=self.sign_in).place(x=200, y=200)

    def menu(self):
        self.root_3 = tk.Tk()
        self.root_3.title('Меню')
        self.root_3.geometry('400x400')
        self.root_3['bg'] = 'gray'
        self.root_3.resizable(False, False)
        
        label = tk.Label(self.root_3, text=self.now.strftime("%H:%M:%S"))
        label.place(x=0, y=0)
        Label(self.root_3, text='Выберите операцию', bg='gray', font=("Arial", 30)).place(x=15, y=100)
        Button(self.root_3, text='Пополнить', width=52, command=self.popolni).place(x=15, y=200)

    def popolni(self):
        self.root_4 = tk.Tk()
        self.root_4.title('Пополнение')
        self.root_4.geometry('400x400')
        self.root_4['bg'] = 'gray'
        self.root_4.resizable(False, False)
        
        label = tk.Label(self.root_4, text=self.now.strftime("%H:%M:%S"))
        label.place(x=0, y=0)
        Label(self.root_4, text="Пополнение", font=("Arial", 30), bg='gray').place(x=100, y=100)
        Button(self.root_4, text='Пополнить', command=self.pop, width=30).place(x=100, y=196)

    def pop(self):
        balance = 0
        amount = int(input('Введите сумму пополнения: '))
        balance += amount
        mb.showinfo("\n Сумма поплнения:", amount) 
        cursor.execute("INSERT INTO users (Баланс) VALUES (amount)") 
        con.commit()
            
    def sign_in(self):
        self.root_2 = tk.Tk()
        self.root_2.title('Вход')
        self.root_2['bg'] = 'gray'
        Label(self.root_2, text="Вход", font=("Arial", 30), bg='gray').place(x=150, y=100)
        self.root_2.geometry('400x400')
        self.root_2.resizable(False, False)
        self.num_2 = Entry(self.root_2, width=20)
        self.pin_2 = Entry(self.root_2, width=20)
        Label(self.root_2, text='Тел:', bg='gray').place(x=40, y= 180)
        self.num_2.place(x=70, y=180)
        Label(self.root_2, text='Пин:', bg='gray').place(x=40, y= 230)
        self.pin_2.place(x=70, y=230)
        label = tk.Label(self.root_2, text=self.now.strftime('%H:%M:%S'))
        label.place(x=0, y=0)
        Button(self.root_2, text='Войти', width=10, command=self.sign_all).place(x=230, y=180)
        Button(self.root_2, text='Меню', width=10, command=self.popolni).place(x=230, y=220)

    def sign_all(self):
        num = self.num_2.get()
        pin = self.pin_2.get()
        cursor.execute("SELECT * FROM users")
        for user in cursor.fetchall():
            if num in user and pin in user:
                mb.showinfo('Вы успешно вошли!')
            else:
                mb.showerror('Зарегистрируйте аккаунт!')
            print(user)

    def exit(self):
        choice = mb.askyesno('Выйти', 'Вы уверены что хотите выйти?')
        if choice:
            self.root_1.destroy()




    def run(self):
        self.widgets_button()
        self.root.mainloop()    
    
    def run_1(self):
        self.root_1.mainloop()
    
    def run_3(self):
        self.root_3.mainloop()

    def run_2(self):
        self.root_2.mainloop()        
    
regist = Registration()
regist.run()
regist.run_1()
regist.run_2()
regist.run_3()