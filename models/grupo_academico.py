from models.horario import Horario

class GrupoAcademico:
    
    def __init__(self, codigo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_fin, salon):
        if(codigo.strip() != ""):
            self.codigo = codigo
        else:
            raise ValueError("El código del grupo no puede estar vacío")
        
        self.set_asignatura(asignatura)
        self.set_docente(docente)
        self.set_capacidad_maxima(capacidad_maxima)
        self._estudiantes = []  # Lista para almacenar los estudiantes inscritos en el grupo académico
        
        # Crear un objeto Horario para el grupo académico
        self._horario = Horario(dia, hora_inicio, hora_fin, salon)  
    
    # Código del grupo
    def get_codigo(self):
        return self.codigo
    
    # Asignatura ofrecida
    def get_asignatura(self):
        return self._asignatura
    
    def set_asignatura(self, asignatura):
        if(asignatura.strip() != ""):
            self._asignatura = asignatura
        else:
            raise ValueError("Debe indicar una asignatura existente")
    
    # Docente responsable
    def get_docente(self):
        return self._docente
    
    def set_docente(self, docente):
        if(docente.strip() != ""):
            self._docente = docente
        else:
            raise ValueError("Debe indicar un docente existente")
    
    # Capacidad máxima del grupo
    def get_capacidad_maxima(self): 
        return self._capacidad_maxima
    
    def set_capacidad_maxima(self, capacidad_maxima):
        if(capacidad_maxima > 0):
            if(capacidad_maxima < len(self._estudiantes)):
                raise ValueError("La capacidad máxima del grupo no puede ser menor al número de estudiantes inscritos")
            else:
                self._capacidad_maxima = capacidad_maxima
        else:
            raise ValueError("La capacidad máxima del grupo debe ser mayor a cero") 
    
     # Estudiantes matriculados
    def get_estudiantes(self):
        return self._estudiantes.copy()  # Copia de la lista para evitar modificaciones externas
    
    def get_cupos_disponibles(self):
        return self._capacidad_maxima - len(self._estudiantes)  
    
    # Horario
    def get_horario(self):
        return self._horario
    
    def mostrar_informacion_grupo(self):
        return (
            f"Código del grupo: {self.get_codigo} -"
            f"Asignatura: {self._asignatura.get_nombre()} ({self._asignatura.get_codigo()}) - "
            f"Docente: {self._docente.get_nombre()} - "
            f"Horario: {self._horario.mostrar_informacion()} - "
            f"Matriculados: {len(self._estudiantes)} - "
            f"Capacidad: {self._capacidad_maxima}"
        )
    
    def matricular_estudiante(self, estudiante):
        
        # verificar si el estudiante ya está matriculado en el grupo
        for matriculado in self._estudiantes:
            if(matriculado.get_codigo_estudiante() == estudiante.get_codigo_estudiante()):
                raise ValueError(f"El estudiante {estudiante.get_codigo_estudiante()} ya está matriculado en el grupo.")
        
        # agregar al estudiante al grupo si hay cupos disponibles          
        if len(self._estudiantes) < self._capacidad_maxima:
            self._estudiantes.append(estudiante)
        else:
            raise ValueError("No se puede matricular al estudiante. El grupo alcanzó su capacidad máxima.")
 
    def retirar_estudiante(self, codigo_estudiantil):
        for matriculado in self._estudiantes:
            if(matriculado.get_codigo_estudiantil() == codigo_estudiantil.strip()):
                self._estudiantes.remove(matriculado)
                return
        raise ValueError(f"El estudiante {codigo_estudiantil.strip()} no está matriculado en el grupo.")
    
    def mostrar_estudiantes(self):
        listado_estudiantes = []
        if len(self._estudiantes) == 0:
            return "No hay estudiantes matriculados en el grupo."
        else:
            for(estudiante in self._estudiantes):
                listado_estudiantes.append(
                    f"{estudiante.get_codigo_estudiantil()} - {estudiante.get_nombre()}"
                    f"({estudiante.get_programa_academico().get_nombre()}, semestre {estudiante.get_semestre()})"
                    )
            return "\n".join(listado_estudiantes)

