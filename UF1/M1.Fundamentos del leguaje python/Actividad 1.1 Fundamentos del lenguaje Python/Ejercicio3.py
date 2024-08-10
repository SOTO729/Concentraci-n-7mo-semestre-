"""
EJERCICIO 3:

Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son:

Candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. 
Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido 
[color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a 
ninguno de los candidatos disponibles, indicar “Opción errónea”.

Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula
"""
print('Bienvenido al sistema de votaciones \nLas opciones con las que cuenta son las siguientes:\nA: partido rojo\nB: partido verde\nC: partido azul')

while True:
    voto=input('Favor de escribir su voto Aquí')
    voto=voto.upper()
    if voto!='A' and voto!='B' and voto!='C':
        print('Opción errónea')
        print('Recuerde que tiene las siguientes opciones:\nA: partido rojo\nB: partido verde\nC: partido azul')
    else:
        print('Su voto ha sido registrado correctamente.')
        if voto=='A':
            print('Usted ha votado por el partido rojo')
        elif voto=='B':
            print('Usted ha votado por el partido verde')
        else:
            print('usted ha votado por el partido azul')
        break
        
