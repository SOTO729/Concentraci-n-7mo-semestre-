"""
EJERCICIO 1:

Se tienen los puntos A y B en el cuadrante positivo del plano cartesiano, elabore el algoritmo que permita obtener la distancia entre A y B.

Pistas: Un punto en el plano tiene dos coordenadas (X ,Y), entonces el punto A tendrá sus coordenadas (AX, AY) y el punto B de manera similar (BX, BY). Para determinar la distancia entre dos puntos, empleamos la fórmula matemática siguiente:

D = ((AX - BX) ** 2 + (AY - BY) ** 2) ** 0.5
"""
AX=float(input('Inserte la coordenada en x del punto A'))
AY=float(input('Inserte la coordenada en y del punto A'))
BX=float(input('Inserte la coordenada en x del punto B'))
BY=float(input('Inserte la coordenada en y del punto B'))
D=((AX-BX)**2+(AY-BY)**2)**0.5
print('La distancia entre puntos es:',round(D,2),':D')