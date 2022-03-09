import sqlite3
from os import getcwd, remove
from sys import argv

from ui_design import *

db_path = getcwd()
db_file = 'data.sqlite'


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


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dateTimeEdit.setDate(QDate.currentDate())
        self.dateTimeEdit.setTime(QTime.currentTime())
        self.dateTimeEdit.setDisplayFormat("dd-MM-yyyy hh:mm")

        self.safe_btn.clicked.connect(self.safe_report)
        self.safe_btn_flag = False
        self.safe_event_btn.clicked.connect(self.safe_event)
        self.safe_event_btn_flag = False

        self.new_event_btn.clicked.connect(self.add_event)
        self.delete_event_btn.clicked.connect(self.delete_event)

        self.org_add_btn.clicked.connect(self.add_org)
        self.org_delete_btn.clicked.connect(self.delete_org)

        self.participant_push_btn.clicked.connect(self.add_participant)
        self.participant_delete_btn.clicked.connect(self.delete_participant)

        self.consumables_push_btn.clicked.connect(self.add_consumables)
        self.consumables_delete_btn.clicked.connect(self.delete_consumables)

        self.db_connection = create_connection(f'{db_path}/{db_file}')

        create_events_table = '\
create table if not exists events \
( \
    id   INTEGER \
    primary key autoincrement, \
    date DATE not null, \
    time TIME, \
    type TEXT \
);'

        create_consumables_table = '\
create table if not exists обеспечение \
( \
    event_id integer  not null, \
    name     char(64) not null, \
    volume   integer, \
    unit     char(16) default \'шт\', \
    id       integer  not null \
);'

        create_orgs_table = '\
create table if not exists организаторы \
( \
    event_id     integer  not null, \
    firstname    char(64) not null, \
    lastname     char(64) not null, \
    phone_number char(16), \
    email        char(64), \
    role         char(64), \
    id           integer  not null \
);'

        create_participants_table = '\
create table if not exists участники \
( \
    event_id     integer  not null, \
    firstname    char(64) not null, \
    lastname     char(64) not null, \
    phone_number char(16), \
    email        char(64), \
    id           integer  not null \
);'

        init_query = [create_events_table, create_consumables_table,
                      create_orgs_table, create_participants_table]

        [execute_query(self.db_connection, i) for i in init_query]

        self.update_events_list()

    def safe_report(self, filename=None):
        print(filename)
        events = execute_read_query(
            self.db_connection, "SELECT id FROM events")
        if filename == False:
            filename = QFileDialog.getSaveFileName()[0]
        else:
            filename = 'tmp'
        f = open(filename, 'w')
        f.close()
        for event in events:
            self.safe_event(event[0], filename)

    def safe_event(self, eid=None, filename=None):
        if eid == None:
            eid = self.safe_event_id_field.toPlainText()

        event = execute_read_query(
            self.db_connection, f'select date, time, type from events where id = {eid}')
        orgs = execute_read_query(
            self.db_connection, f'select id, firstname, lastname, phone_number, email, role from организаторы where event_id = {eid}')
        parts = execute_read_query(
            self.db_connection, f'select id, firstname, lastname, phone_number, email from участники where event_id = {eid}')
        consums = execute_read_query(
            self.db_connection, f'select id, name, volume, unit from обеспечение where event_id = {eid}')

        if filename == None:
            filename = QFileDialog.getSaveFileName()[0]
            perm = 'w'
        else:
            perm = 'a'

        with open(filename, perm, encoding='utf8') as f:
            try:
                print(
                    f'{("= " + str(eid) + " ") if filename != None else ""}= {event[0][-1]} =', file=f)
            except IndexError:
                return
            print(f'дата: {event[0][0]}', file=f)
            print(f'время: {event[0][1]}', file=f)

            print('Организаторы:', file=f)
            for org in orgs:
                print(f'\t{org[0]}. {org[1]} {org[2]}: {org[-1]}', file=f)
                if org[3] != '':
                    print(f'\t\tтелефон: {org[3]}', file=f)
                if org[4] != '':
                    print(f'\t\tпочта: {org[4]}', file=f)

            print(f'Участники:', file=f)
            for part in parts:
                print(f'\t{part[0]}. {part[1]} {part[2]}', file=f)
                if part[3] != '':
                    print(f'\t\tтелефон: {part[3]}', file=f)
                if part[4] != '':
                    print(f'\t\tпочта: {part[4]}', file=f)

            print('Обеспечение:', file=f)
            for consum in consums:
                print(f'\t{consum[0]}. {consum[1]}', end='', file=f)
                if consum[2] != '':
                    print(f' ({consum[2]}{consum[3]})', file=f, end='')
                print(file=f)

            print('='*(len(event[0][-1])+4), file=f, end='\n'*2)

    def add_event(self):
        date, time = self.dateTimeEdit.date().toString(
            "dd-MM-yyyy"), self.dateTimeEdit.time().toString("hh:mm")
        event_name = self.new_event_field.toPlainText()

        q = f'\
INSERT INTO events (date, time, type)\
VALUES (\'{date}\', \'{time}\', \'{event_name}\')'

        print(', '.join([date, time, event_name]))
        execute_query(self.db_connection, q)
        self.update_events_list()

    def delete_event(self):
        field_id = self.delete_event_field.toPlainText()
        q = f'DELETE FROM events WHERE id is {field_id}'
        execute_query(self.db_connection, q)
        self.update_events_list()

    def update_events_list(self):
        self.safe_report('tmp')
        with open('tmp', 'r') as f:
            model = QStandardItemModel()
            self.events_list.setModel(model)
            bold_font = QFont()
            bold_font.setBold(True)
            for line in f.readlines():
                item = QStandardItem(line.strip('\n'))
                if line.startswith('='):
                    item.setFont(bold_font)
                model.appendRow(item)
        remove('tmp')

    def add_org(self):
        eid = self.org_id_input_field.toPlainText()
        role = self.org_role_input_field.toPlainText()
        fname = self.org_firstname_input_field.toPlainText()
        lname = self.org_lastname_input_field.toPlainText()
        phone = self.org_phone_input_field.toPlainText()
        email = self.org_email_input_field.toPlainText()

        try:
            id = int(execute_read_query(self.db_connection, f'\
select id \
from организаторы \
where event_id = {eid} \
order by id desc \
limit 1')[0][0]) + 1
        except IndexError:
            id = 0

        q = f'\
insert into организаторы (event_id, firstname, lastname, phone_number, email, role, id) \
VALUES ({eid}, \'{fname}\', \'{lname}\', \'{phone}\', \'{email}\', \'{role}\', {id})'
        print(q)
        execute_query(self.db_connection, q)
        print('Org table updated')
        self.update_events_list()

    def delete_org(self):
        eid = self.org_delete_event_id_input_field.toPlainText()
        id = self.org_delete_id_input_field.toPlainText()
        q = f'\
delete \
from организаторы \
WHERE id = {id} \
  and event_id = {eid}'
        print(q)
        execute_query(self.db_connection, q)
        print('Org table updated')
        self.update_events_list()

    def add_participant(self):
        eid = self.add_participant_event_id_input_field.toPlainText()
        fname = self.participant_firstname_input_field.toPlainText()
        lname = self.participant_lastname_input_field.toPlainText()
        phone = self.participant_phone_input_field.toPlainText()
        email = self.participant_email_input_field.toPlainText()

        try:
            id = int(execute_read_query(self.db_connection, f'\
select id \
from участники \
where event_id = {eid} \
order by id desc \
limit 1')[0][0]) + 1
        except IndexError:
            id = 0

        q = f'\
insert into участники (event_id, firstname, lastname, phone_number, email, id) \
VALUES ({eid}, \'{fname}\', \'{lname}\', \'{phone}\', \'{email}\', {id})'
        print(q)
        execute_query(self.db_connection, q)
        print('Participant table updated')
        self.update_events_list()

    def delete_participant(self):
        eid = self.participant_delete_event_id_input_field.toPlainText()
        id = self.participant_delete_id_input_field.toPlainText()
        q = f'\
delete \
from участники \
WHERE id = {id} \
  and event_id = {eid}'
        print(q)
        execute_query(self.db_connection, q)
        print('Participant table updated')
        self.update_events_list()

    def add_consumables(self):
        eid = self.consumables_envent_id_input_field.toPlainText()
        vol = self.consumables_volume_input_field.toPlainText()
        unit = self.consumables_unit_input_field.toPlainText()
        name = self.consumables_name_input_field.toPlainText()

        try:
            id = int(execute_read_query(self.db_connection, f'\
select id \
from обеспечение \
where event_id = {eid} \
order by id desc \
limit 1')[0][0]) + 1
        except IndexError:
            id = 0

        q = f'\
insert into обеспечение (event_id, name, volume, unit, id) \
VALUES ({eid}, \'{name}\', \'{vol}\', \'{unit}\', {id})'
        print(q)
        execute_query(self.db_connection, q)
        print('Consumables table updated')
        self.update_events_list()

    def delete_consumables(self):
        eid = self.consumables_event_delete_id_input_field.toPlainText()
        id = self.consumables_delete_id_input_field.toPlainText()
        q = f'\
delete \
from обеспечение \
WHERE id = {id} \
  and event_id = {eid}'
        print(q)
        execute_query(self.db_connection, q)
        print('Consumables table updated')
        self.update_events_list()


def main():
    app = QApplication(argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
