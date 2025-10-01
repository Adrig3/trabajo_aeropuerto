
"""
Representa una reserva de asiento.

Parámetros:
    - asiento (str): número de asiento.
    - nombre (str): nombre del pasajero.
    - clase (str): clase de la reserva (por ejemplo 'Economy', 'Business')
    - destino (str): destino del vuelo.

Devuelve:
    - instancia de `Reserva`.
"""
class Reserva:
    def __init__(self, asiento, nombre, clase, destino):
        self.asiento = asiento
        self.nombre = nombre
        self.clase = clase
        self.destino = destino

reservas = [
    Reserva("12A", "Juan Pérez", "Economy", "Madrid"),
    Reserva("14B", "María López", "Business", "París"),
    Reserva("21C", "Carlos García", "Economy", "Madrid"),
    Reserva("05D", "Ana Sánchez", "Business", "Londres"),
    Reserva("19E", "Luis Gómez", "Economy", "París"),
    Reserva("08F", "Sofía Vargas", "Economy", "Londres")

]

"""
Crea y escribe en el archivo de reservas 'reservas_maestro.txt'.

Parámetros: ninguno.
Devuelve: None. En caso de error imprime un mensaje explicativo.
"""
def crear_y_escribir_archivo_maestro():
    try:
        with open("reservas_maestro.txt", "w", encoding="utf-8") as f:
            for reserva in reservas:
                try:
                    f.write(f"{reserva.asiento}, {reserva.nombre}, {reserva.clase}, {reserva.destino}\n")

                except (TypeError, ValueError) as err:
                    print(f"Error al escribir reserva {reserva}: {err}")

        print("Archivo 'reservas_maestro.txt' creado con éxito.")

    except FileNotFoundError:
        print("Error: No se pudo encontrar la ruta para crear el archivo.")

    except PermissionError:
        print("Error: No tienes permiso para escribir en este directorio.")

    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")


"""
Lee el archivo reservas_maestro.txt, identifica el destino del
vuelo y crear archivos por destino (sin duplicados).

Si hay una linea de reservas incompleta, esa linea en concreto,
no se añadirá a ningún archivo.

Cuenta cuántas reservas hay en cada archivo creado, lo guarda en
la variable 'archivos_creados' para luego mostrarlos por terminal.

Parámetros: ninguno.
Devuelve: El numero de archivos creados. En caso de error imprime un mensaje explicativo.
"""
archivos_creados = {}

def clasificar_reservas_por_destino():
    try:
        with open("reservas_maestro.txt", "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(", ")
                if len(datos) == 4:
                    asiento, nombre, clase, destino = datos
                    nombre_archivo = f"reservas_{destino.lower()}.txt"

                    try:
                        with open(nombre_archivo, "a", encoding="utf-8") as archivo_destino:
                            archivo_destino.write(linea)

                        if nombre_archivo not in archivos_creados:
                            archivos_creados[nombre_archivo] = 0

                        archivos_creados[nombre_archivo] += 1

                    except FileNotFoundError:
                        return f"Error: No se encontró el archivo '{nombre_archivo}'."

                    except PermissionError:
                        return f"Error: No tienes permiso para escribir en '{nombre_archivo}'."

                    except Exception as e:
                        return f"Ha ocurrido un error inesperado al escribir en '{nombre_archivo}': {e}"

                else:
                    return f"Línea incompleta: {linea}, no se ha sido añadida a ningún archivo."

    except FileNotFoundError:
        return "Error: No se encontró el archivo 'reservas_maestro.txt'."

    except PermissionError:
        return "Error: No tienes permiso para leer el archivo 'reservas_maestro.txt'."

    except Exception as e:
        return f"Ha ocurrido un error inesperado: {e}"

    return archivos_creados

"""
Muestra por terminal un resumen de los archivos creados y la cantidad de reservas en cada uno.

Parámetros: numero de archivos creados.
Devuelve: None.
"""

def mostrar_resumen_archivos(archivos_creados):
    if not archivos_creados:
        print("No se han creado archivos de reservas por destino.")
        return

    try:
        print("\nResumen de la clasificación:")
        for archivo, cantidad in archivos_creados.items():
            print(f"- {archivo}: {cantidad} reservas")

    except Exception as e:
        print(f"Ha ocurrido un error inesperado al mostrar el resumen de archivos: {e}")
