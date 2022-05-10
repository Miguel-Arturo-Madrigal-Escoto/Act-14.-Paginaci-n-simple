from PySide2.QtWidgets import QMessageBox

def notify(self,tipo,event,detail=''):
        msg=QMessageBox(self)

        # dia=QtGui.QDialog(self)
        msg.setText(event)
        msg.setInformativeText(detail)
        # dia.setDetailedText(detail)
        #msg.setStandardButtons(QMessageBox.NoButton)
        if tipo=='error':
            msg.setStyleSheet(".QMessageBox{background:rgba(250,30,10,255);color:#fff}QLabel{background:transparent;color:#000}QPushButton{color:#fff}")
            msg.setIcon(QMessageBox.Critical)
        elif tipo=='info':
            msg.setStyleSheet(".QMessageBox{background:#cc0000;color:#fff}QLabel{background:transparent;color:#000}QPushButton{color:#fff}")	
            msg.setIcon(QMessageBox.Information)
        elif tipo=='advertencia':
            msg.setStyleSheet(".QMessageBox{background:rgba(255,200,0,255);color:#000}QLabel{background:transparent;color:#000}QPushButton{color:#fff}")	
            msg.setIcon(QMessageBox.Warning)
        elif tipo=='exito':	
            msg.setStyleSheet(".QMessageBox{background:#4BB543;color:#000}QLabel{background:transparent;color:#000}QPushButton{color:#fff}")	
            msg.setIcon(QMessageBox.Information)
            
        msg.show()