
# Algoritmos de búsqueda/dfs.py
Búsqueda en profundidad.

Como entrada tenemos el modelo de grafo:  
 >`graph = {'A': set(['C', 'B']),  
 >       'B': set(['A', 'D', 'E']),  
 >        'C': set(['A']),  
 >        'D': set(['B']),  
 >        'E': set(['B'])}  `

Luego realizamos la búsqueda:  `dfs(graph, 'A')` esta ejecución empieza en el nodo `A`.

El DFS lo realizamos de manera recursiva:

`def dfs(graph, start, visited=None):  
    if visited is None:  
        visited = set()  
    visited.add(start)  
    visit(start)  
    for next in graph[start] - visited:  
        dfs(graph, next, visited)  
    return visited`

Los nodos visitados los imprimimos con el método `visit(start)`  
`def visit(n):  
    print(n)`
