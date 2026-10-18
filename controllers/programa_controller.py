from models.programa_academico import ProgramaAcademico

class ProgramaController:

    def __init__(self):
        self.programas = []

    def add_programa(self, codigo, nombre, facultad, numero_semestres):
        programa = ProgramaAcademico(codigo, nombre, facultad, numero_semestres)
        self.programas.append(programa)
        return programa

    def get_programas(self):
        return self.programas.copy()