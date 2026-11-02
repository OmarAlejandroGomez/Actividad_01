from models.programa_academico import ProgramaAcademico
from models.excepciones import ProgramaNoEncontradoError
class ProgramaController:

    def __init__(self):
        self.programas = []

    def add_programa(self, codigo, nombre, facultad, numero_semestres):
        programa = ProgramaAcademico(codigo, nombre, facultad, numero_semestres)
        self.programas.append(programa)
        return programa

    def get_programas(self):
        return self.programas.copy()

    # Busca un programa por su código; si no existe lanza la excepción ProgramaNoEncontradoError
    
    def buscar_programa(self, codigo):
        for programa in self.programas:
            if programa.get_codigo() == codigo.strip():
                return programa
        raise ProgramaNoEncontradoError(codigo.strip())    