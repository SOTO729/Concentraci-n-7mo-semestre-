"""
EJERCICIO 3:

 Solicitar al usuario N temperaturas.

 Solicitar una a una estas temperaturas y llenar una lista.

 Se desea calcular su media (presentarla en pantalla) y determinar entre todas ellas el número de temperaturas que son superiores o iguales a esa media 
 (presentar en pantalla cuáles son estas temperaturas y cuántas son en total).

"""
temperaturas=[]
print('Ingrese todas las temperaturas que quiera\nCuando termine de ingresar las temperaturas digite "x"')
while True:
    try:
        temperatura_actual=input('Ingrese su temperatura a registrar')
        temperatura_actual=float(temperatura_actual)
        temperaturas.append(temperatura_actual)
    except:
        if temperatura_actual.upper()=='X':
            temperaturas.pop()
            break
        else:
            print('Valor de temperatura invalido!!!\nFavor de escribir solo numeros...')
print('La media de las temperaturas ingresadas es:',sum(temperaturas)/len(temperaturas))
import numpy as np
print('Resultado funcion de numpy:',np.mean(temperaturas))