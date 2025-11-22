# EJERCICIO 10: Conversión de tipos con type()
# ============================================================
# Transforma la variable "precio" a flotante, utiliza la función "type" para
# guardar el tipo de dato en la variable "clase" e imprime ambos resultados con
# solo una función "print" en el orden que se mencionan en esta instrucción.
# Ejecuta el archivo sin depurar.
# Recuerda que no debes escribir espacios innecesarios.

precio='99.99'
precio=float(precio)
clase=type(precio)
print(precio,clase)
