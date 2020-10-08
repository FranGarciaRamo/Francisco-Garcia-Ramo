'''cAMBIAR MES POR NUMERO'''
def mes():
    abreviames="EneFebMarAbrMayJunJulAgoSepOctNovDic"
    numeromes=input("introduce mes: ")
    pos=(numeromes-1)*3
    print "El mes es: ", abreviames[pos:pos+3]

mes()
