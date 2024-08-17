'1. Una función para obtener la lista de palabras del archivo.'
def obtener_palabras():
    #Obtener el archivo, leer su contenido y obtener la lista de palabras con split
    archivo=open('./UF1/M3. Funciones y programación funcional/Actividad 1.3.1. Estructuras de datos y programación funcional/Fragmento El Principito.txt','r',encoding='utf-8')
    contenido=archivo.read()
    palabras=contenido.split()
    #Cerrar elm archivo
    archivo.close()
    return palabras
#Ejemplo
palabras_del_archivo=obtener_palabras()
print('A continuacion la lista de lapabras del archivo:\n',palabras_del_archivo)