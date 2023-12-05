# var 4
import sqlite3 as db

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QWidget, QVBoxLayout, QMessageBox

def open_regiter():
    global window
    window.close()
    window = QWidget()
    window.setLayout(register.create_register())
    window.show()

def open_change():
    global window
    window.close()
    window = QWidget()
    window.setLayout(change.create_change())
    window.show()

def check_password(password:str) -> bool:
    AVALIABLE = "1234567890+-=*/"
    for i in password:
        if i not in AVALIABLE:
            return False
    return True * (len(password) == 5)

def check_eq_password(pass1:str, pass2:str) -> bool:
    for i in range(len(pass1)):
        if pass1[i] == pass2[i]:
            return False
    return True


# authentification
class Auth:
    def __init__(self):
        self.create_auth()


    def create_auth(self):
        self.layout = QVBoxLayout()

        self.login_field = QLineEdit()
        self.password_field = QLineEdit()
        self.go_to_register = QPushButton("Регистрация")
        self.go_to_register.clicked.connect(open_regiter)
        self.go_to_change = QPushButton("Сменить пароль")
        self.go_to_change.clicked.connect(open_change)
        self.enter_btn = QPushButton("Войти")
        self.enter_btn.clicked.connect(self.complete_enter)

        self.layout.addWidget(QLabel("Имя пользователя"))
        self.layout.addWidget(self.login_field)
        self.layout.addWidget(QLabel("Пароль"))
        self.layout.addWidget(self.password_field)
        self.layout.addWidget(self.enter_btn)
        self.layout.addWidget(self.go_to_register)
        self.layout.addWidget(self.go_to_change)

        return self.layout
    
    def complete_enter(self):
        global window
        global cursor
        global connection

        fields = [
            self.login_field.text(),
            self.password_field.text(),
        ]

        cursor.execute('SELECT username, password FROM Users')
        data = cursor.fetchall()
        users = []
        passwords = []
        for item in data:
            users.append(item[0])
            passwords.append(item[1])

        if fields[0] in users:
            if fields[1] == passwords[users.index(fields[0])]:
                alert = QMessageBox()
                alert.setText('Добро пожаловать ' + fields[0] + "\n Секретный ингредиент крабсбургера: ░░░░░")
                alert.exec_() 
            else:
                alert = QMessageBox()
                alert.setText('Неверный пароль')
                alert.exec_() 
        else:
            alert = QMessageBox()
            alert.setText('Пользователя не существует')
            alert.exec_()



# registration
class Register:
    def __init__(self):
        self.create_register()


    def create_register(self):
        self.layout = QVBoxLayout()

        self.login_field = QLineEdit()
        self.password_field = QLineEdit()
        self.surname_field = QLineEdit()
        self.name_field = QLineEdit()
        self.fathername_field = QLineEdit()
        self.datebirsday_field = QLineEdit()
        self.placebirsday_field = QLineEdit()
        self.telnumber_field = QLineEdit()
        self.save = QPushButton("Сохранить")
        self.save.clicked.connect(self.complete_reg)

        self.layout.addWidget(QLabel("Имя пользователя"))
        self.layout.addWidget(self.login_field)
        self.layout.addWidget(QLabel("Пароль"))
        self.layout.addWidget(self.password_field)
        self.layout.addWidget(QLabel(""))
        self.layout.addWidget(QLabel("Фамилия"))
        self.layout.addWidget(self.surname_field)
        self.layout.addWidget(QLabel("Имя"))
        self.layout.addWidget(self.name_field)
        self.layout.addWidget(QLabel("Отчество"))
        self.layout.addWidget(self.fathername_field)
        self.layout.addWidget(QLabel(""))
        self.layout.addWidget(QLabel("Дата Рождения"))
        self.layout.addWidget(self.datebirsday_field)
        self.layout.addWidget(QLabel("Место Рождения"))
        self.layout.addWidget(self.placebirsday_field)
        self.layout.addWidget(QLabel("Телефон"))
        self.layout.addWidget(self.telnumber_field)
        self.layout.addWidget(self.save)

        return self.layout

    def complete_reg(self):
        global window
        global cursor
        global connection

        cursor.execute('SELECT username FROM Users')
        users = cursor.fetchall()
        fields = [self.login_field.text(),
        self.password_field.text(),
        self.surname_field.text(),
        self.name_field.text(),
        self.fathername_field.text(),
        self.datebirsday_field.text(),
        self.placebirsday_field.text(),
        self.telnumber_field.text()]

        if (fields[0] not in users) and ("" not in fields) and check_password(fields[1]):
            cursor.execute("INSERT INTO Users (username, password, surname, name, fathername, birthday, birthplace, telnumber) VALUES (?,?,?,?,?,?,?,?)",
                           fields)
            connection.commit()
        else:
            alert = QMessageBox()
            alert.setText('Пользователь существует или присутствуют неправильно введённые данные')
            alert.exec_()
            
        window.close()
        window = QWidget()
        window.setLayout(auth.create_auth())
        window.show()

# create change pass
class Change:
    def __init__(self):
        self.create_change()

    def create_change(self):
        self.layout = QVBoxLayout()

        self.login_field = QLineEdit()
        self.current_password_field = QLineEdit()
        self.new_password_field = QLineEdit()
        self.check_new_password_field = QLineEdit()
        self.save = QPushButton("Сохранить")
        self.save.clicked.connect(self.complete_change)

        self.layout.addWidget(QLabel("Логин"))
        self.layout.addWidget(self.login_field)
        self.layout.addWidget(QLabel("Текущий пароль"))
        self.layout.addWidget(self.current_password_field)
        self.layout.addWidget(QLabel("Новый пароль"))
        self.layout.addWidget(self.new_password_field)
        self.layout.addWidget(QLabel("Новый пароль(повторить)"))
        self.layout.addWidget(self.check_new_password_field)
        self.layout.addWidget(self.save)

        return self.layout


    def complete_change(self):
        global window
        global cursor
        global connection
        
        fields = [
        self.login_field.text(),
        self.current_password_field.text(),
        self.new_password_field.text(),
        self.check_new_password_field.text(),
        ]
        cursor.execute('SELECT username, password FROM Users')
        data = cursor.fetchall()
        users = []
        passwords = []
        for item in data:
            users.append(item[0])
            passwords.append(item[1])

        if ("" not in fields) and (fields[0] in users) and (fields[2] == fields[3]) and (
            fields[1] == passwords[users.index(fields[0])]) and check_password(fields[2]) and check_eq_password(fields[1], fields[2]):
            cursor.execute('UPDATE Users SET password = ? WHERE username = ?', (fields[2], fields[0]))
            connection.commit()
        else: 
            alert = QMessageBox()
            alert.setText('Некорректный пароль')
            alert.exec_()

        window.close()
        window = QWidget()
        window.setLayout(auth.create_auth())
        window.show()


app = QApplication([])
window = QWidget()

auth = Auth()
change = Change()
register = Register()

connection = db.connect("users.sqlite3")
cursor = connection.cursor()

with open('create.sql', 'r') as sql_file:
    sql_script = sql_file.read()

cursor.execute(sql_script)
connection.commit()


window.setLayout(auth.layout)
window.show()

app.exec_()
