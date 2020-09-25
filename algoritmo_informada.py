nodos = []
nodos.append([100, 50])
nodos.append([200,300])
nodos.append([330,250])
nodos.append([400,100])
nodos.append([500,300])
nodos.append([600,300])
nodos.append([140,200])
nodos.append([350,100])
nodos.append([700,100])
nodos.append([180,400])
nodos.append([500,450])
nodos.append([790,490])

def menorDistancia(nodoactual,nodos):
    nodoelegido = []

    raizoptima = 100000.0
    speed_x = 0
    speed_y = 0

    valor_x = 0
    valor_y = 0

    for posicion in nodos:
        if(posicion[0] >= nodoactual[0][0] and posicion[1] >= nodoactual[0][1]):
            raiz = ((posicion[0] - nodoactual[0][0])**2 + (posicion[1] - nodoactual[0][1])**2)**0.5

            if(raiz < raizoptima and raiz != 0):
                raizoptima = raiz
                valor_x = posicion[0] - nodoactual[0][0] 
                valor_y = posicion[1] - nodoactual[0][1]

                speed_x = valor_x / mcd(valor_x,valor_y)
                speed_y = valor_y / mcd(valor_x,valor_y)

                nodoelegido = [posicion, speed_x,speed_y]

    #print(raizoptima)

    return nodoelegido

def mcd(x,y):
    mcd = 1

    if(x == 0 or y == 0):
        return 1

    if x % y ==0:
        return y
    
    for k in range(int(y/2),0,-1):
        if x % k == 0  and y % k == 0:
            mcd = k
            break

    return mcd

#print(menorDistancia([[10,10]], nodos))

def imprimirCamino():
    nodoinicial = [[10,10]]
    nuevonodo = menorDistancia(nodoinicial,nodos)
    camino = []

    #print(nodos[len(nodos)-1])

    while(nuevonodo[0] != nodos[len(nodos)-1]):
        
        camino.append(nuevonodo)

        nuevonodo = menorDistancia(camino[len(camino)-1],nodos)

    camino.append(nuevonodo)

    return camino


#PRINCIPAL ALGORITMO
caminooptimo = imprimirCamino()

for i in caminooptimo:
    print(i)





