"""
EJERCICIO 4:

▹Solicitar al usuario la dimensión de un vector que será llenado con valores enteros (máximo 10 elementos).

▹Solicitar uno a uno estos valores y llenar el vector.

▹ A partir de este, crear 2 vectores; uno con los números pares y el otro con los numero impares, además, decir de los vectores cual es más grande y el número de elementos en cada vector.
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
vector=sorted(vector)
pares,inpares=[],[]
for i in vector:
    if i%2==0:
        pares.append(i)
    else:
        inpares.append(i)
N_PARES=len(pares)
N_INPARES=len(inpares)
if N_PARES>N_INPARES:
    print('El vector con los numeros pares es el más grande con',N_PARES,'elementos.\n')
    print('Lista pares:',pares,'\n')
    print('El vector con los numeros inpares tiene',N_INPARES,'elementos.\n')
    print('Lista inpares:',inpares,'\n')
elif N_PARES<N_INPARES:
    print('El vector con los numeros inpares es el más grande con',N_INPARES,'elementos.\n')
    print('Lista pares:',pares,'\n')
    print('El vector con los numeros pares tiene',N_PARES,'elementos.\n')
    print('Lista inpares:',inpares,'\n')
else:
    print('Ambos tienen el mismo tamaño:\n')
    print('Pares:',N_PARES,'\n')
    print('Lista pares:',pares,'\n')
    print('Inpares:',N_INPARES,'\n')
    print('Lista inpares:',inpares,'\n')