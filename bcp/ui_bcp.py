# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bcp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1232, 509)
        Form.setStyleSheet(u"background-color: rgb(57, 62, 70);\n"
"font: 11pt \"Arial\";")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tablaBCP = QTableWidget(Form)
        if (self.tablaBCP.columnCount() < 12):
            self.tablaBCP.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaBCP.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaBCP.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaBCP.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaBCP.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaBCP.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaBCP.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaBCP.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaBCP.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablaBCP.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablaBCP.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tablaBCP.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tablaBCP.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tablaBCP.setObjectName(u"tablaBCP")
        self.tablaBCP.setStyleSheet(u"font: 11pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.tablaBCP.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout.addWidget(self.tablaBCP, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tablaBCP.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tablaBCP.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Operaci\u00f3n", None));
        ___qtablewidgetitem2 = self.tablaBCP.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Res", None));
        ___qtablewidgetitem3 = self.tablaBCP.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Estado", None));
        ___qtablewidgetitem4 = self.tablaBCP.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"T. Max", None));
        ___qtablewidgetitem5 = self.tablaBCP.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"TLL", None));
        ___qtablewidgetitem6 = self.tablaBCP.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"TE", None));
        ___qtablewidgetitem7 = self.tablaBCP.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"TF", None));
        ___qtablewidgetitem8 = self.tablaBCP.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"TRes", None));
        ___qtablewidgetitem9 = self.tablaBCP.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"TRet", None));
        ___qtablewidgetitem10 = self.tablaBCP.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"TS", None));
        ___qtablewidgetitem11 = self.tablaBCP.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"TBloq", None));
    # retranslateUi

