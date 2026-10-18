from models.persona import Persona

class Administrativo(Persona):
    
    contador = 0
    
    def __init__(self, identificacion, nombre, correo, dependencia, cargo, jornada):
        super().__init__(identificacion, nombre, correo)
        self.set_dependencia(dependencia)
        self.set_cargo(cargo)
        self.set_jornada(jornada)
        
        #el número de empleado es un autonumérico, no se solicita al usuario
        Administrativo.contador += 1
        self._numero_empleado = f"ADM-{Administrativo.contador:03d}"
        
    def get_numero_empleado(self):
        return self._numero_empleado
    
    # Dependencia
    def get_dependencia(self):
        return self._dependencia
    
    def set_dependencia(self, dependencia):
        if(dependencia.strip() != "")
            self._dependencia = dependencia
        else:
            raise ValueError("La dependencia no puede esta vacía")
        
    # Cargo
    def get_cargo(self):
        return self._cargo
    
    def set_cargo(self, cargo):
        if(cargo.strip() != "")
            self._cargo = cargo
        else:
            raise ValueError("El cargo no puede estar vacío")
        
    # Jornada
    def get_jornada(self):
        return self._jornada
    
    def set_jornada(self, jornada):
        if(jornada.strip() != ""):
            self._jornada = jornada
        else:
            raise ValueError("La jornada no puede estar vacía")
    
    def mostrar_informacion(self):
        return super().mostrar_informacion()
    
    
    
    