# Escribir dos funciones que permitan calcular la cantidad de segundos en un tiempo dado que van a ser horas minutos y segundos



#Calcular segundos dada hora minutos y segundos
def calc1(horas, minutos, segundos):
    segundosHora = int(horas) * 3600
    segundosMinuto = int(minutos) * 60
    return segundosHora + segundosMinuto + int(segundos)



#Calcular las horas minutos y segundos dados los segundos
def calc2(seconds):
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds) 


