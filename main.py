from PySide2.QtWidgets import QApplication
from main_window import MainWindow
import sys

# Aplicación de Qt
app = QApplication()
"""Se crea una instancia a la clase MainWindow
que hereda de QMainWindow"""
window = MainWindow()
"""Se hace visible la ventana, show es un metodo
heredado de QMainWindow"""
window.show()
# Qt loop
sys.exit(app.exec_())


"""
Tabla de paginas:
    MARCO
    TAMAÑO
    ID
    ESTADO
Colores:
    Listo: #fbff00
    Ejecucion: #12ff00 
    Bloqueado: #ff0000
    SO: #df00ff

    - Colorear espacios de los marcos ←
    - Colorear Estado de los procesos en memoria ←
    - Liberar los marcos cuando se termina el proceso (volver a TRUE), falso es que esta ocupado ←
    - PINTAR DE BLANCO LOS QUE YA SALIERON ←
    - Quitar lo de 5 procesos en memoria ←
    - Hacer todo tecla n  ←
    - Asignen marcos en otro lado porque ta mal (ya que solo se hace al inicio cuando se establecen los 5 procesos listos, cuando el proceso entra a listo en sus variantes) checar varias versiones de entrar a listo (3 variaciones) ←

    - Checar proceso nulo
    - tiempo de llegada -1 checar
"""
