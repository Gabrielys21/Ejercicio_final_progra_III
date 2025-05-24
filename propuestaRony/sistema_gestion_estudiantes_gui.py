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
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Estructuras de datos principales
estudiantes = []  # Lista principal de diccionarios de estudiantes
carnes_unicos = set()  # Set para garantizar carnés únicos

# Contador para el número correlativo del carné (XXXXX)
siguiente_numero_correlativo = 1000

# Opciones para la población inicial (uso de tuplas)
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

# --- Lógica de Negocio (Funciones originales adaptadas ligeramente si es necesario) ---
def generar_carne(anio_inscripcion):
    global siguiente_numero_correlativo
    if not (20 <= anio_inscripcion <= 25):
        raise ValueError("El año de inscripción debe estar entre 20 y 25.")
    yy = str(anio_inscripcion).zfill(2)
    while True:
        xxxxx = str(siguiente_numero_correlativo).zfill(5)
        carne = f"0905-{yy}-{xxxxx}"
        if carne not in carnes_unicos:
            siguiente_numero_correlativo += 1
            return carne
        siguiente_numero_correlativo += 1
        if siguiente_numero_correlativo > 99999:
            # En un sistema real, manejar el agotamiento de carnés.
            # Para este ejercicio, es improbable alcanzarlo con la población inicial.
            raise OverflowError("Se ha agotado el rango de números correlativos para carnés.")

def agregar_estudiante_logica(nombre, anio_inscripcion, materias, promedio):
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
        return True, f"Estudiante {nombre} con carné {carne} agregado exitosamente.", estudiante
    except ValueError as e:
        return False, f"Error al agregar estudiante: {e}", None
    except OverflowError as e:
        return False, f"Error al generar carné: {e}", None
    except Exception as e:
        return False, f"Error inesperado: {e}", None

def eliminar_estudiante_logica(carne_a_eliminar):
    estudiante_encontrado = None
    for est in estudiantes:
        if est["Carné"] == carne_a_eliminar:
            estudiante_encontrado = est
            break
    if estudiante_encontrado:
        estudiantes.remove(estudiante_encontrado)
        carnes_unicos.remove(carne_a_eliminar)
        return True, f"Estudiante con carné {carne_a_eliminar} eliminado exitosamente."
    else:
        return False, f"Estudiante con carné {carne_a_eliminar} no encontrado."

def buscar_estudiante_logica(termino_busqueda):
    resultados = []
    termino_busqueda_lower = termino_busqueda.lower()
    for est in estudiantes:
        if est["Carné"] == termino_busqueda or termino_busqueda_lower in est["Nombre"].lower():
            resultados.append(est)
    return resultados

def mostrar_promedio_superior_logica(umbral):
    return [est for est in estudiantes if est["Promedio"] > umbral]

def mostrar_materias_estudiante_logica(carne_busqueda):
    for est in estudiantes:
        if est["Carné"] == carne_busqueda:
            return est # Devuelve el diccionario del estudiante
    return None

def calcular_promedio_general_logica():
    if not estudiantes:
        return None
    suma_promedios = sum(est["Promedio"] for est in estudiantes)
    return suma_promedios / len(estudiantes)

def poblar_datos_iniciales():
    global siguiente_numero_correlativo # Asegurarse de modificar el global
    siguiente_numero_correlativo = 1000 # Reiniciar para la población
    carnes_unicos.clear()
    estudiantes.clear()
    
    print("Poblando datos iniciales...")
    for i in range(30):
        nombre = random.choice(nombres_ejemplo) + f" {chr(random.randint(65, 90))}."
        anio_inscripcion = random.randint(20, 25)
        num_materias = random.randint(2, 5)
        materias_estudiante = random.sample([m[0] for m in materias_disponibles_opciones], num_materias)
        promedio = round(random.uniform(5.0, 10.0), 2)
        
        # Usar la lógica de agregar directamente, ya que la GUI manejará los mensajes
        try:
            carne = generar_carne(anio_inscripcion)
            estudiante = {"Nombre": nombre, "Carné": carne, "Materias": materias_estudiante, "Promedio": promedio}
            estudiantes.append(estudiante)
            carnes_unicos.add(carne)
        except Exception as e:
            print(f"Error poblando datos: {e}") # Imprimir error si ocurre durante la población
    print(f"Datos iniciales poblados: {len(estudiantes)} estudiantes.")

