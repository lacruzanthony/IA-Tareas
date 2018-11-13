import collections

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    visit(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

def visit(n):
    print(n)

if __name__ == '__main__':
        graph = {'A': set(['C', 'B']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A']),
         'D': set(['B']),
         'E': set(['B'])}
        dfs(graph, 'A')