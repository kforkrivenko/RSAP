from tkinter import *
from tkinter.ttk import Frame, Button, Style

import crypting
from helpfull_func import *
import sqlite3

conn = sqlite3.connect('data.db') # глобальная база данных
conn_local = sqlite3.connect('data_local.db')  # локальная база данных
cursor = conn.cursor()
cursor_local = conn_local.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (username TEXT PRIMARY KEY,
                password TEXT,
                e TEXT, 
                n TEXT)''')  # эта таблица должна быть на сервере

cursor_local.execute('''CREATE TABLE IF NOT EXISTS keys
                (username TEXT PRIMARY KEY,
                 d TEXT,
                 e TEXT,
                 p TEXT,
                 n TEXT,
                 q TEXT)''')


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        super().__init__()
        self.button_back_addfriend = None
        self.button_search = None
        self.entry_1_enter = None
        self.label_2_addfriend = None
        self.label_1_addfriend = None
        self.frame_addfriend_1 = None
        self.send_button = None
        self.entry_dialog = None
        self.button_back_dialog = None
        self.frame_entry_dialog = None
        self.button_add = None
        self.frame_addfriend_2 = None
        self.label_name_dialog = None
        self.frame_dialog = None
        self.canvas_dialog = None
        self.dict_events_dialogs = None
        self.button_exit_dialogs = None
        self.canvas_dialogs = None
        self.label_1_dialogs = None
        self.frame_username_dialogs = None
        self.frame_dialogs = None
        self.entry_4_reg = None
        self.entry_3_reg = None
        self.frame_3_reg = None
        self.label_3_reg = None
        self.entry_2_reg = None
        self.frame_2_reg = None
        self.label_2_reg = None
        self.label_1_reg = None
        self.frame_1_reg = None
        self.entry_3_enter = None
        self.entry_2_enter = None
        self.label_3_enter = None
        self.frame_2_enter = None
        self.label_2_enter = None
        self.label_1_enter = None
        self.frame_1_enter = None
        self.label_3_addfriend = None
        self.label_4_addfriend = None
        self.label_5_addfriend = None
        self.button_addfriend = None
        self.label_3_search = None
        self.canvas = None
        self.buttonTXT = None
        self.buttonNF = None
        self.label_4_enter = None
        self.label_5_enter = None
        self.label_4_reg = None
        self.label_5_reg = None
        self.label_6_reg = None
        self.button_back = None
        self.frame = None
        self.button_check = None
        self.button_confirm = None
        self.button_reg = None
        self.style = None
        self.parent = parent
        self.initUI()
        self.dialog_buttons = []

    def initUI(self):
        self.parent.title("RSA приложение")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        self.frame = Frame(self, borderwidth=1, relief=SOLID, padding=[5, 2], height=800, width=500)
        # enter_window init
        self.button_check = Button(self.frame, text="Войти",
                                   command=lambda: self.check_log(self.entry_2_enter.get(), self.entry_3_enter.get()))
        self.button_reg = Button(self.frame, text="Регистрация",
                                 command=lambda: execute(self.enter_window_quit, self.reg_window_create))
        self.frame_1_enter = Frame(self.frame, borderwidth=1)
        self.label_1_enter = Label(self.frame, text="Вход в аккаунт", font=("Arial", 14))
        self.label_2_enter = Label(self.frame_1_enter, text="Имя: ", font=("Arial", 14))
        self.frame_2_enter = Frame(self.frame, borderwidth=1)
        self.label_3_enter = Label(self.frame_2_enter, text="Пароль: ", font=("Arial", 14))
        self.entry_2_enter = Entry(self.frame_1_enter, width=30)
        self.entry_3_enter = Entry(self.frame_2_enter, width=30)

        # reg_window init
        self.frame_1_reg = Frame(self.frame, borderwidth=1)
        self.label_1_reg = Label(self.frame, text="Создать аккаунт", font=("Arial", 14))
        self.label_2_reg = Label(self.frame_1_reg, text="Имя: ", font=("Arial", 14))
        self.entry_2_reg = Entry(self.frame_1_reg, width=30)
        self.frame_2_reg = Frame(self.frame, borderwidth=1)
        self.label_3_reg = Label(self.frame_2_reg, text="Пароль: ", font=("Arial", 14))
        self.entry_3_reg = Entry(self.frame_2_reg, width=30)
        self.frame_3_reg = Frame(self.frame, borderwidth=1)
        self.label_4_reg = Label(self.frame_3_reg, text="Еще раз пароль: ", font=("Arial", 14))
        self.entry_4_reg = Entry(self.frame_3_reg, width=30)
        self.button_confirm = Button(self.frame, text="Подтвердить",
                                     command=lambda: self.check_reg(self.entry_2_reg.get(), self.entry_3_reg.get(),
                                                                    self.entry_4_reg.get()))
        self.button_back = Button(self.frame, text="Назад",
                                  command=lambda: execute(self.reg_window_quit, self.enter_window_create))

        # dialogs_window init
        self.frame_dialogs = Frame(self, height=800, width=500)
        self.frame_username_dialogs = Frame(self, padding=[10, 10], relief=RIDGE, borderwidth=1)
        self.label_1_dialogs = Label(self.frame_username_dialogs)
        self.button_exit_dialogs = Button(self.frame_dialogs, text="Выход",
                                          command=lambda: execute(self.dialogs_window_quit, self.enter_window_create))
        self.dict_events_dialogs = dict()

        # dialog_window init
        self.frame_dialog = Frame(self, borderwidth=1, relief=SOLID, width=900, height=850)
        self.label_name_dialog = Label(self.frame_dialog, width=900)

        # addfriend_window init
        self.frame_addfriend_2 = Frame(self, borderwidth=1, relief=SOLID, width=300, height=200)
        self.label_3_search = Label(self.frame_addfriend_2, font=("Arial", 14))
        self.button_add = Button(self.frame_addfriend_2, text="Добавить")
        self.frame_entry_dialog = Frame(self, borderwidth=1, height=200)
        self.button_back_dialog = Button(self, text="Назад",
                                         command=lambda: execute(self.dialog_window_quit, self.dialogs_window_create))
        self.entry_dialog = Entry(self.frame_entry_dialog, width=160)
        self.send_button = Button(self.frame_entry_dialog, text="Отправить")
        self.frame_addfriend_1 = Frame(self, borderwidth=1, relief=SOLID, width=300, height=200)
        self.label_1_addfriend = Label(self.frame_addfriend_1, text="Поиск друзей", font=("Arial", 14))
        self.label_2_addfriend = Label(self.frame_addfriend_1, text="Введите имя:", font=("Arial", 14))
        self.entry_1_enter = Entry(self.frame_addfriend_1)
        self.button_search = Button(self.frame_addfriend_1, text="Поиск",
                                    command=lambda: self.search(self.entry_1_enter.get()))
        self.button_back_addfriend = Button(self.frame_addfriend_1, text="Назад",
                                            command=lambda: execute(self.addfriend_window_quit,
                                                                    self.dialogs_window_create))

        # errors
        self.label_4_enter = Label(self.frame, text="Ошибка, неправильный пароль", font=("Arial", 14), foreground='red')
        self.label_5_enter = Label(self.frame, text="Такого пользователя не существует", font=("Arial", 14),
                                   foreground='red')
        self.label_5_reg = Label(self.frame, text="Пароли не совпадают!", font=("Arial", 14), foreground='red')
        self.label_6_reg = Label(self.frame, text="Имя пользователя занято!", font=("Arial", 14), foreground='red')
        self.label_3_addfriend = Label(self.frame_addfriend_2, text="Пользователя с таким именем на существует",
                                       font=("Arial", 14),
                                       foreground='red')
        self.label_4_addfriend = Label(self.frame_addfriend_2, text="Это же вы! Выберете другого пользователя",
                                       font=("Arial", 14),
                                       foreground='red')
        self.label_5_addfriend = Label(self.frame_addfriend_2, text="Этот человек у вас уже в друзьях",
                                       font=("Arial", 14),
                                       foreground='red')

        # entering first window
        self.enter_window_create()

    def reg_window_create(self):
        # labels && entries packing
        self.label_1_reg.pack(side=TOP, pady=20)
        self.label_2_reg.pack(side=LEFT)
        self.entry_2_reg.pack(side=RIGHT, fill=X)
        self.label_3_reg.pack(side=LEFT)
        self.entry_3_reg.pack(side=RIGHT, fill=X)
        self.label_4_reg.pack(side=LEFT)
        self.entry_4_reg.pack(side=RIGHT, fill=X)

        # frames packing
        self.frame_1_reg.pack(side=TOP, fill=X)
        self.frame_2_reg.pack(side=TOP, fill=X)
        self.frame_3_reg.pack(side=TOP, fill=X)
        self.frame.pack(side=TOP, pady=20)

        # buttons packing
        self.button_back.pack(side=BOTTOM, pady=5)
        self.button_confirm.pack(side=BOTTOM, pady=5)

    def enter_window_create(self):
        # labels && entries packing
        self.label_1_enter.pack(side=TOP, pady=50, padx=90, fill=X)
        self.label_2_enter.pack(side=LEFT, fill=X)
        self.entry_2_enter.pack(side=RIGHT, fill=X)
        self.label_3_enter.pack(side=LEFT, fill=X)
        self.entry_3_enter.pack(side=RIGHT, fill=X)

        # frames packing
        self.frame_1_enter.pack(side=TOP, fill=X)
        self.frame_2_enter.pack(side=TOP, fill=X)
        self.frame.pack(side=TOP, pady=20)

        # buttons packing
        self.button_reg.pack(side=BOTTOM)
        self.button_check.pack(side=BOTTOM, pady=10)

    def dialogs_window_create(self):
        # creating canvas
        self.canvas_dialogs = Canvas(self.frame_dialogs, width=1920, height=960)
        self.buttonNF = self.canvas_dialogs.create_rectangle(20, 100, 1820, 200, fill='gray')
        self.buttonTXT = self.canvas_dialogs.create_text(920, 150, text='Добавить друга')

        self.label_1_dialogs.config(text=get_name())
        self.label_1_dialogs.pack()
        self.canvas_dialogs.pack(side=TOP)
        self.button_exit_dialogs.pack(side=BOTTOM)

        # frames packing
        self.frame_username_dialogs.pack(side=LEFT, anchor=NW)
        self.frame_dialogs.pack()

        # adding function to rectangles
        self.canvas_dialogs.tag_bind(self.buttonNF, "<Button-1>", self.addfriend_window_create)
        self.canvas_dialogs.tag_bind(self.buttonTXT, "<Button-1>", self.addfriend_window_create)

        # creating friend list
        cursor.execute(f'''SELECT username FROM friends_{get_name()}''')
        friends = cursor.fetchall()
        for (i, friend) in enumerate(friends):
            A = self.canvas_dialogs.create_rectangle(20, 200 + 100 * i, 1820, 300 + 100 * i, fill='white')
            B = self.canvas_dialogs.create_text(920, 250 + 100 * i, text=friend)
            self.dict_events_dialogs[i + 2] = friend
            self.canvas_dialogs.tag_bind(A, "<Button-1>",
                                         lambda event: execute(self.dialogs_window_quit, self.dialog_window_create,
                                                               event))
            self.canvas_dialogs.tag_bind(B, "<Button-1>",
                                         lambda event: execute(self.dialogs_window_quit, self.dialog_window_create,
                                                               event))

    def addfriend_window_create(self, event):
        self.dialogs_window_quit()

        self.frame_username_dialogs.pack(side=LEFT, anchor=NW)
        self.label_1_dialogs.pack()
        self.frame_addfriend_1.pack(pady=5)
        self.label_1_addfriend.pack(side=TOP)
        self.button_back_addfriend.pack(side=BOTTOM, pady=5)
        self.button_search.pack(side=BOTTOM, pady=5)
        self.label_2_addfriend.pack(padx=5, side=LEFT)
        self.entry_1_enter.pack(padx=5, pady=5, side=RIGHT)

    def dialog_window_create(self, event):
        button_clicked = event.y // 100
        name = self.dict_events_dialogs[button_clicked]
        self.send_button.config(command=lambda: self.send_message(name[0]))

        self.canvas_dialog = Canvas(self, width=1920, height=900)
        self.label_name_dialog.config(text=name)
        self.label_name_dialog.pack(pady=20)
        # self.entry_dialog.bind("<Enter>", func=self.send_message) # GOOGLE узнать какой ивент отвечает за 'Enter'
        self.frame_dialog.pack(padx=10, pady=10)  # FRAME
        self.button_back_dialog.pack(side=BOTTOM, pady=20, fill=Y)
        self.frame_entry_dialog.pack(side=BOTTOM)  ## GOOGLE как увеличить размер входа
        self.entry_dialog.pack(side=LEFT, pady=10, padx=10)

        self.send_button.pack(side=RIGHT, pady=10, padx=10)
        self.canvas_dialog.pack(side=BOTTOM, padx=10)  # FRAME

        # добавляем сообщения
        self.update_dialog(name[0])

    def check_log(self, user, password):
        if len(user) == 0:
            return

        self.delete_mistakes()
        cursor.execute('''SELECT password FROM users WHERE username = ?''', (user,))
        entry = cursor.fetchall()
        if len(entry) != 0:
            real_password = entry[0][0]
        else:
            # красным текстом "Ошибка, такого пользователя не существует"
            self.label_5_enter.pack(pady=10)
            self.entry_3_enter.delete(0, 'end')
            self.entry_2_enter.delete(0, 'end')
            return

        if password != real_password:
            # красным текстом "Ошибка, неправильный пароль"
            self.label_4_enter.pack(pady=10)
            self.entry_3_enter.delete(0, 'end')
            self.entry_2_enter.delete(0, 'end')
        else:
            with open('user_info.txt', 'w') as f:
                f.write(f'{user}')
            self.enter_window_quit()
            self.dialogs_window_create()

    def check_reg(self, user, password, password_2):
        if len(user) == 0:
            return
        self.delete_mistakes()
        if password != password_2:
            # красным текстом "Пароли не совпадают!"
            self.label_5_reg.pack(pady=10)
            self.entry_4_reg.delete(0, 'end')
            self.entry_3_reg.delete(0, 'end')
            self.entry_2_reg.delete(0, 'end')

        else:
            cursor.execute('''SELECT password FROM users WHERE username = ?''', (user,))
            entry = cursor.fetchall()
            if len(entry) != 0:
                # красным текстом "Имя пользователя занято!"
                self.label_6_reg.pack(pady=10)
                self.entry_4_reg.delete(0, 'end')
                self.entry_3_reg.delete(0, 'end')
                self.entry_2_reg.delete(0, 'end')
            else:
                e, d = crypting.get_keys()

                cursor.execute('''INSERT INTO users (username, password, e, n) VALUES (?, ?, ?, ?)''',
                               (user, password, str(e.e), str(e.n)))
                conn.commit()
                cursor_local.execute('''INSERT INTO keys (username, d, e, p, n, q) VALUES (?, ?, ?, ?, ?, ?)''',
                               (user, str(d.d), str(d.e), str(d.p), str(d.n), str(d.q)))
                conn_local.commit()
                cursor.execute(f'''CREATE TABLE IF NOT EXISTS friends_{user}
                                (username TEXT PRIMARY KEY)''')
                conn.commit()
                self.reg_window_quit()
                self.enter_window_create()

    def enter_window_quit(self):
        self.frame.pack_forget()
        self.frame_1_enter.pack_forget()
        self.frame_2_enter.pack_forget()
        self.label_1_enter.pack_forget()
        self.label_2_enter.pack_forget()
        self.label_3_enter.pack_forget()
        self.entry_2_enter.pack_forget()
        self.entry_3_enter.pack_forget()
        self.button_reg.pack_forget()
        self.button_check.pack_forget()
        self.label_4_enter.pack_forget()
        self.label_5_enter.pack_forget()
        self.entry_3_enter.delete(0, 'end')
        self.entry_2_enter.delete(0, 'end')

        self.delete_mistakes()

    def reg_window_quit(self):
        self.frame.pack_forget()
        self.frame_1_reg.pack_forget()
        self.frame_2_reg.pack_forget()
        self.frame_3_reg.pack_forget()
        self.label_1_reg.pack_forget()
        self.label_2_reg.pack_forget()
        self.label_3_reg.pack_forget()
        self.label_4_reg.pack_forget()
        self.entry_2_reg.pack_forget()
        self.entry_3_reg.pack_forget()
        self.entry_4_reg.pack_forget()
        self.button_back.pack_forget()
        self.button_confirm.pack_forget()
        self.entry_2_reg.delete(0, 'end')
        self.entry_3_reg.delete(0, 'end')
        self.entry_4_reg.delete(0, 'end')

        self.delete_mistakes()

    def addfriend_window_quit(self):
        self.frame_addfriend_1.pack_forget()
        self.frame_addfriend_2.pack_forget()
        self.label_1_addfriend.pack_forget()
        self.label_2_addfriend.pack_forget()
        self.entry_1_enter.pack_forget()
        self.button_search.pack_forget()
        self.button_back_addfriend.pack_forget()
        self.frame_username_dialogs.pack_forget()
        self.label_1_dialogs.pack_forget()
        self.entry_1_enter.delete(0, 'end')

        self.delete_mistakes()

    def dialog_window_quit(self):
        self.frame_dialog.pack_forget()
        self.canvas_dialog.pack_forget()

        self.button_back_dialog.pack_forget()
        self.frame_entry_dialog.pack_forget()
        self.entry_dialog.pack_forget()
        self.label_name_dialog.pack_forget()

    def dialogs_window_quit(self):
        self.canvas_dialogs.pack_forget()
        self.frame_dialogs.pack_forget()
        self.button_exit_dialogs.pack_forget()
        self.frame_username_dialogs.pack_forget()
        self.label_1_dialogs.pack_forget()

    def delete_mistakes(self):
        if self.label_5_reg is not None:
            self.label_5_reg.pack_forget()
        if self.label_6_reg is not None:
            self.label_6_reg.pack_forget()
        if self.label_4_enter is not None:
            self.label_4_enter.pack_forget()
        if self.label_5_enter is not None:
            self.label_5_enter.pack_forget()
        if self.label_3_addfriend is not None:
            self.label_3_addfriend.pack_forget()
        if self.label_4_addfriend is not None:
            self.label_4_addfriend.pack_forget()
        if self.label_5_addfriend is not None:
            self.label_5_addfriend.pack_forget()

    def search(self, name):
        if name == "":
            return

        self.label_3_search.pack_forget()
        self.button_add.pack_forget()
        self.delete_mistakes()

        self.frame_addfriend_2.pack()

        cursor.execute('''SELECT username FROM users WHERE username=?''', (name,))
        res = cursor.fetchall()

        if len(res) != 0:
            if name == get_name():
                self.label_4_addfriend.pack()
                return

            self.label_3_search.config(text=f"{res[0][0]}")
            self.button_add.config(command=lambda: self.add_friend(name))
            self.label_3_search.pack(side=LEFT, padx=50, pady=50, fill=X)
            self.button_add.pack(side=LEFT, padx=50, pady=50)
        else:
            self.label_3_addfriend.pack()
            return

    def add_friend(self, name):
        cursor.execute(f'''SELECT username FROM friends_{get_name()} WHERE username = ?''', (name,))
        input = cursor.fetchall()
        if len(input) != 0:
            self.label_3_search.pack_forget()
            self.button_add.pack_forget()
            self.label_5_addfriend.pack()
            return
        cursor.execute(f'''INSERT INTO friends_{get_name()} (username) VALUES (?)''', (name,))
        cursor.execute(f'''INSERT INTO friends_{name} (username) VALUES (?)''', (get_name(),))

        cursor.execute(
            f'''CREATE TABLE IF NOT EXISTS {get_table_name(name, get_name())} (message TEXT, from_{sorted([name, get_name()])[0]} BOOLEAN)''')

        self.addfriend_window_quit()
        self.dialogs_window_create()
        conn.commit()

    def send_message(self, name):
        # получаем ключ
        cursor.execute(f'''SELECT e, n FROM users WHERE username = ?''', (name,))
        e, n = cursor.fetchall()[0]
        print(e, n)
        # шифруем
        message = crypting.crypt(self.entry_dialog.get(), e, n)
        self.entry_dialog.delete(0, 'end')

        cursor.execute(f'''INSERT INTO {get_table_name(get_name(), name)} VALUES (?, ?)''',
                       (message, name == sorted([name, get_name()])[1]))
        conn.commit()

        self.update_dialog(name)

    def update_dialog(self, name):
        # получаем ключ
        cursor_local.execute(f'''SELECT d, e, p, n, q FROM keys WHERE username = ?''', (name,))
        d, e, p, n, q = cursor_local.fetchall()[0]
        # дешифруем
        cursor.execute(f'''SELECT message FROM {get_table_name(name, get_name())}''')
        m = cursor.fetchall()

        cursor.execute(f'''SELECT from_{sorted([name, get_name()])[0]} FROM {get_table_name(name, get_name())}''')
        from_first = cursor.fetchall()
        for (i, message) in enumerate(m):
            res = ''
            for _ in range(len(message)):
                res += (crypting.decrypt(message[0], d, e, p, n, q))
            message = res
            if (from_first[i][0] and get_name() == sorted([name, get_name()])[0]) or (
                    not from_first[i][0] and get_name() != sorted([name, get_name()])[0]):
                self.canvas_dialog.create_rectangle(910, 5 + 100 * i, 1820, 105 + 100 * i,
                                                    fill='white')  # GOOGLE как ввести отступы между прямоугольниками
                self.canvas_dialog.create_text(1360, 55 + 100 * i, text=message, font=("Arial", 24))
            else:
                self.canvas_dialog.create_rectangle(20, 5 + 100 * i, 910, 105 + 100 * i, fill='white')
                self.canvas_dialog.create_text(405, 55 + 100 * i, text=message, font=("Arial", 24))


def main():
    root = Tk()
    root.geometry("1920x1080")
    Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
'''
Что нужно:
1) добавление друзей в обе стороны (пока только в одну) +
1.5) удалить колонку количества друзей +
2) диалог +
3) программа (разработчика) отдельная от пользовательской (там будет таблица users)
4) оформление (должно показываться имя пользователя, возможность выхода, остальное сделать красивее)
5) шифровка (закрытый ключ у пользователя, на сервере только зашифрованные сообщения)
6) сделать код читабельнее + 
7) Удаление друзей, прокрутка сообщений вниз
8) создание программы, сделать так, чтобы открывалось как rsa, а не как tk
'''
