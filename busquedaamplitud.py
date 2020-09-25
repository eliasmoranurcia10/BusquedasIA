def createMaze2():  #Creamos el laberinto 2
    laberinto = []
    laberinto.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    laberinto.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    laberinto.append(["#"," ", "#", "#", "#", " ", "#", "#", "#"])
    laberinto.append(["#"," ", " ", " ", "#", " ", "#", " ", "#"])
    laberinto.append(["#","#", "#", " ", "#", " ", "#", " ", "#"])
    laberinto.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    laberinto.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    laberinto.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    laberinto.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])

    return laberinto

def identificarValornodos(posicion_x,posicion_y):
    laberinto = createMaze2()

    valor = laberinto[posicion_x][posicion_y]

    return valor

def posicionNodo(valor):
    laberinto = createMaze2()
    posicion = []

    for x in range(len(laberinto)):
        for y in range(len(laberinto[x])):
            if (laberinto[x][y] == valor):
                posicion.append([x,y,0])
    
    return posicion

def buscandoNuevosVecinos(posicion_x,posicion_y):
    nvecinos = []
    coste = 1

    d_izquierda = posicion_y - 1
    d_derecha   = posicion_y + 1
    d_arriba    = posicion_x - 1
    d_abajo     = posicion_x + 1

    if(identificarValornodos(posicion_x,d_izquierda) == " "):
        nvecinos.append([posicion_x, d_izquierda, coste])

    if(identificarValornodos(posicion_x,d_derecha) == " "):
        nvecinos.append([posicion_x, d_derecha, coste])

    if(identificarValornodos(d_arriba,posicion_y) == " "):
        nvecinos.append([d_arriba, posicion_y, coste])

    if(identificarValornodos(d_abajo,posicion_y) == " "):
        nvecinos.append([d_abajo, posicion_y, coste])
    
    return nvecinos


#print(identificarValornodos(0,5))

def verificarllegada(posx, posy):
    if(identificarValornodos(posx,posy) == "O"):
        return False
    elif(identificarValornodos(posx,posy) == " "):
        return False
    elif(identificarValornodos(posx,posy) == "X"):
        return True
    else:
        return False

def ubicarMenorCosto(listarecibida = []):
    posicionelegida = []

    menorcoste = listarecibida[0][2]

    for coste in reversed(listarecibida):
        if(coste[2] <= menorcoste):
            posicionelegida = coste
            menorcoste = coste[2]

    return posicionelegida

#print(ubicarMenorCosto([[4,1,9],[2,5,9],[1,6,9]]))



nodoactual = "O"
posicionactual = posicionNodo(nodoactual)
posicion_x = posicionactual[0][0]
posicion_y = posicionactual[0][1]

#print(posicionactual[0][1])

laberinto = createMaze2()
vecinos = []
nuevosvecinos = []
vecinosacumulados = []
explorados = []

while not verificarllegada(posicion_x,posicion_y):

    nuevosvecinos = buscandoNuevosVecinos(posicion_x,posicion_y)
    
    explorados.append([posicion_x,posicion_y])

    posicionactual = ubicarMenorCosto(nuevosvecinos)

    #print(ubicarMenorCosto(nuevosvecinos))

    vecinos = vecinos + nuevosvecinos
    #print(vecinos)
    vecinos.pop(0)
    
    
    posicion_x = posicionactual[0]
    posicion_y = posicionactual[1]

    print(posicion_x , posicion_y)

    if(posicion_y == 1):
        break


