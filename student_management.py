# Sistema de Gestión de Estudiantes
# Este programa permite gestionar la información de estudiantes utilizando diversas estructuras de datos de Python.

# --- Documentación de Estructuras de Datos Utilizadas ---
# - lista_estudiantes (list): Se utiliza una lista para almacenar a todos los estudiantes.
#   Las listas son colecciones ordenadas y mutables, lo que permite agregar, eliminar y acceder
#   a los estudiantes por su índice si fuera necesario, y mantener un orden de inserción.
#
# - set_carnes (set): Se utiliza un set para almacenar todos los carnés de los estudiantes existentes.
#   Los sets son colecciones desordenadas de elementos únicos. Esto es ideal para:
#     1. Asegurar que no se ingresen carnés duplicados (eficiencia en la verificación de unicidad).
#     2. Realizar búsquedas rápidas para comprobar si un carné ya existe (operación O(1) en promedio).
#
# - Estructura de cada estudiante (dict): Cada estudiante se representa como un diccionario.
#   Los diccionarios permiten almacenar datos de forma estructurada mediante pares clave-valor.
#   Esto facilita el acceso a los atributos específicos de un estudiante (nombre, carné, etc.)
#   de manera legible y directa.
#   Ejemplo: {'nombre': 'Ana', 'carne': '0905-23-1234', ...}
#
# - Materias inscritas (list de tuplas): Dentro del diccionario de cada estudiante, la clave 'materias'
#   almacena una lista de tuplas. Cada tupla representa una materia.
#   Ejemplo: [('Programación I', 4), ('Matemática Discreta', 3)]
#   Se usan tuplas para cada materia ('nombre_materia', creditos_materia) porque las tuplas son inmutables.
#   Esto significa que una vez que se define el nombre y los créditos de una materia inscrita,
#   estos no deberían cambiar accidentalmente para esa inscripción específica.

import random

# Lista principal para almacenar estudiantes
lista_estudiantes = []

# Set para almacenar carnés únicos
set_carnes = set()

# Función para agregar un estudiante
# Solicita al usuario los datos del nuevo estudiante y verifica que el carné no exista previamente.
def agregar_estudiante(lista_estudiantes_local, set_carnes_local):
    nombre = input("Ingrese el nombre del estudiante: ")
    while True:
        carne = input("Ingrese el carné del estudiante (formato '0905-YY-xxxx', ej: 0905-24-1234): ")
        # Validación básica del formato (se podría mejorar con regex)
        parts = carne.split('-')
        if len(parts) == 3 and parts[0] == "0905" and len(parts[1]) == 2 and parts[1].isdigit() and len(parts[2]) == 4 and parts[2].isdigit():
            break
        else:
            print("Formato de carné incorrecto. Debe ser '0905-YY-xxxx'. Intente de nuevo.")

    if carne in set_carnes_local:
        print("Error: El carné ya existe.")
        return

    materias = []
    try:
        num_materias = int(input("Ingrese el número de materias: "))
        if num_materias < 0:
            print("El número de materias no puede ser negativo.")
            return
        for i in range(num_materias):
            print(f"--- Materia {i+1} ---")
            nombre_materia = input(f"Ingrese el nombre de la materia {i+1}: ")
            while True:
                try:
                    creditos_materia = int(input(f"Ingrese los créditos de la materia {i+1} (ej: 3): "))
                    if creditos_materia > 0:
                        break
                    else:
                        print("Los créditos deben ser un número positivo.")
                except ValueError:
                    print("Entrada inválida para créditos. Por favor ingrese un número.")
            materias.append((nombre_materia, creditos_materia))
    except ValueError:
        print("Entrada inválida para el número de materias. Por favor ingrese un número.")
        return

    while True:
        try:
            promedio = float(input("Ingrese el promedio del estudiante (ej: 7.5): "))
            if 0.0 <= promedio <= 10.0: # Asumiendo una escala de 0 a 10
                 break
            else:
                print("El promedio debe estar entre 0.0 y 10.0.")
        except ValueError:
            print("Entrada inválida para el promedio. Por favor ingrese un número.")


    estudiante = {'nombre': nombre, 'carne': carne, 'materias': materias, 'promedio': promedio}
    lista_estudiantes_local.append(estudiante)
    set_carnes_local.add(carne)
    print("Estudiante agregado exitosamente.")

