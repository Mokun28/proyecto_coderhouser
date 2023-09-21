from datetime import datetime

tiempoactual = datetime.now()
miCumple = datetime(2022,11,29)
tiempoFalta = miCumple - tiempoactual
print(tiempoFalta.days*60*60*24 + tiempoFalta.seconds)