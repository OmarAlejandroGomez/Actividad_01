from models.persona import Persona

class Estudiante(Persona):
    
    def __init__(self, identificacion, nombre, correo, código_estudiantil, programa_academico, semestre):
        super().__init__(identificacion, nombre, correo)
        self.código_estudiantil = código_estudiantil
        self.programa_academico = programa_academico
        self.semestre = semestre