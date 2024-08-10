"""
EJERCICIO 2:

Un proveedor de estéreos ofrece un descuento del 10% sobre el precio sin IVA, 
de algún aparato si este cuesta $2,000 o más. Además, independientemente de esto, 
ofrece un 5% de descuento adicional (aunque ya tenga el 10% de descuento por la compra de $2,000) 
sobre el precio sin IVA, si la marca es “HUAWEI”.
▹Determinar cuánto pagará, con IVA incluido, un cliente cualquiera por la compra de su aparato. IVA = 16%.
"""
IVA=16#%
PRECIO=2000
PRECIO=PRECIO-PRECIO*0.1#APLICAR PRIMER DESCUENTO
PRECIO=PRECIO-PRECIO*0.05#APLICAR SEGUNDO DESCUENTO SOBRE EL PRIMER DESCUENTO
PRECIO=PRECIO+PRECIO*0.16#APLICAR IVA SOBRE EL VALOR FINAL
print('Metodo 1:',PRECIO)
precio=2000
print('Metodo 2:',((precio*0.9)*0.95)*1.16)