import queue        #Primero importaremos el módulo estándar Queue que permite crear y trabajar con colas de manera sencilla


def createMaze(): #Creamos el laberinto
    maze = []
    maze.append(["#","#", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", " ", " ","#"])
    maze.append(["#"," ", "#", " ", "#", "#","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def createMaze2():  #Creamos el laberinto 2
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", "#", " ", "#", " ", "#"])
    maze.append(["#","#", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "X", "#"])

    return maze


def printMaze(maze, path=""):               #Crea un conjunto de rutas posibles, hasta que encuentra el nodo final
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()                         #Nuevo conjunto de objetos, Crea una colección desordenada de elementos únicos.
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))                    #Agregar las posiciones a la colección pos
    
    for j, row in enumerate(maze):          #Este for me imprimirá dibujar el laberinto con camino optimo
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")            #Rellena laruta con el signo +
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):           #recorrer la primera fila del laberinto hasta encontrar el 0
        if pos == "O":                          #Si es que se encuentra el 0 en la primera fila
            start = x                           #start toma valor de x

    i = start
    j = 0
    for move in moves:
        if move == "L":                         #Movimiento hacia la izquierda
            i -= 1

        elif move == "R":                       #Movimiento la derecha
            i += 1

        elif move == "U":                       #Movimiento hacia arriba
            j -= 1

        elif move == "D":                       #Movimiento hacia abajo
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):       #Verifica si no se salió del rango del laberinto
            return False                                            #si se sale del rango, retornará False
        elif (maze[j][i] == "#"):                                   #Verifica si la coordenada apunta a un #
            return False                                            #si apunta a un # entonces retornará False

    return True


def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):  #recorrer la primera fila del laberinto hasta encontrar el 0
        if pos == "O":                  #Si se encuentra el valor 0
            start = x                   # se almacena en start su posición

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":               #Verifica si ya llegó al valor X
        print("Found: " + moves)        
        printMaze(maze, moves)          #imprime el laberinto con el resultado final
        return True

    return False                        #Si no llegó al valor final retorna false


# MAIN ALGORITHM

nums = queue.Queue() #Construir la función Queue en nums
nums.put("")         #insertar un item a la cola
add = ""                #variable agregar
maze  = createMaze2()   #Crear el array

for j, row in enumerate(maze):          #Este for me imprimirá dibujar el laberinto con camino optimo
        for i, col in enumerate(row):
            if (j, i) in maze:
                print("+ ", end="")            #Rellena laruta con el signo +
            else:
                print(col + " ", end="")
        print()

while not findEnd(maze, add):    #Encontrar fin: Devuelve True si aún no llegó al final 
    add = nums.get()             #Ver los valores de nums en FIFO
    #print(add)
    for j in ["L", "R", "U", "D"]:   #VALORES PARA j --> L: Izquierda, R: Derecha, U: Arriba, D: Abajo
        put = add + j                #Agregar valores de j al put

        if valid(maze, put):         #Retorna si es válido el movimiento, osea si no sale del rango o apunta a un #
            nums.put(put)            #insertar los valores de j válidos en la cola