'''Realizar un programa que al recibir un numero entero muestre por pantalla los 3
num anteriores y los 3 siguientes al num recibido'''
def ejercicio_10():
    numero=input("Introduce un numero que sea entero: ")
    for cont in range(-3,4):
        print numero + cont

ejercicio_10()
