from controllers.persona_controller import PersonaController
from controllers.programa_controller import ProgramaController
from controllers.asignatura_controller import AsignaturaController
from models.estudiante import Estudiante
from models.persona import Persona

## Para pedir datos al usuario

def elegir_de_lista(elementos, mensaje_vacio):
    """Muestra una lista numerada (programas o asignaturas) y devuelve el elemento elegido."""
    if len(elementos) == 0:
        print(mensaje_vacio)
        return None

    posicion = 1
    for elemento in elementos:
        print(f"{posicion}. {elemento.get_codigo()} - {elemento.get_nombre()}")
        posicion += 1

    while True:
        opcion = int(input("Elige el número de la lista: "))
        if opcion >= 1 and opcion <= len(elementos):
            return elementos[opcion - 1]
        print("Opción fuera de la lista")


## Funciones para agregar

def agregar_programa(programa_controller):
    """Pide los datos y repite si alguno es inválido, informando el motivo."""
    while True:
        codigo = input("Ingresa el código del programa: ")
        nombre = input("Ingresa el nombre del programa: ")
        facultad = input("Ingresa la facultad: ")
        numero_semestres = int(input("Ingresa el número de semestres: "))

        try:
            programa_controller.add_programa(codigo, nombre, facultad, numero_semestres)
            print("Programa agregado con éxito")
            return
        except ValueError as error:
            print(f"{error}. Intenta nuevamente.\n")


def agregar_asignatura(asignatura_controller, programa_controller):
    programa = elegir_de_lista(programa_controller.get_programas(),
                               "Primero debe registrar un programa académico")
    if programa is None:
        return

    while True:
        codigo = input("Ingresa el código de la asignatura: ")
        nombre = input("Ingresa el nombre de la asignatura: ")
        creditos = int(input("Ingresa el número de créditos: "))

        try:
            asignatura_controller.add_asignatura(codigo, nombre, creditos, programa)
            print("Asignatura agregada con éxito")
            return
        except ValueError as error:
            print(f"{error}. Intenta nuevamente.\n")


def agregar_estudiante(persona_controller, programa_controller):
    programa = elegir_de_lista(programa_controller.get_programas(),
                               "Primero debe registrar un programa académico")
    if programa is None:
        return

    while True:
        identificacion = input("Ingresa el número de identificación: ")
        nombre = input("Ingresa el nombre del estudiante: ")
        correo = input("Ingresa el correo electrónico: ")
        semestre = int(input("Ingresa el semestre: "))
        promedio = float(input("Ingresa el promedio acumulado (0 a 5): "))

        try:
            estudiante = persona_controller.add_estudiante(identificacion, nombre, correo, programa, semestre, promedio)
            print(f"Estudiante agregado con éxito. Código generado: {estudiante.get_codigo_estudiantil()}")
            return
        except ValueError as error:
            print(f"{error}. Intenta nuevamente.\n")


def agregar_docente(persona_controller):
    while True:
        identificacion = input("Ingresa el número de identificación: ")
        nombre = input("Ingresa el nombre del docente: ")
        correo = input("Ingresa el correo electrónico: ")
        facultad = input("Ingresa la facultad: ")
        tipo_contratacion = input("Ingresa el tipo de contratación: ")
        horas_semanales = int(input("Ingresa las horas semanales: "))

        try:
            docente = persona_controller.add_docente(identificacion, nombre, correo, facultad, tipo_contratacion, horas_semanales)
            print(f"Docente agregado con éxito. Número de empleado generado: {docente.get_numero_empleado()}")
            return
        except ValueError as error:
            print(f"{error}. Intenta nuevamente.\n")


def agregar_administrativo(persona_controller):
    while True:
        identificacion = input("Ingresa el número de identificación: ")
        nombre = input("Ingresa el nombre del administrativo: ")
        correo = input("Ingresa el correo electrónico: ")
        dependencia = input("Ingresa la dependencia: ")
        cargo = input("Ingresa el cargo: ")
        jornada = input("Ingresa la jornada: ")

        try:
            administrativo = persona_controller.add_administrativo(identificacion, nombre, correo, dependencia, cargo, jornada)
            print(f"Administrativo agregado con éxito. Número de empleado generado: {administrativo.get_numero_empleado()}")
            return
        except ValueError as error:
            print(f"{error}. Intenta nuevamente.\n")

