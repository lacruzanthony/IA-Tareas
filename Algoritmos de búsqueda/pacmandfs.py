queue = list()
caminoActual = list()
caminoFinal = list()

def matrizVisitados(index_x, index_y):
    visitados = [[False for col in range(index_y)] for row in range(index_x)]
    return visitados

def dfs(filas_mapa, columnas_mapa, x_pacman, y_pacman, x_comida, y_comida, matrix, encontrado) :

    visitados[x_pacman][y_pacman] = True
    
    movimientoValido = list()

    if(x_pacman == x_comida and y_pacman == y_comida):
        caminoActual.append(str(x_pacman) + " " + str(y_pacman))
        caminoFinal.append(str(x_pacman) + " " + str(y_pacman))
        return True
    
    if encontrado == False :

        if(x_pacman-1 >= 0 and matrix[x_pacman-1][y_pacman] != '%' and visitados[x_pacman-1][y_pacman] == False):
            movimientoValido.append("ARRIBA")
            visitados[x_pacman-1][y_pacman] = True

        if(y_pacman-1 >= 0 and matrix[x_pacman][y_pacman-1] != '%' and visitados[x_pacman][y_pacman-1] == False):
            movimientoValido.append("IZQUIERDA")
            visitados[x_pacman][y_pacman-1] = True
        
        if(y_pacman+1 <= columnas_mapa and matrix[x_pacman][y_pacman+1] != '%' and visitados[x_pacman][y_pacman+1] == False):
            movimientoValido.append("DERECHA")
            visitados[x_pacman][y_pacman+1] = True
        
        if(x_pacman+1 <= filas_mapa and matrix[x_pacman+1][y_pacman] != '%' and visitados[x_pacman+1][y_pacman] == False):
            movimientoValido.append("ABAJO")
            visitados[x_pacman+1][y_pacman] = True
    
    if movimientoValido :
        caminoActual.append(str(x_pacman) + " " + str(y_pacman))
        direccion = movimientoValido.pop()

        if(direccion == "ABAJO" and encontrado == False) :
            encontrado = dfs(filas_mapa, columnas_mapa, x_pacman + 1, y_pacman, x_comida, y_comida, matrix, encontrado)
            if encontrado == True :
                caminoFinal.append(str(x_pacman) + " " + str(y_pacman))
                movimientoValido.clear 

            if(movimientoValido and encontrado == False):
                direccion = movimientoValido.pop()

        if(direccion == "DERECHA" and encontrado == False) :
            encontrado = dfs(filas_mapa, columnas_mapa, x_pacman, y_pacman+1, x_comida, y_comida, matrix, encontrado)
            if encontrado :
                caminoFinal.append(str(x_pacman) + " " + str(y_pacman))
                movimientoValido.clear

            if(movimientoValido and not encontrado) :
                direccion = movimientoValido.pop()
        
        if (direccion == "IZQUIERDA" and not encontrado) :
            encontrado = dfs (filas_mapa, columnas_mapa, x_pacman, y_pacman-1, x_comida, y_comida, matrix, encontrado)
            if encontrado :
                caminoFinal.append(str(x_pacman) + " " + str(y_pacman))
                movimientoValido.clear
            
            if (movimientoValido and not encontrado) :
                direccion = movimientoValido.pop()
        
        if(direccion == "ARRIBA" and not encontrado):
            encontrado = dfs(filas_mapa, columnas_mapa, x_pacman-1, y_pacman, x_comida, y_comida, matrix, encontrado)

            if encontrado :
                caminoFinal.append(str(x_pacman) + " " + str(y_pacman))
                movimientoValido.clear

            if (movimientoValido and not encontrado) :
                direccion = movimientoValido.pop()
                
        
    else : 
        caminoActual.append(str(x_pacman) + " " + str(y_pacman))
        return False

    return encontrado


if __name__ == '__main__':

    pacman =  input().strip()
    comida =  input().strip()
    mapa   =  input().strip()

    coordenadas_pacman = pacman.split()
    coordenadas_comida = comida.split()
    tamanno_mapa = mapa.split()

    x_pacman = int(coordenadas_pacman[0])
    y_pacman = int(coordenadas_pacman[1])

    x_comida = int(coordenadas_comida[0])
    y_comida = int(coordenadas_comida[1])

    filas_mapa = int(tamanno_mapa[0])
    columnas_mapa = int(tamanno_mapa[1])

    array=[]

    for i in range(filas_mapa):
        row = input()
        array.append(row)

    matrix = []
    for cell in array:
        matrix.append(list(cell))

    visitados = matrizVisitados(filas_mapa, columnas_mapa)

    dfs(filas_mapa, columnas_mapa, x_pacman, y_pacman, x_comida, y_comida, matrix, encontrado = False)

    print(len(caminoActual))

    for cell in caminoActual :
        print(cell)

    print(len(caminoFinal) - 1)
    for cell in reversed(caminoFinal) :
        print(cell)