'''CAMBIAR MES POR NUMERO'''
'''genera una contraseña partir de 3 letras del nombre y tres del apellido'''

def contrasena():
    nombre = raw_input("Introduce nombre: ")
    apellidos = raw_input ("Introduce el apellido: ")
    import random
    n = random.randint(0,99)
    contrasena = nombre[0:4]+ apellidos[0]
    nombre=contrasena.capitalize()
    print "Tu contrasena personalizada es: ",nombre,n

    
contrasena()
