import re
print('\nEste es un sistema para validar contraseñas')
print(' ')
print('Es por eso que las contraseñas a ingresar tienen que tener los siguientes requerimientos:\n')
print('\t-Tener al menos 8 caracteres')
print('\t-Contar con al menos 1 letra MAYUSCULA y 1 letra MINUSCULA')
print('\t-Contener al menos un caracter especial (Ej. !@#$%^&.)')
print(' ')

patron1= r'.{8}'
patron2= r'[A-Z][a-z]+|[a-z]+[A-Z]|[a-z]+[A-Z][a-z]+|[a-z][A+Z]+|[A-Z]+[a-z][A-Z]|\$\$[A-Z]+[a-z]+\d+]'
patron3= r'[A-Z][a-z]+\d+\$+|\$\$[A-Z]+[a-z]+\d+|[A-Z]+\$+[a-z]+\d+|\d+[A-Z]+\$[a-z]|\d+[A-Z]+\$+[a-z]+|\$[A-Z][a-z]+\d+'
#Por practicidad unicamente se inculyo el signo $ como caracter especial

contrasenas=[]
for x in range(4):
    password=str(input('Ingrese su contraseña:    '))
    contrasenas.append(password)
    for contra in contrasenas:
        match1= re.match(patron1,contra)
        if match1:
            match2=re.match(patron2,contra)
            if match2:
                match3=re.match(patron3,contra)
                if match3:
                    print(f'\t-Formato valido para contraseña: {contra}\n')
                else:
                    print(f'\t-No es valida el formato de la contraseña, no cuenta con al menos un caracter especial: {contra}\n')
            else:
                print(f'\t-No es valida el formato de la contraseña, no cuenta con 1 letra mayuscula o 1 minuscula: {contra}\n')

        else:
            print(f'\t-No es valida el formato de la contraseña, no cuenta con 8 caracteres: {contra}\n')