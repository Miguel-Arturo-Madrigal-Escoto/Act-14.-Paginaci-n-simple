import threading
from PySide2.QtWidgets import QMainWindow, QTableWidgetItem
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide2.QtCore import Slot, QCoreApplication
from advertencia import notify
from bcp.bcp import BCP
from src.cola_listos import ColaListos
from src.proceso import Proceso
from ui_mainwindow import Ui_MainWindow
from random import randint, choice
from time import sleep
from math import ceil
import keyboard


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Paginación Simple')
        
        # ? boton de agregar
        self.ui.agregarBtn.clicked.connect(self.generarProcesos)

        # ? boton de ejecutar
        self.ui.ejecutarBtn.clicked.connect(self.comenzarEjecucion)

        # proceso
        self.ids = []
   
        self.procesos = []
        self.cola_listos = []
        self.cola_nuevos = []
        self.cola_bloqueados = []
        self.cola_terminados = []

        self.time = 0

        self.operaciones = ['+', '-', '*', '/', '%'] 

        #keyboard
        keyboard.on_press(self.onkeypress)

        # * pause
        self.pause = False
        self._continue = False
        self.interrupt = False
        self.error = False
        self.new = False
        self.bcp = False

        self.last_frame = 0

        # Todo: validar que tamanio + last_frame <= 45

        # quantum
        self.quantum = 0

        self.v = BCP(self.procesos)

        self.setAlternateColorsTables()

        #! Estilos del label
        # label:QLabel = self.findChild(QLabel, 'label' + str(self.consumidor.get_indice()))
        # label.setStyleSheet('Border: 5px solid ' + color + '; background-color: ' + color)
        # Todo 
        # ? dic = {'0': ([(0, '#12ff00'), (1, '#12ff00'), (2, '#12ff00'), (3, '#12ff00')], id_proceso) }
        
        """ ['#fff', False, False, False]
        [False, False, False, False]
        [False, False, False, False]
        [False, False, False, False]
        [False, False, False, False]
        [False, False, False, False] 
        [False, False, False, False]
        [False, False, False, False] """

        self.marcos = [[ True, True, True, True ] for _ in range (46)]
        


    def generarProcesoNuevo(self, id: int, new: bool = False):
        
        while id in self.ids:
            id = randint(1, 1000)

        self.ids.append(id) 

        num1 = randint(0, 1000)
        num2 = randint(0, 1000)

        operacion = choice(self.operaciones)
        tmax = randint(6, 16)
        tamanio = randint(5, 26)

        # ! redondear hacia arriba: tamanio / 4 =  numero de paginas
        aux = str(tamanio/4)
        total = aux.split('.')
        
        paginas = total[0]     # * cantidad de paginas
        subpaginas = total[1]  # * cantidad de subpaginas

        while not Proceso.validarOperacion(self, num2, operacion):
            num2 = randint(0, 1000)
        
        proceso = Proceso(num1, num2, operacion, tmax, 0, 0, id, tamanio)
        proceso.setPaginas(paginas)
        proceso.setSubpaginas(subpaginas)

        self.procesos.append(proceso)
        
        if new:
            # validar solo 5 procesos en memoria
            if len(self.cola_listos) + len(self.cola_bloqueados) < 4:
                # cambiar a listo
                proceso.setEstado('listo')
                proceso.setTLL(self.time)
                self.cola_listos.append(proceso)
            else:
                self.cola_nuevos.append(proceso)
    
    
    @Slot()
    def generarProcesos(self):
        nprocesos = self.ui.spinProcesos.value()

        if nprocesos != 0:
            
            id = randint(1, 1000)

            for i in range(nprocesos):
                self.generarProcesoNuevo(id)

            notify(self, 'exito', 'Mensaje del sistema', 'Procesos agregados con éxito')
            self.ui.agregarBtn.setDisabled(True)

        else:
            notify(self, 'advertencia', 'Mensaje del sistema', 'Favor de agregar procesos')


    @Slot()
    def comenzarEjecucion(self): 
        # ? empieza le ejecución
        self.quantum = self.ui.spinQuantum.value()
        self.ui.labelQuantumGlobal.setText('  ' + str(self.quantum))
        self.procesar()
        

    def procesar(self):
        self.setInicio()  # * limpiar los procesos y lo grafico
        # Todo: clasificar procesos
        self.cola_listos = self.procesos[0:5]
        for i in self.cola_listos:
            # cambiar a listo
            i.setEstado('listo')
            i.setTLL(self.time)

        self.cola_nuevos = self.procesos[5:]
        self.setProcesosListos()

        # para que TF = time en el proceso final
        self.ui.labelCGlobal.setText('  ' + str(self.time))

 
    def setProcesosListos(self):
        # establecer el label de los procesos nuevos
        self.ui.labelPendientes.setText(str(f'  { len(self.cola_nuevos) }'))

        for pr in self.cola_listos:
            self.encolarTablaListos(pr)

            # * Establecer los frames que ocupa el proceso listo
            # 5
            # [2, 7, 9, 12]
            # ? se guardan los indices de los marcos disponibles, true = disponible
            marcos_disponibles = []
            i = 0
            while i < len(self.marcos):
                aux = self.marcos[i]
                if aux[0]:
                    marcos_disponibles.append(i)
                i += 1

            # ? contar la cantidad de marcos que necesita el proceso (paginas + 1 si subpaginas != 0)? paginas
            total_marcos = (int(pr.getPaginas()) + 1) if int(pr.getSubpaginas()) != 0 else int(pr.getPaginas())

            if total_marcos <= len(marcos_disponibles):
                pr.setMarcos(marcos_disponibles[0 : total_marcos])
                swap = pr.getMarcos() # lista con ids disponibles de los marcos
                for s in swap:
                    self.marcos[s] = [False, False, False, False]
                    
            else:
                print('No hay marcos disponibles')

            
            # 4

            #
            # last_frame = 789.....38....3942...434445


            
        # mientras hayan procesos listos        
        while self.cola_listos or self.cola_bloqueados:     
            proceso = self.cola_listos.pop(0)

            # cambiar a listo
            proceso.setEstado('listo')

            self.procesoActual(proceso)
            
            if not self.cola_listos and self.cola_bloqueados:
                bloqueado = self.cola_bloqueados[0]
                self.left = 8 - bloqueado.getCont()
                proc = Proceso(0, 0, '+', self.left, 0, 0, 'NULL')
                self.cola_listos.append(proc)

            if not self.cola_listos:
                self.limpiarProcesoActual()
                return

    
    def pintarTablaPaginas(self, actual):
        # ? dic = {'0': ([(0, '#12ff00'), (1, '#12ff00'), (2, '#12ff00'), (3, '#12ff00')], id_proceso)

        # ? proceso actual
        for marco in actual.getMarcos():
            labelID:QLabel = self.findChild(QLabel, 'tablaID' + str(marco))
            labelID.setText(str(actual.getID()))

        for proceso in self.cola_listos:
            print(f'El proceso { proceso.getID() } tiene disponibles los { proceso.getMarcos() } y tiene un tamaño de { proceso.getTamanio() }')
            # label:QLabel = self.findChild(QLabel, 'label' + str(self.consumidor.get_indice()))
            #label.setStyleSheet('Border: 5px solid ' + color + '; background-color: ' + color)

            for marco in proceso.getMarcos():
                labelID:QLabel = self.findChild(QLabel, 'tablaID' + str(marco))
                labelID.setText(str(proceso.getID()))
        


    def procesoActual(self, proceso:Proceso):
        # cambiar a ejecución
        proceso.setEstado('ejecucion')

        # ? pasa de procesos listos a proceso actual (ejecucion)
        self.ui.tablaProcesos.removeRow(0)
        if str(proceso.getID()) != 'NULL':
            operacion = f'{ proceso.getNum1() } { proceso.getOperador() } { proceso.getNum2() }'
        else:
            operacion = 'NULL'
        tmax = proceso.getTMax()
        id = str(proceso.getID())

        self.ui.labelOperacion.setText('  ' + operacion)
        self.ui.labelTrestante.setText('  ' + str(tmax))
        self.ui.labelID.setText('  ' + id)
        transcurrido = proceso.getTTrans()

        self.ui.labelQuantum_2.setText('  ' + '0')

        for i in range(transcurrido, tmax):

            # Todo: pintar todo xd
            self.pintarTablaPaginas(actual=proceso)

            self.ui.labelPendientes.setText(str(f'  { len(self.cola_nuevos) }'))

            if self.cola_nuevos:
                self.ui.idProximoNuevo.setText(str(f'  { self.cola_nuevos[0].getID() }'))
                self.ui.tamanioProximoNuevo.setText(str(f'  { self.cola_nuevos[0].getTamanio() }'))
            else:
                self.ui.idProximoNuevo.setText(str(f''))
                self.ui.tamanioProximoNuevo.setText(str(f''))
            
            if str(proceso.getID()) != 'NULL' and not proceso.getBandTRes():
                proceso.setTRes(self.time - proceso.getTLL())
                proceso.setBandTRes(True)

            tiempo_transcurrido = i
            tiempo_restante = tmax - i

            proceso.setTTrans(tiempo_transcurrido)
                        
            self.ui.labelCGlobal.setText('  ' + str(self.time))
            if str(proceso.getID()) != 'NULL':
                self.ui.labelTTtranscurrido.setText('  ' + str(tiempo_transcurrido))
                self.ui.labelTrestante.setText('  ' + str(tiempo_restante))
                self.ui.labelQuantum_2.setText('  ' + str(proceso.getQuantum()))
                
            else:
                self.ui.labelTTtranscurrido.setText('  NULL')
                self.ui.labelTrestante.setText('  NULL')
                self.ui.labelQuantum_2.setText('  NULL')

   
            self.mostrarProcesosListos()
            self.mostrarProcesosBloqueados()

            if self.quantum == proceso.getQuantum():
                proceso.setQuantum(0)
                self.cola_listos.append(proceso)
                return

            QCoreApplication.processEvents()
            sleep(1)


            # ! mostrar tabla 'BCP'
            if self.bcp:
                # setter el TS al momento
                proceso.setTS(proceso.getTTrans())
                proceso.setTE(self.time - proceso.getTLL() - proceso.getTS())
                for i in self.cola_listos:
                    # settear a los listos el TS
                    i.setTS(i.getTTrans())
                    i.setTE(self.time - i.getTLL() - i.getTS())
                    
                for j in self.cola_bloqueados:
                    # settear a los bloqueados el TS
                    j.setTS(j.getTTrans())
                    j.setTE(self.time - j.getTLL() - j.getTS())
                    
                self.v = BCP(self.cola_nuevos + self.cola_listos + [proceso] + self.cola_bloqueados + self.cola_terminados)
                self.v.show()
                self.bcp = False   
            
            self.encolarBloqueado()
            self.time += 1

            # set quantum
            proceso.setQuantum(proceso.getQuantum() + 1)
            
            
            # ! error cuando presione 'e'
            if self.error:
                # TODO: validar que no sea el nulo
                if str(proceso.getID()) != 'NULL':
                    proceso.setError('ERROR')
                    self.error = False
                    break

            # ! generar proceso nuevo 'n'
            if self.new:
                id = randint(1, 1000)
                self.generarProcesoNuevo(id, self.new)
                self.new = False
                self.mostrarProcesosListos()
                # * validar que este proceso nulo en ejecución
                if str(proceso.getID()) == 'NULL':
                    return  
            
            # ! interrupcion cuando presione 'i'
            if self.interrupt:
                # TODO: validar que no sea el nulo
                if str(proceso.getID()) != 'NULL':
                    # cambiar a bloqueado
                    proceso.setEstado('bloqueado')
                    self.cola_bloqueados.append(proceso)
                    self.interrupt = False
                    self.limpiarProcesoActual()
                    return   

            # ? pausar la ejecución del programa 'p'
            while self.pause:
                QCoreApplication.processEvents()                                       
            
            # ! ya que se despego la pausa, si se es visible se oculta BCP
            if self.v.isVisible():
                self.v.hide()

        if str(proceso.getID()) != 'NULL':
            self.encolarNuevoAListo()
            self.establecerTiempos(proceso)
            # cambiar a terminado
            proceso.setEstado('terminado')
            self.cola_terminados.append(proceso)
            self.encolarTerminado(proceso)
            self.encolarTiemposTerminados(proceso)
            
        
    def establecerTiempos(self, proceso:Proceso):
        # tiempo de finalización: TF
        proceso.setTF(self.time)
        # tiempo de retorno:  TF - TLL  
        proceso.setTRet(proceso.getTF() - proceso.getTLL())
        # tiempo de servicio: TS
        proceso.setTS(proceso.getTTrans() + 1)
        #tiempo de espera: TR - TS
        proceso.setTE(proceso.getTRet() - proceso.getTS())
        

    def encolarTablaListos(self, proceso:Proceso):
        # ? pasa los procesos a la tabla de listos
        id = str(proceso.getID())
        tmax = str(proceso.getTMax())
        ttrans = str(proceso.getTTrans())
        
        self.ui.tablaProcesos.insertRow(self.ui.tablaProcesos.rowCount())

        itemID = QTableWidgetItem(id)
        itemTMax = QTableWidgetItem(tmax)
        itemTtrans = QTableWidgetItem(ttrans)

        self.ui.tablaProcesos.setItem(self.ui.tablaProcesos.rowCount() - 1, 0, itemID)                
        self.ui.tablaProcesos.setItem(self.ui.tablaProcesos.rowCount() - 1, 1, itemTMax)
        self.ui.tablaProcesos.setItem(self.ui.tablaProcesos.rowCount() - 1, 2, itemTtrans)
    

    def encolarNuevoAListo(self):
        # ? pasa de procesos nuevo a listo
        if self.cola_nuevos and len(self.cola_listos) < 5:
            listo = self.cola_nuevos.pop(0)
            # asignar tiempo de llegada (contador global)
            listo.setTLL(self.time)
            listo.setEstado('listo')
            self.ui.labelPendientes.setText(str(f'   { len(self.cola_nuevos) }  '))
            self.cola_listos.append(listo)  
            self.encolarTablaListos(listo)

 
    def encolarBloqueado(self):
        i = 0
        while i < len(self.cola_bloqueados):
            proceso = self.cola_bloqueados[i]
            proceso.setCont(proceso.getCont() + 1)
            proceso.setTBloq(proceso.getTBloq() + 1) 

            if proceso.getCont() == 8:
                proceso.setCont(1)
                self.cola_bloqueados.pop(i)
                # cambiar a listo
                proceso.setEstado('listo')
                proceso.setQuantum(0)
                self.cola_listos.append(proceso)

                i = -1
             
            i += 1

    def encolarTerminado(self, proceso:Proceso):
        # ? pasa cada proceso a la tabla de terminados
        itemID = QTableWidgetItem(str(proceso.getID()))
        itemOperacion = QTableWidgetItem(f'{ proceso.getNum1() } { proceso.getOperador() } { proceso.getNum2() }')
        itemResultado = QTableWidgetItem(str(proceso.getResultado()))

        self.ui.tablaPTerminados.insertRow(self.ui.tablaPTerminados.rowCount())              
        self.ui.tablaPTerminados.setItem(self.ui.tablaPTerminados.rowCount() - 1, 0, itemID)
        self.ui.tablaPTerminados.setItem(self.ui.tablaPTerminados.rowCount() - 1, 1, itemOperacion)
        self.ui.tablaPTerminados.setItem(self.ui.tablaPTerminados.rowCount() - 1, 2, itemResultado)


    def encolarTiemposTerminados(self, proceso:Proceso):
        itemID = QTableWidgetItem(str(proceso.getID()))
        itemTLL = QTableWidgetItem(str(proceso.getTLL()))
        itemTF = QTableWidgetItem(str(proceso.getTF()))
        itemTRet = QTableWidgetItem(str(proceso.getTRet()))
        itemTRes = QTableWidgetItem(str(proceso.getTRes()))
        itemTE = QTableWidgetItem(str(proceso.getTE()))
        itemTS = QTableWidgetItem(str(proceso.getTS()))

        self.ui.tablaTiemposFinales.insertRow(self.ui.tablaTiemposFinales.rowCount()) 

        self.ui.tablaTiemposFinales.setItem(self.ui.tablaTiemposFinales.rowCount() - 1, 0, itemID)
        self.ui.tablaTiemposFinales.setItem(self.ui.tablaTiemposFinales.rowCount() - 1, 1, itemTLL)
        self.ui.tablaTiemposFinales.setItem(self.ui.tablaTiemposFinales.rowCount() - 1, 2, itemTF)
        self.ui.tablaTiemposFinales.setItem(self.ui.tablaTiemposFinales.rowCount() - 1, 3, itemTRet)
        self.ui.tablaTiemposFinales.setItem(self.ui.tablaTiemposFinales.rowCount() - 1, 4, itemTRes)
        self.ui.tablaTiemposFinales.setItem(self.ui.tablaTiemposFinales.rowCount() - 1, 5, itemTE)
        self.ui.tablaTiemposFinales.setItem(self.ui.tablaTiemposFinales.rowCount() - 1, 6, itemTS)

    """
        HELPERS
    """
    def mostrarProcesosListos(self):
        row = 0
        self.ui.tablaProcesos.setRowCount(len(self.cola_listos))
        for proceso in self.cola_listos:
            id = str(proceso.getID())
            tmax = str(proceso.getTMax())
            ttrans = str(proceso.getTTrans())

            itemID = QTableWidgetItem(id)
            itemTMax = QTableWidgetItem(tmax)
            itemTtrans = QTableWidgetItem(ttrans)

            self.ui.tablaProcesos.setItem(row, 0, itemID)                
            self.ui.tablaProcesos.setItem(row, 1, itemTMax)
            self.ui.tablaProcesos.setItem(row, 2, itemTtrans)
            row += 1
    
    def mostrarProcesosBloqueados(self):
        row = 0
        self.ui.tablaPBloqueados.setRowCount(len(self.cola_bloqueados))
        for proceso in self.cola_bloqueados:
            id = str(proceso.getID())
            cont = str(proceso.getCont())

            itemID = QTableWidgetItem(id)
            itemCont = QTableWidgetItem(cont)

            self.ui.tablaPBloqueados.setItem(row, 0, itemID)                
            self.ui.tablaPBloqueados.setItem(row, 1, itemCont)
            row += 1
 
    def setInicio(self):
        self.cola_listos.clear()
        self.cola_nuevos.clear()
        self.cola_bloqueados.clear()
        self.ui.spinProcesos.clear()
        self.ui.spinQuantum.clear()
        self.ui.agregarBtn.setDisabled(True)
        self.ui.ejecutarBtn.setDisabled(True)
    
    def limpiarProcesoActual(self):
        self.ui.labelID.clear()
        self.ui.labelOperacion.clear()
        self.ui.labelTTtranscurrido.clear()
        self.ui.labelTrestante.clear()
        self.ui.labelQuantum_2.clear()

    def setAlternateColorsTables(self):
        # ? establecer colores alternados
        self.ui.tablaProcesos.setAlternatingRowColors(True)
        self.ui.tablaPTerminados.setAlternatingRowColors(True)
        self.ui.tablaPBloqueados.setAlternatingRowColors(True)
        self.ui.tablaTiemposFinales.setAlternatingRowColors(True)


    def onkeypress(self, event):
        # * evento que detecta las pulsaciones del teclado
        try:
            opc = str(event.name).lower()

            if opc == 'p' or opc == 'a':
                self.pause = True


            elif opc == 'c':
                self._continue = True
                self.pause = False
                self.interrupt = False
                self.error = False
                self.bcp = False

            elif opc == 'i':
                self.interrupt = True

            elif opc == 'e':
                self.error = True

            elif opc == 'n':
                self.new = True

            elif opc == 't':
                self.bcp = True
                self.pause = True

        except:
            pass
    
   



    