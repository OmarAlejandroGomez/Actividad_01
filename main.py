from controllers.persona_controller import PersonaController
from controllers.programa_controller import ProgramaController
from controllers.asignatura_controller import AsignaturaController


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


## main es la función principal, contiene el menú y las acciones correspondientes a cada opción
def main():
    programa_controller = ProgramaController()
    asignatura_controller = AsignaturaController()
    persona_controller = PersonaController()

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
        print("12. Ejecutar demostración")
        print("13. Salir\n")

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
                ejecutar_demostracion(programa_controller, asignatura_controller, persona_controller)

            case "13":
                print("Vuelve pronto")
                break

            case _:
                print("Opción inválida")


if __name__ == "__main__":
    main()
