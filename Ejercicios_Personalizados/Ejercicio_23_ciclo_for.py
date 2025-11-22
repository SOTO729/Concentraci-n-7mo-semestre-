# EJERCICIO 23: Ciclo for con iterador
# ============================================================
# Lea la palabra con un ciclo "for" llamando al iterador como "carácter"
# y no utilice la función "range". Agregue cada carácter a la lista "caracteres"
# utilizando el método "append". Finalmente, imprima la lista caracteres con la
# función "print" y ejecute su código sin depurar.
# Recuerda que no debes escribir espacios innecesarios.

palabra='Python'
caracteres=[]
for carácter in palabra:
    caracteres.append(carácter)
print(caracteres)
