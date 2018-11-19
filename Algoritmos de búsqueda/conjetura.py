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
    return math.factorial(x)
        

def solved(raiz,numero):
    queue = list()
    queue.append(raiz)
    count = 0

    while len(queue) > 0:
        count = count + 1
        elemento = queue.pop(0)
        print(count)

        if elemento.x == numero:
            print("Encontrado")
            break
        print(elemento.x, type(elemento.x) is int)
       
        if type(elemento.x) is int:
            print("es entero")
            if not(abs(factorial(elemento.x)) > (2 ** 31 - 1)):
                print("no explota")
                vertex_3 = Vertex(factorial(elemento.x))
                queue.append(vertex_3)

        elif (elemento.x).is_integer():
            print("es float pero entero")
            if not(abs(factorial(elemento.x)) > (2 ** 31 - 1)):
                print("no explota")
                vertex_3 = Vertex(factorial(elemento.x))
                queue.append(vertex_3)


        if not(abs(raizcuadrada(elemento.x)) > (2 ** 31 - 1)):
            print("no explota raizcuadrada")    
            vertex_1 = Vertex(raizcuadrada(elemento.x))
            queue.append(vertex_1)
            

        if not(abs(redondeo(elemento.x)) > (2 ** 31 - 1)):
            print("no explota redondeo")    
            vertex_2 = Vertex(redondeo(elemento.x))
            queue.append(vertex_2)
            
            


    #numero_niveles = 1
    #for i in range(1,4):
        #v = Vertex(i)
        #v.aplicar(i)
        #raiz.vecinos.append(v)


    #for i in range(1,4):
        #numero_niveles += pow(3,i)
        
    


   


#numero = int(input())
numero = 400
raiz = Vertex(4)

solved(raiz,numero)