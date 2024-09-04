import numpy as np 

lista_2d = [[2,3,9],
            [8,55,12],
            [91,23,74],
            [41,22,14]]

arr = np.array(lista_2d)
print(arr) 

a = np.array([5,88,74,12,33])
print(a)


print(arr.shape) #devolver la forma del arreglo (filas x columnas) 
print(a.shape) 

#f
#i
#l
#a
#s

#columnas 

#devolver el tipo de dato del areglo 

print(arr.dtype) #en la lista todos son enteros, si le pones un decimal aunque sea a un número de la lista devuelve float 

#devuelve la cantidad total de datos del arreglo 
print(arr.size) 

#devuelve las dimensiones del arreglo 
print(arr.ndim)

#devuelve el número de bytes utilizados para almacenar un solo elemento 
print(arr.itemsize) 

#cambiando el tipo de datos 

x = np.array([33,55,98.9])
print(x.dtype)
print(x) 

x1 = x.astype(int) 
print(x1.dtype)  
print(x1) 






