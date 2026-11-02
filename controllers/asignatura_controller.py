from models.asignatura import Asignatura
from models.excepciones import AsignaturaNoEncontradaError

class AsignaturaController:

    def __init__(self):
        self.asignaturas = []

    def add_asignatura(self, codigo, nombre, creditos, programa_academico):
        asignatura = Asignatura(codigo, nombre, creditos, programa_academico)
        self.asignaturas.append(asignatura)
        return asignatura

    def get_asignaturas(self):
        return self.asignaturas.copy()

     # Busca una asignatura por su código; si no existe lanza la excepción AsignaturaNoEncontradaError
    
    def buscar_asignatura(self, codigo):
        for asignatura in self.asignaturas:
            if asignatura.get_codigo() == codigo.strip():
                return asignatura
        raise AsignaturaNoEncontradaError(codigo.strip())   