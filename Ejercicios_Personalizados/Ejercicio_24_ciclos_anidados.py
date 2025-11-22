# EJERCICIO 24: Ciclos for anidados
# ============================================================
# Este código debe obtener los elementos de una matriz y mostrarlos al usuario.
# Complete el código construyendo los ciclos "for" correspondientes. El primer ciclo
# debe recorrer las filas de la matriz, llame al iterador del primer ciclo "fila".
# Mientras que el segundo ciclo debe recorrer las columnas o los elementos de las filas.
# Llame al iterador del segundo ciclo "valor" y ejecute el código sin depurar.
# Recuerda que no debes escribir espacios innecesarios.

matriz=[[1,2,3],[4,5,6],[7,8,9]]
for fila in matriz:
    for valor in fila:
        print(valor)
