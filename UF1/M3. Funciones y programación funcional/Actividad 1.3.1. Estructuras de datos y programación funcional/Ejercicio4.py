'4. Una función que reciba la lista de palabras y regrese una tupla con dos valores: el primero representa la cantidad de palabras que comienzan con una vocal y el segundo representa la cantidad de palabras que comienzan con una consonante.'
def clasificacion_palabras(lista):
    #Definición de vocales:
    vocales='AEIOU'
    #Contadores en 0
    p_vocales=0
    p_consonantes=0
    #Recorrer la lista y revisar si empiezan en vocales, si no, son consonantes.
    for palabra in lista:
        if palabra[0].upper() in vocales:
            p_vocales+=1
        else:
            p_consonantes+=1
    return p_vocales,p_consonantes
#Ejemplo
resultado=clasificacion_palabras(['hola','adios','verde','flor'])
print(resultado)