#Definicion de la clase vertice
class Vertex:
    def __init__(self,x,y,value):
        self.x = x
        self.y = y
        self.neighbors = list()
        self.value = value
        self.visited = False
    #Agregar a los vecinos
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            #self.neighbors.sort()
    def get(self):
        print(self.x," ",self.y," ",self.value)
    #def print_neighbor(self):
        #print(self.name, " Mis vecinos ",self.neighbors)          


#Lectura de variables

pacman =  input().strip()
comida =  input().strip()
mapa   =  input().strip()

coordenadas_pacman = pacman.split()
coordenadas_comida = comida.split()
size_mapa = mapa.split()

x_pacman = int(coordenadas_pacman[0])
y_pacman = int(coordenadas_pacman[1])

x_comida = coordenadas_comida[0]
y_comida = coordenadas_comida[1]

rows_mapa = int(size_mapa[0])
colums_mapa = size_mapa[1]

grid=[]
for i in range(rows_mapa):
    r=input()
    grid.append(r)

print(x_pacman)
print(y_pacman)
print(x_comida)
print(y_comida)
print(rows_mapa)
print(colums_mapa)
print(grid)

raiz = Vertex(x_pacman,y_pacman,'P')
raiz.get()

for x in grid:
    print(x)
    print(list(x))

