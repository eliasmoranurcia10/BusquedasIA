import pygame, sys # inicializando librerias

pygame.init() #inicializando pygame

#DEFINIR COLORES
BLACK   = (0,0,0)
WHITE   = (255,255,255)
GREEN   = (0,255,0)
RED   = (255,0,0)
BLUE    = (0,0,255)

size = (800, 500) #definir tamaño

#crear ventana
screen = pygame.display.set_mode(size)
#Controlar el reloj del programa
clock = pygame.time.Clock()


#coordenadas del objeto
cord_x = 40
cord_y = 40
#velocidad del objeto
speed_x = 3
speed_y = 3


#creando el bucle principal
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit() #SALIR

    #-------------LOGICA DEL JUEGO-------------------

    if(cord_x > 760 or cord_x < 40):
        speed_x *= -1

    if(cord_y > 460 or cord_y < 40):
        speed_y *= -1


    cord_x += speed_x
    cord_y += speed_y

    #----------FIN DE LA LÓGICA DEL JUEGO-----------------------

    #cambiar de color a la pantalla
    screen.fill(WHITE) 
    ### -------zona de dibujo
    
    #pygame.draw.line(screen, GREEN, [0,0],[0,800],5) # Dibujar una línea
    pygame.draw.lines(screen, RED, True, [(0,0),(800,0),(800,500),(0,500)],5)

    pygame.draw.circle(screen, BLUE, (cord_x,cord_y), 40)
    

    ##### -----------------
    #actualizar la pantalla
    pygame.display.flip() 
    #Definir el reloj para controlar los FRAMES POR SEGUNDO
    clock.tick(1000)

    
