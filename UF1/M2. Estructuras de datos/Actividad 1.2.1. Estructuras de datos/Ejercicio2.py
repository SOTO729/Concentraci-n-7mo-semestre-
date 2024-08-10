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

vector=[]
while True:
        try:
            N=input('Ingrese al numero de elementos que desea agregar\n')
            if N.count('.')!=0:
                N=float(N)
                if N>10:
                    1/0
                else:
                    print('Dado que solo se aceptan valores enteros, su registro "',N,'" sera agregado como: "',int(N),'".')
                    N=int(N)
                    break
            else:
                N=int(float(N))

                if N>10:
                    1/0                
                break
        except:
            print('Valor ingresado inválido\n')

for i in range(N):
    while True:
        try:
            elemento=input('Ingrese el elemento del vector No.: '+str(i+1)+'   \n')
            if elemento.count('.')!=0:
                elemento=float(elemento)
                print('Dado que solo se aceptan valores enteros, su registro "',elemento,'" sera modificado a "',int(elemento),'".\n')
            elemento=int(elemento)
            vector.append(elemento)
            break
        except:
            print('Valor ingresado invalido, favor de intentarlo de nuevo.\n')
vector=list(set(sorted(vector)))
print(vector)