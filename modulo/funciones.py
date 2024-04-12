def generar_estructura(names,goals,goals_avoided,assists):
    lista_nombres = [name.strip() for name in names.split(',')]
    return dict(zip(lista_nombres,zip(goals,goals_avoided,assists)))


def conocer_goleador(estructura):
    return max(estructura.items(),key=lambda x: x[1][0])


def conocer_mas_influyente(estructura):
    lista_estadisticas = [tuple([nombre,sum([estadistica[0]*1.5, estadistica[1]*1.25, estadistica[2]])]) 
                          for nombre,estadistica in estructura.items()]
    return max(lista_estadisticas,key=lambda x: x[1])


def calcular_promedio_equipo(estructura,cant_partidos):
    return sum(estadistica[0] for estadistica in estructura.values())/cant_partidos

    
def calcular_promedio_jugador(goleador,cant_partidos):
    return goleador/cant_partidos