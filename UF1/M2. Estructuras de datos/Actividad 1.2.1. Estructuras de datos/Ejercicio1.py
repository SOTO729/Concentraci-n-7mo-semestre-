"""
EJERCICIO 1:

 En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, 

 debe pedir dos datos (de cualquier tipo) y estos nuevos datos ingresados, 

 serán sustituidos en el primer y segundo lugar, y finalmente presentar los nuevos valores al usuario:

 [20, 50, "Curso", 'Python', 3.14]

"""
lista=[20, 50, "Curso", 'Python', 3.14] #Generar la lista original
print('Los valores actuales de la lista son:\n',lista) #Mostrar la lista original
dato1=input('Ingrese el primer valor que sera sustituido en el primer lugar...') #Obtener el primer valor
dato2=input('Ingrese el primer valor que sera sustituido en el segundo lugar...') #Obtener el segundo valor
mini_lista=[dato1,dato2] #Agrupar los resultados en una segunda lista
cont=0#Inicializar el contador en 0
for i in mini_lista: #Iniciar ciclo para aplicar el mismo procedimiento a ambos valores
    try: #Revisar si es un numero
        float(i) #Intentar convertir a flotante para revisar si es un numero
        if i.count('.')==0: #Si es 0 significa que es entero porque el numero no tiene punto decimal
            lista.remove(lista[cont]) #Remover valor en funcion del contador
            lista.insert(cont,int(i)) #Insertar valor en funcion del contador
        else: #Significa que es flotante
            lista.remove(lista[cont])   #Remover valor en funcion del contador
            lista.insert(cont,float(i)) #Insertar valor en funcion del contador
    except: #Significa que es una cadena
        lista.remove(lista[cont]) #Remover valor en funcion del contador
        lista.insert(cont,i)      #Insertar valor en funcion del contador
    cont+=1 #Auemntar en 1 el contador con cada ciclo
print('Los valores finales de la lista son:\n',lista)
for i in lista:
    print(type(i))