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
nodos.append([100,50 ,300])
nodos.append([200,300,200])
nodos.append([330,250,204])
nodos.append([400,100,349])
nodos.append([500,300,220])
nodos.append([600,300,240])
nodos.append([100,200,218])
nodos.append([100,400,430])
nodos.append([500,450,220])
nodos.append([780,480,230])



#crear ventana
screen = pygame.display.set_mode(size)
#Controlar el reloj del programa
clock = pygame.time.Clock()


#coordenadas del objeto
cord_x = 20
cord_y = 20
#velocidad del objeto
speed_x = 0
speed_y = 0

i = 0



#creando el bucle principal
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit() #SALIR

    #-------------LOGICA DEL JUEGO-------------------


    speed_x = abs(int(nodos[i][0]/cord_x))
    speed_y = abs(int(nodos[i][1]/cord_y))

    cord_x += speed_x
    cord_y += speed_y
    
    if(cord_x >= nodos[i][0]):
        i+=1

    if i == len(nodos):
        sys.exit() #SALIR


    #----------FIN DE LA LÓGICA DEL JUEGO-----------------------

    #cambiar de color a la pantalla
    screen.fill(WHITE) 
    ### -------zona de dibujo
    
    #pygame.draw.line(screen, GREEN, [0,0],[0,800],5) # Dibujar una línea
    pygame.draw.lines(screen, RED, True, [(0,0),(800,0),(800,500),(0,500)],5)

    pygame.draw.circle(screen, BLUE, (cord_x,cord_y), 20)

    for punto in nodos:
        pygame.draw.circle(screen, GREEN, (punto[0],punto[1]), 20)




    ##### -----------------
    #actualizar la pantalla
    pygame.display.flip() 
    #Definir el reloj para controlar los FRAMES POR SEGUNDO
    clock.tick(100)

    
