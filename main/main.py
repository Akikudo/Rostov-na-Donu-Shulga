import sqlite3
import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication


class Registration(QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 609)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 70, 591, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_line = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.name_line.setText("")
        self.name_line.setObjectName("name_line")
        self.verticalLayout.addWidget(self.name_line)
        self.surname_line = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.surname_line.setText("")
        self.surname_line.setObjectName("surname_line")
        self.verticalLayout.addWidget(self.surname_line)
        self.otchestvo_line = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.otchestvo_line.setText("")
        self.otchestvo_line.setObjectName("otchestvo_line")
        self.verticalLayout.addWidget(self.otchestvo_line)
        self.login_line = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.login_line.setObjectName("login_line")
        self.verticalLayout.addWidget(self.login_line)
        self.password_line = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.password_line.setObjectName("password_line")
        self.verticalLayout.addWidget(self.password_line)
        self.hello_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.hello_label.setGeometry(QtCore.QRect(110, 10, 601, 51))
        self.hello_label.setObjectName("hello_label")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 290, 591, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 350, 591, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 380, 701, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 410, 591, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 440, 591, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 320, 591, 16))
        self.label_6.setObjectName("label_6")
        self.registrationBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.registrationBtn.setGeometry(QtCore.QRect(320, 480, 151, 28))
        self.registrationBtn.setObjectName("registrationBtn")
        self.alternativeBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.alternativeBtn.setGeometry(QtCore.QRect(602, 510, 171, 28))
        self.alternativeBtn.setObjectName("alternativeBtn")
        self.super_alternativeBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.super_alternativeBtn.setGeometry(QtCore.QRect(70, 510, 171, 28))
        self.super_alternativeBtn.setObjectName("super_alternativeBtn")
        self.name_lable = QtWidgets.QLabel(parent=self.centralwidget)
        self.name_lable.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.name_lable.setObjectName("name_lable")
        self.surname_lable = QtWidgets.QLabel(parent=self.centralwidget)
        self.surname_lable.setGeometry(QtCore.QRect(30, 120, 55, 16))
        self.surname_lable.setObjectName("surname_lable")
        self.login_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(30, 180, 55, 16))
        self.login_label.setObjectName("login_label")
        self.password_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(30, 220, 55, 16))
        self.password_label.setObjectName("password_label")
        self.patronym_descryption_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.patronym_descryption_label.setGeometry(QtCore.QRect(100, 250, 589, 34))
        self.patronym_descryption_label.setObjectName("patronym_descryption_label")
        self.patronym_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.patronym_label.setGeometry(QtCore.QRect(30, 150, 55, 16))
        self.patronym_label.setObjectName("patronym_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_line.setText(_translate("MainWindow", ""))
        self.password_line.setText(_translate("MainWindow", ""))
        self.hello_label.setText(_translate("MainWindow",
                                            "Приветствуем вас на нашем сайте! Чтобы зарегистрироваться, пожалуйста введите ваши данные"))
        self.label.setText(_translate("MainWindow", "Пароль должен соответствовать 5 критериям:"))
        self.label_2.setText(_translate("MainWindow", "Длина пароля не может быть меньше 9 символов."))
        self.label_3.setText(
            _translate("MainWindow", "Должны присутствовать хотя бы одна большая буква и хотя бы одна маленькая."))
        self.label_4.setText(_translate("MainWindow", "Должна присутствовать хотя бы одна цифра."))
        self.label_5.setText(
            _translate("MainWindow",
                       "В пароле нет комбинаций из 3 букв одного алфавита, стоящих рядом. Например: QWE."))
        self.label_6.setText(_translate("MainWindow", "Раскладка русская или английская. Можно комбинировать."))
        self.registrationBtn.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.alternativeBtn.setText(_translate("MainWindow", "Уже есть аккаунт? Войти."))
        self.super_alternativeBtn.setText(_translate("MainWindow", "Вернуться к регистрации"))
        self.name_lable.setText(_translate("MainWindow", "Имя"))
        self.surname_lable.setText(_translate("MainWindow", "Фамилия"))
        self.login_label.setText(_translate("MainWindow", "Логин"))
        self.password_label.setText(_translate("MainWindow", "Пароль"))
        self.patronym_descryption_label.setText(
            _translate("MainWindow", "Если у вас нет отчества, то напишите в поле ввода \"нет\""))
        self.patronym_label.setText(_translate("MainWindow", "Отчество"))
        self.alternativeBtn.clicked.connect(self.enter)
        self.super_alternativeBtn.setVisible(False)
        self.registrationBtn.clicked.connect(self.stat)
        self.super_alternativeBtn.clicked.connect(self.alt_enter)
        self.statusbar.show()
        # Создали интерфейс

    def enter(self):
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)
        self.name_line.setVisible(False)
        self.surname_line.setVisible(False)
        self.otchestvo_line.setVisible(False)
        self.name_lable.setVisible(False)
        self.surname_lable.setVisible(False)
        self.patronym_label.setVisible(False)
        self.login_label.setVisible(False)
        self.password_label.setVisible(False)
        self.login_line.setText('Введите логин')
        self.password_line.setText('Введите пароль')
        self.trfa = True
        self.registrationBtn.setText('Войти')
        self.alternativeBtn.setVisible(False)
        self.super_alternativeBtn.setVisible(True)
        self.patronym_descryption_label.setVisible(False)
        # Меняем виджет регистрации на виджет входа

    def alt_enter(self):
        self.label.setVisible(True)
        self.label_2.setVisible(True)
        self.label_3.setVisible(True)
        self.label_4.setVisible(True)
        self.label_5.setVisible(True)
        self.label_6.setVisible(True)
        self.name_line.setVisible(True)
        self.surname_line.setVisible(True)
        self.otchestvo_line.setVisible(True)
        self.login_line.setText('Введите логин')
        self.password_line.setText('Введите пароль')
        self.trfa = False
        self.registrationBtn.setText('Войти')
        self.alternativeBtn.setVisible(True)
        self.super_alternativeBtn.setVisible(False)
        self.name_lable.setVisible(True)
        self.surname_lable.setVisible(True)
        self.patronym_label.setVisible(True)
        self.login_label.setVisible(True)
        self.password_label.setVisible(True)
        self.patronym_descryption_label.setVisible(True)
        # Возращаем виджет регистрации

    def stat(self):
        if not self.trfa:  # проверка на то, что мы регистрируемся, а не входим
            if self.check_password(self.password_line.text()) != '':
                self.statusbar.showMessage(self.check_password(self.password_line.text()))
            else:
                self.cur = self.con.cursor()
                self.cur.execute('''
                CREATE TABLE IF NOT EXISTS people (
                name TEXT,
                surname TEXT,
                patronym TEXT,
                login TEXT,
                password TEXT
                )
                ''')
                self.cur.execute('INSERT INTO people(name, surname, patronym, login, password) VALUES (?, ?, ?, ?, ?)',
                                 (
                                     self.name_line.text(), self.surname_line.text(), self.otchestvo_line.text(),
                                     self.login_line.text(), self.password_line.text()))
                self.con.commit()
                self.statusbar.showMessage('Вы зарегистрировались!')
        else:  # Проверка на то, что мы входим, а не регистрируемся
            if self.login_line.text() in [i[0] for i in self.cur.execute(
                    'SELECT login from people').fetchall()] and self.password_line.text() in [i[0] for i in
                                                                                              self.cur.execute(
                                                                                                  'SELECT password '
                                                                                                  'from '
                                                                                                  'people').fetchall()]:
                self.statusbar.showMessage('Вы вошли!')
            else:
                self.statusbar.showMessage("Такой пользователь не обнаружен")

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.trfa = False
        self.con = sqlite3.connect('films_db.sqlite')

    def spli(self, ke, le):  # Функция для помощи проверки пароля
        threes = []
        for i in range(len(ke)):
            for j in range(len(ke[i])):
                s = ke[i][j:j + le]
                if len(s) == le:
                    threes.append(s)
        return threes

    def check_password(self, pas: str):  # Проверяю пароль на соблюдение его основных критериев
        all_threes = []
        error = ''
        QWERTY = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        YTSUK = ["йцукенгшщзхъ", "фывапролджэё", "ячсмитьбю"]
        if len(pas) <= 8:
            error = 'Length Error'
        if not any(s.isdigit() for s in pas):
            error = 'Digit error'
        if not any(s.isupper() for s in pas):
            error = 'Letter error'

        if not any(s.islower() for s in pas):
            error = 'Letter error'

        passs = set()
        pasw = pas.lower()
        all_threes.extend(self.spli(QWERTY, 3))
        all_threes.extend(self.spli(YTSUK, 3))
        all_threes.extend('жэё')
        for i in range(len(pas) - 2):
            s = pasw[i:i + 3]
            passs.add(s)
        if passs.intersection(set(all_threes)):
            error = 'Sequence Error'
        if (self.login_line.text() == '' or self.surname_line.text() == '' or
                self.name_line.text() == '' or self.password_line.text() == '' or self.otchestvo_line.text() == ''):
            error = 'Not enough data'
        return error

    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__()
        self.con.close()  # Закрываю базу данных вместе с закрытием программы


def except_hook(cls, exception, traceback):  #
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook
app = QApplication(sys.argv)
ex = Registration()
ex.show()
sys.exit(app.exec())
'''cd pythonProject2\corrupt_films_db.sqlite
                echo ".dump"|sqlite3 corrupt_films_db.sqlite|sqlite3 repaired_corrupt_films_db.sqlite
                mv corrupt_films_db.sqlite corrupt_corrupt_films_db.sqlite
                mv repaired_corrupt_films_db.sqlite corrupt_films_db.sqlite'''  # Чиню базу данных, которая может сломаться
