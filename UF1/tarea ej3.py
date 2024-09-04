import re
with open('./UF1/comentarios.txt','r',encoding='utf-8') as archivo:
    lineas=[]
    for linea in archivo.readlines():
        lineas.append(linea)
    contenido=archivo.read()
print(contenido)
lista_patrones=['excelente','malo','problema','genial','defectuoso']
for i in lista_patrones:
    for j in lineas:
        patron=r'\b'+lista_patrones[i]+'?\b'
