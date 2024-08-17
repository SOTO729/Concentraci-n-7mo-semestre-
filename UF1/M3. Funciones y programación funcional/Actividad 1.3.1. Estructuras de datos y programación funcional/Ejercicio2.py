'2. Una función que reciba la lista de palabras y obtenga la cantidad de palabras aproximadas que tiene el archivo.'
def contar_palabras(lista):
    lista_palabras=[]
    #Obtener el archivo, leer su contenido y obtener la lista de palabras con split
    archivo=open('./UF1/M3. Funciones y programación funcional/Actividad 1.3.1. Estructuras de datos y programación funcional/Fragmento El Principito.txt','r',encoding='utf-8')
    contenido=archivo.read()
    palabras=contenido.split()
    #Guardar en una lista cuantas veces aparecen las palabras ingresadas.
    for i in lista:
        lista_palabras.append(palabras.count(i))
    #Cerrar el archivo
    archivo.close()
    #Construir el diccionario para el resultado
    resultado={key:lista_palabras for (key,lista_palabras) in zip(lista,lista_palabras)}
    return resultado
#Ejemplo
palabras=contar_palabras(['un','dia','flor','sol','principe'])
print(palabras)