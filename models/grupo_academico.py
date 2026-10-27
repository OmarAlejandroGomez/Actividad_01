from models.horario import Horario

class GrupoAcademico:
    
    def __init__(self, codigo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_fin, salon):
        if(codigo.strip() != ""):
            self.codigo = codigo
        else:
            raise ValueError("El código del grupo académico no puede estar vacío")
        
        self.set_asignatura(asignatura)
        self.set_docente(docente)
        self.set_capacidad_maxima(capacidad_maxima)
        self._estudiantes = []  # Lista para almacenar los estudiantes inscritos en el grupo académico
        
        # Crear un objeto Horario para el grupo académico
        self._horario = Horario(dia, hora_inicio, hora_fin, salon)  
    
    # Código del grupo académico
    def get_codigo(self):
        return self.codigo
    
    # Asignatura del grupo académico
    def get_asignatura(self):
        return self._asignatura
    
    def set_asignatura(self, asignatura):
        if(asignatura.strip() != ""):
            self.get_asignatura = asignatura
        else:
            raise ValueError("Debe indicar una asignatura existente")
    
    # Docente del grupo académico
    def get_docente(self):
        return self._docente
    
    def set_docente(self, docente):
        if(docente.strip() != ""):
            self._docente = docente
        else:
            raise ValueError("Debe indicar un docente existente")
    
    # Capacidad máxima del grupo académico
    def get_capacidad_maxima(self): 
        return self._capacidad_maxima
    
    def set_capacidad_maxima(self, capacidad_maxima):
        if(capacidad_maxima > 0):
            if(capacidad_maxima < len(self._estudiantes)):
                raise ValueError("La capacidad máxima del grupo académico no puede ser menor al número de estudiantes inscritos")
            else:
                self._capacidad_maxima = capacidad_maxima
        else:
            raise ValueError("La capacidad máxima del grupo académico debe ser mayor a cero") 
    
    # Horario
    def get_horario(self):
        return self._horario
    
    # Estudiantes matriculados
    def get_estudiantes(self):
        return self._estudiantes.copy()  # Devolver una copia de la lista para evitar modificaciones externas
    
    def get_cupos_disponibles(self):
        return self._capacidad_maxima - len(self._estudiantes)  
    
    