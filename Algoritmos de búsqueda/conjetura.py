import math 

class Vertex:
    def __init__(self,x):
        self.x = x
        self.vecinos  = list()
        self.aplicaciones = list()


def raizcuadrada(x):
    return math.sqrt(x)
def redondeo(x):
    return math.ceil(x)
def factorial(x):
    x = math.ceil(x)
    return math.factorial(x)
        

def solved(raiz,numero):
    queue = list()
    queue.append(raiz)
    count = 0
    while len(queue) > 0:
        count = count + 1
        elemento = queue.pop(0)
        
        print("(")
        for x in queue:
            print(x.x)
        print(")")
        print(count,elemento.x)
        if elemento.x == numero:
            print("Encontrado")
            break
        if(abs(elemento.x) > (2 ** 31 - 1)):
            continue
        vertex_1 = Vertex(raizcuadrada(elemento.x))
        vertex_2 = Vertex(redondeo(elemento.x))
        vertex_3 = Vertex(factorial(elemento.x))
        queue.append(vertex_1)
        queue.append(vertex_2)
        queue.append(vertex_3)

    #numero_niveles = 1
    #for i in range(1,4):
        #v = Vertex(i)
        #v.aplicar(i)
        #raiz.vecinos.append(v)


    #for i in range(1,4):
        #numero_niveles += pow(3,i)
        
    


   


#numero = int(input())
numero = 24
raiz = Vertex(4)

solved(raiz,numero)