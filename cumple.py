from datetime import datetime

def calcularCumple(y,m,d):

    tiempoactual = datetime.now()
    miCumple = datetime(y,m,d)
    tiempoFalta = miCumple - tiempoactual
    resultado = tiempoFalta.days *60*60*24 + tiempoFalta.seconds

    return resultado
