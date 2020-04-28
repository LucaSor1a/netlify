'''
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, 
each of which is in one of two possible states, alive or dead, (or populated and unpopulated, respectively). 
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically,
or diagonally adjacent. At each step in time, the following transitions occur:

    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overpopulation.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

    Any live cell with two or three neighbors survives.
    Any dead cell with three live neighbors becomes a live cell.
    All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The initial pattern constitutes the seed of the system. 
The first generation is created by applying the above rules simultaneously to every cell in the seed; 
births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. 
Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations. 
'''
import time
import random


def randgen(al, la, muerto, vivo):
    matrix = []
    matrixc = []
    for i in range(al):
        matrix.append([])
        matrixc.append([])
        for j in range(la):
            rannum = random.randrange(10)
            if rannum == 0:
                matrix[i].append(vivo)
                matrixc[i].append(True)
            else:
                matrix[i].append(muerto)
                matrixc[i].append(False)
    return matrix, matrixc

def neighbors(radius, rowNumber, columnNumber, matrix):
    return [[
        matrix[i][j] if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) else 0
        for j in range(columnNumber - 1 - radius, columnNumber + radius)
    ] for i in range(rowNumber - 1 - radius, rowNumber + radius)]

def viveomuere(matrix, y, x, muerto, vivo):
    vivos = 0
    matrixch = neighbors(1, y+1, x+1, matrix)
    for i in range(3):
        for j in range(3):
            if matrixch[i][j] == vivo:
                vivos += 1
    if matrix[y][x] == vivo:
        vivos -= 1
    if vivos == 2 or vivos == 3:
        if matrix[y][x] == vivo:
            return True
        else:
            if vivos == 3:
                return True
            else:
                return False
    else:
        return False

def iterar(matrix, matrixc, al, la, muerto, vivo):
    for i in range(al):
        for j in range(la):
            matrixc[i][j] = viveomuere(matrix, i, j, muerto, vivo)
    for i in range(al):
        for j in range(la):
            if matrixc[i][j] == True:
                matrix[i][j] = vivo
            else:
                matrix[i][j] = muerto

def showTable(al, la):
    TableInString = "\n\n"
    for i in range(al):
        for j in range(la):
            TableInString += str(matrix[i][j].replace("", ""))
        TableInString += "\n"
    return TableInString

print("Si no sabe, apriete enter")
# Blanco y negro -> muerto = 2B1B y vivo = 2B1C
# Emojis -> muerto = 1F480 y vivo = 1F642
# Corona Style -> muerto = 1F480 y vivo = 1F637
muerto = chr(int(input("Poner caracter unicode del muerto: ") or "2b1b", 16))
vivo = chr(int(input("Poner caracter unicode del vivo: ") or "2b1c", 16))
pulsar = int(input("Pulsar ejemplo? 0 o 1: ") or 1)
if pulsar == 1:
    # Oscilator(Pulsar)
    matrix = [[muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto],
              [muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto],
              [muerto, muerto, muerto, muerto, vivo, vivo, vivo, muerto, muerto, muerto, vivo, vivo, vivo, muerto, muerto, muerto, muerto],
              [muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto],
              [muerto, muerto, vivo, muerto, muerto, muerto, muerto, vivo, muerto, vivo, muerto, muerto, muerto, muerto, vivo, muerto, muerto],
              [muerto, muerto, vivo, muerto, muerto, muerto, muerto, vivo, muerto, vivo, muerto, muerto, muerto, muerto, vivo, muerto, muerto],
              [muerto, muerto, vivo, muerto, muerto, muerto, muerto, vivo, muerto, vivo, muerto, muerto, muerto, muerto, vivo, muerto, muerto],
              [muerto, muerto, muerto, muerto, vivo, vivo, vivo, muerto, muerto, muerto, vivo, vivo, vivo, muerto, muerto, muerto, muerto],
              [muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto],
              [muerto, muerto, muerto, muerto, vivo, vivo, vivo, muerto, muerto, muerto, vivo, vivo, vivo, muerto, muerto, muerto, muerto],
              [muerto, muerto, vivo, muerto, muerto, muerto, muerto, vivo, muerto, vivo, muerto, muerto, muerto, muerto, vivo, muerto, muerto],
              [muerto, muerto, vivo, muerto, muerto, muerto, muerto, vivo, muerto, vivo, muerto, muerto, muerto, muerto, vivo, muerto, muerto],
              [muerto, muerto, vivo, muerto, muerto, muerto, muerto, vivo, muerto, vivo, muerto, muerto, muerto, muerto, vivo, muerto, muerto],
              [muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto],
              [muerto, muerto, muerto, muerto, vivo, vivo, vivo, muerto, muerto, muerto, vivo, vivo, vivo, muerto, muerto, muerto, muerto],
              [muerto ,muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto],
              [muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto, muerto]]

    matrixc = [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [False, False, False, True, True, True, False, False, False, True, True, True, False, False, False, False, False],
               [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [False, True, False, False, False, False, True, False, True, False, False, False, False, True, False, False, False],
               [False, True, False, False, False, False, True, False, True, False, False, False, False, True, False, False, False],
               [False, True, False, False, False, False, True, False, True, False, False, False, False, True, False, False, False],
               [False, False, False, True, True, True, False, False, False, True, True, True, False, False, False, False, False],
               [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [False, False, False, True, True, True, False, False, False, True, True, True, False, False, False, False, False],
               [False, True, False, False, False, False, True, False, True, False, False, False, False, True, False, False, False],
               [False, True, False, False, False, False, True, False, True, False, False, False, False, True, False, False, False],
               [False, True, False, False, False, False, True, False, True, False, False, False, False, True, False, False, False],
               [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [False, False, False, True, True, True, False, False, False, True, True, True, False, False, False, False, False],
               [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
               [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]]

la = int(input("Ingresa el largo de la tabla: ") or 17)
al = int(input("Ingresa el alto de la tabla: ") or 17)

while True:
    if pulsar == 0:
        matrix, matrixc = randgen(al, la, muerto, vivo)
    print(showTable(al, la))
    time.sleep(0.75)
    iterar(matrix, matrixc, al, la, muerto, vivo)
