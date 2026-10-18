# Actividad_01
# Universidad de Manizales - Asignatura: Programación

Integrantes:
Omar Alejandro Gómez Rocha
Juan Carlos Girón Sanabria
Cristhian Mauricio Hernández Gaviria

Descripción: 

Atendiendo las instrucciones de la actividad, se generó un sistema que organiza información básica de la comunidad académica de una universidad: programas académicos, asignaturas y personas (estudiantes, docentes y personal admininistrativo).

Principios utilizados: 

Clases, atributos, métodos, herencia, sobrescritura y polimorfismo.

Clases: persona (estudiante, docente, administrativo), programa académico, asignatura.

Atributos: Para persona son , en el caso de los hijos, para estudiante son código estudiantil, programa académico, semestre, promedio acumulado; para docente son número de empleado, facultad, tipo de contratación, horas semanales; para administrativo son número de empleado, dependencia, cargo, jornada

Para asignatura son 

Para programa académico son 


Métodos: mostrar_información() y realizar_actividad_principal()

Herencia: Estudiante, docente y administrativo son hijos de persona.

Sobrescritura: A pesar de que estudiante, docente y administrativo son hijos, con super se le asignan atributos propios. 

Polimorfismo: En main.py todas las personas se guardan en una única colección y se recorren con un
solo ciclo:

for persona in personas.get_personas():
print(persona.mostrar_informacion())
print(persona.realizar_actividad_principal())

 # Instrucciones de ejecución

 Requisitos: Vs Code, Python 3.10 o superior. No requiere librerías externas.

    git clone https://github.com/OmarAlejandroGomez/Actividad_01.git
    
    Actividad_01
    python main.py

    El programa ejecuta automáticamente, en orden, las siete pruebas mínimas:

    1.Creación de programas académicos y asignaturas.
    2.Creación de seis personas (dos estudiantes, dos docentes y dos administrativos).
    3.Consulta de la información de los objetos.
    4.Modificación válida de datos encapsulados.
    5.Intento de asignar valores inválidos (el sistema los rechaza e informa el motivo).
    6.Presentación particular de cada tipo de persona.
    7.Recorrido polimórfico de la colección de personas.

  # Uso IA

    Las herramientas de IA se utilizaron así en el siguiente proyecto: para la revisión del modelo, para la escritura  del código (especialmente copilot integrado a Vs Code en su función predictiva), para la identificación de errores en el código. 



