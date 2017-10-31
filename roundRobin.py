import cola
import time
import procesos as ps
import recursos as rs
import queue
import threading
class Procesador(threading.Thread):
    def __init__(self,idProcesador,*args):
        threading.Thread.__init__(self)
        self.idProcesador=idProcesador 
        self.proceso=None
        self.lis=cola.Cola()
        self.blo=cola.Cola()
        self.sus=cola.Cola()
        self._args=args
        self.uso=True
    def __str__(self):
        return str(self.idProcesador)
    def run(self):
        while self.uso:
            self.usarProcesador(*self._args)
    def usarProcesador(self,q):
        while not self.proceso==None or not q.empty() or not self.lis.es_vacia() or not self.sus.es_vacia() or not self.blo.es_vacia():
            
            time.sleep(0.1)
            
            if not q.empty():self.asignar(q.get())
            if not self.lis.es_vacia() and self.proceso==None:
                posible=self.lis.desencolar()
                if posible.recurso.libre:
                    self.ocupado=True
                    self.proceso=posible
                    self.proceso.recurso.libre=False
                    print("\ncomenzando proceso",self.proceso,"en el procesador",self)
                else:
                    print("\nel proceso",posible,"requiere de un recurso ocupado, encolando en bloqueado")
                    self.blo.encolar(posible)
            self.revisarColaSus()
            self.revisarColaBlo()
            self.contarColaLis()
            if not self.proceso==None:
                self.proceso.procesar()
                if self.proceso.t>0 and self.proceso.quantum==0:
                    self.proceso.tr=5
                    self.sus.encolar(self.proceso)
                    self.proceso.recurso.libre=True
                    print("\nse reencolo el proceso",self.proceso,"a suspendidos")
                    self.proceso=None
                elif self.proceso.t==0:
                    self.proceso.recurso.libre=True                    
                    print("\nterminando proceso",self.proceso,"en el procesador",self,",sus",self.proceso.sus,",lis",self.proceso.lis,",blo",self.proceso.blo,",zona critica",self.proceso.zc)
                    self.proceso=None
                    q.task_done()
        print("termino el procesador",self)
        self.uso=False
    def revisarColaSus(self):
        for i in range(len(self.sus.items)):
            self.sus.items[i].tr-=1
            self.sus.items[i].sus+=1
        if not self.sus.es_vacia():
            print(self.sus.items[0],"tr",self.sus.items[0].tr)
            if self.sus.items[0].tr==0:
                a=self.sus.desencolar()
                self.asignar(a)
                print("\nse saco el proceso",a,"de la cola de suspendidos y entro a la cola de listo")
    def revisarColaBlo(self):
        
        for i in self.blo.items:
            if i.recurso.libre:
                i.blo+=1
                a=self.blo.desencolar(self.blo.items.index(i))
                self.asignar(a)
                print("\nse saco el proceso",a," de la cola de bloqueados y entro en la cola de listos")

    def contarColaLis(self):
        for i in self.lis.items:
            i.lis+=1

    def asignar(self,proceso):
        proceso.quantum=proceso.asignarQ()
        self.lis.encolar(proceso)

class cliente:
    def __init__(self):
        self.recursos=[rs.Horno(),rs.Cuchillos(),rs.Licuadora()]
        self.cola1=queue.Queue()
        self.cola1.put(ps.Malteada(0,self.recursos[2]))
        self.cola2=queue.Queue()
        self.cola2.put(ps.PolloConPapas(0,self.recursos[0]))
        self.cola3=queue.Queue()
        self.cola3.put(ps.Ensalada(0,self.recursos[1]))
        
        self.procesador1=Procesador(1,self.cola1)        
        self.procesador2=Procesador(2,self.cola2)      
        self.procesador3=Procesador(3,self.cola3)
    def iniciar(self):
        self.procesador1.start()
        self.procesador2.start()
        self.procesador3.start()
        self.cola1.put(ps.Malteada(1,self.recursos[2]))
        self.cola2.put(ps.PolloConPapas(1,self.recursos[0]))
        self.cola3.put(ps.PolloConPapas(2,self.recursos[0]))
        self.cola1.put(ps.Malteada(2,self.recursos[2]))
        self.cola2.put(ps.Ensalada(1,self.recursos[1]))
        self.cola3.put(ps.PolloConPapas(3,self.recursos[0]))
        self.cola2.put(ps.Malteada(3,self.recursos[2]))
        self.cola1.put(ps.Ensalada(2,self.recursos[1]))
        self.cola2.put(ps.Ensalada(3,self.recursos[1]))
        self.cola1.put(ps.Malteada(4,self.recursos[2]))
        self.cola3.put(ps.PolloConPapas(4,self.recursos[0]))
        self.cola1.put(ps.Ensalada(4,self.recursos[1]))
        self.cola1.put(ps.Malteada(5,self.recursos[2]))

        self.cola1.join()
        self.cola2.join()
        self.cola3.join()

         

cliente = cliente()
cliente.iniciar()
