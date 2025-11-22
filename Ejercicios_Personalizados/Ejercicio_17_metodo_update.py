# EJERCICIO 17: Método update en diccionarios
# ============================================================
# Crea un diccionario llamado "calificaciones_nuevas" con los siguientes valores:
# "Laura":95,"Fernando":88,"Rosa":92 y utilízalo para agregarlos al diccionario
# "calificaciones" con el método "update". Ejecuta el archivo sin depurar.
# Recuerda que no debes escribir espacios innecesarios y que debes utilizar comillas simples.

calificaciones={'Pedro':85,'María':90}
calificaciones_nuevas={'Laura':95,'Fernando':88,'Rosa':92}
calificaciones.update(calificaciones_nuevas)
print(calificaciones)