## Incluir en grupo

def elegir_con_descripcion(elementos, descripciones, mensaje_vacio):

    """Muestra una lista numerada (programas o asignaturas) y devuelve el elemento elegido."""
    if len(elementos) == 0:
        print(mensaje_vacio)
        return None

    posicion = 1
    for descripcion in descripciones:
        print(f"{posicion}. {descripcion}")
        posicion += 1

    while True:
        opcion = int(input("Elige el número de la lista: "))
        if opcion >= 1 and opcion <= len(elementos):
            return elementos[opcion - 1]
        print("Opción fuera de la lista")

def elegir_docente(persona_controller):
    docentes = persona_controller.get_docentes()
    descripciones = [f"{docente.get_numero_empleado()} - {docente.get_nombre()}" for docente in docentes]
    return elegir_con_descripcion(docentes, descripciones, "Primero debe registrar un docente")

def elegir_grupo(grupo_controller):
    grupos = grupo_controller.get_grupos()
    descripciones = [grupo.mostrar_informacion_grupo() for grupo in grupos]
    return elegir_con_descripcion(grupos, descripciones, "Primero debe registrar un grupo académico")            

def agregar_grupo(grupo_controller, asignatura_controller, persona_controller):
    codigo_asignatura = input("Ingresa el código de la asignatura: ")
    
    asignatura = asignatura_controller.buscar_asignatura(codigo_asignatura)
    if asignatura is None:
        print("No existe una asignatura con ese código")
        return

    docente = elegir_docente(persona_controller)
    if docente is None:
        return

    while True:
        codigo = input("Ingresa el código del grupo: ")
        capacidad_maxima = int(input("Ingresa la capacidad máxima del grupo: "))
        dia = input("Ingresa el día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes): ")
        hora_inicio = input("Ingresa la hora de inicio (HH:MM): ")
        hora_fin = input("Ingresa la hora de fin (HH:MM): ")
        salon = input("Ingresa el salón: ")

        try:
            grupo_controller.add_grupo(codigo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_fin, salon)
            print("Grupo agregado con éxito")
            return
        except ValueError as error:
            print(f"{error}. Intenta nuevamente.\n")

#def retirar_de_grupo(grupo_controller):


## Funciones para mostrar

def mostrar_programas(programa_controller):
    programas = programa_controller.get_programas()

    if not programas:
        print("No existen programas registrados")
        return

    for programa in programas:
        print(programa.mostrar_informacion())


def mostrar_asignaturas(asignatura_controller):
    asignaturas = asignatura_controller.get_asignaturas()

    if not asignaturas:
        print("No existen asignaturas registradas")
        return

    for asignatura in asignaturas:
        print(asignatura.mostrar_informacion())


def mostrar_personas(persona_controller):
    """Un solo ciclo recorre todas las personas; cada objeto ejecuta SU versión de los métodos."""
    personas = persona_controller.get_personas()

    if not personas:
        print("No existen personas registradas")
        return

    for persona in personas:
        print(persona.mostrar_informacion())
        print("   Actividad: " + persona.realizar_actividad_principal())
        print()


## Funciones para modificar (los setters rechazan los valores inválidos)

def modificar_correo(persona_controller):
    identificacion = input("Ingresa la identificación de la persona: ")
    persona = persona_controller.buscar_persona(identificacion)

    if persona is None:
        print("No existe una persona con esa identificación")
        return

    nuevo_correo = input("Ingresa el nuevo correo electrónico: ")
    try:
        persona.set_correo(nuevo_correo)
        print("Correo actualizado con éxito")
    except ValueError as error:
        print(f"No se pudo modificar: {error}")


def modificar_semestres(programa_controller):
    programa = elegir_de_lista(programa_controller.get_programas(),
                               "No existen programas registrados")
    if programa is None:
        return

    nuevo_numero = int(input("Ingresa el nuevo número de semestres: "))
    try:
        programa.set_numero_semestres(nuevo_numero)
        print("Número de semestres actualizado con éxito")
    except ValueError as error:
        print(f"No se pudo modificar: {error}")


def modificar_creditos(asignatura_controller):
    asignatura = elegir_de_lista(asignatura_controller.get_asignaturas(),
                                 "No existen asignaturas registradas")
    if asignatura is None:
        return

    nuevos_creditos = int(input("Ingresa el nuevo número de créditos: "))
    try:
        asignatura.set_creditos(nuevos_creditos)
        print("Créditos actualizados con éxito")
    except ValueError as error:
        print(f"No se pudo modificar: {error}")


