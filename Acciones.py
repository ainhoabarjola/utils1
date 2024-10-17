import math    

def calcular_distancia(persona1, persona2):#aqui se llaman como quieras, persona1 no es necesariamente la persona1 definida
    distancia12 = math.sqrt((persona2.posicionx - persona1.posicionx)**2 + (persona2.posiciony - persona1.posiciony)**2)
    return (distancia12)


def misma_posicion(persona1, persona2):
    if (persona1.posicionx == persona2.posicionx and persona1.posiciony == persona2.posiciony):
        return f"{persona1.nombre} y {persona2.nombre} están en el mismo sitio."#como un print q no imprime si no es necesario, sin ()

def contar_personas_en_espacio(espacio):
    lista_personas = espacio.personas # persona1, persona2, persona3...
    numero_personas = len(lista_personas)  #len se usa para para contar elementos dentro de listas
    return (numero_personas)
