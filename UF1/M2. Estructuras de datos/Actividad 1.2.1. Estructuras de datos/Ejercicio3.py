"""
EJERCICIO 3:

 Solicitar al usuario N temperaturas.

 Solicitar una a una estas temperaturas y llenar una lista.

 Se desea calcular su media (presentarla en pantalla) y determinar entre todas ellas el número de temperaturas que son superiores o iguales a esa media 
 (presentar en pantalla cuáles son estas temperaturas y cuántas son en total).

"""
temperaturas=[]
print('Ingrese todas las temperaturas que quiera\nCuando termine de ingresar las temperaturas digite "x"')
while True:#Inicia ciclo while para verificar si el contenido ingresado por el usuario es correcto
    try:#Inicia bloque try
        temperatura_actual=input('Ingrese su temperatura a registrar')#Se pide la temperatura
        temperatura_actual=float(temperatura_actual)#Se convierte a flotante, si es una cadena pasa al bloque except
        temperaturas.append(temperatura_actual)#Si es un numero se añade a la lista temperaturas
    except:
        if temperatura_actual.upper()=='X':#Se verifica si se ingreso x para romper el ciclo
            temperaturas.pop()#Si es asi se elimina la x de la lista temperaturas
            break#Y se rompe el ciclo
        else:
            print('Valor de temperatura invalido!!!\nFavor de escribir solo numeros...')#Mensaje de error
print('La media de las temperaturas ingresadas es:',sum(temperaturas)/len(temperaturas))#Calculo de la media.