## Demostración automática 

def ejecutar_demostracion(programa_controller, asignatura_controller, persona_controller):
    if persona_controller.buscar_persona("1001") is not None:
        print("La demostración ya se ejecutó")
        return

    print("\n1) Creación de programas y asignaturas")
    sistemas = programa_controller.add_programa("ISIS", "Ingeniería de Sistemas", "Ciencias e Ingenierías", 10)
    derecho = programa_controller.add_programa("DER", "Derecho", "Ciencias Jurídicas", 10)
    programacion = asignatura_controller.add_asignatura("PRG1", "Programación I", 3, sistemas)
    asignatura_controller.add_asignatura("DC01", "Derecho Civil", 4, derecho)
    mostrar_programas(programa_controller)
    mostrar_asignaturas(asignatura_controller)

    print("\n2) Creación de seis personas")
    persona_controller.add_estudiante("1001", "Ana Ruiz", "ana@correo.com", sistemas, 3, 4.2)
    persona_controller.add_estudiante("1002", "Luis Gómez", "luis@correo.com", derecho, 5, 3.8)
    persona_controller.add_docente("2001", "Marta Díaz", "marta@correo.com", "Ciencias e Ingenierías", "Tiempo completo", 40)
    persona_controller.add_docente("2002", "Jorge Pardo", "jorge@correo.com", "Ciencias Jurídicas", "Cátedra", 12)
    persona_controller.add_administrativo("3001", "Sofía León", "sofia@correo.com", "Registro Académico", "Coordinadora", "Mañana")
    persona_controller.add_administrativo("3002", "Carlos Mora", "carlos@correo.com", "Tesorería", "Auxiliar", "Tarde")
    print("Se crearon 2 estudiantes, 2 docentes y 2 administrativos")

    print("\n3) Modificaciones válidas")
    ana = persona_controller.buscar_persona("1001")
    ana.set_correo("ana.ruiz@correo.com")
    programacion.set_creditos(4)
    print(ana.mostrar_informacion())
    print(programacion.mostrar_informacion())

    print("\n4) Intentos de asignar valores inválidos")
    try:
        ana.set_correo("")
    except ValueError as error:
        print(f"Rechazado: {error}")

    try:
        sistemas.set_numero_semestres(0)
    except ValueError as error:
        print(f"Rechazado: {error}")

    try:
        programacion.set_creditos(-2)
    except ValueError as error:
        print(f"Rechazado: {error}")

    try:
        persona_controller.add_docente("1001", "Pedro", "pedro@correo.com", "Ciencias", "Planta", 20)
    except ValueError as error:
        print(f"Rechazado: {error}")

    print("\n5) Presentación particular de cada tipo de persona")
    mostrar_personas(persona_controller)





    # ---------------- Pruebas Actividad Colaborativa N° 2 ----------------

    print("\n6) Intento de crear directamente una Persona (clase abstracta)")
    try:
        Persona("9999", "Sin Tipo", "sintipo@correo.com")
    except TypeError as error:
        print(f"Rechazado: no se puede crear una Persona directamente ({error})")

    print("\n7) Creación de estudiantes adicionales")
    persona_controller.add_estudiante("1003", "Camila Torres", "camila@correo.com", sistemas, 2, 4.5)
    persona_controller.add_estudiante("1004", "Diego Ríos", "diego@correo.com", sistemas, 4, 3.5)
    ana = persona_controller.buscar_persona("1001")
    luis = persona_controller.buscar_persona("1002")
    camila = persona_controller.buscar_persona("1003")
    diego = persona_controller.buscar_persona("1004")
    marta = persona_controller.buscar_persona("2001")
    jorge = persona_controller.buscar_persona("2002")
    derecho_civil = asignatura_controller.buscar_asignatura("DC01")
    print("Se crearon 2 estudiantes adicionales")

    print("\n8) Creación de dos grupos académicos (cada grupo crea su horario)")
    grupo1 = grupo_controller.add_grupo("G01", programacion, marta, 2, "Lunes", "08:00", "10:00", "Salón 201")
    grupo2 = grupo_controller.add_grupo("G02", derecho_civil, jorge, 30, "Miércoles", "14:00", "16:00", "Salón 305")
    print(grupo1.mostrar_informacion_grupo())
    print(grupo2.mostrar_informacion_grupo())

    print("\n9) Matrícula correcta de estudiantes")
    grupo1.matricular_estudiante(ana)
    grupo1.matricular_estudiante(camila)
    grupo2.matricular_estudiante(luis)
    print(grupo1.mostrar_estudiantes())

    print("\n10) Intento de matricular un estudiante duplicado")
    try:
        grupo2.matricular_estudiante(luis)
    except EstudianteYaMatriculadoError as error:
        print(f"Error controlado: {error}")

    print("\n11) Intento de superar la capacidad del grupo")
    try:
        grupo1.matricular_estudiante(diego)
    except CapacidadMaximaError as error:
        print(f"Error controlado: {error}")

    print("\n12) Retiro correcto de un estudiante")
    grupo1.retirar_estudiante(camila.get_codigo_estudiantil())
    print(f"Se retiró a {camila.get_nombre()}. Estudiantes del grupo {grupo1.get_codigo()}:")
    print(grupo1.mostrar_estudiantes())

    print("\n13) Intento de retirar un estudiante que no está matriculado")
    try:
        grupo1.retirar_estudiante("EST-999")
    except EstudianteNoMatriculadoError as error:
        print(f"Error controlado: {error}")

    print("\n14) Búsqueda de una asignatura inexistente")
    try:
        asignatura_controller.buscar_asignatura("XXX1")
    except AsignaturaNoEncontradaError as error:
        print(f"Error controlado: {error}")

    print("\n15) Búsqueda de un programa inexistente")
    try:
        programa_controller.buscar_programa("MED")
    except ProgramaNoEncontradoError as error:
        print(f"Error controlado: {error}")

    print("\n16) El programa continúa su ejecución después de controlar cada excepción")
    mostrar_grupos(grupo_controller)

