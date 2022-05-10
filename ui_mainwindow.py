# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
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
        MainWindow.resize(1925, 1491)
        MainWindow.setMinimumSize(QSize(1925, 1000))
        MainWindow.setMaximumSize(QSize(1925, 1500))
        MainWindow.setStyleSheet(u"font: 11pt \"Arial\";\n"
"background-color: #393e46;\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setVerticalSpacing(25)
        self.gridLayout_2.setContentsMargins(25, 0, 25, -1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 10, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.gridLayout_2.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 16777215))
        self.label.setStyleSheet(u"color: rgb(238, 238, 238);")

        self.horizontalLayout_6.addWidget(self.label)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.tablaPBloqueados = QTableWidget(self.centralwidget)
        if (self.tablaPBloqueados.columnCount() < 3):
            self.tablaPBloqueados.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tablaPBloqueados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaPBloqueados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaPBloqueados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tablaPBloqueados.setObjectName(u"tablaPBloqueados")
        self.tablaPBloqueados.setMinimumSize(QSize(250, 0))
        self.tablaPBloqueados.setMaximumSize(QSize(250, 16777215))
        self.tablaPBloqueados.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tablaPBloqueados.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_2.addWidget(self.tablaPBloqueados, 12, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:rgb(67, 183, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.label_2, 11, 0, 1, 1)

        self.ejecutarBtn = QPushButton(self.centralwidget)
        self.ejecutarBtn.setObjectName(u"ejecutarBtn")
        self.ejecutarBtn.setMinimumSize(QSize(80, 35))
        self.ejecutarBtn.setMaximumSize(QSize(80, 35))
        self.ejecutarBtn.setStyleSheet(u"background-color: rgb(67, 183, 255);\n"
"color: #eeeeee;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;")

        self.gridLayout_2.addWidget(self.ejecutarBtn, 9, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.gridLayout_2.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.agregarBtn = QPushButton(self.centralwidget)
        self.agregarBtn.setObjectName(u"agregarBtn")
        self.agregarBtn.setMinimumSize(QSize(80, 35))
        self.agregarBtn.setMaximumSize(QSize(80, 35))
        self.agregarBtn.setStyleSheet(u"background-color: rgb(67, 183, 255);\n"
"color: #eeeeee;\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;")

        self.gridLayout_2.addWidget(self.agregarBtn, 7, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.spinProcesos = QSpinBox(self.centralwidget)
        self.spinProcesos.setObjectName(u"spinProcesos")
        self.spinProcesos.setMinimumSize(QSize(80, 30))
        self.spinProcesos.setMaximumSize(QSize(80, 30))
        self.spinProcesos.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(67, 183, 255);\n"
"border-radius: 6px;")

        self.horizontalLayout_5.addWidget(self.spinProcesos)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(100, 16777215))
        self.label_5.setStyleSheet(u"color: rgb(238, 238, 238);")

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1, Qt.AlignHCenter)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_2.addLayout(self.verticalLayout, 13, 0, 1, 1)

        self.label_45 = QLabel(self.centralwidget)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"color:rgb(67, 183, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.label_45, 0, 0, 1, 1)

        self.spinQuantum = QSpinBox(self.centralwidget)
        self.spinQuantum.setObjectName(u"spinQuantum")
        self.spinQuantum.setMinimumSize(QSize(80, 30))
        self.spinQuantum.setMaximumSize(QSize(80, 30))
        self.spinQuantum.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(67, 183, 255);\n"
