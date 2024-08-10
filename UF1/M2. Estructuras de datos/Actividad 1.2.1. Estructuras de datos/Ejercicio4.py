"""
EJERCICIO 4:

▹Solicitar al usuario la dimensión de un vector que será llenado con valores enteros (máximo 10 elementos).

▹Solicitar uno a uno estos valores y llenar el vector.

▹ A partir de este, crear 2 vectores; uno con los números pares y el otro con los numero impares, además, decir de los vectores cual es más grande y el número de elementos en cada vector.
"""
print("""#### INSTRUCCIONES ####\n1. Insertar los elementos que desea agregar a la lista (deben ser menores a 10)\n
      2. Ingresar elementos de la lista uno por uno.\n
      3. Recuerde que no son validos los caracteres en secciones donde se le solicita un numero.\n""")

vector=[] #Se inicia la lista vector
while True: #Inicia ciclo para pedir varias veces el numero de elementos que se desea que tenga el vector hasta que cumpla con las especificaciones.
        try:#Inicia bloque try
            N=input('Ingrese al numero de elementos que desea agregar\n')#Se obtiene el numero de elementos a agregar en forma de cadena
            if N.count('.')!=0: #se verifica si existe un punto decimal, si existe significa que puede ser flotante o una cadena
                N=float(N)#si esta seccion arroja error entonces es una cadena y se pasa al bloque except
                if N>10:#si el dato ingresado es mayor a 10 se fierza el error dividiendo entre 0
                    1/0
                else:
                    print('Dado que solo se aceptan valores enteros, su registro "',N,'" sera agregado como: "',int(N),'".')#se notifica que se eliminara la parte decimal del resultado
                    N=int(N)#Se transforma a entero el valor
                    break#Se rompe el ciclo while
            else:
                N=int(float(N))#significa que el dato ingresado siempre fue entero
                if N>10: #Se vuelve a verificar si el dato ingresado es entero y si es asi se fuerza el error dividiendo entre 0
                    1/0                
                break#se rompe el ciclo while
        except:
            print('Valor ingresado inválido\n')#siempre que se llegue a error saldra este mensaje

for i in range(N):#inicia ciclo for que considera la longitud ingresada por el usuario, con un range para poder imprimir el numero de cada iteracion
    while True:
        try:
            elemento=input('Ingrese el elemento del vector No.: '+str(i+1)+'   \n')#se pide en formato str el elemento del vector cuyo numero depende del iterador i
            if elemento.count('.')!=0:#Se repite el mismo proceso que en el primer while para verificar si es flotante o cadena
                elemento=float(elemento)#En caso de ser cadena se pasa al bloque except
                print('Dado que solo se aceptan valores enteros, su registro "',elemento,'" sera modificado a "',int(elemento),'".\n')#Se notifica al usuario que su parte decimal sera eliminada
            elemento=int(elemento)#Se convierte ba entero
            vector.append(elemento)#Se añade a la lista vector
            break
        except:
            print('Valor ingresado invalido, favor de intentarlo de nuevo.\n')#Mensaje de error de este bloque except
pares,inpares=[],[]#Se definen las listas pares e inpares como listas vacias.
for i in vector:
    if i%2==0:#se verifica si el residuo de dividir entre dos cada elemento de la lista principal tiene residuo cero para saber si es par o no y se añade en pares o inpares respectivamente.
        pares.append(i)
    else:
        inpares.append(i)
N_PARES=len(pares)#Se obtiene el numero de elementos pares
N_INPARES=len(inpares)#Se obtiene el numero de elementos inpares
if N_PARES>N_INPARES:#Se verifica si pares es mayor que inpares y se imprimien los resultados
    print('El vector con los numeros pares es el más grande con',N_PARES,'elementos.\n')
    print('Lista pares:',pares,'\n')
    print('El vector con los numeros inpares tiene',N_INPARES,'elementos.\n')
    print('Lista inpares:',inpares,'\n')
elif N_PARES<N_INPARES:#Se verifica si inpares es mayor que pares y se imprimien los resultados
    print('El vector con los numeros inpares es el más grande con',N_INPARES,'elementos.\n')
    print('Lista pares:',pares,'\n')
    print('El vector con los numeros pares tiene',N_PARES,'elementos.\n')
    print('Lista inpares:',inpares,'\n')
else:#Se activa cuando ambas listas son iguales
    print('Ambos tienen el mismo tamaño:\n')
    print('Pares:',N_PARES,'\n')
    print('Lista pares:',pares,'\n')
    print('Inpares:',N_INPARES,'\n')
    print('Lista inpares:',inpares,'\n')