## main es la función principal, contiene el menú y las acciones correspondientes a cada opción
def main():
    programa_controller = ProgramaController()
    asignatura_controller = AsignaturaController()
    persona_controller = PersonaController()
    grupo_controller = GrupoController()

    while True:
        print("\n Opciones")
        print("1. Agregar programa académico")
        print("2. Agregar asignatura")
        print("3. Agregar estudiante")
        print("4. Agregar docente")
        print("5. Agregar administrativo")
        print("6. Mostrar programas")
        print("7. Mostrar asignaturas")
        print("8. Mostrar personas")
        print("9. Modificar correo de una persona")
        print("10. Modificar semestres de un programa")
        print("11. Modificar créditos de una asignatura")
        print("12. Agregar grupo académico")
        print("13. Matricular estudiante en un grupo")
        print("14. Retirar estudiante de un grupo")
        print("15. Mostrar grupos y estudiantes")
        print("16. Buscar asignatura por código")
        print("17. Buscar programa por código")
        print("18. Ejecutar demostración")
        print("19. Salir\n")

        option = input("Selecciona una opción: ")

        match option:
            case "1":
                agregar_programa(programa_controller)

            case "2":
                agregar_asignatura(asignatura_controller, programa_controller)

            case "3":
                agregar_estudiante(persona_controller, programa_controller)

            case "4":
                agregar_docente(persona_controller)

            case "5":
                agregar_administrativo(persona_controller)

            case "6":
                mostrar_programas(programa_controller)

            case "7":
                mostrar_asignaturas(asignatura_controller)

            case "8":
                mostrar_personas(persona_controller)

            case "9":
                modificar_correo(persona_controller)

            case "10":
                modificar_semestres(programa_controller)

            case "11":
                modificar_creditos(asignatura_controller)

            case "12":
                agregar_grupo(grupo_controller, asignatura_controller, persona_controller)

            case "13":
                matricular_en_grupo(grupo_controller, persona_controller)

            case "14":
                retirar_de_grupo(grupo_controller)

            case "15":
                mostrar_grupos(grupo_controller)

            case "16":
                buscar_asignatura(asignatura_controller)

            case "17":
                buscar_programa(programa_controller)

            case "18":
                ejecutar_demostracion(programa_controller, asignatura_controller, persona_controller, grupo_controller)

            case "19":
                print("Vuelve pronto")
                break

            case "20":
                print("Opción inválida")


if __name__ == "__main__":
    main()
