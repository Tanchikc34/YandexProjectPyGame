import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.titles = None
        self.setFixedSize(810, 440)
        self.setWindowTitle('Кофе')
        # Подключение кнопки к обработчику
        self.pushButton.clicked.connect(self.item_edit)
        # Подключение к БД и создание курсора
        self.connection = sqlite3.connect("coffee")
        self.cursor = self.connection.cursor()
        # Выравнивание окна
        frame_gm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        center_point = QApplication.desktop().screenGeometry(screen).center()
        frame_gm.moveCenter(center_point)
        self.move(frame_gm.topLeft())

    def item_edit(self):
        # Получили результат запроса
        result = self.cursor.execute("SELECT name, degree, which, description, price, size FROM coffee").fetchall()
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(6)
        # Названия колонок
        self.tableWidget.setHorizontalHeaderLabels(["Название", "Степень прожарки", "Какой",
                                                   "Описание вкуса", "Цена", "Объем"])
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.resizeRowsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec_())
