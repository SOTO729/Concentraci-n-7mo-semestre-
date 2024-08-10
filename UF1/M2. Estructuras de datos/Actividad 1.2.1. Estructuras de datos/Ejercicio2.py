"""
EJERCICIO 2:

 Escriba un script en Python que solicite al usuario indicar el número de elementos que tendrá un vector a llenar
  
 (máximo 10 elementos), de datos tipo enteros y con posibles repeticiones de valores.

 Con base al número de elementos ingresado, solicite introducir los elementos del vector uno a uno.

 Obtenga como salida una lista de los números ordenados (de menor a mayor), pero sin repeticiones.

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
vector=list(set(sorted(vector)))#sorted ordena los elementos de la lista de menor a mayor, set elimina los repetidos, pero devuelve una especie de diccionario y list se asegura de que el resultado final sea una lista.
print(vector)