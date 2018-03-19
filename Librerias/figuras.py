
# coding: utf-8

# In[11]:


import math
import random

class Figura(object):
    """ Una figura """
    def __init__(self, color=""):
        self.color = color
        
    def area(self):
        " Este método debe ser redefinido o sobreescrito. "
        pass

class Circulo(Figura):
    """ Un círculo  """
    def __init__(self, radio=0):
        " Constructor de círculo. "
        self.radio = radio
 
    def area(self):
        " Devuelve el área del círculo. "
        return math.pi * self.radio * self.radio
    
class Triangulo(Figura):
    """ Un triángulo """
    def __init__(self, base=0, altura=0):
        " Constructor de triángulo. "
        self.base = base
        self.altura = altura
 
    def area(self):
        " Devuelve el área del triángulo. "
        return self.base * self.altura / 2.
    
def figura_aleatoria():
    seleccion = random.randint(1,2)
    if seleccion == 1:
        radio = random.random() * 100
        return Circulo(radio)
    elif seleccion == 2:
        base = random.random() * 100
        altura = random.random() * 100
        return Triangulo(base, altura)