# Función para eliminar un estudiante
def eliminar_estudiante(lista_estudiantes_local, set_carnes_local, carne_a_eliminar):
    estudiante_encontrado = None
    for estudiante in lista_estudiantes_local:
        if estudiante['carne'] == carne_a_eliminar:
            estudiante_encontrado = estudiante
            break # Optimización: salir del bucle una vez encontrado

    if estudiante_encontrado:
        lista_estudiantes_local.remove(estudiante_encontrado)
        set_carnes_local.remove(carne_a_eliminar) # Asumimos que si está en la lista, está en el set
        print("Estudiante eliminado exitosamente.")
    else:
        print("Error: Estudiante no encontrado.")


# Función para buscar un estudiante
def buscar_estudiante(lista_estudiantes_local, criterio, valor_busqueda):
    resultados = []
    valor_busqueda_lower = valor_busqueda.lower() # Para búsqueda insensible a mayúsculas

    for estudiante in lista_estudiantes_local:
        if criterio == 'nombre' and valor_busqueda_lower in estudiante['nombre'].lower():
            resultados.append(estudiante)
        elif criterio == 'carne' and estudiante['carne'] == valor_busqueda: # El carné es único, búsqueda exacta
            resultados.append(estudiante)
            break # Si se busca por carné y se encuentra, no hay necesidad de seguir buscando

    if resultados:
        print("\n--- Resultados de la Búsqueda ---")
        for estudiante in resultados:
            print(f"Nombre: {estudiante['nombre']}, Carné: {estudiante['carne']}, Promedio: {estudiante['promedio']}")
            print("  Materias:")
            for materia, creditos in estudiante['materias']:
                print(f"    - {materia} ({creditos} créditos)")
            print("-" * 20)
    else:
        print("No se encontraron estudiantes que coincidan con el criterio de búsqueda.")

# Función para mostrar estudiantes con promedio superior a un valor dado
def mostrar_estudiantes_promedio_superior(lista_estudiantes_local, promedio_minimo):
    encontrados = False
    print(f"\n--- Estudiantes con Promedio Superior a {promedio_minimo} ---")
    for estudiante in lista_estudiantes_local:
        if estudiante['promedio'] > promedio_minimo:
            print(f"Nombre: {estudiante['nombre']}, Carné: {estudiante['carne']}, Promedio: {estudiante['promedio']}")
            encontrados = True
    if not encontrados:
        print(f"No hay estudiantes con promedio superior a {promedio_minimo}.")

# Función para mostrar materias de un estudiante
def mostrar_materias_estudiante(lista_estudiantes_local, carne_estudiante):
    for estudiante in lista_estudiantes_local:
        if estudiante['carne'] == carne_estudiante:
            print(f"\n--- Materias de {estudiante['nombre']} (Carné: {estudiante['carne']}) ---")
            if estudiante['materias']:
                for materia, creditos in estudiante['materias']:
                    print(f"- {materia} ({creditos} créditos)")
            else:
                print("Este estudiante no tiene materias inscritas.")
            return
    print("Error: Estudiante no encontrado.")

# Función para calcular el promedio general del grupo
def calcular_promedio_general_grupo(lista_estudiantes_local):
    if not lista_estudiantes_local:
        print("No hay estudiantes en la lista para calcular el promedio general.")
        return
    suma_promedios = sum(estudiante['promedio'] for estudiante in lista_estudiantes_local)
    promedio_general = suma_promedios / len(lista_estudiantes_local)
    print(f"El promedio general del grupo es: {promedio_general:.2f}")


