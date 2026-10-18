from models.persona import Persona

class Docente(Persona):

    contador = 0

    def __init__(self, identificacion, nombre, correo, facultad, tipo_contratacion, horas_semanales):
        super().__init__(identificacion, nombre, correo)
        self.set_facultad(facultad)
        self.set_tipo_contratacion(tipo_contratacion)
        self.set_horas_semanales(horas_semanales)
        
        #dejar el número de empleado para no ser solicitado en la creación del docente, sino que se asignará automáticamente
        Docente.contador += 1
        self._numero_empleado = f"Docente-{Docente.contador:03d}"

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

    # Tipo de contratación

    def get_tipo_contratacion(self):
        return self._tipo_contratacion

    def set_tipo_contratacion(self, tipo_contratacion):
        if(tipo_contratacion.strip() != ""):
            self._tipo_contratacion = tipo_contratacion.strip()
        else: 
            raise ValueError("El tipo de contratación no puede ser vacía")

    # Horas semanales
    def get_horas_semanales(self):
        return self._horas_semanales

    def set_horas_semanales(self, horas_semanales):
        if(horas_semanales > 0):
            self._horas_semanales = horas_semanales
        else: 
            raise ValueError("Las horas semanales deben ser mayores a cero")

    
    # Mostrar información, los datos de personas y los datos de docente            
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} - Número de Empleado: {self.get_numero_empleado()}, - Facultad: {self.get_facultad()}, Tipo de Contratación: {self.get_tipo_contratacion()}, Horas Semanales: {self.get_horas_semanales()}"

    # Actividad del docente

    def realizar_actividad_principal(self):
        return f"El docente {self.get_nombre()} está realizando su actividad principal de docencia en la facultad de {self.get_facultad()} con un contrato de {self.get_tipo_contratacion()} y trabajando {self.get_horas_semanales()} horas semanales."