# -*- coding: utf-8 -*-
class Cola:
	""" Representa una cola con operaciones de encolar, desencolar y verificar si está vacía. """
	def __init__(self):
        	""" Crea una cola vacía. """
		# La cola vacía se representa con una lista vacía
        	self.items=[]
	def encolar(self, x):
	        """ Agrega el elemento x a la cola. """
	        # Encolar es agregar al final de la cola.
	        self.items.append(x)
	def desencolar(self,n=0):
	        """ Devuelve el elemento inicial y lo elimina de la cola.
	            Si la cola está vacía levanta una excepción. """
	        try:
	            return self.items.pop(n)
	        except IndexError:
	            raise ValueError("La cola está vacía")
	def es_vacia(self):
		""" Devuelve True si la lista está vacía, False si no. """
		return self.items == []
