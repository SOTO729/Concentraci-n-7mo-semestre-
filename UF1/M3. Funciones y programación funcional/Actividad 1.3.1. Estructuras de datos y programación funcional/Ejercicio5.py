'5. Una función que reciba la lista de palabras y regrese un diccionario donde las llaves son las letras del abecedario y cada elemento una lista de las palabras que comienzan con dicha letra. '

def palabras_por_letra(lista_palabras):
    # Crear un diccionario vacío para almacenar las palabras por letra
    palabras_por_letra = {}

    # Recorrer cada palabra en la lista
    for palabra in lista_palabras:
        if palabra and palabra[0].isalpha():
            # Obtener la primera letra de la palabra en minúsculas
            primera_letra = palabra[0].lower()

            # Agregar la palabra al diccionario correspondiente
            if primera_letra not in palabras_por_letra:
                palabras_por_letra[primera_letra] = [palabra]
            else:
                palabras_por_letra[primera_letra].append(palabra)

    return palabras_por_letra

# Ejemplo
palabras=['hola','abb','skf','soto']
diccionario_palabras = palabras_por_letra(palabras)
print(diccionario_palabras)