# --- Interfaz Gráfica (GUI) con Tkinter ---
class AppGestionEstudiantes:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Sistema de Gestión de Estudiantes")
        self.root.geometry("950x600")

        # Frame para botones
        self.frame_botones = ttk.Frame(self.root, padding="10")
        self.frame_botones.pack(side=tk.TOP, fill=tk.X)

        # Botones
        ttk.Button(self.frame_botones, text="Agregar Estudiante", command=self.gui_agregar_estudiante).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Eliminar Estudiante", command=self.gui_eliminar_estudiante).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Buscar Estudiante", command=self.gui_buscar_estudiante).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Promedio Superior a...", command=self.gui_promedio_superior).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Materias de Estudiante", command=self.gui_materias_estudiante).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Promedio General", command=self.gui_promedio_general).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_botones, text="Refrescar Lista", command=self.actualizar_tabla_estudiantes).pack(side=tk.LEFT, padx=5)

        # Treeview para mostrar estudiantes
        self.cols = ("Carné", "Nombre", "Materias", "Promedio")
        self.tree = ttk.Treeview(self.root, columns=self.cols, show='headings', selectmode="browse")
        for col in self.cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor=tk.W) # Ajustar ancho según necesidad
        self.tree.column("Materias", width=300)
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Scrollbar para el Treeview
        scrollbar = ttk.Scrollbar(self.tree, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.actualizar_tabla_estudiantes()

    def actualizar_tabla_estudiantes(self, lista_filtrada=None):
        # Limpiar tabla actual
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        # Poblar tabla con datos (todos o filtrados)
        fuente_datos = lista_filtrada if lista_filtrada is not None else estudiantes
        for est in fuente_datos:
            materias_str = ", ".join(est["Materias"])
            self.tree.insert("", tk.END, values=(est["Carné"], est["Nombre"], materias_str, f"{est['Promedio']:.2f}"))

    def gui_agregar_estudiante(self):
        # Crear una ventana Toplevel para el formulario de agregar estudiante
        self.win_agregar = tk.Toplevel(self.root)
        self.win_agregar.title("Agregar Nuevo Estudiante")
        self.win_agregar.geometry("400x250")
        self.win_agregar.transient(self.root) # Hacerla modal respecto a la principal
        self.win_agregar.grab_set() # Capturar eventos para esta ventana

        frame_form = ttk.Frame(self.win_agregar, padding="10")
        frame_form.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame_form, text="Nombre Completo:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nombre = ttk.Entry(frame_form, width=40)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Año Inscripción (20-25):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_anio = ttk.Entry(frame_form, width=10)
        self.entry_anio.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame_form, text="Materias (separadas por coma):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_materias = ttk.Entry(frame_form, width=40)
        self.entry_materias.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Promedio (0.0-10.0):").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_promedio = ttk.Entry(frame_form, width=10)
        self.entry_promedio.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        btn_guardar = ttk.Button(frame_form, text="Guardar Estudiante", command=self.guardar_nuevo_estudiante)
        btn_guardar.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.entry_nombre.focus_set() # Poner foco en el primer campo

    def guardar_nuevo_estudiante(self):
        nombre = self.entry_nombre.get().strip()
        anio_str = self.entry_anio.get().strip()
        materias_str = self.entry_materias.get().strip()
        promedio_str = self.entry_promedio.get().strip()

        if not all([nombre, anio_str, materias_str, promedio_str]):
            messagebox.showerror("Error de Entrada", "Todos los campos son obligatorios.", parent=self.win_agregar)
            return

        try:
            anio = int(anio_str)
            if not (20 <= anio <= 25):
                messagebox.showerror("Error de Entrada", "El año de inscripción debe estar entre 20 y 25.", parent=self.win_agregar)
                return
        except ValueError:
            messagebox.showerror("Error de Entrada", "El año de inscripción debe ser un número.", parent=self.win_agregar)
            return

        materias = [m.strip() for m in materias_str.split(',') if m.strip()]
        if not materias:
            messagebox.showerror("Error de Entrada", "Debe ingresar al menos una materia.", parent=self.win_agregar)
            return

        try:
            promedio = float(promedio_str)
            if not (0.0 <= promedio <= 10.0):
                messagebox.showerror("Error de Entrada", "El promedio debe estar entre 0.0 y 10.0.", parent=self.win_agregar)
                return
        except ValueError:
            messagebox.showerror("Error de Entrada", "El promedio debe ser un número.", parent=self.win_agregar)
            return

        exito, mensaje, _ = agregar_estudiante_logica(nombre, anio, materias, promedio)
        if exito:
            messagebox.showinfo("Éxito", mensaje, parent=self.win_agregar)
            self.actualizar_tabla_estudiantes()
            self.win_agregar.destroy()
        else:
            messagebox.showerror("Error", mensaje, parent=self.win_agregar)

    def gui_eliminar_estudiante(self):
        carne = simpledialog.askstring("Eliminar Estudiante", "Ingrese el Carné del estudiante a eliminar:", parent=self.root)
        if carne:
            exito, mensaje = eliminar_estudiante_logica(carne.strip())
            if exito:
                messagebox.showinfo("Éxito", mensaje, parent=self.root)
                self.actualizar_tabla_estudiantes()
            else:
                messagebox.showerror("Error", mensaje, parent=self.root)

    def gui_buscar_estudiante(self):
        termino = simpledialog.askstring("Buscar Estudiante", "Ingrese Nombre o Carné a buscar:", parent=self.root)
        if termino:
            resultados = buscar_estudiante_logica(termino.strip())
            if resultados:
                self.actualizar_tabla_estudiantes(lista_filtrada=resultados)
                messagebox.showinfo("Resultados de Búsqueda", f"{len(resultados)} estudiante(s) encontrado(s). Mostrando en tabla.", parent=self.root)
            else:
                messagebox.showinfo("Sin Resultados", f"No se encontraron estudiantes para '{termino}'.", parent=self.root)
                self.actualizar_tabla_estudiantes() # Mostrar todos si no hay resultados
    
    def gui_promedio_superior(self):
        umbral_str = simpledialog.askstring("Promedio Superior", "Ingrese el umbral de promedio (ej. 8.0):", parent=self.root)
        if umbral_str:
            try:
                umbral = float(umbral_str)
                resultados = mostrar_promedio_superior_logica(umbral)
                if resultados:
                    self.actualizar_tabla_estudiantes(lista_filtrada=resultados)
                    messagebox.showinfo("Resultados", f"{len(resultados)} estudiante(s) con promedio superior a {umbral:.2f}.", parent=self.root)
                else:
                    messagebox.showinfo("Sin Resultados", f"No hay estudiantes con promedio superior a {umbral:.2f}.", parent=self.root)
                    self.actualizar_tabla_estudiantes() # Mostrar todos si no hay resultados
            except ValueError:
                messagebox.showerror("Error de Entrada", "El umbral debe ser un número.", parent=self.root)

    def gui_materias_estudiante(self):
        carne = simpledialog.askstring("Materias del Estudiante", "Ingrese el Carné del estudiante:", parent=self.root)
        if carne:
            estudiante = mostrar_materias_estudiante_logica(carne.strip())
            if estudiante:
                materias_str = "\n".join([f"- {m}" for m in estudiante['Materias']]) if estudiante['Materias'] else "No tiene materias inscritas."
                messagebox.showinfo(f"Materias de {estudiante['Nombre']}", 
                                    f"Carné: {estudiante['Carné']}\n\nMaterias:\n{materias_str}", parent=self.root)
            else:
                messagebox.showerror("Error", f"Estudiante con carné {carne} no encontrado.", parent=self.root)

    def gui_promedio_general(self):
        promedio = calcular_promedio_general_logica()
        if promedio is not None:
            messagebox.showinfo("Promedio General", f"El promedio general de todos los estudiantes es: {promedio:.2f}", parent=self.root)
        else:
            messagebox.showinfo("Promedio General", "No hay estudiantes registrados para calcular el promedio.", parent=self.root)

# --- Ejecución Principal ---
if __name__ == "__main__":
    poblar_datos_iniciales() # Poblar datos antes de iniciar la GUI
    
    main_window = tk.Tk()
    app = AppGestionEstudiantes(main_window)
    main_window.mainloop()