import pygame, sys # inicializando librerias
import random

pygame.init() #inicializando pygame

#DEFINIR COLORES
BLACK   = (0,0,0)
WHITE   = (255,255,255)
GREEN   = (0,255,0)
RED     = (255,0,0)
BLUE    = (0,0,255)

size = (800, 500) #definir tamaño

#Lista de nodos
nodos = []
nodos.append([100, 50])
total = 50
for i in range(total):
    nodos.append([random.randrange(1,79)*10,random.randrange(1,49)*10])

nodos.append([790,490])

#crear ventana
screen = pygame.display.set_mode(size)
#Controlar el reloj del programa
clock = pygame.time.Clock()

#Funciones

# Esta función nos devuelve mediante heurística la siguiente posición que parece mejor a escoger
def menorDistancia(nodoactual,nodos):  
    nodoelegido = []                        #creamos la lista del nodo que escogeremos

    heuristica = 100000.0                   #Definimos un número muy grande, como límite a elegir
    speed_x = 0                             #speed_x y speed_y, serán las velocidades que tendrá la pelota negra con respecto eje x e y
    speed_y = 0

    valor_x = 0
    valor_y = 0

    for posicion in nodos:                                                                      #recorremos todos los nodos
        #el nodo que escogeremos tiene que ser mayor al nodo actual, con eso verificamos los nodos que ya se recorrieron
        if(posicion[0] >= nodoactual[0][0] and posicion[1] >= nodoactual[0][1]): 
            #encontramos la distancia entre el nodo actual y el nodo a escoger                
            raiz = ((posicion[0] - nodoactual[0][0])**2 + (posicion[1] - nodoactual[0][1])**2)**0.5              

            if(raiz < heuristica and raiz != 0):    #con esta condicional, verificamos el siguiente nodo a escoger, osea el menor
                heuristica = raiz
                valor_x = posicion[0] - nodoactual[0][0] 
                valor_y = posicion[1] - nodoactual[0][1]

                speed_x = valor_x / mcd(valor_x,valor_y)             #calculamos la velocidad con respecto al eje x y con respecto y
                speed_y = valor_y / mcd(valor_x,valor_y)


                #Almacenamos esta información del nodo escogido en una lista, alamacenará la coordenada, la velocidad x y la velocidad y
                nodoelegido = [posicion, speed_x,speed_y]           

    #print(heuristica)

    return nodoelegido

def mcd(x,y):
    mcd = 1

    if(x == 0):
        return y

    if (y == 0):
        return x

    if x % y ==0:
        return y
    
    for k in range(int(y/2),0,-1):
        if x % k == 0  and y % k == 0:
            mcd = k
            break

    return mcd
    

# Esta función retornará el camino elegido para el recorrido de la pelota negra para alcanzar el objetivo
def imprimirCamino(cord_x,cord_y):
    nodoinicial = [[cord_x,cord_y]] # establecemos en una lista las coordenadas iniciales
    nuevonodo = menorDistancia(nodoinicial,nodos)       #esta función nos retornará el nodo elegido
    camino = []                                         #creamos la lista en la cual se almacenará el recorrrido

    #print(nodos[len(nodos)-1])

    while(nuevonodo[0] != nodos[len(nodos)-1]):     # mientras no llegue hacia el nodo final, seguirá en el bucle
        
        camino.append(nuevonodo)                    #agrega los nodos elegidos a la lista camino

        nuevonodo = menorDistancia(camino[len(camino)-1],nodos)         #actualizará los nodos elegidos

    camino.append(nuevonodo)

    return camino



#coordenadas del objeto
cord_x = 10
cord_y = 10
#velocidad del objeto
speed_x = 0
speed_y = 0

i = 0

caminooptimo = imprimirCamino(cord_x,cord_y)


#creando el bucle principal
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit() #SALIR

    #-------------LOGICA DEL JUEGO-------------------

    speed_x = int(caminooptimo[i][1])            #las velocidades toman valor de la columna 1 y 2 en la lista caminooptimo
    speed_y = int(caminooptimo[i][2])

    
    cord_x += speed_x                            #Se aumentan en velocidades a las coordenadas x e y
    cord_y += speed_y

    if(cord_x >= caminooptimo[i][0][0] and cord_y >= caminooptimo[i][0][1]):        # Evalua los nodos a escoger
        cord_x = caminooptimo[i][0][0]                      #ajusta las coordenadas
        cord_y = caminooptimo[i][0][1]
        print(cord_x , " , " , cord_y)                      #imprime la ruta 
        i+=1                                                #aumenta mas 1 la iteración 


    if ( [cord_x, cord_y] == caminooptimo[len(caminooptimo)-1][0]):         # Evalúa si llegó al objetivo para salir del programa
        #print(cord_x , " , " , cord_y)
        sys.exit() #SALIR

    

    #----------FIN DE LA LÓGICA DEL JUEGO-----------------------

    #cambiar de color a la pantalla
    screen.fill(WHITE) 
    ### -------zona de dibujo
    
    #pygame.draw.line(screen, GREEN, [0,0],[0,800],5) # Dibujar una línea
    pygame.draw.lines(screen, RED, True, [(0,0),(800,0),(800,500),(0,500)],5)

    pygame.draw.circle(screen, BLACK, (cord_x,cord_y), 10)

    for punto in nodos:
        if(punto == nodos[len(nodos)-1]):
            pygame.draw.circle(screen, BLUE, (punto[0],punto[1]), 10)
        else:
            pygame.draw.circle(screen, GREEN, (punto[0],punto[1]), 10)


    ##### -----------------------------
    #actualizar la pantalla
    pygame.display.flip() 
    #Definir el reloj para controlar los FRAMES POR SEGUNDO
    clock.tick(50)

    
