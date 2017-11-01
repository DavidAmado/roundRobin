import threading
import numpy as np
class Proceso:
    def __init__(self,idProceso,quantum,nombre,recurso,t,tr):
        self.idProceso=idProceso
        self.nombre=nombre
        self.recurso=recurso
        self.t=t
        self.tr=tr
        self.quantum=quantum
        self.sus=0
        self.blo=0
        self.lis=0
        self.zc=0
    def __str__(self):
        return self.nombre+" "+str(self.idProceso)
    def procesar(self):
        self.quantum-=1
        self.t-=1
        self.zc+=1
        print("Preparando",self.nombre,self.idProceso,"quantum",self.quantum,"t",self.t,"recurso",self.recurso)
            
    def asignarQ(self): 
        if self.t>7:
            return(round(self.t*0.6)) 
        else:
            return self.t

        
class PolloConPapas(Proceso):
    def __init__(self,idProceso,recurso,quantum=0,nombre="Pollo con papas",t=25,tr=0):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t,tr)

class Malteada(Proceso):
    def __init__(self,idProceso,recurso,quantum=0,nombre="Malteada",t=10,tr=0):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t,tr)

class Ensalada(Proceso):
    def __init__(self,idProceso,recurso,quantum=0,nombre="Ensalada",t=15,tr=0):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t,tr)

