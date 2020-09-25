import pygame, sys # inicializando librerias

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

#crear ventana
screen = pygame.display.set_mode(size)
#Controlar el reloj del programa
clock = pygame.time.Clock()

#Funciones


def menorDistancia(nodoactual,nodos):  
    nodoelegido = []                        

    heuristica = 100000.0                   
    speed_x = 0                             
    speed_y = 0

    valor_x = 0
    valor_y = 0

    for posicion in nodos:                                                                      
        
        if(posicion[0] >= nodoactual[0][0] and posicion[1] >= nodoactual[0][1]): 
                            
            raiz = ((posicion[0] - nodoactual[0][0])**2 + (posicion[1] - nodoactual[0][1])**2)**0.5              

            if(raiz < heuristica and raiz != 0):    
                heuristica = raiz
                valor_x = posicion[0] - nodoactual[0][0] 
                valor_y = posicion[1] - nodoactual[0][1]

                speed_x = valor_x / mcd(valor_x,valor_y)             
                speed_y = valor_y / mcd(valor_x,valor_y)


                
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
    


def imprimirCamino(cord_x,cord_y):
    nodoinicial = [[cord_x,cord_y]]
    nuevonodo = menorDistancia(nodoinicial,nodos)      
    camino = []                                         

    #print(nodos[len(nodos)-1])

    while(nuevonodo[0] != nodos[len(nodos)-1]):     
        
        camino.append(nuevonodo)                   

        nuevonodo = menorDistancia(camino[len(camino)-1],nodos)    

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

    
    cord_x += speed_x                            
    cord_y += speed_y

    if(cord_x >= caminooptimo[i][0][0] and cord_y >= caminooptimo[i][0][1]):        
        cord_x = caminooptimo[i][0][0]                     
        cord_y = caminooptimo[i][0][1]
        print(cord_x , " , " , cord_y)                      
        i+=1                                               


    if ( [cord_x, cord_y] == caminooptimo[len(caminooptimo)-1][0]):         
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

    
