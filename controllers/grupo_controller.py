from models.grupo_academico import GrupoAcademico

class GrupoController:

    def __init__(self):
        self.grupos = []

    def add_grupo(self, codigo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_fin, salon):
        if any(grupo.get_codigo() == codigo for grupo in self.grupos):
            raise ValueError("Ya existe un grupo con el mismo código")
        
        grupo = GrupoAcademico(codigo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_fin, salon)
        self.grupos.append(grupo)
        return grupo

    def get_grupos(self):
        return self.grupos.copy()