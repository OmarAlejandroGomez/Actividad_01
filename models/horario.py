import datetime

class Horario:
    def __init__(self, dia, hora_inicio, hora_fin, salon):
        self.set_dia(dia)
        self.set_rago_horas(hora_inicio, hora_fin)
        self.set_salon(salon)
        
    # Día
    def get_dia(self):
        return self._dia
    
    def set_dia(self, dia):
        if dia.strip() != "":
            self._dia = dia.strip()
        else:
            raise ValueError("El día no puede estar vacío")
    
    # Rango de horas, formato "HH:MM"
    def get_hora_inicio(self):
        return self._hora_inicio
    
    def get_hora_fin(self):
        return self._hora_fin 
    
    def convertir_hora(self, hora_str):
        try:
            return datetime.strptime(hora_str.strip(), "%H:%M").time()
        except ValueError:
            raise ValueError("El formato de la hora debe ser HH:MM, por ejemplo 14:30")
    
    def set_rago_horas(self, hora_inicio, hora_fin):
        inicio = self.convertir_hora(hora_inicio)
        fin = self.convertir_hora(hora_fin)
        if(inicio < fin):
            self._hora_inicio = inicio
            self._hora_fin = fin
        else:
            raise ValueError("La hora de inicio debe ser menor que la hora de fin")
    
    # Salón
    def get_salon(self):
        return self._salon
    
    def set_salon(self, salon):
        if(salon.strip() != ""):
            self._salon = salon.strip()
        else:
            raise ValueError("El salón no puede estar vacío")
    
    def mostrar_informacion(self):
        return (
            f"Día: {self.get_dia()}, Hora de inicio: {self.get_hora_inicio().strftime('%H:%M')} "
            f" Hora de fin: {self.get_hora_fin().strftime('%H:%M')}, Salón: {self.get_salon()}"
        )