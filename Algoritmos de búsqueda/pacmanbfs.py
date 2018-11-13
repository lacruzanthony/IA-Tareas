#Definicion de la clase vertice
class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbors = list()

        self.distance = 9999
        self.visited = False
    #Agregar a los vecinos
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            #self.neighbors.sort()
    def print_neighbor(self):
        print(self.name, " Mis vecinos ",self.neighbors)          


#Lectura de variables
#Coordenadas de Pacman

pacman =  input().strip()
comida =  input().strip()
mapa   =  input().strip()

coordenadas_pacman = pacman.split()
coordenadas_comida = comida.split()
size_mapa = mapa.split()

x_pacman = coordenadas_pacman[0]
y_pacman = coordenadas_pacman[1]

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


