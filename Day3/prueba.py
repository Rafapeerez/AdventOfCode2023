#MY TRY, IT DOESN'T WORK

import re

filas = []
allowedCharacters = set('+$*#%/=&@-')

def procesar_vector(vector):
    resultado = []
    numero_actual = ''

    for elemento in vector:
        if elemento.isdigit():
            numero_actual += elemento
        elif elemento == '+':
            if numero_actual:
                resultado.append(int(numero_actual))
                numero_actual = ''

    if numero_actual:
        resultado.append(int(numero_actual))

    return resultado

def deleteRep( lst ): 
    vector_sin_repetidos = []  # Inicializamos la lista con el primer elemento

    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            vector_sin_repetidos.append(lst[i])

    return vector_sin_repetidos

def eliminar_repetidos_con_coincidencia_delante(lst):

    # Resultado final sin duplicados
    resultado = []

    for i in range(len(lst)):
        convert = str(lst[i])
        compare = str(lst[i-1])

        if compare != convert[-2:] :
            resultado.append(lst[i-1]) 

    return resultado

def eliminar_repetidos_con_coincidencia_detras(lst):

    # Resultado final sin duplicados
    resultado = []

    for i in range(len(lst)):
        convert = str(lst[i-1])
        compare = str(lst[i])

        if convert != compare[-2:] :
            resultado.append(lst[i-1]) 

    return resultado


with open("Puzzle.txt", "r") as f:
    for line in f :
        filas.append(line)
print(filas)

afectados = []
cont = 0

for i in range(len(filas)):
    for j in range(len(filas[i])):
        if cont == 0:
            if filas[i][j].isdigit():
                if (
                    (j > 0 and filas[i][j-1] in allowedCharacters) or
                    (j < len(filas[i]) - 1 and filas[i][j+1] in allowedCharacters) or
                    (i > 0 and j > 0 and filas[i-1][j-1] in allowedCharacters) or
                    (i > 0 and filas[i-1][j] in allowedCharacters) or
                    (i > 0 and j < len(filas[i]) - 1 and filas[i-1][j+1] in allowedCharacters) or
                    (i < len(filas) - 1 and j > 0 and filas[i+1][j-1] in allowedCharacters) or
                    (i < len(filas) - 1 and filas[i+1][j] in allowedCharacters) or
                    (i < len(filas) - 1 and j < len(filas[i]) - 1 and filas[i+1][j+1] in allowedCharacters)
                ):

                    if (filas[i][j+1].isdigit()) :
                        if (filas[i][j+1].isdigit() and filas[i][j+2].isdigit()) :
                            afectados.append(filas[i][j])
                            afectados.append(filas[i][j+1])
                            afectados.append(filas[i][j+2])
                        else :
                            afectados.append(filas[i][j])
                            afectados.append(filas[i][j+1])


                    elif (filas[i][j-1].isdigit()) :
                        if ( (filas[i][j-1].isdigit())  and (filas[i][j-2].isdigit())): 
                            afectados.append(filas[i][j-2])
                            afectados.append(filas[i][j-1])
                            afectados.append(filas[i][j])
                        else :
                            afectados.append(filas[i][j-1])
                            afectados.append(filas[i][j])

                    elif ( filas[i][j-1].isdigit() and  filas[i][j+1].isdigit() ) :
                        afectados.append(filas[i][j-1])                    
                        afectados.append(filas[i][j])
                        afectados.append(filas[i][j+1])

                    afectados.append('+')
        #cont += 1
                
print(afectados)
print(procesar_vector(afectados))
print(eliminar_repetidos_con_coincidencia_delante(procesar_vector(afectados))) 
print(deleteRep(procesar_vector(afectados))) 
print(eliminar_repetidos_con_coincidencia_detras(eliminar_repetidos_con_coincidencia_delante(deleteRep(procesar_vector(afectados)))))
print(sum(eliminar_repetidos_con_coincidencia_detras(eliminar_repetidos_con_coincidencia_delante(deleteRep(procesar_vector(afectados))))))  
f.close()
