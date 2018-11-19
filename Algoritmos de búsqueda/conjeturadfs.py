import math 

tree = [{'value':24, 'op':'!'},{'value':2, 'op':'V'},{'value':4, 'op':'|'}]
temp = []
reach = 7
stop = False

def isStackble(value,op):

    if(value - math.trunc(value) == 0):
        if not (abs(math.factorial(value)) > (2 ** 31 - 1)):
            temp.append({'value':math.factorial(value),'op':op + '!'})

    temp.append({'value':math.sqrt(value), 'op':op + 'V'})
    temp.append({'value':math.floor(value),'op':op + '|'})


while (tree != [] and stop == False):
    #print(tree)
    temp = [tree[0]]

    for it in range(10000000):
        current = temp[0]['value']
        print(it,current,temp[0]['op'])

        if ( current == 39916800):
            continue 

        if(current == reach):
            print('encontrado')
            stop = True
            break 

        isStackble(current, temp[0]['op'])

        #print(temp)
        temp.pop(0)
        
    tree.pop(0)