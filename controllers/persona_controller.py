from models.persona import Persona

class PersonaController:

    #def __init__(self, programa_controller):
    def __init__(self):
        self.personas = []

    def add_personas(self, identificacion, nombre, correo):
        persona = Persona(identificacion, nombre, correo)
        
        if any(p.get_identificacion() == persona.get_identificacion() for p in self.personas):
            raise ValueError("Ya existe una persona con esa identificación")
            
        self.personas.append(persona)
        #self.personas.append(persona)

    def get_personas(self):
        return self.personas.copy()
