"""
Explicación del Uso de Estructuras de Datos:

1. Listas (estudiantes):
   - Propósito: Almacenar la colección principal de todos los estudiantes.
   - Razón: Las listas en Python son ordenadas y mutables, lo que permite agregar, eliminar y modificar
     estudiantes fácilmente. Son ideales para mantener una secuencia de elementos (en este caso, diccionarios
     de estudiantes) a los que se puede acceder por índice si fuera necesario, aunque la búsqueda principal
     se realiza por carné o nombre.

2. Diccionarios (para cada estudiante):
   - Propósito: Representar la información detallada de cada estudiante de forma estructurada.
   - Razón: Los diccionarios utilizan pares clave-valor, lo que es perfecto para modelar objetos con atributos
     específicos como 'Nombre', 'Carné', 'Materias' y 'Promedio'. Permiten un acceso rápido y legible
     a los datos de un estudiante mediante sus claves.

3. Sets (carnes_unicos):
   - Propósito: Garantizar la unicidad de los carnés de los estudiantes y permitir una verificación rápida
     de existencia.
   - Razón: Los sets almacenan solo elementos únicos y ofrecen operaciones de búsqueda (como verificar si un
     carné ya existe) con una complejidad promedio de O(1), lo cual es mucho más eficiente que buscar
     en una lista, especialmente a medida que crece el número de estudiantes.

4. Tuplas (materias_disponibles_opciones):
   - Propósito: Almacenar una colección fija de opciones de materias que no cambiarán durante la ejecución del programa.
     En este caso, se usó una lista de tuplas donde cada tupla representa una materia con su nombre y un código (ej: ('Matemáticas', 'MAT101')).
     Aunque el requisito principal para las materias del estudiante es una lista de strings (nombres de materias),
     las tuplas se utilizan aquí para demostrar su uso en un contexto relacionado: definir un conjunto de datos inmutables
     que pueden ser usados para poblar la información de los estudiantes.
   - Razón: Las tuplas son inmutables, lo que significa que una vez creadas, no pueden ser modificadas.
     Esto las hace adecuadas para representar colecciones de datos que deben permanecer constantes,
     como configuraciones fijas o, en este caso, un catálogo de materias disponibles para la asignación inicial.
     También pueden usarse para devolver múltiples valores desde una función de forma compacta.
"""

import random

# Estructuras de datos principales
estudiantes = []  # Lista principal de diccionarios de estudiantes
carnes_unicos = set()  # Set para garantizar carnés únicos

# Contador para el número correlativo del carné (XXXXX)
# Se inicializa para cada año, pero necesitamos un contador global para el XXXXX parte
# Para simplificar, usaremos un único contador global para XXXXX que se reinicia conceptualmente
# o se gestiona por año. Aquí, para el auto-incremental XXXXX, lo haremos global.
siguiente_numero_correlativo = 1000

# Opciones para la población inicial (uso de tuplas)
# Cada tupla es (NombreMateria, CodigoMateria) - aunque solo usaremos NombreMateria para el estudiante
materias_disponibles_opciones = [
    ("Matemáticas Discretas", "MD001"),
    ("Programación I", "PRG101"),
    ("Cálculo I", "CAL101"),
    ("Física General", "FIS101"),
    ("Química General", "QUM101"),
    ("Introducción a la Ingeniería", "ING101"),
    ("Algoritmos y Estructuras de Datos", "AED201"),
    ("Bases de Datos I", "BD1201"),
    ("Sistemas Operativos", "SO301"),
    ("Redes de Computadoras", "RED301"),
    ("Inglés Técnico", "IT401"),
    ("Desarrollo Web", "WEB401")
]

nombres_ejemplo = [
    "Ana Pérez", "Luis García", "Sofía Rodríguez", "Carlos Martínez", "Laura Gómez",
    "Juan Hernández", "María López", "José Torres", "Patricia Sánchez", "David Ramírez",
    "Elena Flores", "Miguel Romero", "Carmen Ruiz", "Javier Vargas", "Isabel Castro"
]

