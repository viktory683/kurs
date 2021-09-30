import sqlite3
from os import getcwd
from sys import argv

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QDate, QTime

import design


def create_connection(path: str):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred\nCheck path to a database\n{path}")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dateTimeEdit.setDate(QDate.currentDate())
        self.dateTimeEdit.setTime(QTime.currentTime())
        self.dateTimeEdit.setDisplayFormat("dd-MM-yyyy hh:mm")
        self.new_event_field.setPlaceholderText("Введите название события")

        self.safe_btn.clicked.connect(self.safe_report)

        self.new_event_btn.clicked.connect(self.add_event)

        self.delete_event_field.setPlaceholderText("Введите id события")
        self.delete_evenet_btn.clicked.connect(self.delete_event)

        self.path_to_database = getcwd() + '/data.sqlite'
        self.database_connection = create_connection(self.path_to_database)

        create_users_table = """
            CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            time TIME,
            type TEXT);
            """

        execute_query(self.database_connection, create_users_table)

        self.update_events_list()

    def safe_report(self):
        events = execute_read_query(self.database_connection, "SELECT * FROM events")
        with open(QtWidgets.QFileDialog.getSaveFileName()[0], 'w', encoding='utf-8') as f:
            for event in events:
                print(' '.join([str(e) for e in event]), file=f)

    def add_event(self):
        date, time = self.dateTimeEdit.date().toString("dd-MM-yyyy"), self.dateTimeEdit.time().toString("hh:mm")
        event_name = self.new_event_field.toPlainText()

        queue = f"""
            INSERT INTO events (date, time, type)
            VALUES ('{date}', '{time}', '{event_name}')
        """

        print(', '.join([date, time, event_name]))
        execute_query(self.database_connection, queue)
        self.update_events_list()

    def delete_event(self):
        field_id = self.delete_event_field.toPlainText()
        queue = "DELETE FROM events WHERE id is " + str(field_id)
        execute_query(self.database_connection, queue)
        self.update_events_list()

    def update_events_list(self):
        print("UPDATE")
        query = "SELECT * from events"
        events = execute_read_query(self.database_connection, query)

        model = QtGui.QStandardItemModel()
        self.events_list.setModel(model)
        item = QtGui.QStandardItem(" id |    Дата    | Время | Название")
        bold_font = QtGui.QFont()
        bold_font.setBold(True)
        item.setFont(bold_font)
        model.appendRow(item)
        for event in events:
            t = ' ' * (3 - len(str(event[0])))
            item = QtGui.QStandardItem(t + (' | '.join([str(e) for e in event])))
            model.appendRow(item)


def main():
    app = QtWidgets.QApplication(argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
