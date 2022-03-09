# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designBIuLtx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(841, 582)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(540, 10, 20, 541))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 258, 541))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.events_list_label = QLabel(self.layoutWidget)
        self.events_list_label.setObjectName(u"events_list_label")
        self.events_list_label.setLayoutDirection(Qt.LeftToRight)
        self.events_list_label.setTextFormat(Qt.PlainText)
        self.events_list_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.events_list_label)

        self.events_list = QListView(self.layoutWidget)
        self.events_list.setObjectName(u"events_list")

        self.verticalLayout_2.addWidget(self.events_list)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(259, 10, 31, 541))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(280, 10, 258, 541))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.new_event_label = QLabel(self.layoutWidget1)
        self.new_event_label.setObjectName(u"new_event_label")
        self.new_event_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.new_event_label)

        self.new_event_field = QTextEdit(self.layoutWidget1)
        self.new_event_field.setObjectName(u"new_event_field")
        self.new_event_field.setLocale(QLocale(QLocale.Russian, QLocale.Russia))

        self.verticalLayout.addWidget(self.new_event_field)

        self.dateTimeEdit = QDateTimeEdit(self.layoutWidget1)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.verticalLayout.addWidget(self.dateTimeEdit)

        self.new_event_btn = QPushButton(self.layoutWidget1)
        self.new_event_btn.setObjectName(u"new_event_btn")

        self.verticalLayout.addWidget(self.new_event_btn)

        self.line_4 = QFrame(self.layoutWidget1)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.org_id_input_field = QTextEdit(self.layoutWidget1)
        self.org_id_input_field.setObjectName(u"org_id_input_field")

        self.horizontalLayout_5.addWidget(self.org_id_input_field)

        self.org_role_input_field = QTextEdit(self.layoutWidget1)
        self.org_role_input_field.setObjectName(u"org_role_input_field")

        self.horizontalLayout_5.addWidget(self.org_role_input_field)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.org_firstname_input_field = QTextEdit(self.layoutWidget1)
        self.org_firstname_input_field.setObjectName(u"org_firstname_input_field")

        self.horizontalLayout_4.addWidget(self.org_firstname_input_field)

        self.org_lastname_input_field = QTextEdit(self.layoutWidget1)
        self.org_lastname_input_field.setObjectName(u"org_lastname_input_field")

        self.horizontalLayout_4.addWidget(self.org_lastname_input_field)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.org_phone_input_field = QTextEdit(self.layoutWidget1)
        self.org_phone_input_field.setObjectName(u"org_phone_input_field")

        self.verticalLayout.addWidget(self.org_phone_input_field)

        self.org_email_input_field = QTextEdit(self.layoutWidget1)
        self.org_email_input_field.setObjectName(u"org_email_input_field")

        self.verticalLayout.addWidget(self.org_email_input_field)

        self.org_add_btn = QPushButton(self.layoutWidget1)
        self.org_add_btn.setObjectName(u"org_add_btn")

        self.verticalLayout.addWidget(self.org_add_btn)

        self.line_2 = QFrame(self.layoutWidget1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.delete_label = QLabel(self.layoutWidget1)
        self.delete_label.setObjectName(u"delete_label")
        self.delete_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.delete_label)

        self.delete_event_field = QTextEdit(self.layoutWidget1)
        self.delete_event_field.setObjectName(u"delete_event_field")

        self.verticalLayout.addWidget(self.delete_event_field)

        self.delete_event_btn = QPushButton(self.layoutWidget1)
        self.delete_event_btn.setObjectName(u"delete_event_btn")

        self.verticalLayout.addWidget(self.delete_event_btn)

        self.line_3 = QFrame(self.layoutWidget1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.safe_label = QLabel(self.layoutWidget1)
        self.safe_label.setObjectName(u"safe_label")
        self.safe_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.safe_label)

        self.safe_btn = QPushButton(self.layoutWidget1)
        self.safe_btn.setObjectName(u"safe_btn")

        self.verticalLayout.addWidget(self.safe_btn)

        self.line_8 = QFrame(self.layoutWidget1)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_8)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.safe_event_id_field = QTextEdit(self.layoutWidget1)
        self.safe_event_id_field.setObjectName(u"safe_event_id_field")

        self.horizontalLayout_3.addWidget(self.safe_event_id_field)

        self.safe_event_btn = QPushButton(self.layoutWidget1)
        self.safe_event_btn.setObjectName(u"safe_event_btn")

        self.horizontalLayout_3.addWidget(self.safe_event_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(560, 10, 271, 541))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.add_participant_event_id_input_field = QTextEdit(self.verticalLayoutWidget)
        self.add_participant_event_id_input_field.setObjectName(u"add_participant_event_id_input_field")

        self.verticalLayout_3.addWidget(self.add_participant_event_id_input_field)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.participant_firstname_input_field = QTextEdit(self.verticalLayoutWidget)
        self.participant_firstname_input_field.setObjectName(u"participant_firstname_input_field")

        self.horizontalLayout_6.addWidget(self.participant_firstname_input_field)

        self.participant_lastname_input_field = QTextEdit(self.verticalLayoutWidget)
        self.participant_lastname_input_field.setObjectName(u"participant_lastname_input_field")

        self.horizontalLayout_6.addWidget(self.participant_lastname_input_field)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.participant_phone_input_field = QTextEdit(self.verticalLayoutWidget)
        self.participant_phone_input_field.setObjectName(u"participant_phone_input_field")

        self.verticalLayout_3.addWidget(self.participant_phone_input_field)

        self.participant_email_input_field = QTextEdit(self.verticalLayoutWidget)
        self.participant_email_input_field.setObjectName(u"participant_email_input_field")

        self.verticalLayout_3.addWidget(self.participant_email_input_field)

        self.participant_push_btn = QPushButton(self.verticalLayoutWidget)
        self.participant_push_btn.setObjectName(u"participant_push_btn")

        self.verticalLayout_3.addWidget(self.participant_push_btn)

        self.line_6 = QFrame(self.verticalLayoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_6)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.consumables_envent_id_input_field = QTextEdit(self.verticalLayoutWidget)
        self.consumables_envent_id_input_field.setObjectName(u"consumables_envent_id_input_field")

        self.horizontalLayout_7.addWidget(self.consumables_envent_id_input_field)

        self.consumables_volume_input_field = QTextEdit(self.verticalLayoutWidget)
        self.consumables_volume_input_field.setObjectName(u"consumables_volume_input_field")

        self.horizontalLayout_7.addWidget(self.consumables_volume_input_field)

        self.consumables_unit_input_field = QTextEdit(self.verticalLayoutWidget)
        self.consumables_unit_input_field.setObjectName(u"consumables_unit_input_field")

        self.horizontalLayout_7.addWidget(self.consumables_unit_input_field)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.consumables_name_input_field = QTextEdit(self.verticalLayoutWidget)
        self.consumables_name_input_field.setObjectName(u"consumables_name_input_field")

        self.verticalLayout_3.addWidget(self.consumables_name_input_field)

        self.consumables_push_btn = QPushButton(self.verticalLayoutWidget)
        self.consumables_push_btn.setObjectName(u"consumables_push_btn")

        self.verticalLayout_3.addWidget(self.consumables_push_btn)

        self.line_9 = QFrame(self.verticalLayoutWidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_9)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.consumables_event_delete_id_input_field = QTextEdit(self.verticalLayoutWidget)
        self.consumables_event_delete_id_input_field.setObjectName(u"consumables_event_delete_id_input_field")

        self.horizontalLayout_8.addWidget(self.consumables_event_delete_id_input_field)

        self.consumables_delete_id_input_field = QTextEdit(self.verticalLayoutWidget)
        self.consumables_delete_id_input_field.setObjectName(u"consumables_delete_id_input_field")

        self.horizontalLayout_8.addWidget(self.consumables_delete_id_input_field)

        self.consumables_delete_btn = QPushButton(self.verticalLayoutWidget)
        self.consumables_delete_btn.setObjectName(u"consumables_delete_btn")

        self.horizontalLayout_8.addWidget(self.consumables_delete_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.line_10 = QFrame(self.verticalLayoutWidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_10)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.org_delete_event_id_input_field = QTextEdit(self.verticalLayoutWidget)
        self.org_delete_event_id_input_field.setObjectName(u"org_delete_event_id_input_field")

        self.horizontalLayout.addWidget(self.org_delete_event_id_input_field)

        self.org_delete_id_input_field = QTextEdit(self.verticalLayoutWidget)
        self.org_delete_id_input_field.setObjectName(u"org_delete_id_input_field")

        self.horizontalLayout.addWidget(self.org_delete_id_input_field)

        self.org_delete_btn = QPushButton(self.verticalLayoutWidget)
        self.org_delete_btn.setObjectName(u"org_delete_btn")

        self.horizontalLayout.addWidget(self.org_delete_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.line_7 = QFrame(self.verticalLayoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_7)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.participant_delete_event_id_input_field = QTextEdit(self.verticalLayoutWidget)
        self.participant_delete_event_id_input_field.setObjectName(u"participant_delete_event_id_input_field")

        self.horizontalLayout_2.addWidget(self.participant_delete_event_id_input_field)

        self.participant_delete_id_input_field = QTextEdit(self.verticalLayoutWidget)
        self.participant_delete_id_input_field.setObjectName(u"participant_delete_id_input_field")

        self.horizontalLayout_2.addWidget(self.participant_delete_id_input_field)

        self.participant_delete_btn = QPushButton(self.verticalLayoutWidget)
        self.participant_delete_btn.setObjectName(u"participant_delete_btn")

        self.horizontalLayout_2.addWidget(self.participant_delete_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.events_list_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u0431\u044b\u0442\u0438\u0439", None))
        self.new_event_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u043e\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u0435", None))
        self.new_event_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.new_event_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u0430", None))
        self.org_id_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.org_role_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u043b\u044c \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u0430", None))
        self.org_firstname_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.org_lastname_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.org_phone_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.org_email_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0447\u0430\u044f \u043f\u043e\u0447\u0442\u0430", None))
        self.org_add_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u043e\u0431\u044b\u0442\u0438\u0435", None))
        self.delete_event_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id \u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0434\u043b\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f", None))
        self.delete_event_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.safe_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.safe_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442 \u043f\u043e \u0441\u043e\u0431\u044b\u0442\u0438\u044e", None))
        self.safe_event_id_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.safe_event_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u0430", None))
        self.add_participant_event_id_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.participant_firstname_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.participant_lastname_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.participant_phone_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.participant_email_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0447\u0430\u044f \u043f\u043e\u0447\u0442\u0430", None))
        self.participant_push_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u0435", None))
        self.consumables_envent_id_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.consumables_volume_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043b\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.consumables_unit_input_field.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0448\u0442</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.consumables_unit_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0435\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.consumables_name_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0440\u0435\u0431\u0443\u0435\u043c\u043e\u0433\u043e", None))
        self.consumables_push_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u0435", None))
        self.consumables_event_delete_id_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.consumables_delete_id_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.consumables_delete_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u0430", None))
        self.org_delete_event_id_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.org_delete_id_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0442\u043e\u0440\u0430", None))
        self.org_delete_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u0430", None))
        self.participant_delete_event_id_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id \u0441\u043e\u0431\u044b\u0442\u0438\u044f", None))
        self.participant_delete_id_input_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u0430", None))
        self.participant_delete_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

