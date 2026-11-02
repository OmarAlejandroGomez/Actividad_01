# 5 Excepciones en del Sistema de Gestión Académica.
# Cada clase hereda de Exception y después entrega un mensaje descriptivo del error que se ha producido.

class EstudianteYaMatriculadoError(Exception):
    def __init__(self, codigo_estudiantil, codigo_grupo):
        super().__init__(f"Estudiante {codigo_estudiantil} ya está matriculado en el grupo {codigo_grupo}")


class CapacidadMaximaError(Exception):
    def __init__(self, codigo_grupo, capacidad_maxima):
        super().__init__(f"El grupo {codigo_grupo} alcanzó su capacidad máxima de {capacidad_maxima} estudiantes")


class EstudianteNoMatriculadoError(Exception):
    def __init__(self, codigo_estudiantil, codigo_grupo):
        super().__init__(f"Estudiante {codigo_estudiantil} no está matriculado en el grupo {codigo_grupo}")


class AsignaturaNoEncontradaError(Exception):
    def __init__(self, codigo_asignatura):
        super().__init__(f"No existe una asignatura con el código {codigo_asignatura}")


class ProgramaNoEncontradoError(Exception):
    def __init__(self, codigo_programa):
        super().__init__(f"No existe un programa académico con el código {codigo_programa}")