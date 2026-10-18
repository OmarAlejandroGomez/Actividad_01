class Asignatura:

    def __init__(self, codigo, nombre, creditos, programa_academico):
        if codigo.strip() != "":
            self._codigo = codigo.strip()
        else:
            raise ValueError("El código de la asignatura no puede ser vacío")
            
        self.set_nombre(nombre)
        self.set_creditos(creditos)
        self.set_programa_academico(programa_academico)

    # Código de la asignatura
    def get_codigo(self):
        return self._codigo

    # Nombre de la asignatura
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if nombre.strip() != "":
            self._nombre = nombre.strip()
        else:
            raise ValueError("El nombre de la asignatura no puede ser vacío")

    # Créditos de la asignatura
    def get_creditos(self):
        return self._creditos   

    def set_creditos(self, creditos):
        if creditos > 0:
            self._creditos = creditos
        else:
            raise ValueError("Los créditos de la asignatura deben ser mayores a cero")

    # Programa académico de la asignatura
    def get_programa_academico(self):
        return self._programa_academico 

    def set_programa_academico(self, programa_academico):
        if (programa_academico is not None):
            self._programa_academico = programa_academico
        else:
            raise ValueError("Debe indicar un programa académico")

    # Mostrar información de la asignatura
    def mostrar_informacion(self):
        return f"Código: {self.get_codigo()}, Nombre: {self.get_nombre()}, Créditos: {self.get_creditos()}, Programa Académico: {self.get_programa_academico().get_nombre()}"