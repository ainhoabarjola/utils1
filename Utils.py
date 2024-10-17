from Clases import Persona
from Clases import Espacio
from Acciones import calcular_distancia
from Acciones import misma_posicion
from Acciones import contar_personas_en_espacio

"""
for persona in personan
    print("Cuando no halla más personas di: No hay mas personas")
    if personan(imput(f"Dime como se llama la persona: {persona.nombre} y dime en que posicion x esta: {posicionx.persona}
     y en que posicion y está: {distanciay.persona}")):
    elif 
    

"""

persona1 = Persona("Marta", 3, 4)
print(persona1)

persona2 = Persona("Mariano") #hay valores que no hace falta poner porque ya tienen una cifra definida
print(persona2)

persona3 = Persona("Julia", 3, 4)
print(persona3)

persona4 = Persona("Carlota")
print(persona4)

personas = [persona1, persona2, persona3, persona4]

for persona in personas: #elegimos una persona
    personas.remove(persona)
    for persona_aux in personas: #vamos elegiendo las demás
        print(f"{persona.nombre} y {persona_aux.nombre} están a {calcular_distancia(persona,persona_aux)} metros" ) 
        iguales = misma_posicion(persona, persona_aux)
        if iguales: #si iguales es none (no existe) no pasa por aqui y no se imprime
            print (iguales)


espacio1 = Espacio("Casa")
print(f"\n{espacio1}")
espacio1.anadir_persona(persona1)
espacio1.anadir_persona(persona3)
numero_personas = contar_personas_en_espacio(espacio1)
print( f"En {espacio1.nombre} hay {numero_personas} personas")

espacio2 = Espacio("Sevilla", "20000","10000")
print(espacio2)
espacio2.anadir_persona(persona2)
numero_personas = contar_personas_en_espacio(espacio2)
print( f"En {espacio2.nombre} hay {numero_personas} personas")
