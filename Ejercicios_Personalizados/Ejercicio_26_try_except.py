# EJERCICIO 26: Try-except para manejo de excepciones
# ============================================================
# El siguiente código obtiene la multiplicación de dos números, sin embargo,
# se desea evitar el problema de tipos incompatibles. Utilice las excepciones
# "try" y "except" para completar el código y ejecute el archivo sin depurar
# el código para comprobar su resultado.
# Recuerda que no debes escribir espacios innecesarios.

try:
    numero=int('50')
    resultado=numero*5
    print(resultado)
except ValueError:
    print('Error: Valor inválido')
