import threading
import numpy as np
import pygame
from pygame.sprite import Sprite
from pygame.locals import *

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
        self.estado=0 #0:listo ; 1:blo ; 2:sus ; 3:ejecucion ; 4:terminado

    def __str__(self):
        return self.nombre+" "+str(self.idProceso)

    def procesar(self):
        self.quantum-=1
        self.t-=1
        self.zc+=1
#        print("Preparando",self.nombre,self.idProceso,"quantum",self.quantum,"t",self.t,"recurso",self.recurso)

    def asignarQ(self,ttotal):
        if self.t>=ttotal*0.7:
            return self.t
        elif self.t>=ttotal*0.4:
            return round(self.t*0.6)
        else:
            return round(self.t*0.4)


class PolloConPapas(Sprite, Proceso):
    def __init__(self,idProceso,recurso,cont_size,quantum=0,nombre="Pollo con papas",t=25,tr=0):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t,tr)
        Sprite.__init__(self)
        self.cont_size = cont_size
        self.iml = pygame.image.load("imagenes/pollo.png")
        self.imb = pygame.image.load("imagenes/pollo.png")
        self.ims = pygame.image.load("imagenes/pollo.png")
        self.ime = pygame.image.load("imagenes/pollo.png")
        self.rect = self.iml.get_rect()
        self.rect.move_ip(cont_size[0] - 200, cont_size[1] - 685)

class Malteada(Sprite, Proceso):
    def __init__(self,idProceso,recurso,cont_size,quantum=0,nombre="Malteada",t=10,tr=0):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t,tr)
        Sprite.__init__(self)
        self.cont_size = cont_size
        self.iml = pygame.image.load("imagenes/malteada.png")
        self.imb = pygame.image.load("imagenes/malteada.png")
        self.ims = pygame.image.load("imagenes/malteada.png")
        self.ime = pygame.image.load("imagenes/malteada.png")
        self.rect = self.iml.get_rect()
        self.rect.move_ip(cont_size[0] - 200, cont_size[1] - 430)

class Ensalada(Sprite, Proceso):
    def __init__(self,idProceso,recurso,cont_size,quantum=0,nombre="Ensalada",t=15,tr=0):
        Proceso.__init__(self,idProceso,quantum,nombre,recurso,t,tr)
        Sprite.__init__(self)
        self.cont_size = cont_size
        self.iml = pygame.image.load("imagenes/ensalada.png")
        self.imb = pygame.image.load("imagenes/ensalada.png")
        self.ims = pygame.image.load("imagenes/ensalada.png")
        self.ime = pygame.image.load("imagenes/ensalada.png")
        self.rect = self.iml.get_rect()
        self.rect.move_ip(cont_size[0] - 200, cont_size[1] - 575)
