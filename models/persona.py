class Persona():

    def __init__(self, identificacion, nombre, correo):
        if(identificacion.strip() != ""):
            self._identificacion = identificacion.strip()
        else:
            raise ValueError("La identificación no puede estar vacía")
        self.set_nombre(nombre)
        self.set_correo(correo)
   
    # Identificación
    def get_identificacion(self):
        return self._identificacion

    # Nombre
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if(nombre.strip() != ""):
            self._nombre = nombre
        else: 
            raise ValueError("El nombre no puede ser vacío")
    
    # Correo electrónico            
    def get_correo(self):
        return self._correo

    def set_correo(self, correo):
        if(correo.strip() != ""):
            self._correo = correo
        else: 
            raise ValueError("El correo electrónico no puede estar vacío")
    
    # Mostrar información            
    def mostrar_informacion(self):
        return f"Identificación: {self.get_identificacion()} - Nombre: {self.get_nombre()} - Email: {self.get_correo()}"