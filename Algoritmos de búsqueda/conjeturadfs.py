import math 

tree = [
    {'value':4, 'op':''}
]

bd = []
bd.append(tree[0])

reach = 9
stop = False

def factorialAprox(n):
    #Aproximacion stirling a factoriales muy grandes
    return math.log(n)

def isStackble(value,op):

<<<<<<< HEAD
    if (math.floor(value) == reach):
        tree.insert(1,{'value':math.floor(value), 'op':op + '-'})
        bd.append({'value':math.floor(value), 'op':op + '-'})

    elif(math.sqrt(value) == reach):
        tree.insert(1,{'value':math.sqrt(value), 'op':op + '-'})
        bd.append({'value':math.sqrt(value), 'op':op + '-'})

    else:

        if not any(elm['value'] == math.sqrt(value) for elm in bd):
            tree.append({'value':math.sqrt(value), 'op':op + 'V'})
            bd.append({'value':math.sqrt(value), 'op':op + 'V'})

        if not any(elm['value'] == math.floor(value) for elm in bd):
            tree.append({'value':math.floor(value),'op':op + '-'})
            bd.append({'value':math.floor(value), 'op':op + '-'})
=======
    
    if not any(elm['value'] == math.sqrt(value) for elm in bd):
        #ESTA ES LA CONDIFCION LOCA 
        
        if ( math.floor(math.sqrt(value)) == reach ):
            print("Entrando aqui")
            tree.insert(1,{'value':math.floor(math.sqrt(value)),'op':op + 'V-'})
            bd.append({'value':math.floor(math.sqrt(value)), 'op':op + 'V-'})

        tree.append({'value':math.sqrt(value), 'op':op + 'V'})
        bd.append({'value':math.sqrt(value), 'op':op + 'V'})
        
        if(math.floor(math.sqrt(value)) == 8):
            print(math.floor(math.sqrt(value)))
            print(tree)
    
    if not any(elm['value'] == math.floor(value) for elm in bd):
        tree.append({'value':math.floor(value),'op':op + '-'})
        bd.append({'value':math.floor(value), 'op':op + '-'})
>>>>>>> cc350adcc64f032e3728013f6b3b44104819ccea

        if(value - math.trunc(value) == 0):
            if not (abs(math.factorial(value)) > (2 ** 31 - 1)):
                if not any(elm['value'] == math.factorial(value) for elm in bd):
                    tree.append({'value':math.factorial(value), 'op':op + '!'})
                    bd.append({'value':math.factorial(value),'op':op + '!'})

            elif (value <= 24):
                if not any(elm['value'] == factorialAprox(value) for elm in bd):
                    tree.append({'value':factorialAprox(value), 'op':op + '!'})
                    bd.append({'value':factorialAprox(value),'op':op + '!'})



while (tree != [] and stop == False):


    current = tree[0]['value']
    
    for i in tree:
        print(i)
    
    if(current == reach):
        print('encontrado')
        stop = True
        break 

    isStackble(current, tree[0]['op'])
        
    tree.pop(0)

print(bd)