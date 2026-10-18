from models.persona import Persona
from models.programa_academico import ProgramaAcademico

class Estudiante(Persona):

    # Algunos atributos de la clase Estudiante son heredados de la clase Persona, como identificacion, nombre y correo. Además, la clase Estudiante tiene atributos adicionales como código_estudiantil, programa_academico y semestre. 
    # Estudiante cuenta con un atributo denominado código_estudiantil, que representa el código único asignado a cada estudiante. Este solo es para consulta y lo genera automáticamente el sistema por lo que requiere un contador 
    contador_estudiantes = 0
    
    def __init__(self, identificacion, nombre, correo, promedio_acumulado, programa_academico, semestre):
        super().__init__(identificacion, nombre, correo)
        self.set_programa_academico (programa_academico)
        self.set_semestre (semestre)
        self.set_promedio_acumulado (promedio_acumulado)
        Estudiante.contador_estudiantes += 1
        self._codigo_estudiantil = f"EST-{Estudiante.contador_estudiantes:03d}"
               
    # el código estudiantil es de consulta, por lo que no se solicita al usuario    
    def get_codigo_estudiantil(self):
        return self._codigo_estudiantil

    def get_promedio_acumulado(self):
        return self._promedio_acumulado

    #revisar que el promedio acumulado sea un número entre 0 y 5, de lo contrario se lanza una excepción

    def set_promedio_acumulado(self, promedio_acumulado):
        if isinstance(promedio_acumulado, (int, float)) and 0 <= promedio_acumulado <= 5:
            self._promedio_acumulado = promedio_acumulado
        else:
            raise ValueError("El promedio acumulado debe estar entre 0 y 5")

    # revisar que el programa académico no esté vacío

    def get_programa_academico(self):
        return self._programa_academico

    def set_programa_academico(self, programa_academico):
        if isinstance(programa_academico, ProgramaAcademico):
            self._programa_academico = programa_academico
        else:
            raise ValueError("El programa académico debe existir")

    def get_semestre(self):
        return self._semestre

    def set_semestre(self, semestre):
        if isinstance(semestre, int) and semestre > 0 and semestre <= 10:
            self._semestre = semestre
        else:
            raise ValueError("El semestre debe ser un número entero entre 1 y 10")

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} - Código Estudiantil: {self.get_codigo_estudiantil()}, - Promedio Acumulado: {self.get_promedio_acumulado()}, - Programa Académico: {self.get_programa_academico() .get_nombre()}, - Semestre: {self.get_semestre()}"

    def realizar_actividad_principal(self):
        return f"El estudiante {self.get_nombre()} está realizando su actividad principal de estudio en el programa académico de {self.get_programa_academico() .get_nombre()} en el semestre {self.get_semestre()} con un promedio acumulado de {self.get_promedio_acumulado()}"
    