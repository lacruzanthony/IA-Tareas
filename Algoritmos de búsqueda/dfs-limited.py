# Python program: ejecuta dfs limitado 
# También conocido como dls.
from collections import defaultdict 
  
# Esta clase representa un grafo dirigido usando listas
# para la representación de adjacencias.
class Graph: 
  
    def __init__(self,vertices): 
  
        # Nro. vertices.
        self.V = vertices 
  
        # Diccionario por defecto para almacenar listas.
        self.graph = defaultdict(list) 
  
    # Agrega un vértice al grafo.
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Ejecuta DLS dado una fuente/nodo. 
    def DLS(self,src,target,maxDepth): 
  
        if src == target : return True
  
        # Si llega a la profundida máxima, detiene la recursión. 
        if maxDepth <= 0 : return False
  
        # Recursión sobre los vertices adjancentes al nodo 
        for i in self.graph[src]:
                if(self.DLS(i,target,maxDepth-1)): 
                    return True
        return False
   
    # Iterative delimited DFS, busca si target es alcanzable desde src
    # usa DLS() recursivo.
    def IDDFS(self,src, target, maxDepth): 

        # Repite DLS hasta la máxima profundidad.
        for i in range(maxDepth): 
            if (self.DLS(src, target, i)): 
                return True
        return False
  
# Crea un grafo 
g = Graph (7); 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(1, 4) 
g.addEdge(2, 5) 
g.addEdge(2, 6) 

target = 6; maxDepth = 3; src = 0
  
if g.IDDFS(src, target, maxDepth) == True: 
    print ("Target is reachable from source " +
        "within max depth") 
else : 
    print ("Target is NOT reachable from source " +
        "within max depth") 
 