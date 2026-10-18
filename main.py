from controllers.persona_controller import PersonaController


def agregar_persona(persona_controller):
    
    while True:
        identificacion = input("Ingresa el número de identificación: ")
        nombre = input("Ingresa el nombre de la persona: ")
        correo = input("Ingresa el correo electrónico: ")

        try:
            persona_controller.add_personas(identificacion, nombre, correo)
            print("Persona agregada con éxito")
            return
        except ValueError as error:
            print(f"{error}. Intenta nuevamente.\n")


def mostrar_personas(persona_controller):
    personas = persona_controller.get_personas()

    if not personas:
        print("No existen personas registradas")
        return

    for persona in personas:
        print(persona.mostrar_informacion())


##--------------------------------------------------------
## main es la función principal, contiene el menú y las acciones correspondientes a cada opción
def main():
    persona_controller = PersonaController()

    while True:
        print("\n Opciones")
        print("1. Agrega persona")
        print("2. Muestra personas")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                agregar_persona(persona_controller)

            case "2":
                mostrar_personas(persona_controller)

            case "3":
                print("Saliste del programa")
                break

            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()
 