def generar_carne(anio_inscripcion):
    """Genera un carné único para un estudiante."""
    global siguiente_numero_correlativo
    
    if not (20 <= anio_inscripcion <= 25):
        raise ValueError("El año de inscripción debe estar entre 20 y 25.")

    yy = str(anio_inscripcion).zfill(2)
    
    # Intentar generar un carné hasta encontrar uno único para el XXXXX correlativo
    # Esta implementación asume que el XXXXX es global y no se reinicia por año.
    # Si se quisiera reiniciar por año, la lógica de `siguiente_numero_correlativo` necesitaría ser más compleja (ej. un dict por año)
    while True:
        xxxxx = str(siguiente_numero_correlativo).zfill(5)
        carne = f"0905-{yy}-{xxxxx}"
        if carne not in carnes_unicos:
            siguiente_numero_correlativo += 1
            return carne
        # Si el carné ya existe (improbable con XXXXX incremental global, pero seguro tenerlo)
        # se incrementa el correlativo y se reintenta.
        siguiente_numero_correlativo += 1
        if siguiente_numero_correlativo > 99999: # Límite teórico para XXXXX
            # En un caso real, aquí se manejaría el agotamiento de números para un año
            # o se pasaría a una estrategia diferente.
            # Para este ejercicio, si se agotan los XXXXX para un año, se podría lanzar un error
            # o reiniciar el contador si la lógica de unicidad se maneja por año.
            # Como es global, este límite es muy alto.
            print("ADVERTENCIA: Se ha alcanzado el límite del número correlativo XXXXX.")
            # Podríamos optar por reiniciar si la lógica de unicidad por año fuera más estricta
            # siguiente_numero_correlativo = 1000 # Ejemplo si se quisiera reiniciar
            # O simplemente dejar que falle si no hay más carnés disponibles bajo el esquema actual.
            # Para este ejercicio, asumimos que no se agotará.
            pass # Continuar para ver si el siguiente intento funciona (poco probable que se alcance)

def agregar_estudiante(nombre, anio_inscripcion, materias, promedio):
    """Agrega un nuevo estudiante al sistema."""
    try:
        carne = generar_carne(anio_inscripcion)
        estudiante = {
            "Nombre": nombre,
            "Carné": carne,
            "Materias": materias,
            "Promedio": promedio
        }
        estudiantes.append(estudiante)
        carnes_unicos.add(carne)
        print(f"Estudiante {nombre} con carné {carne} agregado exitosamente.")
        return True
    except ValueError as e:
        print(f"Error al agregar estudiante: {e}")
        return False
    except Exception as e:
        print(f"Error inesperado al generar carné o agregar estudiante: {e}")
        return False

def eliminar_estudiante(carne_a_eliminar):
    """Elimina un estudiante del sistema por su carné."""
    global estudiantes
    estudiante_encontrado = None
    for est in estudiantes:
        if est["Carné"] == carne_a_eliminar:
            estudiante_encontrado = est
            break
    
    if estudiante_encontrado:
        estudiantes.remove(estudiante_encontrado)
        carnes_unicos.remove(carne_a_eliminar)
        print(f"Estudiante con carné {carne_a_eliminar} eliminado exitosamente.")
    else:
        print(f"Estudiante con carné {carne_a_eliminar} no encontrado.")

def buscar_estudiante(termino_busqueda):
    """Busca estudiantes por nombre (parcial/completo) o carné (exacto)."""
    resultados = []
    termino_busqueda_lower = termino_busqueda.lower()
    for est in estudiantes:
        # Búsqueda por carné (exacta)
        if est["Carné"] == termino_busqueda:
            resultados.append(est)
            continue # Si coincide por carné, es único, no seguir buscando en este estudiante
        # Búsqueda por nombre (parcial, insensible a mayúsculas)
        if termino_busqueda_lower in est["Nombre"].lower():
            resultados.append(est)
            
    if resultados:
        print(f"\n--- Resultados de la búsqueda para '{termino_busqueda}' ---")
        for i, est in enumerate(resultados):
            print(f"Estudiante #{i+1}")
            print(f"  Nombre: {est['Nombre']}")
            print(f"  Carné: {est['Carné']}")
            print(f"  Materias: {', '.join(est['Materias'])}")
            print(f"  Promedio: {est['Promedio']:.2f}")
            print("-" * 20)
    else:
        print(f"No se encontraron estudiantes que coincidan con '{termino_busqueda}'.")

def mostrar_promedio_superior(umbral):
    """Muestra estudiantes con promedio superior a un umbral dado."""
    resultados = []
    for est in estudiantes:
        if est["Promedio"] > umbral:
            resultados.append(est)
            
    if resultados:
        print(f"\n--- Estudiantes con promedio superior a {umbral:.2f} ---")
        for est in resultados:
            print(f"  Nombre: {est['Nombre']}, Carné: {est['Carné']}, Promedio: {est['Promedio']:.2f}")
        print("-" * 20)
    else:
        print(f"No hay estudiantes con promedio superior a {umbral:.2f}.")

def mostrar_materias_estudiante(carne_busqueda):
    """Muestra las materias de un estudiante específico por su carné."""
    estudiante_encontrado = None
    for est in estudiantes:
        if est["Carné"] == carne_busqueda:
            estudiante_encontrado = est
            break
            
    if estudiante_encontrado:
        print(f"\n--- Materias de {estudiante_encontrado['Nombre']} (Carné: {carne_busqueda}) ---")
        if estudiante_encontrado['Materias']:
            for materia in estudiante_encontrado['Materias']:
                print(f"  - {materia}")
        else:
            print("  Este estudiante no tiene materias inscritas.")
        print("-" * 20)
    else:
        print(f"Estudiante con carné {carne_busqueda} no encontrado.")

