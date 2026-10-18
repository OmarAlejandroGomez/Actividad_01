class ProgramaAcademico():

    def __init__(self, codigo, nombre, facultad, numero_semetsres):
        if codigo.strip() != "":
            self.codigo = codigo.strip()
        else:
            raise ValueError("El código del programa académico no puede ser vacío")
            
        self.set_nombre(nombre)
        self.set_facultad(facultad)
        self.set_numero_semestres(numero_semetsres)


    # Código del programa académico
    def get_codigo(self):
        return self.codigo

    # Nombre del programa académico
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if nombre.strip() != "":
            self._nombre = nombre.strip()
        else:
            raise ValueError("El nombre del programa académico no puede ser vacío")

    # Facultad del programa académico
    def get_facultad(self):
        return self._facultad

    def set_facultad(self, facultad):
        if facultad.strip() != "":
            self._facultad = facultad.strip()
        else:
            raise ValueError("La facultad del programa académico no puede ser vacía")

    # Número de semestres del programa académico
    def get_numero_semestres(self):
        return self._numero_semestres

    def set_numero_semestres(self, numero_semestres):
        if numero_semestres > 0:
            self._numero_semestres = numero_semestres
        else:
            raise ValueError("El número de semestres del programa académico debe ser mayor a cero")


    # Mostrar información del programa académico
    def mostrar_informacion(self):
        return f"Código: {self.get_codigo()}, Nombre: {self.get_nombre()}, Facultad: {self.get_facultad()}, Número de Semestres: {self.get_numero_semestres()}"