class Pila:
    def __init__(self):
        self.items = []
    def push(self,elemento):
        self.items.append(elemento)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def get_peek(self):
        return self.items[-1]

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
        
#Definicion de la clase grafo
class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors)+ " " + str(self.vertices[key].distance))
    def bfs(self,vert):
        q = list()
        c = list()
        c.append(vert)
        vert.distance = 0
        vert.visited = True
        vert.print_neighbor()
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance +1
            q.append(v)
        
        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.visited = True
            #print('Nodo a visitar', node_u.name)
            c.append(node_u)
            node_u.print_neighbor()
            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if not node_v.visited:
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance +1
        return c

    def dfs(self,vertex):
        self.print_graph()
        pila = Pila()
        camino = list()
        vertex.visited = True
        camino.append(vertex.name)
        for v in vertex.neighbors:
            pila.push(v)
        while pila.size() > 0:
            item = pila.pop()
            print(item)
            camino.append(item)
            node_u = self.vertices[item]
            node_u.visited = True
            #node_u.print_neighbor()
            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if not node_v.visited:
                    pila.push(v)
                    #print(v)
        print(camino)
    
    def idfs(self):
        self.print_graph()

g = Graph()
a = Vertex('A')
g.add_vertex(a)
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
#edges = ['AB','AC','BD','BE','CF','CG']
#edges = ['AC','CB','AF','FG','FD','FE']
#edges = ['AB','AC','AE','BD','BF','CG']

for edge in edges:
	g.add_edge(edge[:1], edge[1:])
	

#print("dfs")
#g.dfs(a)

camino = g.bfs(a)
cola = list()

for vertex in camino:
    cola.append(vertex.name)

print(cola)
g.print_graph()
