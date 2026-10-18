from models.persona import Persona

class Estudiante(Persona):

    # Algunos atributos de la clase Estudiante son heredados de la clase Persona, como identificacion, nombre y correo. Además, la clase Estudiante tiene atributos adicionales como código_estudiantil, programa_academico y semestre. 
    # Estudiante cuenta con un atributo denominado código_estudiantil, que representa el código único asignado a cada estudiante. Este solo es para consulta y lo genera automáticamente el sistema por lo que requiere un contador 
    contador_estudiantes = 0
    
    def __init__(self, identificacion, nombre, correo, promedio_acumulado, programa_academico, semestre):
        super().__init__(identificacion, nombre, correo)
        Estudiante.contador_estudiantes += 1
        self.codigo_estudiantil = f"EST-{Estudiante.contador_estudiantes + 1:04d}"
        self.promedio_acumulado = promedio_acumulado
        self.programa_academico = programa_academico
        self.semestre = semestre