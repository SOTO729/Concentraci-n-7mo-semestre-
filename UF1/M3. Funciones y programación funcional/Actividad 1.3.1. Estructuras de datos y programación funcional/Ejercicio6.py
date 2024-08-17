def contar_puntuacion(texto):
    #Definición de signos de puntuación:
    puntuacion = ".,;:!?¿¡()[]{}\"'"
    # Inicializar el contador
    contador = 0
    # Recorrer cada carácter en el texto
    for caracter in texto:
        if caracter in puntuacion:
            contador += 1
    return contador

# Ejemplo
texto_ejemplo = "¡Hola, mundo! ¿Cómo estás? Esto es una prueba."
cantidad_puntuacion = contar_puntuacion(texto_ejemplo)
print(f"Se utilizaron {cantidad_puntuacion} signos de puntuación en el texto.")
