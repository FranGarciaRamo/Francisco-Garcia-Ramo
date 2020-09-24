def Franco():
    NumeroFinal=100
    SumaAcumulada=0

    for cont in range(1,NumeroFinal+1):
        SumaAcumulada=SumaAcumulada+cont

    print "La suma de los numeros hasta", NumeroFinal
    print "=", SumaAcumulada

Franco()

    NumeroFinal=input("Hasta que numero deseas sumar: ")
    SumaAcumulada=0

    for cont in range(1,NumeroFinal+1):
        SumaAcumulada=SumaAcumulada+cont

    print "La suma de los numeros hasta", NumeroFinal
    print "=", SumaAcumulada

