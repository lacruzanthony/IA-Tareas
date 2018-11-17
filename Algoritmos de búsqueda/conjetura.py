import math 

class Vertex:
    def __init__(self,x):
        self.x = x
        self.vecinos  = list()
    def aplicar(self,i):
        if i == 1:
            self.x = redondeo(self.x)
        if i == 2:
            self.x = raizcuadrada(self.x)
        if i == 3:
            self.x = factorial(self.x)

def raizcuadrada(x):
    return math.sqrt(x)
def redondeo(x):
    return math.ceil(x)
def factorial(x):
    return math.factorial(x)
        

def solved(raiz,numero):
    numero_niveles = 1
    for i in range(1,4):
        v = Vertex(i)
        v.aplicar(i)
        raiz.vecinos.append(v)


    for i in range(1,4):
        numero_niveles += pow(3,i)
        
    


   


#numero = int(input())
numero = 2
raiz = Vertex(4)

solved(raiz,numero)