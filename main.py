import sqlite3

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import QDate, QTime
import design

import sys


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.dateTimeEdit.date().__format__("dd-mm-yyyy")
        # self.dateTimeEdit.time().__format__("hh:mm:ss")
        self.dateTimeEdit.setDate(QDate.currentDate())
        self.dateTimeEdit.setTime(QTime.currentTime())
        self.dateTimeEdit.setDisplayFormat("dd-MM-yyyy hh:mm:ss")
        self.new_event_field.setPlaceholderText("Введите название события")

        self.safe_btn.clicked.connect(self.safe_rept)

        self.new_event_btn.clicked.connect(self.add_event)

        self.delete_event_field.setPlaceholderText("Введите id события")
        self.delete_evenet_btn.clicked.connect(self.delete_event)

        self.path_to_database = "/home/god/Documents/kurs/data.sqlite"
        self.database_connection = self.create_connection(self.path_to_database)

        create_users_table = """
            CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            time TIME,
            type TEXT);
            """
        self.execute_query(self.database_connection, create_users_table)

        self.update_events_list()

    def safe_rept(self):
        f = QtWidgets.QFileDialog.getSaveFileName()
        f = f[0]

        events = self.execute_read_query(self.database_connection, "SELECT * FROM events")
        with open(f, 'w', encoding="utf-8") as outFile:
            for event in events:
                print(str(event[0]) + " " + str(event[1]) + " " + str(event[2]) + " " + str(event[3]), file=outFile)

    def add_event(self):
        event_name = self.new_event_field.toPlainText()
        queue = "INSERT INTO events (date, time, type) VALUES (\'"
        queue += self.dateTimeEdit.date().toString("yyyy-MM-dd")
        queue += "\', \'" 
        queue += self.dateTimeEdit.time().toString("hh:mm:ss")
        queue += "\', \'" + event_name + "\')"
        print(self.dateTimeEdit.date().toString("yyyy-MM-dd") + ", " + self.dateTimeEdit.time().toString("hh:mm:ss") + ", " + event_name)
        self.execute_query(self.database_connection, queue)
        self.update_events_list()

    def delete_event(self):
        id = self.delete_event_field.toPlainText()
        queue = "DELETE FROM events WHERE id is " + str(id)
        self.execute_query(self.database_connection, queue)
        self.update_events_list()

    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred\nCheck path to a database\n{path}")

        return connection

    def execute_query(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

    def update_events_list(self):
        print("UPDATE")
        query = "SELECT * from events"
        events = self.execute_read_query(self.database_connection, query)

        model = QtGui.QStandardItemModel()
        self.events_list.setModel(model)
        item = QtGui.QStandardItem("id  |     Дата     |   Время   |   Название")
        bold_font = QtGui.QFont()
        bold_font.setBold(True)
        item.setFont(bold_font)
        model.appendRow(item)
        for event in events:
            item = QtGui.QStandardItem(str(event[0]) + "  | " + str(event[1]) + " | " + str(event[2]) + " | " + str(event[3]))
            model.appendRow(item)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
