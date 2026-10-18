from models.asignatura import Asignatura

class AsignaturaController:

    def __init__(self):
        self.asignaturas = []

    def add_asignatura(self, codigo, nombre, creditos, programa_academico):
        asignatura = Asignatura(codigo, nombre, creditos, programa_academico)
        self.asignaturas.append(asignatura)
        return asignatura

    def get_asignaturas(self):
        return self.asignaturas.copy()