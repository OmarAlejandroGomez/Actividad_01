from models.persona import Persona
from models.estudiante import Estudiante
from models.docente import Docente
from models.administrativo import Administrativo

class PersonaController:

    def __init__(self):
        self.personas = []

    def _agregar_persona(self, persona):
        if any(p.get_identificacion() == persona.get_identificacion() for p in self.personas):
            raise ValueError("Ya existe una persona con esa identificación")

        self.personas.append(persona)
        return persona

    # Se comentó el método add_personas ya que no se puede instanciar la clase abstracta Persona directamente
    #def add_personas(self, identificacion, nombre, correo):
    #    return self._agregar_persona(Persona(identificacion, nombre, correo))

    def add_estudiante(self, identificacion, nombre, correo, programa_academico, semestre, promedio_acumulado):
        estudiante = Estudiante(identificacion, nombre, correo, promedio_acumulado, programa_academico, semestre)
        return self._agregar_persona(estudiante)

    def add_docente(self, identificacion, nombre, correo, facultad, tipo_contratacion, horas_semanales):
        docente = Docente(identificacion, nombre, correo, facultad, tipo_contratacion, horas_semanales)
        return self._agregar_persona(docente)

    def add_administrativo(self, identificacion, nombre, correo, dependencia, cargo, jornada):
        administrativo = Administrativo(identificacion, nombre, correo, dependencia, cargo, jornada)
        return self._agregar_persona(administrativo)

    def buscar_persona(self, identificacion):
        for persona in self.personas:
            if persona.get_identificacion() == identificacion:
                return persona
        return None

    def get_personas(self):
        return self.personas.copy()
