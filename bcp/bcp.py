import PySide2
from PySide2.QtWidgets import QWidget, QTableWidgetItem
from PySide2.QtCore import QCoreApplication
from bcp.ui_bcp import Ui_Form
#from bcp import BCP

class BCP(QWidget):
    def __init__(self, procesos: list):
        super().__init__()
        self.ui =  Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('Tabla de BCP')

        self.__procesos = procesos
        self.mostrarTablaBCP()


    def mostrarTablaBCP(self):
        row = 0
        #self.ui.tablaBCP.setRowCount(len(self.__procesos))
        for proceso in self.__procesos:
            id = str(proceso.getID())
            if str(proceso.getID()) != 'NULL':
                operacion = f'{ proceso.getNum1() } { proceso.getOperador() } { proceso.getNum2() }'
                resultado = str(proceso.getResultado())
                estado = proceso.getEstado()
                tmax = str(proceso.getTMax())
                #TIEMPOS
                tll = str('-' if proceso.getTLL() == -1 else proceso.getTLL())
                tf= str('-' if proceso.getTF() == -1 else proceso.getTF())
                tres= str('-' if proceso.getTRes() == -1 else proceso.getTRes())
                tret= str('-' if proceso.getTRet() == -1 else proceso.getTRet())
                ts= str('-' if proceso.getEstado() == 'nuevo' else proceso.getTS())
                te= str('-' if proceso.getEstado() == 'nuevo' else proceso.getTE())
                tb = str(proceso.getCont() if proceso.getEstado() == 'bloqueado' else '-')

                self.ui.tablaBCP.insertRow(self.ui.tablaBCP.rowCount())

                itemID = QTableWidgetItem(id)
                itemOperacion = QTableWidgetItem(operacion)
                itemResultado = QTableWidgetItem(resultado)
                itemEstado = QTableWidgetItem(estado)
                itemTMax = QTableWidgetItem(tmax)
                itemTLL = QTableWidgetItem(tll)
                itemTE = QTableWidgetItem(te)
                itemTF = QTableWidgetItem(tf)
                itemTRes = QTableWidgetItem(tres)
                itemTRet = QTableWidgetItem(tret)
                itemTS = QTableWidgetItem(ts)
                itemTB = QTableWidgetItem(tb)

                self.ui.tablaBCP.setItem(row, 0, itemID)                
                self.ui.tablaBCP.setItem(row, 1, itemOperacion)
                self.ui.tablaBCP.setItem(row, 2, itemResultado)
                self.ui.tablaBCP.setItem(row, 3, itemEstado)
                self.ui.tablaBCP.setItem(row, 4, itemTMax)
                self.ui.tablaBCP.setItem(row, 5, itemTLL)
                self.ui.tablaBCP.setItem(row, 6, itemTE)
                self.ui.tablaBCP.setItem(row, 7, itemTF)
                self.ui.tablaBCP.setItem(row, 8, itemTRes)
                self.ui.tablaBCP.setItem(row, 9, itemTRet)
                self.ui.tablaBCP.setItem(row, 10, itemTS)
                self.ui.tablaBCP.setItem(row, 11, itemTB)
                row += 1

        # self.ui.tablaBCP.setEnabled(False)
        self.ui.tablaBCP.setAlternatingRowColors(True)

        