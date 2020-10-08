'''cAMBIAR MES POR NUMERO'''
'''genera una contraseña partir de 3 letras del nombre y tres del apellido'''

def contrasena():
    nombre = raw_input("Introduce nombre: ")
    apellidos = raw_input ("Introduce el apellido: ")
    contrasena=nombre[-3:]+apellidos[-3:]
    print "Tu contrasena es: ",contrasena


contrasena()
