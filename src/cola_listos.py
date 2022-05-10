from .proceso import Proceso

class ColaListos:
    def __init__(self) -> None:
        self.__procesos = []
    
    def agregarProceso(self, proceso:Proceso):
        self.__procesos.append(proceso)
    
    def getProcesos(self):
        return self.__procesos

    # def __str__(self) -> str:
    #     return (
    #         ''.join(str(proceso) for proceso in self.__procesos)
    #     )