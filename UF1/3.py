import re
with open('./UF1/comentarios.txt','r',encoding='utf-8') as archivo:
    lineas=[]
    for linea in archivo.readlines():
        lineas.append(linea.lower())
lista_patrones=['excelente','malo','problema','genial','defectuoso','caro','vale','maravilla']
coincidencias=[]
for i in lista_patrones:
    for j in lineas:
        patron=rf'\b{i}\b'
        #print(patron)
        buscar=re.findall(patron,j)
        if len(buscar)>0:
            coincidencias.append(buscar[0])
resumen={}
palabras=[]
total=0
for i in coincidencias:
    if i in palabras:
        continue
    else:
        veces_que_aparece=coincidencias.count(i)
    palabras.append(i)
    resumen.update({palabras[-1]:veces_que_aparece})
    total+=veces_que_aparece
satisfaccion=['excelente','genial','vale','maravilla']
insatisfaccion=['malo','problema','defectuoso','caro']
porcentajes={}
buenas,malas=0,0
for key in resumen:
    porcentajes.update({key:round(resumen[key]/total*100,2)})
    if key in satisfaccion:
        buenas+=porcentajes[key]
    else:
        malas+=porcentajes[key]
print('Resumen:')
print(resumen)
print()
print('Porcentajes:')
print(porcentajes)
print()
print('Porcentaje de buenas:',buenas)
print()
print('Porcentaje de malas:',malas)

oeoe=2