class Persona:
    def __init__(self, nombre, posicionx=0, posiciony=0): #si algún parámetro viene con cifra predefinida, se ponen detrás
        self.nombre = nombre
        self.posicionx = posicionx
        self.posiciony = posiciony

    def __str__(self):
        return f"Nombre: {self.nombre}. Posición: x= {self.posicionx} y= {self.posiciony}" # se meten {} para no tener que poner "" todo el rato

        
class Espacio:
    def __init__(self, nombre, largo= 10, ancho=10): #Pone =10 porque lo de por hecho si no te lo definen
        self.nombre = nombre
        self.personas = [] #No hace falta definir atributos vacíos, esto ahora es una lista vacía
        self.largo = largo
        self.ancho = ancho

    def anadir_persona(self, persona):
        self.personas.append(persona) #append está añadiendo persona a la lista personas
        print(f"He añadido a {persona.nombre} al espacio {self.nombre}")

    def __str__ (self):
        return f"Este espacio es {self.nombre} y mide {self.ancho} metros por {self.largo} metros"
        