# --- Población Inicial de Datos ---
# Generar y agregar automáticamente 30 estudiantes de ejemplo
def poblar_datos_iniciales(num_estudiantes=30):
    print(f"Generando {num_estudiantes} estudiantes de ejemplo...")
    nombres_base = ["Ana", "Juan", "María", "Carlos", "Laura", "Luis", "Sofía", "David", "Elena", "Miguel", "Valentina", "Diego", "Camila", "Andrés", "Isabella"]
    apellidos = ["Pérez", "López", "García", "Sánchez", "Fernández", "Rodríguez", "Martínez", "Gómez", "Jiménez", "Hernández", "Díaz", "Ruiz", "Álvarez", "Moreno", "Romero"]
    nombres_materias_posibles = ["Programación", "Cálculo", "Física", "Química", "Historia", "Literatura", "Álgebra Lineal", "Estadística Aplicada", "Bases de Datos", "Redes de Computadoras", "Inglés Técnico", "Metodología de Investigación"]
    sufijos_materias = ["I", "II", "Avanzada", "Fundamental"]

    for _ in range(num_estudiantes):
        nombre_completo = f"{random.choice(nombres_base)} {random.choice(apellidos)} {random.choice(apellidos)}"

        # Generar carné en formato 0905-YY-xxxx
        yy = random.randint(18, 25) # Para años entre 2018 y 2025
        xxxx = random.randint(1, 9999)
        carne_generado = f"0905-{yy:02d}-{xxxx:04d}" # :02d y :04d aseguran ceros a la izquierda

        while carne_generado in set_carnes: # Asegurar unicidad
            yy = random.randint(18, 25)
            xxxx = random.randint(1, 9999)
            carne_generado = f"0905-{yy:02d}-{xxxx:04d}"

        # Generar materias aleatorias
        num_materias_rand = random.randint(2, 5)
        materias_generadas = []
        materias_usadas_temp = set() # Para evitar materias duplicadas para el mismo estudiante
        for _ in range(num_materias_rand):
            nombre_mat_base = random.choice(nombres_materias_posibles)
            sufijo_mat = random.choice(sufijos_materias)
            nombre_mat_completo = f"{nombre_mat_base} {sufijo_mat}"
            # Asegurar que la materia no se repita para el mismo estudiante
            while nombre_mat_completo in materias_usadas_temp:
                 nombre_mat_base = random.choice(nombres_materias_posibles)
                 sufijo_mat = random.choice(sufijos_materias)
                 nombre_mat_completo = f"{nombre_mat_base} {sufijo_mat}"
            materias_usadas_temp.add(nombre_mat_completo)

            cred_mat = random.randint(2, 5)
            materias_generadas.append((nombre_mat_completo, cred_mat))

        promedio_generado = round(random.uniform(5.0, 10.0), 1) # Promedios con un decimal

        estudiante = {'nombre': nombre_completo, 'carne': carne_generado, 'materias': materias_generadas, 'promedio': promedio_generado}
        lista_estudiantes.append(estudiante)
        set_carnes.add(carne_generado)
    print(f"Se han generado y agregado {len(lista_estudiantes)} estudiantes de ejemplo.")

# Llama a la función para poblar los datos al iniciar el programa
poblar_datos_iniciales()


# --- Menú de Usuario ---
def mostrar_menu():
    print("\n--- Sistema de Gestión de Estudiantes ---")
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Buscar estudiante")
    print("4. Mostrar estudiantes con promedio superior a...")
    print("5. Mostrar materias de un estudiante")
    print("6. Calcular promedio general del grupo")
    print("7. Mostrar todos los estudiantes (para depuración)")
    print("8. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar_estudiante(lista_estudiantes, set_carnes)
    elif opcion == '2':
        if not lista_estudiantes:
            print("No hay estudiantes para eliminar.")
            continue
        carne_a_eliminar = input("Ingrese el carné del estudiante a eliminar (formato '0905-YY-xxxx'): ")
        eliminar_estudiante(lista_estudiantes, set_carnes, carne_a_eliminar)
    elif opcion == '3':
        if not lista_estudiantes:
            print("No hay estudiantes para buscar.")
            continue
        while True:
            criterio = input("Buscar por 'nombre' o 'carne': ").lower()
            if criterio in ['nombre', 'carne']:
                break
            print("Criterio no válido. Por favor ingrese 'nombre' o 'carne'.")
        valor_busqueda = input("Ingrese el valor de búsqueda: ")
        buscar_estudiante(lista_estudiantes, criterio, valor_busqueda)
    elif opcion == '4':
        if not lista_estudiantes:
            print("No hay estudiantes para mostrar.")
            continue
        while True:
            try:
                promedio_minimo = float(input("Ingrese el promedio mínimo para mostrar (ej: 8.0): "))
                break
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")
        mostrar_estudiantes_promedio_superior(lista_estudiantes, promedio_minimo)
    elif opcion == '5':
        if not lista_estudiantes:
            print("No hay estudiantes para mostrar sus materias.")
            continue
        carne_estudiante = input("Ingrese el carné del estudiante (formato '0905-YY-xxxx'): ")
        mostrar_materias_estudiante(lista_estudiantes, carne_estudiante)
    elif opcion == '6':
        calcular_promedio_general_grupo(lista_estudiantes)
    elif opcion == '7': # Opción de depuración para ver todos los estudiantes
        if not lista_estudiantes:
            print("No hay estudiantes registrados.")
        else:
            print("\n--- Lista Completa de Estudiantes ---")
            for idx, est in enumerate(lista_estudiantes):
                print(f"{idx+1}. {est['nombre']} - {est['carne']} - Prom: {est['promedio']}")
                # print(f"   Materias: {est['materias']}") # Descomentar para ver materias
            print(f"Total de carnés en set_carnes: {len(set_carnes)}") # Verificar consistencia
    elif opcion == '8':
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")