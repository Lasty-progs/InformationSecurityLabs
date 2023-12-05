from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QWidget, QCheckBox, QGridLayout, QMessageBox
from math import log, ceil
from random import randint

class Solve:
    def __init__(self):
        self.create_layout()


    def create_layout(self):
        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.P_field = QLineEdit()
        self.V_field = QLineEdit()
        self.T_field = QLineEdit()
        self.latin_upper_field = QCheckBox()
        self.latin_lower_field = QCheckBox()
        self.russian_upper_field = QCheckBox()
        self.russian_lower_field = QCheckBox()
        self.symbols_field = QCheckBox()
        self.numbers_field = QCheckBox()
        self.generate_pass = QPushButton("Сформировать пароль")
        self.generate_pass.clicked.connect(self.generator)
        
        self.layout.addWidget(QLabel("P(вероятность)"),0, 0)
        self.layout.addWidget(QLabel("V(скорость перебора)"),1, 0)
        self.layout.addWidget(QLabel("P(срок действия пароля)"),2, 0)
        self.layout.addWidget(self.P_field, 0, 1)
        self.layout.addWidget(self.V_field, 1, 1)
        self.layout.addWidget(self.T_field, 2, 1)

        self.layout.addWidget(QLabel(" "*10), 0, 2)

        self.layout.addWidget(self.latin_upper_field, 0, 3)
        self.layout.addWidget(self.latin_lower_field, 1, 3)
        self.layout.addWidget(self.russian_upper_field, 2, 3)
        self.layout.addWidget(self.russian_lower_field, 3, 3)
        self.layout.addWidget(self.symbols_field, 4, 3)
        self.layout.addWidget(self.numbers_field, 5, 3)
        
        self.layout.addWidget(QLabel("Латинские большие"),0, 4)
        self.layout.addWidget(QLabel("Латинские Маленькие"),1, 4)
        self.layout.addWidget(QLabel("Русские большие"),2, 4)
        self.layout.addWidget(QLabel("Русские маленькие"),3, 4)
        self.layout.addWidget(QLabel("Символы"),4, 4)
        self.layout.addWidget(QLabel("Цифры"),5, 4)

        self.layout.addWidget(self.generate_pass, 5, 0)


    def generator(self):
        P = float(self.P_field.text())
        V = int(self.V_field.text())
        T = int(self.T_field.text())
        flags = [
            self.latin_upper_field.isChecked(),
            self.latin_lower_field.isChecked(),
            self.russian_upper_field.isChecked(),
            self.russian_lower_field.isChecked(),
            self.symbols_field.isChecked(),
            self.numbers_field.isChecked()
            ]

        outs = self.logics(P, V, T, flags)

        alert = QMessageBox()
        alert.setText(f'''
S*(нижняя граница паролей) {outs[0]}
A(мощность алфавита) {outs[1]}
L(длина пароля) {outs[2]}
Пароль: {outs[3]}
''')
        alert.exec_()

    def logics(self, P:float, V:int, T:int , flags:list):
        A = ""
        alfabet = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                   "abcdefghijklmnopqrstuvwxyz",
                   "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ",
                   "абвгдеёжзийклмнопрстуфхцчшщьыъэюя",
                   "=+-_}{()*&^%$#@!;:.,><",
                   "0123456789"]
        for i, item in enumerate(alfabet):
            if flags[i]:
                A += item

        pswd = ""
        for i in range(ceil(log(V*T/P, len(A)))):
            pswd += A[randint(0, len(A)-1)]
        
        out = []
        out.append(str(V*T/P))
        out.append(str(len(A)))
        out.append(str(ceil(log(V*T/P, len(A)))))
        out.append(pswd)

        return out



app = QApplication([])
window = QWidget()

solve = Solve()

window.setLayout(solve.layout)
window.show()

app.exec_()