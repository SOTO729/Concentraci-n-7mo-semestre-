'3. Una función que reciba la lista de palabras y obtenga el promedio de letras que tienen las palabras.'
def promedio_letras(lista):
    #Inicia contador en 0
    contador_palabras=0
    #Suma la longitud de las palabras
    for i in lista: contador_palabras+=(len(i))
    #Retorna el promedio
    return contador_palabras/len(lista)
#Ejemplo
lista=['hola','que','hace','yeah']
resultado=promedio_letras(lista)
print(resultado)