def calcular_promedio_general():
    """Calcula y muestra el promedio general de todos los estudiantes."""
    if not estudiantes:
        print("No hay estudiantes registrados para calcular el promedio general.")
        return
        
    suma_promedios = 0
    for est in estudiantes:
        suma_promedios += est["Promedio"]
        
    promedio_general = suma_promedios / len(estudiantes)
    print(f"\nEl promedio general de calificaciones de los {len(estudiantes)} estudiantes es: {promedio_general:.2f}")

def poblar_datos_iniciales():
    """Genera y agrega 30 estudiantes iniciales con datos variados."""
    print("\nPoblando datos iniciales...")
    
    for i in range(30):
        nombre = random.choice(nombres_ejemplo) + f" {chr(random.randint(65, 90))}." # Apellido aleatorio
        # Asegurar que el año de inscripción esté en el rango 20-25
        anio_inscripcion = random.randint(20, 25)
        
        # Seleccionar un número aleatorio de materias (entre 2 y 5)
        num_materias = random.randint(2, 5)
        materias_estudiante = random.sample([m[0] for m in materias_disponibles_opciones], num_materias)
        
        promedio = round(random.uniform(5.0, 10.0), 2)
        
        # Usar la función agregar_estudiante para asegurar la lógica de generación de carné y unicidad
        agregar_estudiante(nombre, anio_inscripcion, materias_estudiante, promedio)
    print("\nDatos iniciales poblados.")

def mostrar_menu():
    """Muestra el menú interactivo y maneja la entrada del usuario."""
    while True:
        print("\n--- Sistema de Gestión de Estudiantes ---")
        print("1. Agregar Estudiante")
        print("2. Eliminar Estudiante")
        print("3. Buscar Estudiante (por nombre o carné)")
        print("4. Mostrar Estudiantes con Promedio Superior a X")
        print("5. Mostrar Materias de un Estudiante")
        print("6. Calcular Promedio General de Calificaciones")
        print("7. Mostrar todos los estudiantes (para depuración)")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre completo del estudiante: ")
            while True:
                try:
                    anio_str = input("Año de inscripción (YY, ej. 20 para 2020, 25 para 2025): ")
                    anio = int(anio_str)
                    if not (20 <= anio <= 25):
                        print("Año inválido. Debe ser entre 20 y 25.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida para el año. Por favor, ingrese un número.")
            
            materias_str = input("Materias inscritas (separadas por coma): ")
            materias = [m.strip() for m in materias_str.split(',')]
            
            while True:
                try:
                    promedio_str = input("Promedio actual del estudiante: ")
                    promedio = float(promedio_str)
                    if not (0.0 <= promedio <= 10.0):
                         print("Promedio inválido. Debe ser entre 0.0 y 10.0.")
                         continue
                    break
                except ValueError:
                    print("Entrada inválida para el promedio. Por favor, ingrese un número.")
            agregar_estudiante(nombre, anio, materias, promedio)
            
        elif opcion == '2':
            carne = input("Carné del estudiante a eliminar (formato 0905-YY-XXXXX): ")
            eliminar_estudiante(carne)
            
        elif opcion == '3':
            termino = input("Ingrese nombre o carné a buscar: ")
            buscar_estudiante(termino)
            
        elif opcion == '4':
            while True:
                try:
                    umbral_str = input("Ingrese el umbral de promedio (ej. 8.0): ")
                    umbral = float(umbral_str)
                    break
                except ValueError:
                    print("Entrada inválida para el umbral. Por favor, ingrese un número.")
            mostrar_promedio_superior(umbral)
            
        elif opcion == '5':
            carne = input("Carné del estudiante para mostrar sus materias (formato 0905-YY-XXXXX): ")
            mostrar_materias_estudiante(carne)
            
        elif opcion == '6':
            calcular_promedio_general()

        elif opcion == '7': # Opción de depuración para ver todos los estudiantes
            if estudiantes:
                print("\n--- Lista Completa de Estudiantes ---")
                for i, est in enumerate(estudiantes):
                    print(f"Estudiante #{i+1}")
                    print(f"  Nombre: {est['Nombre']}")
                    print(f"  Carné: {est['Carné']}")
                    print(f"  Materias: {', '.join(est['Materias'])}")
                    print(f"  Promedio: {est['Promedio']:.2f}")
                    print("-" * 10)
            else:
                print("No hay estudiantes registrados.")
            
        elif opcion == '8':
            print("Saliendo del sistema. ¡Hasta luego!")
            # Imprimir la explicación de estructuras de datos al final (opcional)
            # print("\n" + __doc__)
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# --- Ejecución Principal ---
if __name__ == "__main__":
    # Poblar con datos iniciales al arrancar el programa
    poblar_datos_iniciales()
    
    # Mostrar el menú interactivo
    mostrar_menu()

    # Opcional: Mostrar la explicación de las estructuras de datos al final si no se hizo en la opción de salir.
    # print("\n" + """
    # Explicación del Uso de Estructuras de Datos:
    # ... (copiar el texto de la documentación aquí si se prefiere al final) ...
    # """)