import time
import abc
import threading
import numpy as np
class Nodo:
    def __init__(self,info):
        self.info=info
 

    def __str__(self):
        return (str(self.info))

class Cola:
    def __init__(self):
        self.elementos=[]
    
    def push(self,nuevo):
        self.elementos.append(nuevo)

    def pop(self):
        if not self.elementos==[]:
            return self.elementos.pop(0)
        else:
            print("no hay elementos en la cola")
            return None

class Procesador:
    def __init__(self,idProcesador):
        self.id=idProcesador
        self.ocupado=False
        self.proceso=None
        self.lis=Cola()
        self.blo=Cola()
        self.sus=Cola()

    def procesar(self):
        self.ocupado=True
        self.proceso=self.lis.pop()
        self.proceso.start()

    def asignar(self,proceso):
        proceso.quantum=proceso.asignarQ()
        self.lis.push(proceso)

class cliente:
    def __init__(self):
        self.procesador1=Procesador(1)        
        self.procesador2=Procesador(2)      
        self.procesador3=Procesador(3)
    def iniciar(self):
        self.procesador1.asignar(PolloConPapas(1))
        self.procesador1.procesar()
        self.procesador2.asignar(Ensalada(2))
        self.procesador2.procesar()
        self.procesador3.asignar(Malteada(3))
        self.procesador3.procesar()
        #self.procesador1.proceso.join()
        #self.procesador2.proceso.join()
        #self.procesador3.proceso.join()
       
class Recurso:
    def __init__(self,nombre):
        self.nombre=nombre
        self.libre=True
    def __str__(self):
        return(nombre)
    def utilizar(self):
        if self.libre:
            print("usando el ",self.nombre)
            self.libre=False
        else:
            print("el ",self.nombre," esta ocupado")
    def liberar(self):
        if not self.libre:
            print("el ",self.nombre," fue liberado")
            self.libre=True
        else:
            print("el ",self.nombre," no estaba siendo usado")

class Horno(Recurso):
    def __init__(self,nombre="Horno"):
        Recurso.__init__(self,nombre)

class Cuchillos(Recurso):
    def __init__(self,nombre="Cuchillos"):
        Recurso.__init__(self,nombre)

class Licuadora(Recurso):
    def __init__(self,nombre="Licuadora"):
        Recurso.__init__(self,nombre)

class Proceso(threading.Thread):
    def __init__(self,idProceso,quantum,nombre,recurso,t):
        threading.Thread.__init__(self)
        self.idProceso=idProceso
        self.nombre=nombre
        self.recurso=recurso
        self.t=t
        self.quantum=quantum
    def run(self):
        while self.quantum:
            time.sleep(1)
            print("Preparando ",self.nombre,", quantum ",self.quantum)
            self.quantum-=1
        self.join()
    def asignarQ(self):
        return np.random.randint(5,15) 

class PolloConPapas(Proceso):
    def __init__(self,idProceso,quantum=0,nombre="Pollo con papas",recurso="Horno",t=25):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t)

class Malteada(Proceso):
    def __init__(self,idProceso,quantum=0,nombre="Malteada",recurso="Licuadora",t=5):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t)

class Ensalada(Proceso):
    def __init__(self,idProceso,quantum=0,nombre="Ensalada",recurso="Cuchillo",t=12):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t)

cliente = cliente()
cliente.iniciar()
