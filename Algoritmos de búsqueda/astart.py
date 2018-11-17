import time
import math



matrix = [
['*', '-', '-', '-'],
['%', '-', '%', '-'],
['-', '-', '%', '%'],
['-', '%', '%', 'P'],
['-', '-', '-', '-']
]



nextStep = []
openList =[]
closedList =[]
isEnd = False

start =(3,3)
position = start
end = (0,0)

closedList.append(position)

m = 5 # row
n = 4 # col

def heuristic(current,end):
    return abs(end[0] - current[0]) + abs(end[1] - current[1])

def fcost(gCost,hCost):
    return gCost+hCost

def hasCost(current):
    if ( matrix[ current[0] ][ current[1] ] == '%' or matrix[ current[0] ][ current[1] ] == 'P' ):
        return False
    elif ( matrix[ current[0] ][ current[1] ] == '*'):
        nextStep.append({  'cost': fcost ( 0, heuristic( (current[0], current[1]), end)), 'pos': (current[0],current[1]), 'parent': current})
        return False
    else:
        return True


# Movements
# Vertical and horizontal
def top(current,currentCost):
    if(hasCost( (current[0]-1,current[1]) )):
        nextStep.append({'cost':fcost (currentCost + 1,heuristic( (current[0]-1, current[1]), end)),'pos': (current[0]-1,current[1]),'parent': current })
def bottom(current,currentCost):
    if(hasCost( (current[0]+1,current[1]) )):
        nextStep.append({ 'cost': fcost (currentCost + 1, heuristic( (current[0]+1, current[1]), end)), 'pos': (current[0]+1, current[1]), 'parent': current  })
def left(current,currentCost):
    if(hasCost( (current[0],current[1]-1) )):
        nextStep.append({ 'cost': fcost (currentCost + 1, heuristic( (current[0], current[1]-1), end)), 'pos': (current[0], current[1]-1), 'parent': current })
def right(current,currentCost):
    if(hasCost( (current[0],current[1]+1) )):
        nextStep.append({ 'cost': fcost (currentCost + 1, heuristic( (current[0], current[1]+1), end)), 'pos': (current[0], current[1]+1), 'parent': current })

def seeNeighbors(current,currentCost):

    if (current[0] == 0 and current[1] != n-1 ):
        left(current,currentCost)
        bottom(current,currentCost)
        right(current,currentCost)
    
    elif (current[0] == 0 and current[1] == 0):
            bottom(current, currentCost)
            right(current, currentCost)

    elif ( (current[0] != 0 and current[0] != m-1) and current[1] == 0):
        #print(3)
        top(current,currentCost)
        bottom(current,currentCost)
        right(current,currentCost)

    elif ( current[0] == m-1 and current[1] == 0):
        #print(4)
        top(current,currentCost)
        right(current,currentCost)

    elif ( current[0] == m-1 and (current[1] != 0 and current[1] != n-1) ):
        #print(5)
        top(current,currentCost)
        left(current,currentCost)
        right(current,currentCost)

    elif ( current[0] == m-1 and current[1] == n-1):
        #print(6)
        top(current,currentCost)
        left(current,currentCost)

    elif ( (current[0] != 0 and current[0] != m-1) and current[1] == n-1 ):
        #print(7)
        top(current,currentCost)
        left(current,currentCost)
        bottom(current,currentCost)

    elif (current[0] == 0 and current[1] == n-1):
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
while (isEnd == False):
    nextStep = []
    minCost = []
    print ('closedList')
    print (closedList)
    seeNeighbors(position,currentCost)
    print('nextStep')
    print(nextStep)
    #print(nextStep)
    minCost = [min(value['cost'] for value in nextStep)]
    #get min moves
    nextStep = [obj for obj in nextStep if obj['cost'] in minCost]
    print('min nextSteps')
    print(nextStep)

    #print(nextStep)
    #print (nextStep[0]['pos'])
    print('no repeat')
    print(nextStep)
    nextStep = [obj for obj in nextStep if obj['pos'] not in closedList]
    print('nextStep')
    print(nextStep)
    position = nextStep[0]['pos']
    currentCost = nextStep[0]['cost']
    if (position not in closedList):
        print('pushing')
        print(position)
        closedList.append(position)
    if (position == end):
        isEnd = True
    time.sleep(2)

#print(nextStep)
#print(min(nextStep))
        