"border-radius: 6px;")

        self.gridLayout_2.addWidget(self.spinQuantum, 5, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color: rgb(85, 255, 127);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 2, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_39 = QLabel(self.centralwidget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"color: rgb(67, 183, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_22.addWidget(self.label_39)

        self.label_41 = QLabel(self.centralwidget)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_22.addWidget(self.label_41)

        self.label_40 = QLabel(self.centralwidget)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"color: rgb(67, 183, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_22.addWidget(self.label_40)

        self.labelPendientes = QLabel(self.centralwidget)
        self.labelPendientes.setObjectName(u"labelPendientes")
        self.labelPendientes.setMinimumSize(QSize(50, 30))
        self.labelPendientes.setMaximumSize(QSize(50, 20))
        self.labelPendientes.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.horizontalLayout_22.addWidget(self.labelPendientes)


        self.verticalLayout_4.addLayout(self.horizontalLayout_22)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tablaProcesos = QTableWidget(self.centralwidget)
        if (self.tablaProcesos.columnCount() < 5):
            self.tablaProcesos.setColumnCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tablaProcesos.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaProcesos.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        self.tablaProcesos.setObjectName(u"tablaProcesos")
        self.tablaProcesos.setMinimumSize(QSize(180, 0))
        self.tablaProcesos.setMaximumSize(QSize(380, 250))
        self.tablaProcesos.setLayoutDirection(Qt.LeftToRight)
        self.tablaProcesos.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tablaProcesos.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_5.addWidget(self.tablaProcesos)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_62 = QLabel(self.centralwidget)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(150, 0))
        self.label_62.setMaximumSize(QSize(150, 16777215))
        self.label_62.setStyleSheet(u"color: rgb(67, 183, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_29.addWidget(self.label_62)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_51 = QLabel(self.centralwidget)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_21.addWidget(self.label_51)

        self.label_53 = QLabel(self.centralwidget)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"color: rgb(238, 238, 238);")

        self.horizontalLayout_21.addWidget(self.label_53)

        self.idProximoNuevo = QLabel(self.centralwidget)
        self.idProximoNuevo.setObjectName(u"idProximoNuevo")
        self.idProximoNuevo.setMinimumSize(QSize(50, 30))
        self.idProximoNuevo.setMaximumSize(QSize(50, 20))
        self.idProximoNuevo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.horizontalLayout_21.addWidget(self.idProximoNuevo)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_64 = QLabel(self.centralwidget)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_30.addWidget(self.label_64)

        self.label_65 = QLabel(self.centralwidget)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"color: rgb(238, 238, 238);")

        self.horizontalLayout_30.addWidget(self.label_65)

        self.tamanioProximoNuevo = QLabel(self.centralwidget)
        self.tamanioProximoNuevo.setObjectName(u"tamanioProximoNuevo")
        self.tamanioProximoNuevo.setMinimumSize(QSize(50, 30))
        self.tamanioProximoNuevo.setMaximumSize(QSize(50, 20))
        self.tamanioProximoNuevo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.horizontalLayout_30.addWidget(self.tamanioProximoNuevo)

        self.label_66 = QLabel(self.centralwidget)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_30.addWidget(self.label_66)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_30)


        self.horizontalLayout_29.addLayout(self.horizontalLayout_21)


        self.verticalLayout_5.addLayout(self.horizontalLayout_29)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color: rgb(67, 183, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")

        self.verticalLayout_4.addWidget(self.label_19)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(50)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")

        self.formLayout_3.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_14.addWidget(self.label_26)

        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"color: rgb(238, 238, 238);")

        self.horizontalLayout_14.addWidget(self.label_27)

        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_14.addWidget(self.label_28)


        self.formLayout_3.setLayout(1, QFormLayout.LabelRole, self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.labelOperacion = QLabel(self.centralwidget)
        self.labelOperacion.setObjectName(u"labelOperacion")
        self.labelOperacion.setMinimumSize(QSize(220, 30))
        self.labelOperacion.setMaximumSize(QSize(220, 16777215))
        self.labelOperacion.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.labelOperacion)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_17.addWidget(self.label_29)

        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"color: rgb(238, 238, 238);")

        self.horizontalLayout_17.addWidget(self.label_30)

        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_17.addWidget(self.label_31)


        self.formLayout_3.setLayout(2, QFormLayout.LabelRole, self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_18.addWidget(self.label_32)

        self.labelTTtranscurrido = QLabel(self.centralwidget)
        self.labelTTtranscurrido.setObjectName(u"labelTTtranscurrido")
        self.labelTTtranscurrido.setMinimumSize(QSize(80, 30))
        self.labelTTtranscurrido.setMaximumSize(QSize(400, 16777215))
        self.labelTTtranscurrido.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.horizontalLayout_18.addWidget(self.labelTTtranscurrido)

        self.label_33 = QLabel(self.centralwidget)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_18.addWidget(self.label_33)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_18)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_35 = QLabel(self.centralwidget)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_24.addWidget(self.label_35)

        self.label_54 = QLabel(self.centralwidget)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"color: rgb(238, 238, 238);")

        self.horizontalLayout_24.addWidget(self.label_54)

        self.label_55 = QLabel(self.centralwidget)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_24.addWidget(self.label_55)


        self.formLayout_3.setLayout(3, QFormLayout.LabelRole, self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_56 = QLabel(self.centralwidget)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_25.addWidget(self.label_56)

        self.labelTrestante = QLabel(self.centralwidget)
        self.labelTrestante.setObjectName(u"labelTrestante")
        self.labelTrestante.setMinimumSize(QSize(80, 30))
        self.labelTrestante.setMaximumSize(QSize(400, 16777215))
        self.labelTrestante.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.horizontalLayout_25.addWidget(self.labelTrestante)

        self.label_58 = QLabel(self.centralwidget)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_25.addWidget(self.label_58)


        self.formLayout_3.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_25)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_36 = QLabel(self.centralwidget)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_20.addWidget(self.label_36)

        self.label_37 = QLabel(self.centralwidget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"color: rgb(238, 238, 238);")

        self.horizontalLayout_20.addWidget(self.label_37)

        self.label_38 = QLabel(self.centralwidget)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_20.addWidget(self.label_38)


        self.formLayout_3.setLayout(5, QFormLayout.LabelRole, self.horizontalLayout_20)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_52 = QLabel(self.centralwidget)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_19.addWidget(self.label_52)

        self.labelID = QLabel(self.centralwidget)
        self.labelID.setObjectName(u"labelID")
        self.labelID.setMinimumSize(QSize(80, 30))
        self.labelID.setMaximumSize(QSize(400, 16777215))
        self.labelID.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.horizontalLayout_19.addWidget(self.labelID)

        self.label_34 = QLabel(self.centralwidget)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_19.addWidget(self.label_34)


        self.formLayout_3.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_19)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")

        self.formLayout_3.setLayout(6, QFormLayout.LabelRole, self.horizontalLayout_16)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_46 = QLabel(self.centralwidget)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_26.addWidget(self.label_46)

        self.label_57 = QLabel(self.centralwidget)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"color: rgb(238, 238, 238);")

        self.horizontalLayout_26.addWidget(self.label_57)

        self.label_59 = QLabel(self.centralwidget)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_26.addWidget(self.label_59)


        self.formLayout_3.setLayout(4, QFormLayout.LabelRole, self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_60 = QLabel(self.centralwidget)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_27.addWidget(self.label_60)

        self.labelQuantum_2 = QLabel(self.centralwidget)
        self.labelQuantum_2.setObjectName(u"labelQuantum_2")
        self.labelQuantum_2.setMinimumSize(QSize(80, 30))
        self.labelQuantum_2.setMaximumSize(QSize(400, 16777215))
        self.labelQuantum_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.horizontalLayout_27.addWidget(self.labelQuantum_2)

        self.label_61 = QLabel(self.centralwidget)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_27.addWidget(self.label_61)


        self.formLayout_3.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_27)


        self.verticalLayout_4.addLayout(self.formLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 2, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 3, 2, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(25, -1, 0, -1)
        self.label_44 = QLabel(self.centralwidget)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"color: rgb(67, 183, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_44)

        self.tablaPTerminados = QTableWidget(self.centralwidget)
        if (self.tablaPTerminados.columnCount() < 3):
            self.tablaPTerminados.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tablaPTerminados.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablaPTerminados.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tablaPTerminados.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        self.tablaPTerminados.setObjectName(u"tablaPTerminados")
        self.tablaPTerminados.setMinimumSize(QSize(400, 300))
        self.tablaPTerminados.setMaximumSize(QSize(305, 300))
        self.tablaPTerminados.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tablaPTerminados.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_6.addWidget(self.tablaPTerminados, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(67, 183, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.label_4)

        self.tablaTiemposFinales = QTableWidget(self.centralwidget)
        if (self.tablaTiemposFinales.columnCount() < 7):
            self.tablaTiemposFinales.setColumnCount(7)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tablaTiemposFinales.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tablaTiemposFinales.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tablaTiemposFinales.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tablaTiemposFinales.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tablaTiemposFinales.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tablaTiemposFinales.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tablaTiemposFinales.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        self.tablaTiemposFinales.setObjectName(u"tablaTiemposFinales")
        self.tablaTiemposFinales.setMinimumSize(QSize(700, 0))
        self.tablaTiemposFinales.setMaximumSize(QSize(700, 16777215))
        self.tablaTiemposFinales.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tablaTiemposFinales.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_6.addWidget(self.tablaTiemposFinales)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, -1, 30, -1)
        self.label_43 = QLabel(self.centralwidget)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"color: rgb(67, 183, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_23.addWidget(self.label_43)

        self.labelQuantumGlobal = QLabel(self.centralwidget)
        self.labelQuantumGlobal.setObjectName(u"labelQuantumGlobal")
        self.labelQuantumGlobal.setMinimumSize(QSize(50, 30))
        self.labelQuantumGlobal.setMaximumSize(QSize(80, 16777215))
        self.labelQuantumGlobal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.horizontalLayout_23.addWidget(self.labelQuantumGlobal)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_23.addWidget(self.label_6)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_23.addWidget(self.label_9)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_23.addWidget(self.label_10)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_23.addWidget(self.label_11)

        self.label_42 = QLabel(self.centralwidget)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"color: rgb(67, 183, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_23.addWidget(self.label_42, 0, Qt.AlignRight)

        self.labelCGlobal = QLabel(self.centralwidget)
        self.labelCGlobal.setObjectName(u"labelCGlobal")
        self.labelCGlobal.setMinimumSize(QSize(50, 30))
        self.labelCGlobal.setMaximumSize(QSize(50, 16777215))
        self.labelCGlobal.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.horizontalLayout_23.addWidget(self.labelCGlobal)


        self.verticalLayout_6.addLayout(self.horizontalLayout_23)


        self.gridLayout.addLayout(self.verticalLayout_6, 1, 4, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_47 = QLabel(self.centralwidget)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"color: rgb(67, 183, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_47)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.tablaID0_6 = QLabel(self.centralwidget)
        self.tablaID0_6.setObjectName(u"tablaID0_6")
        self.tablaID0_6.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.tablaID0_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.tablaID0_6)

        self.label_78 = QLabel(self.centralwidget)
        self.label_78.setObjectName(u"label_78")

        self.horizontalLayout_35.addWidget(self.label_78)

        self.label_79 = QLabel(self.centralwidget)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_79.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_79)

        self.label_80 = QLabel(self.centralwidget)
        self.label_80.setObjectName(u"label_80")

        self.horizontalLayout_35.addWidget(self.label_80)

        self.m00_6 = QLabel(self.centralwidget)
        self.m00_6.setObjectName(u"m00_6")
        self.m00_6.setStyleSheet(u"")
        self.m00_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.m00_6)

        self.m01_6 = QLabel(self.centralwidget)
        self.m01_6.setObjectName(u"m01_6")
        self.m01_6.setStyleSheet(u"")
        self.m01_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.m01_6)

        self.m02_6 = QLabel(self.centralwidget)
        self.m02_6.setObjectName(u"m02_6")
        self.m02_6.setStyleSheet(u"")
        self.m02_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.m02_6)

        self.m03_6 = QLabel(self.centralwidget)
        self.m03_6.setObjectName(u"m03_6")
        self.m03_6.setStyleSheet(u"")
        self.m03_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.m03_6)


        self.horizontalLayout_34.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_81 = QLabel(self.centralwidget)
        self.label_81.setObjectName(u"label_81")

        self.horizontalLayout_36.addWidget(self.label_81)

        self.tablaID1_6 = QLabel(self.centralwidget)
        self.tablaID1_6.setObjectName(u"tablaID1_6")
        self.tablaID1_6.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.tablaID1_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.tablaID1_6)

        self.label_82 = QLabel(self.centralwidget)
        self.label_82.setObjectName(u"label_82")

        self.horizontalLayout_36.addWidget(self.label_82)

        self.label_83 = QLabel(self.centralwidget)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_83.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_83)

        self.label_84 = QLabel(self.centralwidget)
        self.label_84.setObjectName(u"label_84")

        self.horizontalLayout_36.addWidget(self.label_84)

        self.m10_6 = QLabel(self.centralwidget)
        self.m10_6.setObjectName(u"m10_6")
        self.m10_6.setStyleSheet(u"")
        self.m10_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.m10_6)

        self.m11_6 = QLabel(self.centralwidget)
        self.m11_6.setObjectName(u"m11_6")
        self.m11_6.setStyleSheet(u"")
        self.m11_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.m11_6)

        self.m12_6 = QLabel(self.centralwidget)
        self.m12_6.setObjectName(u"m12_6")
        self.m12_6.setStyleSheet(u"")
        self.m12_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.m12_6)

        self.m13_6 = QLabel(self.centralwidget)
        self.m13_6.setObjectName(u"m13_6")
        self.m13_6.setStyleSheet(u"")
        self.m13_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.m13_6)


        self.horizontalLayout_34.addLayout(self.horizontalLayout_36)


        self.verticalLayout_2.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.tablaID0 = QLabel(self.centralwidget)
        self.tablaID0.setObjectName(u"tablaID0")
        self.tablaID0.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.tablaID0)

        self.label_99 = QLabel(self.centralwidget)
        self.label_99.setObjectName(u"label_99")

        self.horizontalLayout_44.addWidget(self.label_99)

        self.label_100 = QLabel(self.centralwidget)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_100.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.label_100)

        self.label_101 = QLabel(self.centralwidget)
        self.label_101.setObjectName(u"label_101")

        self.horizontalLayout_44.addWidget(self.label_101)

        self.m00 = QLabel(self.centralwidget)
        self.m00.setObjectName(u"m00")
        self.m00.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m00.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.m00)

        self.m01 = QLabel(self.centralwidget)
        self.m01.setObjectName(u"m01")
        self.m01.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m01.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.m01)

        self.m02 = QLabel(self.centralwidget)
        self.m02.setObjectName(u"m02")
        self.m02.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m02.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.m02)

        self.m03 = QLabel(self.centralwidget)
        self.m03.setObjectName(u"m03")
        self.m03.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m03.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.m03)


        self.horizontalLayout_43.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_102 = QLabel(self.centralwidget)
        self.label_102.setObjectName(u"label_102")

        self.horizontalLayout_45.addWidget(self.label_102)

        self.tablaID1 = QLabel(self.centralwidget)
        self.tablaID1.setObjectName(u"tablaID1")
        self.tablaID1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.tablaID1)

        self.label_103 = QLabel(self.centralwidget)
        self.label_103.setObjectName(u"label_103")

        self.horizontalLayout_45.addWidget(self.label_103)

        self.label_104 = QLabel(self.centralwidget)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_104.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.label_104)

        self.label_105 = QLabel(self.centralwidget)
        self.label_105.setObjectName(u"label_105")

        self.horizontalLayout_45.addWidget(self.label_105)

        self.m10 = QLabel(self.centralwidget)
        self.m10.setObjectName(u"m10")
        self.m10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.m10)

        self.m11 = QLabel(self.centralwidget)
        self.m11.setObjectName(u"m11")
        self.m11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.m11)

        self.m12 = QLabel(self.centralwidget)
        self.m12.setObjectName(u"m12")
        self.m12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.m12)

        self.m13 = QLabel(self.centralwidget)
        self.m13.setObjectName(u"m13")
        self.m13.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.m13)


        self.horizontalLayout_43.addLayout(self.horizontalLayout_45)


        self.verticalLayout_2.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.tablaID2 = QLabel(self.centralwidget)
        self.tablaID2.setObjectName(u"tablaID2")
        self.tablaID2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.tablaID2)

        self.label_92 = QLabel(self.centralwidget)
        self.label_92.setObjectName(u"label_92")

        self.horizontalLayout_41.addWidget(self.label_92)

        self.label_93 = QLabel(self.centralwidget)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_93.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.label_93)

        self.label_94 = QLabel(self.centralwidget)
        self.label_94.setObjectName(u"label_94")

        self.horizontalLayout_41.addWidget(self.label_94)

        self.m20 = QLabel(self.centralwidget)
        self.m20.setObjectName(u"m20")
        self.m20.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.m20)

        self.m21 = QLabel(self.centralwidget)
        self.m21.setObjectName(u"m21")
        self.m21.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.m21)

        self.m22 = QLabel(self.centralwidget)
        self.m22.setObjectName(u"m22")
        self.m22.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.m22)

        self.m23 = QLabel(self.centralwidget)
        self.m23.setObjectName(u"m23")
        self.m23.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.m23)


        self.horizontalLayout_40.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_95 = QLabel(self.centralwidget)
        self.label_95.setObjectName(u"label_95")

        self.horizontalLayout_42.addWidget(self.label_95)

        self.tablaID3 = QLabel(self.centralwidget)
        self.tablaID3.setObjectName(u"tablaID3")
        self.tablaID3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.tablaID3)

        self.label_96 = QLabel(self.centralwidget)
        self.label_96.setObjectName(u"label_96")

        self.horizontalLayout_42.addWidget(self.label_96)

        self.label_97 = QLabel(self.centralwidget)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_97.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_97)

        self.label_98 = QLabel(self.centralwidget)
        self.label_98.setObjectName(u"label_98")

        self.horizontalLayout_42.addWidget(self.label_98)

        self.m30 = QLabel(self.centralwidget)
        self.m30.setObjectName(u"m30")
        self.m30.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.m30)

        self.m31 = QLabel(self.centralwidget)
        self.m31.setObjectName(u"m31")
        self.m31.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.m31)

        self.m32 = QLabel(self.centralwidget)
        self.m32.setObjectName(u"m32")
        self.m32.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.m32)

        self.m33 = QLabel(self.centralwidget)
        self.m33.setObjectName(u"m33")
        self.m33.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.m33)


        self.horizontalLayout_40.addLayout(self.horizontalLayout_42)


        self.verticalLayout_2.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.tablaID4 = QLabel(self.centralwidget)
        self.tablaID4.setObjectName(u"tablaID4")
        self.tablaID4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.tablaID4)

        self.label_85 = QLabel(self.centralwidget)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_38.addWidget(self.label_85)

        self.label_86 = QLabel(self.centralwidget)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_86.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_86)

        self.label_87 = QLabel(self.centralwidget)
        self.label_87.setObjectName(u"label_87")

        self.horizontalLayout_38.addWidget(self.label_87)

        self.m40 = QLabel(self.centralwidget)
        self.m40.setObjectName(u"m40")
        self.m40.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.m40)

        self.m41 = QLabel(self.centralwidget)
        self.m41.setObjectName(u"m41")
        self.m41.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.m41)

        self.m42 = QLabel(self.centralwidget)
        self.m42.setObjectName(u"m42")
        self.m42.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.m42)

        self.m43 = QLabel(self.centralwidget)
        self.m43.setObjectName(u"m43")
        self.m43.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.m43)


        self.horizontalLayout_37.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_88 = QLabel(self.centralwidget)
        self.label_88.setObjectName(u"label_88")

        self.horizontalLayout_39.addWidget(self.label_88)

        self.tablaID5 = QLabel(self.centralwidget)
        self.tablaID5.setObjectName(u"tablaID5")
        self.tablaID5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.tablaID5)

        self.label_89 = QLabel(self.centralwidget)
        self.label_89.setObjectName(u"label_89")

        self.horizontalLayout_39.addWidget(self.label_89)

        self.label_90 = QLabel(self.centralwidget)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_90.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_90)

        self.label_91 = QLabel(self.centralwidget)
        self.label_91.setObjectName(u"label_91")

        self.horizontalLayout_39.addWidget(self.label_91)

        self.m50 = QLabel(self.centralwidget)
        self.m50.setObjectName(u"m50")
        self.m50.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m50.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.m50)

        self.m51 = QLabel(self.centralwidget)
        self.m51.setObjectName(u"m51")
        self.m51.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m51.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.m51)

        self.m52 = QLabel(self.centralwidget)
        self.m52.setObjectName(u"m52")
        self.m52.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.m52)

        self.m53 = QLabel(self.centralwidget)
        self.m53.setObjectName(u"m53")
        self.m53.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.m53)


        self.horizontalLayout_37.addLayout(self.horizontalLayout_39)


        self.verticalLayout_2.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.tablaID6 = QLabel(self.centralwidget)
        self.tablaID6.setObjectName(u"tablaID6")
        self.tablaID6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.tablaID6)

        self.label_106 = QLabel(self.centralwidget)
        self.label_106.setObjectName(u"label_106")

        self.horizontalLayout_47.addWidget(self.label_106)

        self.label_107 = QLabel(self.centralwidget)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_107.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.label_107)

        self.label_108 = QLabel(self.centralwidget)
        self.label_108.setObjectName(u"label_108")

        self.horizontalLayout_47.addWidget(self.label_108)

        self.m60 = QLabel(self.centralwidget)
        self.m60.setObjectName(u"m60")
        self.m60.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m60.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.m60)

        self.m61 = QLabel(self.centralwidget)
        self.m61.setObjectName(u"m61")
        self.m61.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m61.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.m61)

        self.m62 = QLabel(self.centralwidget)
        self.m62.setObjectName(u"m62")
        self.m62.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m62.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.m62)

        self.m63 = QLabel(self.centralwidget)
        self.m63.setObjectName(u"m63")
        self.m63.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m63.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.m63)


        self.horizontalLayout_46.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_109 = QLabel(self.centralwidget)
        self.label_109.setObjectName(u"label_109")

        self.horizontalLayout_48.addWidget(self.label_109)

        self.tablaID7 = QLabel(self.centralwidget)
        self.tablaID7.setObjectName(u"tablaID7")
        self.tablaID7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.tablaID7)

        self.label_110 = QLabel(self.centralwidget)
        self.label_110.setObjectName(u"label_110")

        self.horizontalLayout_48.addWidget(self.label_110)

        self.label_111 = QLabel(self.centralwidget)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_111.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.label_111)

        self.label_112 = QLabel(self.centralwidget)
        self.label_112.setObjectName(u"label_112")

        self.horizontalLayout_48.addWidget(self.label_112)

        self.m70 = QLabel(self.centralwidget)
        self.m70.setObjectName(u"m70")
        self.m70.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m70.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.m70)

        self.m71 = QLabel(self.centralwidget)
        self.m71.setObjectName(u"m71")
        self.m71.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m71.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.m71)

        self.m72 = QLabel(self.centralwidget)
        self.m72.setObjectName(u"m72")
        self.m72.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m72.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.m72)

        self.m73 = QLabel(self.centralwidget)
        self.m73.setObjectName(u"m73")
        self.m73.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m73.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.m73)


        self.horizontalLayout_46.addLayout(self.horizontalLayout_48)


        self.verticalLayout_2.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.tablaID8 = QLabel(self.centralwidget)
        self.tablaID8.setObjectName(u"tablaID8")
        self.tablaID8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.tablaID8)

        self.label_121 = QLabel(self.centralwidget)
        self.label_121.setObjectName(u"label_121")

        self.horizontalLayout_53.addWidget(self.label_121)

        self.label_122 = QLabel(self.centralwidget)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_122.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.label_122)

        self.label_123 = QLabel(self.centralwidget)
        self.label_123.setObjectName(u"label_123")

        self.horizontalLayout_53.addWidget(self.label_123)

        self.m80 = QLabel(self.centralwidget)
        self.m80.setObjectName(u"m80")
        self.m80.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m80.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.m80)

        self.m81 = QLabel(self.centralwidget)
        self.m81.setObjectName(u"m81")
        self.m81.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m81.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.m81)

        self.m82 = QLabel(self.centralwidget)
        self.m82.setObjectName(u"m82")
        self.m82.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m82.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.m82)

        self.m83 = QLabel(self.centralwidget)
        self.m83.setObjectName(u"m83")
        self.m83.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m83.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.m83)


        self.horizontalLayout_52.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_124 = QLabel(self.centralwidget)
        self.label_124.setObjectName(u"label_124")

        self.horizontalLayout_54.addWidget(self.label_124)

        self.tablaID9 = QLabel(self.centralwidget)
        self.tablaID9.setObjectName(u"tablaID9")
        self.tablaID9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.tablaID9)

        self.label_125 = QLabel(self.centralwidget)
        self.label_125.setObjectName(u"label_125")

        self.horizontalLayout_54.addWidget(self.label_125)

        self.label_126 = QLabel(self.centralwidget)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_126.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.label_126)

        self.label_127 = QLabel(self.centralwidget)
        self.label_127.setObjectName(u"label_127")

        self.horizontalLayout_54.addWidget(self.label_127)

        self.m90 = QLabel(self.centralwidget)
        self.m90.setObjectName(u"m90")
        self.m90.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m90.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.m90)

        self.m91 = QLabel(self.centralwidget)
        self.m91.setObjectName(u"m91")
        self.m91.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m91.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.m91)

        self.m92 = QLabel(self.centralwidget)
        self.m92.setObjectName(u"m92")
        self.m92.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m92.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.m92)

        self.m93 = QLabel(self.centralwidget)
        self.m93.setObjectName(u"m93")
        self.m93.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m93.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.m93)


        self.horizontalLayout_52.addLayout(self.horizontalLayout_54)


        self.verticalLayout_2.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.tablaID10 = QLabel(self.centralwidget)
        self.tablaID10.setObjectName(u"tablaID10")
        self.tablaID10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.tablaID10)

        self.label_128 = QLabel(self.centralwidget)
        self.label_128.setObjectName(u"label_128")

        self.horizontalLayout_56.addWidget(self.label_128)

        self.label_129 = QLabel(self.centralwidget)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_129.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.label_129)

        self.label_130 = QLabel(self.centralwidget)
        self.label_130.setObjectName(u"label_130")

        self.horizontalLayout_56.addWidget(self.label_130)

        self.m100 = QLabel(self.centralwidget)
        self.m100.setObjectName(u"m100")
        self.m100.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m100.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.m100)

        self.m101 = QLabel(self.centralwidget)
        self.m101.setObjectName(u"m101")
        self.m101.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m101.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.m101)

        self.m102 = QLabel(self.centralwidget)
        self.m102.setObjectName(u"m102")
        self.m102.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m102.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.m102)

        self.m103 = QLabel(self.centralwidget)
        self.m103.setObjectName(u"m103")
        self.m103.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m103.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.m103)


        self.horizontalLayout_55.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_131 = QLabel(self.centralwidget)
        self.label_131.setObjectName(u"label_131")

        self.horizontalLayout_57.addWidget(self.label_131)

        self.tablaID11 = QLabel(self.centralwidget)
        self.tablaID11.setObjectName(u"tablaID11")
        self.tablaID11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.tablaID11)

        self.label_132 = QLabel(self.centralwidget)
        self.label_132.setObjectName(u"label_132")

        self.horizontalLayout_57.addWidget(self.label_132)

        self.label_133 = QLabel(self.centralwidget)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_133.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.label_133)

        self.label_134 = QLabel(self.centralwidget)
        self.label_134.setObjectName(u"label_134")

        self.horizontalLayout_57.addWidget(self.label_134)

        self.m110 = QLabel(self.centralwidget)
        self.m110.setObjectName(u"m110")
        self.m110.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m110.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.m110)

        self.m111 = QLabel(self.centralwidget)
        self.m111.setObjectName(u"m111")
        self.m111.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m111.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.m111)

        self.m112 = QLabel(self.centralwidget)
        self.m112.setObjectName(u"m112")
        self.m112.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m112.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.m112)

        self.m113 = QLabel(self.centralwidget)
        self.m113.setObjectName(u"m113")
        self.m113.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m113.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.m113)


        self.horizontalLayout_55.addLayout(self.horizontalLayout_57)


        self.verticalLayout_2.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.tablaID12 = QLabel(self.centralwidget)
        self.tablaID12.setObjectName(u"tablaID12")
        self.tablaID12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.tablaID12)

        self.label_135 = QLabel(self.centralwidget)
        self.label_135.setObjectName(u"label_135")

        self.horizontalLayout_59.addWidget(self.label_135)

        self.label_136 = QLabel(self.centralwidget)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_136.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.label_136)

        self.label_137 = QLabel(self.centralwidget)
        self.label_137.setObjectName(u"label_137")

        self.horizontalLayout_59.addWidget(self.label_137)

        self.m120 = QLabel(self.centralwidget)
        self.m120.setObjectName(u"m120")
        self.m120.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m120.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.m120)

        self.m121 = QLabel(self.centralwidget)
        self.m121.setObjectName(u"m121")
        self.m121.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m121.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.m121)

        self.m122 = QLabel(self.centralwidget)
        self.m122.setObjectName(u"m122")
        self.m122.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m122.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.m122)

        self.m123 = QLabel(self.centralwidget)
        self.m123.setObjectName(u"m123")
        self.m123.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m123.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.m123)


        self.horizontalLayout_58.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_138 = QLabel(self.centralwidget)
        self.label_138.setObjectName(u"label_138")

        self.horizontalLayout_60.addWidget(self.label_138)

        self.tablaID13 = QLabel(self.centralwidget)
        self.tablaID13.setObjectName(u"tablaID13")
        self.tablaID13.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.tablaID13)

        self.label_139 = QLabel(self.centralwidget)
        self.label_139.setObjectName(u"label_139")

        self.horizontalLayout_60.addWidget(self.label_139)

        self.label_140 = QLabel(self.centralwidget)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_140.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.label_140)

        self.label_141 = QLabel(self.centralwidget)
        self.label_141.setObjectName(u"label_141")

        self.horizontalLayout_60.addWidget(self.label_141)

        self.m130 = QLabel(self.centralwidget)
        self.m130.setObjectName(u"m130")
        self.m130.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m130.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.m130)

        self.m131 = QLabel(self.centralwidget)
        self.m131.setObjectName(u"m131")
        self.m131.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m131.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.m131)

        self.m132 = QLabel(self.centralwidget)
        self.m132.setObjectName(u"m132")
        self.m132.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m132.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.m132)

        self.m133 = QLabel(self.centralwidget)
        self.m133.setObjectName(u"m133")
        self.m133.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m133.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.m133)


        self.horizontalLayout_58.addLayout(self.horizontalLayout_60)


        self.verticalLayout_2.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.tablaID14 = QLabel(self.centralwidget)
        self.tablaID14.setObjectName(u"tablaID14")
        self.tablaID14.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.tablaID14)

        self.label_142 = QLabel(self.centralwidget)
        self.label_142.setObjectName(u"label_142")

        self.horizontalLayout_62.addWidget(self.label_142)

        self.label_143 = QLabel(self.centralwidget)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_143.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.label_143)

        self.label_144 = QLabel(self.centralwidget)
        self.label_144.setObjectName(u"label_144")

        self.horizontalLayout_62.addWidget(self.label_144)

        self.m140 = QLabel(self.centralwidget)
        self.m140.setObjectName(u"m140")
        self.m140.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m140.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.m140)

        self.m141 = QLabel(self.centralwidget)
        self.m141.setObjectName(u"m141")
        self.m141.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m141.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.m141)

        self.m142 = QLabel(self.centralwidget)
        self.m142.setObjectName(u"m142")
        self.m142.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m142.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.m142)

        self.m143 = QLabel(self.centralwidget)
        self.m143.setObjectName(u"m143")
        self.m143.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m143.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.m143)


        self.horizontalLayout_61.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_145 = QLabel(self.centralwidget)
        self.label_145.setObjectName(u"label_145")

        self.horizontalLayout_63.addWidget(self.label_145)

        self.tablaID15 = QLabel(self.centralwidget)
        self.tablaID15.setObjectName(u"tablaID15")
        self.tablaID15.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.tablaID15)

        self.label_146 = QLabel(self.centralwidget)
        self.label_146.setObjectName(u"label_146")

        self.horizontalLayout_63.addWidget(self.label_146)

        self.label_147 = QLabel(self.centralwidget)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_147.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.label_147)

        self.label_148 = QLabel(self.centralwidget)
        self.label_148.setObjectName(u"label_148")

        self.horizontalLayout_63.addWidget(self.label_148)

        self.m150 = QLabel(self.centralwidget)
        self.m150.setObjectName(u"m150")
        self.m150.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m150.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.m150)

        self.m151 = QLabel(self.centralwidget)
        self.m151.setObjectName(u"m151")
        self.m151.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m151.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.m151)

        self.m152 = QLabel(self.centralwidget)
        self.m152.setObjectName(u"m152")
        self.m152.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m152.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.m152)

        self.m153 = QLabel(self.centralwidget)
        self.m153.setObjectName(u"m153")
        self.m153.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m153.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.m153)


        self.horizontalLayout_61.addLayout(self.horizontalLayout_63)


        self.verticalLayout_2.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.tablaID16 = QLabel(self.centralwidget)
        self.tablaID16.setObjectName(u"tablaID16")
        self.tablaID16.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.tablaID16)

        self.label_114 = QLabel(self.centralwidget)
        self.label_114.setObjectName(u"label_114")

        self.horizontalLayout_50.addWidget(self.label_114)

        self.label_115 = QLabel(self.centralwidget)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_115.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_115)

        self.label_116 = QLabel(self.centralwidget)
        self.label_116.setObjectName(u"label_116")

        self.horizontalLayout_50.addWidget(self.label_116)

        self.m160 = QLabel(self.centralwidget)
        self.m160.setObjectName(u"m160")
        self.m160.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m160.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.m160)

        self.m161 = QLabel(self.centralwidget)
        self.m161.setObjectName(u"m161")
        self.m161.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m161.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.m161)

        self.m162 = QLabel(self.centralwidget)
        self.m162.setObjectName(u"m162")
        self.m162.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m162.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.m162)

        self.m163 = QLabel(self.centralwidget)
        self.m163.setObjectName(u"m163")
        self.m163.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m163.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.m163)


        self.horizontalLayout_49.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_117 = QLabel(self.centralwidget)
        self.label_117.setObjectName(u"label_117")

        self.horizontalLayout_51.addWidget(self.label_117)

        self.tablaID17 = QLabel(self.centralwidget)
        self.tablaID17.setObjectName(u"tablaID17")
        self.tablaID17.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.tablaID17)

        self.label_118 = QLabel(self.centralwidget)
        self.label_118.setObjectName(u"label_118")

        self.horizontalLayout_51.addWidget(self.label_118)

        self.label_119 = QLabel(self.centralwidget)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_119.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.label_119)

        self.label_120 = QLabel(self.centralwidget)
        self.label_120.setObjectName(u"label_120")

        self.horizontalLayout_51.addWidget(self.label_120)

        self.m170 = QLabel(self.centralwidget)
        self.m170.setObjectName(u"m170")
        self.m170.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m170.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.m170)

        self.m171 = QLabel(self.centralwidget)
        self.m171.setObjectName(u"m171")
        self.m171.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m171.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.m171)

        self.m172 = QLabel(self.centralwidget)
        self.m172.setObjectName(u"m172")
        self.m172.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m172.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.m172)

        self.m173 = QLabel(self.centralwidget)
        self.m173.setObjectName(u"m173")
        self.m173.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m173.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.m173)


        self.horizontalLayout_49.addLayout(self.horizontalLayout_51)


        self.verticalLayout_2.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.tablaID18 = QLabel(self.centralwidget)
        self.tablaID18.setObjectName(u"tablaID18")
        self.tablaID18.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.tablaID18)

        self.label_163 = QLabel(self.centralwidget)
        self.label_163.setObjectName(u"label_163")

        self.horizontalLayout_71.addWidget(self.label_163)

        self.label_164 = QLabel(self.centralwidget)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_164.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.label_164)

        self.label_165 = QLabel(self.centralwidget)
        self.label_165.setObjectName(u"label_165")

        self.horizontalLayout_71.addWidget(self.label_165)

        self.m180 = QLabel(self.centralwidget)
        self.m180.setObjectName(u"m180")
        self.m180.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m180.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.m180)

        self.m181 = QLabel(self.centralwidget)
        self.m181.setObjectName(u"m181")
        self.m181.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m181.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.m181)

        self.m182 = QLabel(self.centralwidget)
        self.m182.setObjectName(u"m182")
        self.m182.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m182.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.m182)

        self.m183 = QLabel(self.centralwidget)
        self.m183.setObjectName(u"m183")
        self.m183.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m183.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.m183)


        self.horizontalLayout_70.addLayout(self.horizontalLayout_71)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_166 = QLabel(self.centralwidget)
        self.label_166.setObjectName(u"label_166")

        self.horizontalLayout_72.addWidget(self.label_166)

        self.tablaID19 = QLabel(self.centralwidget)
        self.tablaID19.setObjectName(u"tablaID19")
        self.tablaID19.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.tablaID19)

        self.label_167 = QLabel(self.centralwidget)
        self.label_167.setObjectName(u"label_167")

        self.horizontalLayout_72.addWidget(self.label_167)

        self.label_168 = QLabel(self.centralwidget)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_168.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.label_168)

        self.label_169 = QLabel(self.centralwidget)
        self.label_169.setObjectName(u"label_169")

        self.horizontalLayout_72.addWidget(self.label_169)

        self.m190 = QLabel(self.centralwidget)
        self.m190.setObjectName(u"m190")
        self.m190.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m190.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.m190)

        self.m191 = QLabel(self.centralwidget)
        self.m191.setObjectName(u"m191")
        self.m191.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m191.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.m191)

        self.m192 = QLabel(self.centralwidget)
        self.m192.setObjectName(u"m192")
        self.m192.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m192.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.m192)

        self.m193 = QLabel(self.centralwidget)
        self.m193.setObjectName(u"m193")
        self.m193.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m193.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.m193)


        self.horizontalLayout_70.addLayout(self.horizontalLayout_72)


        self.verticalLayout_2.addLayout(self.horizontalLayout_70)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.tablaID20 = QLabel(self.centralwidget)
        self.tablaID20.setObjectName(u"tablaID20")
        self.tablaID20.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.tablaID20)

        self.label_156 = QLabel(self.centralwidget)
        self.label_156.setObjectName(u"label_156")

        self.horizontalLayout_68.addWidget(self.label_156)

        self.label_157 = QLabel(self.centralwidget)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_157.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.label_157)

        self.label_158 = QLabel(self.centralwidget)
        self.label_158.setObjectName(u"label_158")

        self.horizontalLayout_68.addWidget(self.label_158)

        self.m200 = QLabel(self.centralwidget)
        self.m200.setObjectName(u"m200")
        self.m200.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m200.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.m200)

        self.m201 = QLabel(self.centralwidget)
        self.m201.setObjectName(u"m201")
        self.m201.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m201.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.m201)

        self.m202 = QLabel(self.centralwidget)
        self.m202.setObjectName(u"m202")
        self.m202.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m202.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.m202)

        self.m203 = QLabel(self.centralwidget)
        self.m203.setObjectName(u"m203")
        self.m203.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m203.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.m203)


        self.horizontalLayout_67.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_159 = QLabel(self.centralwidget)
        self.label_159.setObjectName(u"label_159")

        self.horizontalLayout_69.addWidget(self.label_159)

        self.tablaID21 = QLabel(self.centralwidget)
        self.tablaID21.setObjectName(u"tablaID21")
        self.tablaID21.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.tablaID21)

        self.label_160 = QLabel(self.centralwidget)
        self.label_160.setObjectName(u"label_160")

        self.horizontalLayout_69.addWidget(self.label_160)

        self.label_161 = QLabel(self.centralwidget)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_161.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.label_161)

        self.label_162 = QLabel(self.centralwidget)
        self.label_162.setObjectName(u"label_162")

        self.horizontalLayout_69.addWidget(self.label_162)

        self.m210 = QLabel(self.centralwidget)
        self.m210.setObjectName(u"m210")
        self.m210.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m210.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.m210)

        self.m211 = QLabel(self.centralwidget)
        self.m211.setObjectName(u"m211")
        self.m211.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m211.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.m211)

        self.m212 = QLabel(self.centralwidget)
        self.m212.setObjectName(u"m212")
        self.m212.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m212.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.m212)

        self.m213_2 = QLabel(self.centralwidget)
        self.m213_2.setObjectName(u"m213_2")
        self.m213_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m213_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.m213_2)


        self.horizontalLayout_67.addLayout(self.horizontalLayout_69)


        self.verticalLayout_2.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.tablaID22 = QLabel(self.centralwidget)
        self.tablaID22.setObjectName(u"tablaID22")
        self.tablaID22.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.tablaID22)

        self.label_177 = QLabel(self.centralwidget)
        self.label_177.setObjectName(u"label_177")

        self.horizontalLayout_77.addWidget(self.label_177)

        self.label_178 = QLabel(self.centralwidget)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_178.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.label_178)

        self.label_179 = QLabel(self.centralwidget)
        self.label_179.setObjectName(u"label_179")

        self.horizontalLayout_77.addWidget(self.label_179)

        self.m220 = QLabel(self.centralwidget)
        self.m220.setObjectName(u"m220")
        self.m220.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m220.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.m220)

        self.m221 = QLabel(self.centralwidget)
        self.m221.setObjectName(u"m221")
        self.m221.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m221.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.m221)

        self.m222 = QLabel(self.centralwidget)
        self.m222.setObjectName(u"m222")
        self.m222.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m222.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.m222)

        self.m213 = QLabel(self.centralwidget)
        self.m213.setObjectName(u"m213")
        self.m213.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m213.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_77.addWidget(self.m213)


        self.horizontalLayout_76.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.label_180 = QLabel(self.centralwidget)
        self.label_180.setObjectName(u"label_180")

        self.horizontalLayout_78.addWidget(self.label_180)

        self.tablaID23 = QLabel(self.centralwidget)
        self.tablaID23.setObjectName(u"tablaID23")
        self.tablaID23.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.tablaID23)

        self.label_181 = QLabel(self.centralwidget)
        self.label_181.setObjectName(u"label_181")

        self.horizontalLayout_78.addWidget(self.label_181)

        self.label_182 = QLabel(self.centralwidget)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_182.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.label_182)

        self.label_183 = QLabel(self.centralwidget)
        self.label_183.setObjectName(u"label_183")

        self.horizontalLayout_78.addWidget(self.label_183)

        self.m230 = QLabel(self.centralwidget)
        self.m230.setObjectName(u"m230")
        self.m230.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m230.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.m230)

        self.m231 = QLabel(self.centralwidget)
        self.m231.setObjectName(u"m231")
        self.m231.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m231.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.m231)

        self.m232 = QLabel(self.centralwidget)
        self.m232.setObjectName(u"m232")
        self.m232.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m232.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.m232)

        self.m233 = QLabel(self.centralwidget)
        self.m233.setObjectName(u"m233")
        self.m233.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m233.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.m233)


        self.horizontalLayout_76.addLayout(self.horizontalLayout_78)


        self.verticalLayout_2.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.tablaID24 = QLabel(self.centralwidget)
        self.tablaID24.setObjectName(u"tablaID24")
        self.tablaID24.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.tablaID24)

        self.label_149 = QLabel(self.centralwidget)
        self.label_149.setObjectName(u"label_149")

        self.horizontalLayout_65.addWidget(self.label_149)

        self.label_150 = QLabel(self.centralwidget)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_150.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.label_150)

        self.label_151 = QLabel(self.centralwidget)
        self.label_151.setObjectName(u"label_151")

        self.horizontalLayout_65.addWidget(self.label_151)

        self.m240 = QLabel(self.centralwidget)
        self.m240.setObjectName(u"m240")
        self.m240.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m240.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.m240)

        self.m241 = QLabel(self.centralwidget)
        self.m241.setObjectName(u"m241")
        self.m241.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m241.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.m241)

        self.m242 = QLabel(self.centralwidget)
        self.m242.setObjectName(u"m242")
        self.m242.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m242.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.m242)

        self.m244 = QLabel(self.centralwidget)
        self.m244.setObjectName(u"m244")
        self.m244.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m244.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.m244)


        self.horizontalLayout_64.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_152 = QLabel(self.centralwidget)
        self.label_152.setObjectName(u"label_152")

        self.horizontalLayout_66.addWidget(self.label_152)

        self.tablaID25 = QLabel(self.centralwidget)
        self.tablaID25.setObjectName(u"tablaID25")
        self.tablaID25.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.tablaID25)

        self.label_153 = QLabel(self.centralwidget)
        self.label_153.setObjectName(u"label_153")

        self.horizontalLayout_66.addWidget(self.label_153)

        self.label_154 = QLabel(self.centralwidget)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_154.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.label_154)

        self.label_155 = QLabel(self.centralwidget)
        self.label_155.setObjectName(u"label_155")

        self.horizontalLayout_66.addWidget(self.label_155)

        self.m250 = QLabel(self.centralwidget)
        self.m250.setObjectName(u"m250")
        self.m250.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m250.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.m250)

        self.m251 = QLabel(self.centralwidget)
        self.m251.setObjectName(u"m251")
        self.m251.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m251.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.m251)

        self.m252 = QLabel(self.centralwidget)
        self.m252.setObjectName(u"m252")
        self.m252.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m252.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.m252)

        self.m253 = QLabel(self.centralwidget)
        self.m253.setObjectName(u"m253")
        self.m253.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m253.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.m253)


        self.horizontalLayout_64.addLayout(self.horizontalLayout_66)


        self.verticalLayout_2.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.tablaID26 = QLabel(self.centralwidget)
        self.tablaID26.setObjectName(u"tablaID26")
        self.tablaID26.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.tablaID26)

        self.label_170 = QLabel(self.centralwidget)
        self.label_170.setObjectName(u"label_170")

        self.horizontalLayout_74.addWidget(self.label_170)

        self.label_171 = QLabel(self.centralwidget)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_171.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.label_171)

        self.label_172 = QLabel(self.centralwidget)
        self.label_172.setObjectName(u"label_172")

        self.horizontalLayout_74.addWidget(self.label_172)

        self.m260 = QLabel(self.centralwidget)
        self.m260.setObjectName(u"m260")
        self.m260.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m260.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.m260)

        self.m261 = QLabel(self.centralwidget)
        self.m261.setObjectName(u"m261")
        self.m261.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m261.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.m261)

        self.m262 = QLabel(self.centralwidget)
        self.m262.setObjectName(u"m262")
        self.m262.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m262.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.m262)

        self.m263 = QLabel(self.centralwidget)
        self.m263.setObjectName(u"m263")
        self.m263.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m263.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.m263)


        self.horizontalLayout_73.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_173 = QLabel(self.centralwidget)
        self.label_173.setObjectName(u"label_173")

        self.horizontalLayout_75.addWidget(self.label_173)

        self.tablaID27 = QLabel(self.centralwidget)
        self.tablaID27.setObjectName(u"tablaID27")
        self.tablaID27.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.tablaID27)

        self.label_174 = QLabel(self.centralwidget)
        self.label_174.setObjectName(u"label_174")

        self.horizontalLayout_75.addWidget(self.label_174)

        self.label_175 = QLabel(self.centralwidget)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_175.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.label_175)

        self.label_176 = QLabel(self.centralwidget)
        self.label_176.setObjectName(u"label_176")

        self.horizontalLayout_75.addWidget(self.label_176)

        self.m270 = QLabel(self.centralwidget)
        self.m270.setObjectName(u"m270")
        self.m270.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m270.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.m270)

        self.m271 = QLabel(self.centralwidget)
        self.m271.setObjectName(u"m271")
        self.m271.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m271.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.m271)

        self.m272 = QLabel(self.centralwidget)
        self.m272.setObjectName(u"m272")
        self.m272.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m272.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.m272)

        self.m273 = QLabel(self.centralwidget)
        self.m273.setObjectName(u"m273")
        self.m273.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m273.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.m273)


        self.horizontalLayout_73.addLayout(self.horizontalLayout_75)


        self.verticalLayout_2.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setSpacing(0)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.tablaID28 = QLabel(self.centralwidget)
        self.tablaID28.setObjectName(u"tablaID28")
        self.tablaID28.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_110.addWidget(self.tablaID28)

        self.label_254 = QLabel(self.centralwidget)
        self.label_254.setObjectName(u"label_254")

        self.horizontalLayout_110.addWidget(self.label_254)

        self.label_255 = QLabel(self.centralwidget)
        self.label_255.setObjectName(u"label_255")
        self.label_255.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_255.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_110.addWidget(self.label_255)

        self.label_256 = QLabel(self.centralwidget)
        self.label_256.setObjectName(u"label_256")

        self.horizontalLayout_110.addWidget(self.label_256)

        self.m280 = QLabel(self.centralwidget)
        self.m280.setObjectName(u"m280")
        self.m280.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m280.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_110.addWidget(self.m280)

        self.m281 = QLabel(self.centralwidget)
        self.m281.setObjectName(u"m281")
        self.m281.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m281.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_110.addWidget(self.m281)

        self.m282 = QLabel(self.centralwidget)
        self.m282.setObjectName(u"m282")
        self.m282.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m282.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_110.addWidget(self.m282)

        self.m283 = QLabel(self.centralwidget)
        self.m283.setObjectName(u"m283")
        self.m283.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m283.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_110.addWidget(self.m283)


        self.horizontalLayout_109.addLayout(self.horizontalLayout_110)

        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setSpacing(0)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.label_257 = QLabel(self.centralwidget)
        self.label_257.setObjectName(u"label_257")

        self.horizontalLayout_111.addWidget(self.label_257)

        self.tablaID29 = QLabel(self.centralwidget)
        self.tablaID29.setObjectName(u"tablaID29")
        self.tablaID29.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_111.addWidget(self.tablaID29)

        self.label_258 = QLabel(self.centralwidget)
        self.label_258.setObjectName(u"label_258")

        self.horizontalLayout_111.addWidget(self.label_258)

        self.label_259 = QLabel(self.centralwidget)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_259.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_111.addWidget(self.label_259)

        self.label_260 = QLabel(self.centralwidget)
        self.label_260.setObjectName(u"label_260")

        self.horizontalLayout_111.addWidget(self.label_260)

        self.m290 = QLabel(self.centralwidget)
        self.m290.setObjectName(u"m290")
        self.m290.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m290.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_111.addWidget(self.m290)

        self.m291 = QLabel(self.centralwidget)
        self.m291.setObjectName(u"m291")
        self.m291.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m291.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_111.addWidget(self.m291)

        self.m292 = QLabel(self.centralwidget)
        self.m292.setObjectName(u"m292")
        self.m292.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m292.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_111.addWidget(self.m292)

        self.m293 = QLabel(self.centralwidget)
        self.m293.setObjectName(u"m293")
        self.m293.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m293.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_111.addWidget(self.m293)


        self.horizontalLayout_109.addLayout(self.horizontalLayout_111)


        self.verticalLayout_2.addLayout(self.horizontalLayout_109)

        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_119 = QHBoxLayout()
        self.horizontalLayout_119.setSpacing(0)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.tablaID30 = QLabel(self.centralwidget)
        self.tablaID30.setObjectName(u"tablaID30")
        self.tablaID30.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_119.addWidget(self.tablaID30)

        self.label_275 = QLabel(self.centralwidget)
        self.label_275.setObjectName(u"label_275")

        self.horizontalLayout_119.addWidget(self.label_275)

        self.label_276 = QLabel(self.centralwidget)
        self.label_276.setObjectName(u"label_276")
        self.label_276.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_276.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_119.addWidget(self.label_276)

        self.label_277 = QLabel(self.centralwidget)
        self.label_277.setObjectName(u"label_277")

        self.horizontalLayout_119.addWidget(self.label_277)

        self.m300 = QLabel(self.centralwidget)
        self.m300.setObjectName(u"m300")
        self.m300.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m300.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_119.addWidget(self.m300)

        self.m301 = QLabel(self.centralwidget)
        self.m301.setObjectName(u"m301")
        self.m301.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m301.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_119.addWidget(self.m301)

        self.m302 = QLabel(self.centralwidget)
        self.m302.setObjectName(u"m302")
        self.m302.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m302.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_119.addWidget(self.m302)

        self.m303 = QLabel(self.centralwidget)
        self.m303.setObjectName(u"m303")
        self.m303.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m303.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_119.addWidget(self.m303)


        self.horizontalLayout_118.addLayout(self.horizontalLayout_119)

        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setSpacing(0)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.label_278 = QLabel(self.centralwidget)
        self.label_278.setObjectName(u"label_278")

        self.horizontalLayout_120.addWidget(self.label_278)

        self.tablaID31 = QLabel(self.centralwidget)
        self.tablaID31.setObjectName(u"tablaID31")
        self.tablaID31.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_120.addWidget(self.tablaID31)

        self.label_279 = QLabel(self.centralwidget)
        self.label_279.setObjectName(u"label_279")

        self.horizontalLayout_120.addWidget(self.label_279)

        self.label_280 = QLabel(self.centralwidget)
        self.label_280.setObjectName(u"label_280")
        self.label_280.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_280.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_120.addWidget(self.label_280)

        self.label_281 = QLabel(self.centralwidget)
        self.label_281.setObjectName(u"label_281")

        self.horizontalLayout_120.addWidget(self.label_281)

        self.m310 = QLabel(self.centralwidget)
        self.m310.setObjectName(u"m310")
        self.m310.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m310.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_120.addWidget(self.m310)

        self.m311 = QLabel(self.centralwidget)
        self.m311.setObjectName(u"m311")
        self.m311.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m311.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_120.addWidget(self.m311)

        self.m312 = QLabel(self.centralwidget)
        self.m312.setObjectName(u"m312")
        self.m312.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m312.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_120.addWidget(self.m312)

        self.m313 = QLabel(self.centralwidget)
        self.m313.setObjectName(u"m313")
        self.m313.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m313.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_120.addWidget(self.m313)


        self.horizontalLayout_118.addLayout(self.horizontalLayout_120)


        self.verticalLayout_2.addLayout(self.horizontalLayout_118)

        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_113 = QHBoxLayout()
        self.horizontalLayout_113.setSpacing(0)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.tablaID32 = QLabel(self.centralwidget)
        self.tablaID32.setObjectName(u"tablaID32")
        self.tablaID32.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_113.addWidget(self.tablaID32)

        self.label_261 = QLabel(self.centralwidget)
        self.label_261.setObjectName(u"label_261")

        self.horizontalLayout_113.addWidget(self.label_261)

        self.label_262 = QLabel(self.centralwidget)
        self.label_262.setObjectName(u"label_262")
        self.label_262.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_262.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_113.addWidget(self.label_262)

        self.label_263 = QLabel(self.centralwidget)
        self.label_263.setObjectName(u"label_263")

        self.horizontalLayout_113.addWidget(self.label_263)

        self.m320 = QLabel(self.centralwidget)
        self.m320.setObjectName(u"m320")
        self.m320.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m320.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_113.addWidget(self.m320)

        self.m321 = QLabel(self.centralwidget)
        self.m321.setObjectName(u"m321")
        self.m321.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m321.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_113.addWidget(self.m321)

        self.m322 = QLabel(self.centralwidget)
        self.m322.setObjectName(u"m322")
        self.m322.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m322.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_113.addWidget(self.m322)

        self.m323 = QLabel(self.centralwidget)
        self.m323.setObjectName(u"m323")
        self.m323.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m323.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_113.addWidget(self.m323)


        self.horizontalLayout_112.addLayout(self.horizontalLayout_113)

        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setSpacing(0)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.label_264 = QLabel(self.centralwidget)
        self.label_264.setObjectName(u"label_264")

        self.horizontalLayout_114.addWidget(self.label_264)

        self.tablaID33 = QLabel(self.centralwidget)
        self.tablaID33.setObjectName(u"tablaID33")
        self.tablaID33.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_114.addWidget(self.tablaID33)

        self.label_265 = QLabel(self.centralwidget)
        self.label_265.setObjectName(u"label_265")

        self.horizontalLayout_114.addWidget(self.label_265)

        self.label_266 = QLabel(self.centralwidget)
        self.label_266.setObjectName(u"label_266")
        self.label_266.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_266.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_114.addWidget(self.label_266)

        self.label_267 = QLabel(self.centralwidget)
        self.label_267.setObjectName(u"label_267")

        self.horizontalLayout_114.addWidget(self.label_267)

        self.m330 = QLabel(self.centralwidget)
        self.m330.setObjectName(u"m330")
        self.m330.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m330.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_114.addWidget(self.m330)

        self.m331 = QLabel(self.centralwidget)
        self.m331.setObjectName(u"m331")
        self.m331.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m331.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_114.addWidget(self.m331)

        self.m332 = QLabel(self.centralwidget)
        self.m332.setObjectName(u"m332")
        self.m332.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m332.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_114.addWidget(self.m332)

        self.m333 = QLabel(self.centralwidget)
        self.m333.setObjectName(u"m333")
        self.m333.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m333.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_114.addWidget(self.m333)


        self.horizontalLayout_112.addLayout(self.horizontalLayout_114)


        self.verticalLayout_2.addLayout(self.horizontalLayout_112)

        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setSpacing(0)
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.tablaID34 = QLabel(self.centralwidget)
        self.tablaID34.setObjectName(u"tablaID34")
        self.tablaID34.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_122.addWidget(self.tablaID34)

        self.label_282 = QLabel(self.centralwidget)
        self.label_282.setObjectName(u"label_282")

        self.horizontalLayout_122.addWidget(self.label_282)

        self.label_283 = QLabel(self.centralwidget)
        self.label_283.setObjectName(u"label_283")
        self.label_283.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_283.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_122.addWidget(self.label_283)

        self.label_284 = QLabel(self.centralwidget)
        self.label_284.setObjectName(u"label_284")

        self.horizontalLayout_122.addWidget(self.label_284)

        self.m340 = QLabel(self.centralwidget)
        self.m340.setObjectName(u"m340")
        self.m340.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m340.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_122.addWidget(self.m340)

        self.m341 = QLabel(self.centralwidget)
        self.m341.setObjectName(u"m341")
        self.m341.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m341.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_122.addWidget(self.m341)

        self.m342 = QLabel(self.centralwidget)
        self.m342.setObjectName(u"m342")
        self.m342.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m342.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_122.addWidget(self.m342)

        self.m343 = QLabel(self.centralwidget)
        self.m343.setObjectName(u"m343")
        self.m343.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m343.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_122.addWidget(self.m343)


        self.horizontalLayout_121.addLayout(self.horizontalLayout_122)

        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setSpacing(0)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.label_285 = QLabel(self.centralwidget)
        self.label_285.setObjectName(u"label_285")

        self.horizontalLayout_123.addWidget(self.label_285)

        self.tablaID35 = QLabel(self.centralwidget)
        self.tablaID35.setObjectName(u"tablaID35")
        self.tablaID35.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_123.addWidget(self.tablaID35)

        self.label_286 = QLabel(self.centralwidget)
        self.label_286.setObjectName(u"label_286")

        self.horizontalLayout_123.addWidget(self.label_286)

        self.label_287 = QLabel(self.centralwidget)
        self.label_287.setObjectName(u"label_287")
        self.label_287.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_287.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_123.addWidget(self.label_287)

        self.label_288 = QLabel(self.centralwidget)
        self.label_288.setObjectName(u"label_288")

        self.horizontalLayout_123.addWidget(self.label_288)

        self.m350 = QLabel(self.centralwidget)
        self.m350.setObjectName(u"m350")
        self.m350.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m350.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_123.addWidget(self.m350)

        self.m351 = QLabel(self.centralwidget)
        self.m351.setObjectName(u"m351")
        self.m351.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m351.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_123.addWidget(self.m351)

        self.m352 = QLabel(self.centralwidget)
        self.m352.setObjectName(u"m352")
        self.m352.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m352.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_123.addWidget(self.m352)

        self.m353 = QLabel(self.centralwidget)
        self.m353.setObjectName(u"m353")
        self.m353.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m353.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_123.addWidget(self.m353)


        self.horizontalLayout_121.addLayout(self.horizontalLayout_123)


        self.verticalLayout_2.addLayout(self.horizontalLayout_121)

        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setSpacing(0)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.tablaID36 = QLabel(self.centralwidget)
        self.tablaID36.setObjectName(u"tablaID36")
        self.tablaID36.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_116.addWidget(self.tablaID36)

        self.label_268 = QLabel(self.centralwidget)
        self.label_268.setObjectName(u"label_268")

        self.horizontalLayout_116.addWidget(self.label_268)

        self.label_269 = QLabel(self.centralwidget)
        self.label_269.setObjectName(u"label_269")
        self.label_269.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_269.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_116.addWidget(self.label_269)

        self.label_270 = QLabel(self.centralwidget)
        self.label_270.setObjectName(u"label_270")

        self.horizontalLayout_116.addWidget(self.label_270)

        self.m360 = QLabel(self.centralwidget)
        self.m360.setObjectName(u"m360")
        self.m360.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m360.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_116.addWidget(self.m360)

        self.m361 = QLabel(self.centralwidget)
        self.m361.setObjectName(u"m361")
        self.m361.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m361.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_116.addWidget(self.m361)

        self.m362 = QLabel(self.centralwidget)
        self.m362.setObjectName(u"m362")
        self.m362.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m362.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_116.addWidget(self.m362)

        self.m363 = QLabel(self.centralwidget)
        self.m363.setObjectName(u"m363")
        self.m363.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m363.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_116.addWidget(self.m363)


        self.horizontalLayout_115.addLayout(self.horizontalLayout_116)

        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setSpacing(0)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.label_271 = QLabel(self.centralwidget)
        self.label_271.setObjectName(u"label_271")

        self.horizontalLayout_117.addWidget(self.label_271)

        self.tablaID37 = QLabel(self.centralwidget)
        self.tablaID37.setObjectName(u"tablaID37")
        self.tablaID37.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_117.addWidget(self.tablaID37)

        self.label_272 = QLabel(self.centralwidget)
        self.label_272.setObjectName(u"label_272")

        self.horizontalLayout_117.addWidget(self.label_272)

        self.label_273 = QLabel(self.centralwidget)
        self.label_273.setObjectName(u"label_273")
        self.label_273.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_273.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_117.addWidget(self.label_273)

        self.label_274 = QLabel(self.centralwidget)
        self.label_274.setObjectName(u"label_274")

        self.horizontalLayout_117.addWidget(self.label_274)

        self.m370 = QLabel(self.centralwidget)
        self.m370.setObjectName(u"m370")
        self.m370.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m370.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_117.addWidget(self.m370)

        self.m371 = QLabel(self.centralwidget)
        self.m371.setObjectName(u"m371")
        self.m371.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m371.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_117.addWidget(self.m371)

        self.m372 = QLabel(self.centralwidget)
        self.m372.setObjectName(u"m372")
        self.m372.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m372.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_117.addWidget(self.m372)

        self.m373 = QLabel(self.centralwidget)
        self.m373.setObjectName(u"m373")
        self.m373.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m373.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_117.addWidget(self.m373)


        self.horizontalLayout_115.addLayout(self.horizontalLayout_117)


        self.verticalLayout_2.addLayout(self.horizontalLayout_115)

        self.horizontalLayout_163 = QHBoxLayout()
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalLayout_164 = QHBoxLayout()
        self.horizontalLayout_164.setSpacing(0)
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.tablaID38 = QLabel(self.centralwidget)
        self.tablaID38.setObjectName(u"tablaID38")
        self.tablaID38.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_164.addWidget(self.tablaID38)

        self.label_380 = QLabel(self.centralwidget)
        self.label_380.setObjectName(u"label_380")

        self.horizontalLayout_164.addWidget(self.label_380)

        self.label_381 = QLabel(self.centralwidget)
        self.label_381.setObjectName(u"label_381")
        self.label_381.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_381.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_164.addWidget(self.label_381)

        self.label_382 = QLabel(self.centralwidget)
        self.label_382.setObjectName(u"label_382")

        self.horizontalLayout_164.addWidget(self.label_382)

        self.m380 = QLabel(self.centralwidget)
        self.m380.setObjectName(u"m380")
        self.m380.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m380.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_164.addWidget(self.m380)

        self.m381 = QLabel(self.centralwidget)
        self.m381.setObjectName(u"m381")
        self.m381.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m381.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_164.addWidget(self.m381)

        self.m382 = QLabel(self.centralwidget)
        self.m382.setObjectName(u"m382")
        self.m382.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m382.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_164.addWidget(self.m382)

        self.m383 = QLabel(self.centralwidget)
        self.m383.setObjectName(u"m383")
        self.m383.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m383.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_164.addWidget(self.m383)


        self.horizontalLayout_163.addLayout(self.horizontalLayout_164)

        self.horizontalLayout_165 = QHBoxLayout()
        self.horizontalLayout_165.setSpacing(0)
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.label_383 = QLabel(self.centralwidget)
        self.label_383.setObjectName(u"label_383")

        self.horizontalLayout_165.addWidget(self.label_383)

        self.tablaID39 = QLabel(self.centralwidget)
        self.tablaID39.setObjectName(u"tablaID39")
        self.tablaID39.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_165.addWidget(self.tablaID39)

        self.label_384 = QLabel(self.centralwidget)
        self.label_384.setObjectName(u"label_384")

        self.horizontalLayout_165.addWidget(self.label_384)

        self.label_385 = QLabel(self.centralwidget)
        self.label_385.setObjectName(u"label_385")
        self.label_385.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_385.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_165.addWidget(self.label_385)

        self.label_386 = QLabel(self.centralwidget)
        self.label_386.setObjectName(u"label_386")

        self.horizontalLayout_165.addWidget(self.label_386)

        self.m390 = QLabel(self.centralwidget)
        self.m390.setObjectName(u"m390")
        self.m390.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m390.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_165.addWidget(self.m390)

        self.m391 = QLabel(self.centralwidget)
        self.m391.setObjectName(u"m391")
        self.m391.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m391.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_165.addWidget(self.m391)

        self.m392 = QLabel(self.centralwidget)
        self.m392.setObjectName(u"m392")
        self.m392.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m392.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_165.addWidget(self.m392)

        self.m393 = QLabel(self.centralwidget)
        self.m393.setObjectName(u"m393")
        self.m393.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m393.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_165.addWidget(self.m393)


        self.horizontalLayout_163.addLayout(self.horizontalLayout_165)


        self.verticalLayout_2.addLayout(self.horizontalLayout_163)

        self.horizontalLayout_154 = QHBoxLayout()
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalLayout_155 = QHBoxLayout()
        self.horizontalLayout_155.setSpacing(0)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.tablaID40 = QLabel(self.centralwidget)
        self.tablaID40.setObjectName(u"tablaID40")
        self.tablaID40.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_155.addWidget(self.tablaID40)

        self.label_359 = QLabel(self.centralwidget)
        self.label_359.setObjectName(u"label_359")

        self.horizontalLayout_155.addWidget(self.label_359)

        self.label_360 = QLabel(self.centralwidget)
        self.label_360.setObjectName(u"label_360")
        self.label_360.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_360.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_155.addWidget(self.label_360)

        self.label_361 = QLabel(self.centralwidget)
        self.label_361.setObjectName(u"label_361")

        self.horizontalLayout_155.addWidget(self.label_361)

        self.m400 = QLabel(self.centralwidget)
        self.m400.setObjectName(u"m400")
        self.m400.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m400.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_155.addWidget(self.m400)

        self.m401 = QLabel(self.centralwidget)
        self.m401.setObjectName(u"m401")
        self.m401.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m401.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_155.addWidget(self.m401)

        self.m402 = QLabel(self.centralwidget)
        self.m402.setObjectName(u"m402")
        self.m402.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m402.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_155.addWidget(self.m402)

        self.m403 = QLabel(self.centralwidget)
        self.m403.setObjectName(u"m403")
        self.m403.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m403.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_155.addWidget(self.m403)


        self.horizontalLayout_154.addLayout(self.horizontalLayout_155)

        self.horizontalLayout_156 = QHBoxLayout()
        self.horizontalLayout_156.setSpacing(0)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.label_362 = QLabel(self.centralwidget)
        self.label_362.setObjectName(u"label_362")

        self.horizontalLayout_156.addWidget(self.label_362)

        self.tablaID41 = QLabel(self.centralwidget)
        self.tablaID41.setObjectName(u"tablaID41")
        self.tablaID41.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_156.addWidget(self.tablaID41)

        self.label_363 = QLabel(self.centralwidget)
        self.label_363.setObjectName(u"label_363")

        self.horizontalLayout_156.addWidget(self.label_363)

        self.label_364 = QLabel(self.centralwidget)
        self.label_364.setObjectName(u"label_364")
        self.label_364.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_364.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_156.addWidget(self.label_364)

        self.label_365 = QLabel(self.centralwidget)
        self.label_365.setObjectName(u"label_365")

        self.horizontalLayout_156.addWidget(self.label_365)

        self.m410 = QLabel(self.centralwidget)
        self.m410.setObjectName(u"m410")
        self.m410.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m410.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_156.addWidget(self.m410)

        self.m411 = QLabel(self.centralwidget)
        self.m411.setObjectName(u"m411")
        self.m411.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m411.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_156.addWidget(self.m411)

        self.m412 = QLabel(self.centralwidget)
        self.m412.setObjectName(u"m412")
        self.m412.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m412.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_156.addWidget(self.m412)

        self.m413 = QLabel(self.centralwidget)
        self.m413.setObjectName(u"m413")
        self.m413.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m413.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_156.addWidget(self.m413)


        self.horizontalLayout_154.addLayout(self.horizontalLayout_156)


        self.verticalLayout_2.addLayout(self.horizontalLayout_154)

        self.horizontalLayout_160 = QHBoxLayout()
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.horizontalLayout_161 = QHBoxLayout()
        self.horizontalLayout_161.setSpacing(0)
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.tablaID42 = QLabel(self.centralwidget)
        self.tablaID42.setObjectName(u"tablaID42")
        self.tablaID42.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_161.addWidget(self.tablaID42)

        self.label_373 = QLabel(self.centralwidget)
        self.label_373.setObjectName(u"label_373")

        self.horizontalLayout_161.addWidget(self.label_373)

        self.label_374 = QLabel(self.centralwidget)
        self.label_374.setObjectName(u"label_374")
        self.label_374.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_374.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_161.addWidget(self.label_374)

        self.label_375 = QLabel(self.centralwidget)
        self.label_375.setObjectName(u"label_375")

        self.horizontalLayout_161.addWidget(self.label_375)

        self.m420 = QLabel(self.centralwidget)
        self.m420.setObjectName(u"m420")
        self.m420.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m420.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_161.addWidget(self.m420)

        self.m421 = QLabel(self.centralwidget)
        self.m421.setObjectName(u"m421")
        self.m421.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m421.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_161.addWidget(self.m421)

        self.m422 = QLabel(self.centralwidget)
        self.m422.setObjectName(u"m422")
        self.m422.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m422.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_161.addWidget(self.m422)

        self.m423 = QLabel(self.centralwidget)
        self.m423.setObjectName(u"m423")
        self.m423.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m423.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_161.addWidget(self.m423)


        self.horizontalLayout_160.addLayout(self.horizontalLayout_161)

        self.horizontalLayout_162 = QHBoxLayout()
        self.horizontalLayout_162.setSpacing(0)
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.label_376 = QLabel(self.centralwidget)
        self.label_376.setObjectName(u"label_376")

        self.horizontalLayout_162.addWidget(self.label_376)

        self.tablaID43 = QLabel(self.centralwidget)
        self.tablaID43.setObjectName(u"tablaID43")
        self.tablaID43.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_162.addWidget(self.tablaID43)

        self.label_377 = QLabel(self.centralwidget)
        self.label_377.setObjectName(u"label_377")

        self.horizontalLayout_162.addWidget(self.label_377)

        self.label_378 = QLabel(self.centralwidget)
        self.label_378.setObjectName(u"label_378")
        self.label_378.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_378.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_162.addWidget(self.label_378)

        self.label_379 = QLabel(self.centralwidget)
        self.label_379.setObjectName(u"label_379")

        self.horizontalLayout_162.addWidget(self.label_379)

        self.m430 = QLabel(self.centralwidget)
        self.m430.setObjectName(u"m430")
        self.m430.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m430.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_162.addWidget(self.m430)

        self.m431 = QLabel(self.centralwidget)
        self.m431.setObjectName(u"m431")
        self.m431.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m431.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_162.addWidget(self.m431)

        self.m432 = QLabel(self.centralwidget)
        self.m432.setObjectName(u"m432")
        self.m432.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m432.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_162.addWidget(self.m432)

        self.m433 = QLabel(self.centralwidget)
        self.m433.setObjectName(u"m433")
        self.m433.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m433.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_162.addWidget(self.m433)


        self.horizontalLayout_160.addLayout(self.horizontalLayout_162)


        self.verticalLayout_2.addLayout(self.horizontalLayout_160)

        self.horizontalLayout_157 = QHBoxLayout()
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalLayout_158 = QHBoxLayout()
        self.horizontalLayout_158.setSpacing(0)
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.tablaID44 = QLabel(self.centralwidget)
        self.tablaID44.setObjectName(u"tablaID44")
        self.tablaID44.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_158.addWidget(self.tablaID44)

        self.label_366 = QLabel(self.centralwidget)
        self.label_366.setObjectName(u"label_366")

        self.horizontalLayout_158.addWidget(self.label_366)

        self.label_367 = QLabel(self.centralwidget)
        self.label_367.setObjectName(u"label_367")
        self.label_367.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_367.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_158.addWidget(self.label_367)

        self.label_368 = QLabel(self.centralwidget)
        self.label_368.setObjectName(u"label_368")

        self.horizontalLayout_158.addWidget(self.label_368)

        self.m440 = QLabel(self.centralwidget)
        self.m440.setObjectName(u"m440")
        self.m440.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m440.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_158.addWidget(self.m440)

        self.m441 = QLabel(self.centralwidget)
        self.m441.setObjectName(u"m441")
        self.m441.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m441.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_158.addWidget(self.m441)

        self.m442 = QLabel(self.centralwidget)
        self.m442.setObjectName(u"m442")
        self.m442.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m442.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_158.addWidget(self.m442)

        self.m443 = QLabel(self.centralwidget)
        self.m443.setObjectName(u"m443")
        self.m443.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m443.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_158.addWidget(self.m443)


        self.horizontalLayout_157.addLayout(self.horizontalLayout_158)

        self.horizontalLayout_159 = QHBoxLayout()
        self.horizontalLayout_159.setSpacing(0)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.label_369 = QLabel(self.centralwidget)
        self.label_369.setObjectName(u"label_369")

        self.horizontalLayout_159.addWidget(self.label_369)

        self.tablaID45 = QLabel(self.centralwidget)
        self.tablaID45.setObjectName(u"tablaID45")
        self.tablaID45.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_159.addWidget(self.tablaID45)

        self.label_370 = QLabel(self.centralwidget)
        self.label_370.setObjectName(u"label_370")

        self.horizontalLayout_159.addWidget(self.label_370)

        self.label_371 = QLabel(self.centralwidget)
        self.label_371.setObjectName(u"label_371")
        self.label_371.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_371.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_159.addWidget(self.label_371)

        self.label_372 = QLabel(self.centralwidget)
        self.label_372.setObjectName(u"label_372")

        self.horizontalLayout_159.addWidget(self.label_372)

        self.m450 = QLabel(self.centralwidget)
        self.m450.setObjectName(u"m450")
        self.m450.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m450.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_159.addWidget(self.m450)

        self.m451 = QLabel(self.centralwidget)
        self.m451.setObjectName(u"m451")
        self.m451.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m451.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_159.addWidget(self.m451)

        self.m452 = QLabel(self.centralwidget)
        self.m452.setObjectName(u"m452")
        self.m452.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m452.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_159.addWidget(self.m452)

        self.m453 = QLabel(self.centralwidget)
        self.m453.setObjectName(u"m453")
        self.m453.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.m453.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_159.addWidget(self.m453)


        self.horizontalLayout_157.addLayout(self.horizontalLayout_159)


        self.verticalLayout_2.addLayout(self.horizontalLayout_157)

        self.horizontalLayout_166 = QHBoxLayout()
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.horizontalLayout_167 = QHBoxLayout()
        self.horizontalLayout_167.setSpacing(0)
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.tablaID46 = QLabel(self.centralwidget)
        self.tablaID46.setObjectName(u"tablaID46")
        self.tablaID46.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_167.addWidget(self.tablaID46)

        self.label_387 = QLabel(self.centralwidget)
        self.label_387.setObjectName(u"label_387")

        self.horizontalLayout_167.addWidget(self.label_387)

        self.label_388 = QLabel(self.centralwidget)
        self.label_388.setObjectName(u"label_388")
        self.label_388.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_388.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_167.addWidget(self.label_388)

        self.label_389 = QLabel(self.centralwidget)
        self.label_389.setObjectName(u"label_389")

        self.horizontalLayout_167.addWidget(self.label_389)

        self.m460 = QLabel(self.centralwidget)
        self.m460.setObjectName(u"m460")
        self.m460.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m460.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_167.addWidget(self.m460)

        self.m461 = QLabel(self.centralwidget)
        self.m461.setObjectName(u"m461")
        self.m461.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m461.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_167.addWidget(self.m461)

        self.m462 = QLabel(self.centralwidget)
        self.m462.setObjectName(u"m462")
        self.m462.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m462.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_167.addWidget(self.m462)

        self.m463 = QLabel(self.centralwidget)
        self.m463.setObjectName(u"m463")
        self.m463.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m463.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_167.addWidget(self.m463)


        self.horizontalLayout_166.addLayout(self.horizontalLayout_167)

        self.horizontalLayout_168 = QHBoxLayout()
        self.horizontalLayout_168.setSpacing(0)
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.label_390 = QLabel(self.centralwidget)
        self.label_390.setObjectName(u"label_390")

        self.horizontalLayout_168.addWidget(self.label_390)

        self.tablaID47 = QLabel(self.centralwidget)
        self.tablaID47.setObjectName(u"tablaID47")
        self.tablaID47.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_168.addWidget(self.tablaID47)

        self.label_391 = QLabel(self.centralwidget)
        self.label_391.setObjectName(u"label_391")

        self.horizontalLayout_168.addWidget(self.label_391)

        self.label_392 = QLabel(self.centralwidget)
        self.label_392.setObjectName(u"label_392")
        self.label_392.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_392.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_168.addWidget(self.label_392)

        self.label_393 = QLabel(self.centralwidget)
        self.label_393.setObjectName(u"label_393")

        self.horizontalLayout_168.addWidget(self.label_393)

        self.m470 = QLabel(self.centralwidget)
        self.m470.setObjectName(u"m470")
        self.m470.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m470.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_168.addWidget(self.m470)

        self.m471 = QLabel(self.centralwidget)
        self.m471.setObjectName(u"m471")
        self.m471.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m471.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_168.addWidget(self.m471)

        self.m472 = QLabel(self.centralwidget)
        self.m472.setObjectName(u"m472")
        self.m472.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m472.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_168.addWidget(self.m472)

        self.m473 = QLabel(self.centralwidget)
        self.m473.setObjectName(u"m473")
        self.m473.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m473.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_168.addWidget(self.m473)


        self.horizontalLayout_166.addLayout(self.horizontalLayout_168)


        self.verticalLayout_2.addLayout(self.horizontalLayout_166)

        self.horizontalLayout_187 = QHBoxLayout()
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.horizontalLayout_188 = QHBoxLayout()
        self.horizontalLayout_188.setSpacing(0)
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.tablaID48 = QLabel(self.centralwidget)
        self.tablaID48.setObjectName(u"tablaID48")
        self.tablaID48.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_188.addWidget(self.tablaID48)

        self.label_436 = QLabel(self.centralwidget)
        self.label_436.setObjectName(u"label_436")

        self.horizontalLayout_188.addWidget(self.label_436)

        self.label_437 = QLabel(self.centralwidget)
        self.label_437.setObjectName(u"label_437")
        self.label_437.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_437.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_188.addWidget(self.label_437)

        self.label_438 = QLabel(self.centralwidget)
        self.label_438.setObjectName(u"label_438")

        self.horizontalLayout_188.addWidget(self.label_438)

        self.m480 = QLabel(self.centralwidget)
        self.m480.setObjectName(u"m480")
        self.m480.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m480.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_188.addWidget(self.m480)

        self.m481 = QLabel(self.centralwidget)
        self.m481.setObjectName(u"m481")
        self.m481.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m481.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_188.addWidget(self.m481)

        self.m482 = QLabel(self.centralwidget)
        self.m482.setObjectName(u"m482")
        self.m482.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m482.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_188.addWidget(self.m482)

        self.m483 = QLabel(self.centralwidget)
        self.m483.setObjectName(u"m483")
        self.m483.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m483.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_188.addWidget(self.m483)


        self.horizontalLayout_187.addLayout(self.horizontalLayout_188)

        self.horizontalLayout_189 = QHBoxLayout()
        self.horizontalLayout_189.setSpacing(0)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.label_439 = QLabel(self.centralwidget)
        self.label_439.setObjectName(u"label_439")

        self.horizontalLayout_189.addWidget(self.label_439)

        self.tablaID49 = QLabel(self.centralwidget)
        self.tablaID49.setObjectName(u"tablaID49")
        self.tablaID49.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tablaID49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_189.addWidget(self.tablaID49)

        self.label_440 = QLabel(self.centralwidget)
        self.label_440.setObjectName(u"label_440")

        self.horizontalLayout_189.addWidget(self.label_440)

        self.label_441 = QLabel(self.centralwidget)
        self.label_441.setObjectName(u"label_441")
        self.label_441.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_441.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_189.addWidget(self.label_441)

        self.label_442 = QLabel(self.centralwidget)
        self.label_442.setObjectName(u"label_442")

        self.horizontalLayout_189.addWidget(self.label_442)

        self.m490 = QLabel(self.centralwidget)
        self.m490.setObjectName(u"m490")
        self.m490.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m490.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_189.addWidget(self.m490)

        self.m491 = QLabel(self.centralwidget)
        self.m491.setObjectName(u"m491")
        self.m491.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m491.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_189.addWidget(self.m491)

        self.m492 = QLabel(self.centralwidget)
        self.m492.setObjectName(u"m492")
        self.m492.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m492.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_189.addWidget(self.m492)

        self.m493 = QLabel(self.centralwidget)
        self.m493.setObjectName(u"m493")
        self.m493.setStyleSheet(u"background-color: #df00ff;\n"
"color: rgb(0, 0, 0);")
        self.m493.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_189.addWidget(self.m493)


        self.horizontalLayout_187.addLayout(self.horizontalLayout_189)


        self.verticalLayout_2.addLayout(self.horizontalLayout_187)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 6, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout.addLayout(self.horizontalLayout, 2, 5, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1925, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.label_7.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"N. de procesos", None))
        self.label_8.setText("")
        ___qtablewidgetitem = self.tablaPBloqueados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tablaPBloqueados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T. Bloqueado", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Procesos bloqueados", None))
        self.ejecutarBtn.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.agregarBtn.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Quantum", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Captura inicial", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Procesos listos", None))
        self.label_41.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Procesos nuevos", None))
        self.labelPendientes.setText("")
        ___qtablewidgetitem2 = self.tablaProcesos.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem3 = self.tablaProcesos.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"T. M\u00e1x", None));
        ___qtablewidgetitem4 = self.tablaProcesos.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"T. Trans", None));
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Pr\u00f3ximo nuevo", None))
        self.label_51.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.idProximoNuevo.setText("")
        self.label_64.setText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o", None))
        self.tamanioProximoNuevo.setText("")
        self.label_66.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Proceso en ejecuci\u00f3n", None))
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None))
        self.label_28.setText("")
        self.labelOperacion.setText("")
        self.label_29.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Tiempo transcurrido", None))
        self.label_31.setText("")
        self.label_32.setText("")
        self.labelTTtranscurrido.setText("")
        self.label_33.setText("")
        self.label_35.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Tiempo restante", None))
        self.label_55.setText("")
        self.label_56.setText("")
        self.labelTrestante.setText("")
        self.label_58.setText("")
        self.label_36.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_38.setText("")
        self.label_52.setText("")
        self.labelID.setText("")
        self.label_34.setText("")
        self.label_46.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Quantum", None))
        self.label_59.setText("")
        self.label_60.setText("")
        self.labelQuantum_2.setText("")
        self.label_61.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Procesos Terminados", None))
        ___qtablewidgetitem5 = self.tablaPTerminados.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem6 = self.tablaPTerminados.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem7 = self.tablaPTerminados.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tiempos calculados", None))
        ___qtablewidgetitem8 = self.tablaTiemposFinales.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem9 = self.tablaTiemposFinales.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TLL", None));
        ___qtablewidgetitem10 = self.tablaTiemposFinales.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"TF", None));
        ___qtablewidgetitem11 = self.tablaTiemposFinales.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"TRet", None));
        ___qtablewidgetitem12 = self.tablaTiemposFinales.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"TRes", None));
        ___qtablewidgetitem13 = self.tablaTiemposFinales.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"TE", None));
        ___qtablewidgetitem14 = self.tablaTiemposFinales.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"TS", None));
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Quantum", None))
        self.labelQuantumGlobal.setText("")
        self.label_6.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Contador", None))
        self.labelCGlobal.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Tabla de p\u00e1ginas", None))
        self.tablaID0_6.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_78.setText("")
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"N.M", None))
        self.label_80.setText("")
        self.m00_6.setText("")
        self.m01_6.setText("")
        self.m02_6.setText("")
        self.m03_6.setText("")
        self.label_81.setText("")
        self.tablaID1_6.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_82.setText("")
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"N.M", None))
        self.label_84.setText("")
        self.m10_6.setText("")
        self.m11_6.setText("")
        self.m12_6.setText("")
        self.m13_6.setText("")
        self.tablaID0.setText("")
        self.label_99.setText("")
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_101.setText("")
        self.m00.setText("")
        self.m01.setText("")
        self.m02.setText("")
        self.m03.setText("")
        self.label_102.setText("")
        self.tablaID1.setText("")
        self.label_103.setText("")
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_105.setText("")
        self.m10.setText("")
        self.m11.setText("")
        self.m12.setText("")
        self.m13.setText("")
        self.tablaID2.setText("")
        self.label_92.setText("")
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_94.setText("")
        self.m20.setText("")
        self.m21.setText("")
        self.m22.setText("")
        self.m23.setText("")
        self.label_95.setText("")
        self.tablaID3.setText("")
        self.label_96.setText("")
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_98.setText("")
        self.m30.setText("")
        self.m31.setText("")
        self.m32.setText("")
        self.m33.setText("")
        self.tablaID4.setText("")
        self.label_85.setText("")
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_87.setText("")
        self.m40.setText("")
        self.m41.setText("")
        self.m42.setText("")
        self.m43.setText("")
        self.label_88.setText("")
        self.tablaID5.setText("")
        self.label_89.setText("")
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_91.setText("")
        self.m50.setText("")
        self.m51.setText("")
        self.m52.setText("")
        self.m53.setText("")
        self.tablaID6.setText("")
        self.label_106.setText("")
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_108.setText("")
        self.m60.setText("")
        self.m61.setText("")
        self.m62.setText("")
        self.m63.setText("")
        self.label_109.setText("")
        self.tablaID7.setText("")
        self.label_110.setText("")
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_112.setText("")
        self.m70.setText("")
        self.m71.setText("")
        self.m72.setText("")
        self.m73.setText("")
        self.tablaID8.setText("")
        self.label_121.setText("")
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_123.setText("")
        self.m80.setText("")
        self.m81.setText("")
        self.m82.setText("")
        self.m83.setText("")
        self.label_124.setText("")
        self.tablaID9.setText("")
        self.label_125.setText("")
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.label_127.setText("")
        self.m90.setText("")
        self.m91.setText("")
        self.m92.setText("")
        self.m93.setText("")
        self.tablaID10.setText("")
        self.label_128.setText("")
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_130.setText("")
        self.m100.setText("")
        self.m101.setText("")
        self.m102.setText("")
        self.m103.setText("")
        self.label_131.setText("")
        self.tablaID11.setText("")
        self.label_132.setText("")
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.label_134.setText("")
        self.m110.setText("")
        self.m111.setText("")
        self.m112.setText("")
        self.m113.setText("")
        self.tablaID12.setText("")
        self.label_135.setText("")
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_137.setText("")
        self.m120.setText("")
        self.m121.setText("")
        self.m122.setText("")
        self.m123.setText("")
        self.label_138.setText("")
        self.tablaID13.setText("")
        self.label_139.setText("")
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_141.setText("")
        self.m130.setText("")
        self.m131.setText("")
        self.m132.setText("")
        self.m133.setText("")
        self.tablaID14.setText("")
        self.label_142.setText("")
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.label_144.setText("")
        self.m140.setText("")
        self.m141.setText("")
        self.m142.setText("")
        self.m143.setText("")
        self.label_145.setText("")
        self.tablaID15.setText("")
        self.label_146.setText("")
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.label_148.setText("")
        self.m150.setText("")
        self.m151.setText("")
        self.m152.setText("")
        self.m153.setText("")
        self.tablaID16.setText("")
        self.label_114.setText("")
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.label_116.setText("")
        self.m160.setText("")
        self.m161.setText("")
        self.m162.setText("")
        self.m163.setText("")
        self.label_117.setText("")
        self.tablaID17.setText("")
        self.label_118.setText("")
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_120.setText("")
        self.m170.setText("")
        self.m171.setText("")
        self.m172.setText("")
        self.m173.setText("")
        self.tablaID18.setText("")
        self.label_163.setText("")
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.label_165.setText("")
        self.m180.setText("")
        self.m181.setText("")
        self.m182.setText("")
        self.m183.setText("")
        self.label_166.setText("")
        self.tablaID19.setText("")
        self.label_167.setText("")
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_169.setText("")
        self.m190.setText("")
        self.m191.setText("")
        self.m192.setText("")
        self.m193.setText("")
        self.tablaID20.setText("")
        self.label_156.setText("")
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_158.setText("")
        self.m200.setText("")
        self.m201.setText("")
        self.m202.setText("")
        self.m203.setText("")
        self.label_159.setText("")
        self.tablaID21.setText("")
        self.label_160.setText("")
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.label_162.setText("")
        self.m210.setText("")
        self.m211.setText("")
        self.m212.setText("")
        self.m213_2.setText("")
        self.tablaID22.setText("")
        self.label_177.setText("")
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.label_179.setText("")
        self.m220.setText("")
        self.m221.setText("")
        self.m222.setText("")
        self.m213.setText("")
        self.label_180.setText("")
        self.tablaID23.setText("")
        self.label_181.setText("")
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_183.setText("")
        self.m230.setText("")
        self.m231.setText("")
        self.m232.setText("")
        self.m233.setText("")
        self.tablaID24.setText("")
        self.label_149.setText("")
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.label_151.setText("")
        self.m240.setText("")
        self.m241.setText("")
        self.m242.setText("")
        self.m244.setText("")
        self.label_152.setText("")
        self.tablaID25.setText("")
        self.label_153.setText("")
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_155.setText("")
        self.m250.setText("")
        self.m251.setText("")
        self.m252.setText("")
        self.m253.setText("")
        self.tablaID26.setText("")
        self.label_170.setText("")
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.label_172.setText("")
        self.m260.setText("")
        self.m261.setText("")
        self.m262.setText("")
        self.m263.setText("")
        self.label_173.setText("")
        self.tablaID27.setText("")
        self.label_174.setText("")
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.label_176.setText("")
        self.m270.setText("")
        self.m271.setText("")
        self.m272.setText("")
        self.m273.setText("")
        self.tablaID28.setText("")
        self.label_254.setText("")
        self.label_255.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.label_256.setText("")
        self.m280.setText("")
        self.m281.setText("")
        self.m282.setText("")
        self.m283.setText("")
        self.label_257.setText("")
        self.tablaID29.setText("")
        self.label_258.setText("")
        self.label_259.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.label_260.setText("")
        self.m290.setText("")
        self.m291.setText("")
        self.m292.setText("")
        self.m293.setText("")
        self.tablaID30.setText("")
        self.label_275.setText("")
        self.label_276.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_277.setText("")
        self.m300.setText("")
        self.m301.setText("")
        self.m302.setText("")
        self.m303.setText("")
        self.label_278.setText("")
        self.tablaID31.setText("")
        self.label_279.setText("")
        self.label_280.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.label_281.setText("")
        self.m310.setText("")
        self.m311.setText("")
        self.m312.setText("")
        self.m313.setText("")
        self.tablaID32.setText("")
        self.label_261.setText("")
        self.label_262.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.label_263.setText("")
        self.m320.setText("")
        self.m321.setText("")
        self.m322.setText("")
        self.m323.setText("")
        self.label_264.setText("")
        self.tablaID33.setText("")
        self.label_265.setText("")
        self.label_266.setText(QCoreApplication.translate("MainWindow", u"33", None))
        self.label_267.setText("")
        self.m330.setText("")
        self.m331.setText("")
        self.m332.setText("")
        self.m333.setText("")
        self.tablaID34.setText("")
        self.label_282.setText("")
        self.label_283.setText(QCoreApplication.translate("MainWindow", u"34", None))
        self.label_284.setText("")
        self.m340.setText("")
        self.m341.setText("")
        self.m342.setText("")
        self.m343.setText("")
        self.label_285.setText("")
        self.tablaID35.setText("")
        self.label_286.setText("")
        self.label_287.setText(QCoreApplication.translate("MainWindow", u"35", None))
        self.label_288.setText("")
        self.m350.setText("")
        self.m351.setText("")
        self.m352.setText("")
        self.m353.setText("")
        self.tablaID36.setText("")
        self.label_268.setText("")
        self.label_269.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.label_270.setText("")
        self.m360.setText("")
        self.m361.setText("")
        self.m362.setText("")
        self.m363.setText("")
        self.label_271.setText("")
        self.tablaID37.setText("")
        self.label_272.setText("")
        self.label_273.setText(QCoreApplication.translate("MainWindow", u"37", None))
        self.label_274.setText("")
        self.m370.setText("")
        self.m371.setText("")
        self.m372.setText("")
        self.m373.setText("")
        self.tablaID38.setText("")
        self.label_380.setText("")
        self.label_381.setText(QCoreApplication.translate("MainWindow", u"38", None))
        self.label_382.setText("")
        self.m380.setText("")
        self.m381.setText("")
        self.m382.setText("")
        self.m383.setText("")
        self.label_383.setText("")
        self.tablaID39.setText("")
        self.label_384.setText("")
        self.label_385.setText(QCoreApplication.translate("MainWindow", u"39", None))
        self.label_386.setText("")
        self.m390.setText("")
        self.m391.setText("")
        self.m392.setText("")
        self.m393.setText("")
        self.tablaID40.setText("")
        self.label_359.setText("")
        self.label_360.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.label_361.setText("")
        self.m400.setText("")
        self.m401.setText("")
        self.m402.setText("")
        self.m403.setText("")
        self.label_362.setText("")
        self.tablaID41.setText("")
        self.label_363.setText("")
        self.label_364.setText(QCoreApplication.translate("MainWindow", u"41", None))
        self.label_365.setText("")
        self.m410.setText("")
        self.m411.setText("")
        self.m412.setText("")
        self.m413.setText("")
        self.tablaID42.setText("")
        self.label_373.setText("")
        self.label_374.setText(QCoreApplication.translate("MainWindow", u"42", None))
        self.label_375.setText("")
        self.m420.setText("")
        self.m421.setText("")
        self.m422.setText("")
        self.m423.setText("")
        self.label_376.setText("")
        self.tablaID43.setText("")
        self.label_377.setText("")
        self.label_378.setText(QCoreApplication.translate("MainWindow", u"43", None))
        self.label_379.setText("")
        self.m430.setText("")
        self.m431.setText("")
        self.m432.setText("")
        self.m433.setText("")
        self.tablaID44.setText("")
        self.label_366.setText("")
        self.label_367.setText(QCoreApplication.translate("MainWindow", u"44", None))
        self.label_368.setText("")
        self.m440.setText("")
        self.m441.setText("")
        self.m442.setText("")
        self.m443.setText("")
        self.label_369.setText("")
        self.tablaID45.setText("")
        self.label_370.setText("")
        self.label_371.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.label_372.setText("")
        self.m450.setText("")
        self.m451.setText("")
        self.m452.setText("")
        self.m453.setText("")
        self.tablaID46.setText(QCoreApplication.translate("MainWindow", u"SO", None))
        self.label_387.setText("")
        self.label_388.setText(QCoreApplication.translate("MainWindow", u"46", None))
        self.label_389.setText("")
        self.m460.setText("")
        self.m461.setText("")
        self.m462.setText("")
        self.m463.setText("")
        self.label_390.setText("")
        self.tablaID47.setText(QCoreApplication.translate("MainWindow", u"SO", None))
        self.label_391.setText("")
        self.label_392.setText(QCoreApplication.translate("MainWindow", u"47", None))
        self.label_393.setText("")
        self.m470.setText("")
        self.m471.setText("")
        self.m472.setText("")
        self.m473.setText("")
        self.tablaID48.setText(QCoreApplication.translate("MainWindow", u"SO", None))
        self.label_436.setText("")
        self.label_437.setText(QCoreApplication.translate("MainWindow", u"48", None))
        self.label_438.setText("")
        self.m480.setText("")
        self.m481.setText("")
        self.m482.setText("")
        self.m483.setText("")
        self.label_439.setText("")
        self.tablaID49.setText(QCoreApplication.translate("MainWindow", u"SO", None))
        self.label_440.setText("")
        self.label_441.setText(QCoreApplication.translate("MainWindow", u"49", None))
        self.label_442.setText("")
        self.m490.setText("")
        self.m491.setText("")
        self.m492.setText("")
        self.m493.setText("")
    # retranslateUi

