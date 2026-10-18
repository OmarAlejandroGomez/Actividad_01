from models.persona import Persona

class Docente(Persona):

    def __init__(self, identificacion, nombre, correo, facultad, tipo_contratacion, horas_semanales):
        super().__init__(identificacion, nombre, correo)
        self.set_facultad(facultad)
        self.set_tipo_contratacion(tipo_contratacion)
        self.set_horas_semanales(horas_semanales)
        
        #dejar el número de empleado para no ser solicitado en la creación del docente, sino que se asignará automáticamente
        Docente.contador += 1
        self._numero_empleado = f"Docente-{Docente.contador:04d}"

    # Número de empleado
    def get_numero_empleado(self):
        return self._numero_empleado 

    # Facultad

    def get_facultad(self):
        return self._facultad

    def set_facultad(self, facultad):
        if(facultad.strip() != ""):
            self._facultad = facultad.strip()
        else: 
            raise ValueError("La facultad no puede ser vacía")


    # Título
    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        if(titulo.strip() != ""):
            self._titulo = titulo
        else: 
            raise ValueError("El título no puede ser vacío")
    
    # Mostrar información            
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} - Título: {self.get_titulo()}"