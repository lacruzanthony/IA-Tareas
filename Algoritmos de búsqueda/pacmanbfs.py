lista = list()
queue = list()
class Vertex:
    def __init__(self,x,y,value):
        self.x = x
        self.y = y
        self.value = value
        self.papa  = list()
     
def bfs(matriz,raiz,visitados,x_comida,y_comida):
    
    raiz.visited =True
    visitados[raiz.x][raiz.y] = 1
    queue.append(raiz)
    count = 0
    
    while len(queue) > 0:
        elemento = queue.pop(0)
        count = count + 1
        
        lista.append(elemento)

        if(elemento.x == x_comida and elemento.y == y_comida ):
            break

        if(visitados[elemento.x-1][elemento.y] != 1 and matriz[elemento.x-1][elemento.y] != "%"):
            b = Vertex(elemento.x-1,elemento.y,matriz[elemento.x-1][elemento.y])
            visitados[elemento.x-1][elemento.y] = 1
            b.papa.append(elemento)
            queue.append(b)
       
        if(visitados[elemento.x][elemento.y-1] != 1 and matriz[elemento.x][elemento.y-1] != "%"):
            c = Vertex(elemento.x,elemento.y-1,matriz[elemento.x-1][elemento.y-1])
            visitados[elemento.x][elemento.y-1] = 1
            c.papa.append(elemento)
            queue.append(c)
       
        if(visitados[elemento.x][elemento.y+1] != 1 and matriz[elemento.x][elemento.y+1] != "%"):
            d = Vertex(elemento.x,elemento.y+1,matriz[elemento.x][elemento.y+1])
            visitados[elemento.x][elemento.y+1] = 1
            d.papa.append(elemento)
            queue.append(d)
   
        if(visitados[elemento.x+1][elemento.y] != 1 and matriz[elemento.x+1][elemento.y] != "%"):
            e = Vertex(elemento.x+1,elemento.y,matriz[elemento.x+1][elemento.y])
            visitados[elemento.x+1][elemento.y] = 1
            e.papa.append(elemento)
            queue.append(e)
    return count

pacman =  input().strip()
comida =  input().strip()
mapa   =  input().strip()

coordenadas_pacman = pacman.split()
coordenadas_comida = comida.split()
size_mapa = mapa.split()

x_pacman = int(coordenadas_pacman[0])
y_pacman = int(coordenadas_pacman[1])

x_comida = int(coordenadas_comida[0])
y_comida = int(coordenadas_comida[1])

rows_mapa = int(size_mapa[0])
colums_mapa =int(size_mapa[1])

grid=[]
for i in range(rows_mapa):
    r=input()
    grid.append(r)

matrix=[]

for x in grid:
    matrix.append(list(x))

raiz = Vertex(x_pacman,y_pacman,'P')
visitados = [[0 for col in range(colums_mapa)] for row in range(rows_mapa)]

print(bfs(matrix,raiz,visitados,x_comida,y_comida))
for elemento in lista:
    print(elemento.x,elemento.y)

q = list()
ultimo = lista[-1]
q.append(ultimo)
ultimo_papa = ultimo.papa
final = len(ultimo_papa)
index =  lista.index(ultimo_papa[0])

q.append(lista[index])

while index != 0:
    ultimo = lista[index]
    ultimo_papa = ultimo.papa
    final = len(ultimo_papa)
    index =  lista.index(ultimo_papa[0])
    q.append(lista[index])

print(len(q)-1)
q.reverse()
for elemento in q:
    print(elemento.x,elemento.y)


