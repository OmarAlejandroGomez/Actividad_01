# Actividad_01
# Universidad de Manizales - Asignatura: Programación I

# Integrantes:

Omar Alejandro Gómez Rocha

Juan Carlos Girón Sanabria

Cristhian Mauricio Hernández Gaviria

# Construcción de un Sistema de Gestión Académica 

Atendiendo las instrucciones de la actividad, se generó un sistema que organiza información básica de la comunidad académica de una universidad: programas académicos, asignaturas y personas (estudiantes, docentes y personal admininistrativo).

Inicialmente, a partir del análisis conjunto de las instrucciones de la actividad y los acuerdos alcanzados por los integrantes del grupo, se construyó el diagrama de clases, el cual se dispone en el presente repositorio. Tenga en cuenta que el diagrama fue construido en la herramienta web draw.io (con extensión .drawio), por lo que podrá abrirlo directamente en dicha plataforma.

Respecto del sistema, este funciona por medio de una consola que contiene un menú. También se incluye una opción de demostración.

# Estructura archivos

Actividad_01/

    |── README.md
    |── diagrama_clases_SistemaGestionAcademica.drawio  # Diagrama de clases UML (draw.io)
    |── main.py                                         # Archivo principal: menú y demostración
    ├── models/
        ├── persona.py                # Clase base Persona
        ├── estudiante.py             # Estudiante (hereda de Persona)
        ├── docente.py                # Docente (hereda de Persona)
        ├── administrativo.py         # Administrativo (hereda de Persona)
        ├── programa_academico.py     # ProgramaAcademico
        └── asignatura.py             # Asignatura (pertenece a un ProgramaAcademico)
    └── controllers/
        ├── persona_controller.py     # Colección única de personas (registro y búsqueda)
        ├── programa_controller.py    # Registro de programas académicos
        └── asignatura_controller.py  # Registro de asignaturas

# Principios utilizados: 

Clases, atributos, métodos, herencia, sobrescritura y polimorfismo.

Clases: persona (estudiante, docente, administrativo), programa académico, asignatura.

Atributos de las clases: 
- Para persona son: identificación, nombre y correo; 
- para estudiante son: código estudiantil, programa académico, semestre, promedio acumulado;
- para docente son: número de empleado, facultad, tipo de contratación, horas semanales;
- para administrativo son: número de empleado, dependencia, cargo, jornada
- Para asignatura son código, nombre, número de créditos, programa académico.
- Para programa académico son código, nombre, facultad, número de semestres.

Métodos: mostrar_información() y realizar_actividad_principal()

Herencia: Persona es la clase padre. Contiene los atributos comunes a toda persona vinculada (identificación, nombre y correo), sus métodos get_ y set_, y los métodos mostrar_informacion() y realizar_actividad_principal().

Estudiante, Docente y Administrativo son hijos: heredan de Persona y en su constructor llaman a super().__init__(identificacion, nombre, correo). Así reutilizan la inicialización y las validaciones comunes sin repetirlas.

Sobrescritura: Las tres clases hijas de persona utilizan super().mostrar_informacion() para llamar los datos generales de persona y les agrega datos particulares. 

Polimorfismo: En main.py todas las personas se guardan en una única colección y se recorren con un solo ciclo.

 # Instrucciones de ejecución

 Requisitos: Vs Code, Python. No requiere librerías externas.

    git clone https://github.com/OmarAlejandroGomez/Actividad_01.git
    cd Actividad_01
    python main.py

    Al ejecutar el programa, se muestra el siguiente menú: 

    1. Agregar programa académico
    2. Agregar asignatura
    3. Agregar estudiante
    4. Agregar docente
    5. Agregar administrativo
    6. Mostrar programas
    7. Mostrar asignaturas
    8. Mostrar personas
    9. Modificar correo de una persona
    10. Modificar semestres de un programa
    11. Modificar créditos de una asignatura
    12. Ejecutar demostración
    13. Salir

    Demostración: 

    La opción 12 permite validar lo siguiente: 

    1.Creación de dos programas académicos y dos asignaturas.
    2.Creación de seis personas: dos estudiantes, dos docentes y dos administrativos.
    3.Consulta de la información de los objetos.
    4.Modificación válida de datos encapsulados (correo de un estudiante y créditos de una asignatura).
    5.Intento de asignar valores inválidos
    6.Presentación particular de cada tipo de persona.
    7.Recorrido polimórfico de la colección de personas.

  # Uso IA

Las herramientas de IA se utilizaron en el siguiente proyecto para: 
    - la revisión del modelo 
    - la escritura del código (especialmente copilot integrado a VsCode en su función predictiva) 
    - la identificación de errores en el código 



