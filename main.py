import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTextBrowser, QLabel, QComboBox, QTableWidget, QLineEdit,QTableWidgetItem, QPlainTextEdit
import pandas as pd

data = pd.read_csv('https://docs.google.com/spreadsheets/d/1Pr-NpbDcIzWnSPU7--uokU7R7Gtj2Xg8YnstJ0pnU1E/export?format=csv')
vebinar = data[['Вебинар']]
z = data[['Пункты']]
z2 = data[['Пункты_зума']]
zoom = data[['Зум']]
n = 0

mas = [""] * 50
mis = [""] * 50

num = []
num2 = []


class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')
        self.setMinimumWidth(1286)
        self.setMinimumHeight(459)

        self.t = QPlainTextEdit(self)
        self.t.setGeometry(579, 10, 351, 391)

        self.t2 = QPlainTextEdit(self)
        self.t2.setGeometry(940, 10, 331, 391)


        self.combo = QComboBox(self)
        self.combo.setGeometry(10, 420, 181, 41)
        self.combo.addItem("Вебинар")
        self.combo.addItem("Зум")

        self.primenit = QPushButton(self)
        self.primenit.setGeometry(200, 420, 171, 41)
        self.primenit.setText("Применить")

        self.rez = QPushButton(self)
        self.rez.setGeometry(380, 420, 170, 40)
        self.rez.setText("Показать")

        self.save = QPushButton(self)
        self.save.setGeometry(560, 420, 170, 40)
        self.save.setText("Сохранить")

        self.but = QPushButton(self)
        self.but.setGeometry(740, 420, 170, 40)
        self.but.setText("Добавить")

        self.table = QTableWidget(self)
        self.table.setGeometry(10, 10, 560, 391)
        self.table.setColumnCount(2)
        self.table.setRowCount(50)
        self.table.setHorizontalHeaderLabels(["Пункты оценки","+/-"])
        self.table.setColumnWidth(0, 400)
        self.table.setColumnWidth(1, 70)
        #self.table.horizontalHeader().setStretchLastSection(True)

        self.primenit.clicked.connect(self.on_click)
        self.rez.clicked.connect(self.on_click2)
        self.save.clicked.connect(self.on_click3)
        self.but.clicked.connect(self.on_click4)

    def on_click4(self):
        tex = self.t2.toPlainText()
        if tex != "":
            t = self.t.toPlainText()
            t = t + "\n" + tex
            self.t.clear()
            self.t.appendPlainText(t)


    def on_click3(self):
        tex = self.t.toPlainText()
        t = tex.split("\n")
        if self.combo.currentText() == "Вебинар":
            for i in range(len(num)):
                s = t[i]
                s = s[3:]
                t[i] = s
                if t[i] != vebinar.iloc[num[0]][0]:
                    vebinar.iloc[num[0]][0] = t[i]
                num.pop(0)
        else:
            for i in range(len(num)):
                s = t[i]
                s = s[3:]
                t[i] = s
                if t[i] != zoom.iloc[num[0]][0]:
                    zoom.iloc[num[0]][0] = t[i]
                num.pop(0)

    def on_click2(self):
        self.t.clear()
        mas = [""] * 50
        num.clear()
        if self.combo.currentText() == "Вебинар":
            n = int(vebinar.shape[0]) - 2
            for i in range(n):
                if self.table.item(i, 1).text() == "1":
                    mas[i] = vebinar.iloc[i][0]
                    num.append(i)
        else:
            n = int(zoom.shape[0])
            for i in range(n):
                if self.table.item(i, 1).text() == "1":
                    mas[i] = zoom.iloc[i][0]
                    num.append(i)
        kol = 1
        for j in range(n):
            if mas[j] != "":
                self.t.appendPlainText(str(kol) + ". " + mas[j])
                kol += 1


    def on_click(self):
        if self.combo.currentText() == "Вебинар":
            n = int(vebinar.shape[0]) - 2
            for i in range(n):
                p2 = z.iloc[i]
                self.table.setItem(i, 0, QTableWidgetItem(p2[0]))
                self.table.setItem(i, 1, QTableWidgetItem(""))
        elif self.combo.currentText() == "Зум":
            n = int(zoom.shape[0])
            for i in range(n):
                p2 = z2.iloc[i]
                self.table.setItem(i, 0, QTableWidgetItem(p2[0]))
                self.table.setItem(i, 1, QTableWidgetItem(""))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window2()
    w.show()  # открытие 1 окна
    sys.exit(app.exec_())
