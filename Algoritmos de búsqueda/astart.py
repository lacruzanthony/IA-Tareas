import time
import math
from operator import itemgetter

#pacman =  input().strip()
#comida =  input().strip()
#mapa   =  input().strip()

#coordenadas_pacman = pacman.split()
#coordenadas_comida = comida.split()
#size_mapa = mapa.split()

#x_pacman = int(coordenadas_pacman[0])
#y_pacman = int(coordenadas_pacman[1])

#x_comida = int(coordenadas_comida[0])
#y_comida = int(coordenadas_comida[1])

#rows_mapa = int(size_mapa[0])
#colums_mapa =int(size_mapa[1])

grid=[
['*', '-', '-'],
['-', '%', '-'],
['-', '%', '-'],
['%', '-', '-'],
['%', '-', 'P'],
]
#for i in range(rows_mapa):
    #r=input()
    #grid.append(r)

#for x in grid:
    #grid.append(list(x))

#start =(x_pacman,y_pacman)
#position = start
#end = (x_comida,y_comida)

start= (4,2)
end = (0,0)
rows_mapa = 5
colums_mapa = 3
neighbors = []
openList = []
closedList =[]
goBack = []
isEnd = False
position = start
closedList.append(position)

def heuristic(current,end):
    return abs(end[0] - current[0]) + abs(end[1] - current[1])

def fcost(gCost,hCost):
    return gCost+hCost

def hasCost(current, parent):
    if ( grid[ current[0] ][ current[1] ] == '%' or grid[ current[0] ][ current[1] ] == 'P' or (current in closedList) ):
        return False
    elif ( current == end):
        neighbors.append({  'cost': fcost ( 0, heuristic( (current[0], current[1]), end)), 'pos': (current[0],current[1]), 'parent': parent})
        return False
    else:
        return True

# Movements
def top(current,currentCost):
    if(hasCost( (current[0]-1,current[1]), current )):
        neighbors.append({'cost':fcost (currentCost + 1,heuristic( (current[0]-1, current[1]), end)),'pos': (current[0]-1,current[1]),'parent': current })
def bottom(current,currentCost):
    if(hasCost( (current[0]+1,current[1]), current )):
        neighbors.append({ 'cost': fcost (currentCost + 1, heuristic( (current[0]+1, current[1]), end)), 'pos': (current[0]+1, current[1]), 'parent': current  })
def left(current,currentCost):
    if(hasCost( (current[0],current[1]-1), current )):
        neighbors.append({ 'cost': fcost (currentCost + 1, heuristic( (current[0], current[1]-1), end)), 'pos': (current[0], current[1]-1), 'parent': current })
def right(current,currentCost):
    if(hasCost( (current[0],current[1]+1), current )):
        neighbors.append({ 'cost': fcost (currentCost + 1, heuristic( (current[0], current[1]+1), end)), 'pos': (current[0], current[1]+1), 'parent': current })

def seeNeighbors(current,currentCost):

    if (current[0] == 0 and current[1] != colums_mapa-1 ):
        left(current,currentCost)
        bottom(current,currentCost)
        right(current,currentCost)
    
    elif (current[0] == 0 and current[1] == 0):
        bottom(current, currentCost)
        right(current, currentCost)

    elif ( (current[0] != 0 and current[0] != rows_mapa-1) and current[1] == 0):
        #print(3)
        top(current,currentCost)
        bottom(current,currentCost)
        right(current,currentCost)

    elif ( current[0] == rows_mapa-1 and current[1] == 0):
        #print(4)
        top(current,currentCost)
        right(current,currentCost)

    elif ( current[0] == rows_mapa-1 and (current[1] != 0 and current[1] != colums_mapa-1) ):
        #print(5)
        top(current,currentCost)
        left(current,currentCost)
        right(current,currentCost)

    elif ( current[0] == rows_mapa-1 and current[1] == colums_mapa-1):
        #print(6)
        top(current,currentCost)
        left(current,currentCost)

    elif ( (current[0] != 0 and current[0] != rows_mapa-1) and current[1] == colums_mapa-1 ):
        #print(7)
        top(current,currentCost)
        left(current,currentCost)
        bottom(current,currentCost)

    elif (current[0] == 0 and current[1] == colums_mapa-1):
        #print(8)
        left(current,currentCost)
        bottom(current,currentCost)

    else:
        #print(9)
        top(current,currentCost)
        bottom(current,currentCost)
        left(current,currentCost)
        right(current,currentCost)

currentCost = 0
seeNeighbors(position,currentCost)
neighbors = sorted(neighbors, key=itemgetter('cost')) 
openList.append(neighbors)
#print(openList)

while (isEnd == False):
    item = openList[0]
    for obj in item:

        if(len(neighbors) != 0 and min(value['cost'] for value in neighbors) == 0):
            isEnd = True
            position = end
            break 

        neighbors = []
        position = obj['pos']
        #print(position)
        closedList.append(position)
        goBack.append(obj)
        seeNeighbors(position,currentCost)
        neighbors = sorted(neighbors, key=itemgetter('cost'))
        #print(neighbors)

        if(len(neighbors) != 0 and min(value['cost'] for value in neighbors) == 0):
            isEnd = True
            position = neighbors[0]['parent']
            break

        openList.append(neighbors)

    openList.pop(0)


print(position)
while(position != start):
    parent = [d for d in goBack if d['pos'] in [position]]
    position = parent[0]['parent'] 
    print(position)

#temp = openList.pop(0)
#print(temp)
#print(temp[0]['cost'])






#print(openList)
#print(min(openList))
        
