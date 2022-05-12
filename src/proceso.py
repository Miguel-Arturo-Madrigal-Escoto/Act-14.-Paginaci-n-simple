
from numpy import array


class Proceso:
    
    def __init__(self, num1, num2, operador, tmax, ttrans, tbloq, id, tamanio) -> None:
        self.__num1 = num1
        self.__num2 = num2
        self.__operador = operador
        self.__tmax = tmax
        self.__ttrans = ttrans
        self.__tbloq = tbloq
        self.__id = id
        self.__cont = 1
        self.__tll = 0 #llegada
        self.__tf = 0 #final
        self.__tret = 0 #retorno
        self.__tres = 0 #respuestaf
        self.__te = 0 #espera
        self.__ts = 0 #servicio
        self.__error = ''
        self.__band_tres = False
        self.__quantum = 0
        self.__estado = 'nuevo'
        self.__tamanio = tamanio
        self.__marcos = []
        self.__paginas = 0
        self.__subpaginas = 0
        
            
    def validarOperacion(self, num2, operador) -> bool:
        if num2 == 0 and operador == '/':
            return False
            
        elif num2 == 0 and operador == '%':
            return False
        
        else:
            return True
    
    def getNum1(self) -> int:
        return self.__num1
    
    def setNum1(self, num1) -> None:
        self.__num1 = num1

    def getNum2(self) -> int:
        return self.__num2
    
    def setNum2(self, num2) -> None:
        self.__num2 = num2

    def getOperador(self) -> str:
        return self.__operador

    def setOperador(self, operador) -> None:
        self.__operador = operador

    def getTMax(self) -> int:
        return self.__tmax
    
    def setTMax(self, tmax) -> None:
        self.__tmax = tmax

    def getTTrans(self) -> int:
        return self.__ttrans

    def setTTrans(self, ttrans) -> None:
        self.__ttrans = ttrans
    
    def getTBloq(self) -> int:
        return self.__tbloq
    
    def getBandTRes(self) -> bool:
        return self.__band_tres

    def setTBloq(self, tbloq) -> None:
        self.__tbloq = tbloq

    def setCont(self, cont) -> None:
        self.__cont = cont

    def getCont(self) -> int:
        return self.__cont

    def getID(self) -> int:
        return self.__id
    
    def setID(self, id) -> None:
        self.__id = id
    
    def setError(self, error) -> None:
        self.__error = error
    
    def setBandTRes(self, band) -> None:
        self.__band_tres = band

    
    """ Tiempos Calculados """

    def getTLL(self) -> int:
        return self.__tll
    
    def setTLL(self, tll) -> None:
        self.__tll = tll
 
    def getTF(self) -> int:
        return self.__tf
    
    def setTF(self, tf) -> None:
        self.__tf= tf

    def getTRet(self) -> int:
        return self.__tret

    def setTRet(self, tret) -> None:
        self.__tret = tret

    def getTRes(self) -> int:
        return self.__tres
    
    def setTRes(self, tres) -> None:
        self.__tres = tres

    def getTE(self) -> int:
        return self.__te
    
    def setTE(self, te) -> None:
        self.__te = te
    
    def getTS(self) -> int:
        return self.__ts
    
    def setTS(self, ts) -> None:
        self.__ts = ts  

    def getEstado(self) -> str:
        return self.__estado
    
    def setEstado(self, estado) -> None:
        self.__estado = estado

    def getQuantum(self) -> int:
        return self.__quantum

    def setQuantum(self, quantum) -> None:
        self.__quantum = quantum

    def getTamanio(self) -> int:
        return self.__tamanio

    def setTamanio(self, tamanio) -> None:
        self.__tamanio = tamanio

    def getMarcos(self) -> list:
        return self.__marcos

    def setMarcos(self, marcos) -> None:
        self.__marcos = marcos

    # ! ---------------------------------- #
    
    def setPaginas(self, paginas) -> None:
        self.__paginas = int(paginas)

    def getPaginas(self) -> int:
        return self.__paginas

    def setSubpaginas(self, subpaginas) -> None:
        if subpaginas == '25':
            self.__subpaginas = 1
        elif subpaginas == '5':
            self.__subpaginas = 2
        elif subpaginas == '75':
            self.__subpaginas = 3
        elif subpaginas == '0':
            self.__subpaginas = 0

    def getSubpaginas(self) -> int:
        return self.__subpaginas
    
    # ! ---------------------------------- #
            
    def getResultado(self):
        if self.__error.__eq__('') and self.__estado == 'terminado':
            if self.__operador == '+':
                return self.__num1 + self.__num2
            elif self.__operador == '-':
                return self.__num1 - self.__num2
            elif self.__operador == '*':
                return self.__num1 * self.__num2
            elif self.__operador == '/':
                return round(self.__num1 / self.__num2, 2)
            elif self.__operador == '%':
                return self.__num1 % self.__num2
        elif self.__estado == 'nuevo' or self.__estado == 'listo' \
            or self.__estado == 'ejecucion' or self.__estado == 'bloqueado':
            return ' - '
        else:
            return self.__error
