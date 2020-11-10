def ejercicio_9():
    horas_totales=input("Cuantas horas has hecho: ")
    precio_normal=30
    precio_extra=1.5*precio_normal
    if(horas_totales<=30):
        salario=horas_totales*precio_normal
    else:
        salario=30*precio_normal+(horas_totales-30)*precio_extra
    print "Salario= ", salario
ejercicio_9()
